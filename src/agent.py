import random
from typing import List
from .schema import ContractClause, ContractAnalysis

class LegalAgent:
    """
    An experimental autonomous agent for legal contract analysis.
    This is a PoC for research purposes.
    """
    
    def __init__(self, model_name: str = "experimental-legal-v1"):
        self.model_name = model_name
        self.clause_types = ["Termination", "Indemnification", "Limitation of Liability", "Governing Law", "IP Ownership"]

    def analyze_contract(self, text: str) -> ContractAnalysis:
        # In a real scenario, this would call an LLM with structured output.
        # For this PoC, we simulate the analysis logic based on keywords.
        
        extracted_clauses = []
        for c_type in self.clause_types:
            if c_type.lower() in text.lower():
                risk = random.randint(3, 9)
                extracted_clauses.append(ContractClause(
                    clause_type=c_type,
                    content=f"Found {c_type} language in the document...",
                    risk_score=risk,
                    risk_rationale=f"Simulated risk rationale for {c_type}.",
                    suggested_revision=f"Revision for {c_type} to mitigate risk level {risk}."
                ))
        
        overall_risk = sum(c.risk_score for c in extracted_clauses) // len(extracted_clauses) if extracted_clauses else 1
        
        return ContractAnalysis(
            contract_title="Experimental MSA Analysis",
            summary="Automated extraction of high-risk legal provisions.",
            clauses=extracted_clauses,
            overall_risk_score=overall_risk,
            recommendations=["Review indemnification caps", "Clarify termination triggers"]
        )

def run_simulation(contract_samples: int = 50) -> List[ContractAnalysis]:
    agent = LegalAgent()
    results = []
    
    sample_text = """
    This Master Service Agreement governs the termination and indemnification between parties.
    The Limitation of Liability is capped at 1x contract value. 
    IP Ownership belongs to the Client upon payment.
    """
    
    for _ in range(contract_samples):
        # Add some randomness to simulate different contracts
        results.append(agent.analyze_contract(sample_text))
    
    return results
