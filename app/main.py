import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from search_client import retrieve_context
from sql_generator_agent import generate_sql
from sql_validator import validate_sql
from executor import execute_sql

load_dotenv()

app = FastAPI(
    title="NLQ Service",
    description="Natural Language to SQL microservice for regulated financial services data",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─────────────────────────────────────────
# Request / Response Models
# ─────────────────────────────────────────

class NLQRequest(BaseModel):
    question: str


class NLQResponse(BaseModel):
    question: str
    inferred_domain: str
    platform: str
    sql: str
    sql_formatted: str
    validation: dict
    execution: dict


# ─────────────────────────────────────────
# Health check
# ─────────────────────────────────────────

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "NLQ Service",
        "version": "1.0.0"
    }


# ─────────────────────────────────────────
# Main NLQ endpoint
# ─────────────────────────────────────────

@app.post("/nlq", response_model=NLQResponse)
def nlq(request: NLQRequest):

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    # ── Step 1: Retrieve context from Azure AI Search ──
    context = retrieve_context(question)

    domain = context.get("domain", "unknown")
    platform = context.get("platform", "unknown")

    # ── Step 2: Generate SQL ──
    sql = generate_sql(question, context)

    # ── Step 3: Validate SQL ──
    validation = validate_sql(sql, platform, domain)

    # ── Step 4: Execute if valid ──
    if validation["syntax_valid"] and validation["schema_valid"]:
        execution = execute_sql(sql, platform)
    else:
        execution = {
            "success": False,
            "rows": [],
            "row_count": 0,
            "error": "Validation failed — SQL not executed",
            "issues": validation.get("issues", [])
        }

    return NLQResponse(
        question=question,
        inferred_domain=domain,
        platform=platform,
        sql=sql,
        sql_formatted=sql.strip().replace("\n", " ").replace("    ", " "),
        validation=validation,
        execution=execution
    )


# ─────────────────────────────────────────
# Run
# ─────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True
    )