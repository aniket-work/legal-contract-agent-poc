from pydantic import BaseModel, Field
from typing import List, Optional

class ContractClause(BaseModel):
    clause_type: str = Field(..., description="The type of clause (e.g., Termination, Indemnification, Liability)")
    content: str = Field(..., description="The actual text of the clause")
    risk_score: int = Field(..., description="Risk score from 1 to 10", ge=1, le=10)
    risk_rationale: str = Field(..., description="Reasoning for the risk score")
    suggested_revision: Optional[str] = Field(None, description="A safer alternative for the clause")

class ContractAnalysis(BaseModel):
    contract_title: str
    summary: str
    clauses: List[ContractClause]
    overall_risk_score: int
    recommendations: List[str]
