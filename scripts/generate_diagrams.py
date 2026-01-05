import base64
import requests
import os

def generate_diagrams():
    diagrams = {
        "architecture": """
graph TD
    A[Contract PDF/Text] --> B[Text Extractor]
    B --> C[Legal Context Agent]
    C --> D{Structured Extraction}
    D --> E[Clause Classifier]
    D --> F[Risk Scorer]
    E --> G[Final Analysis Report]
    F --> G
    G --> H[Human-in-the-Loop Review]
""",
        "sequence": """
sequenceDiagram
    participant U as User
    participant A as Legal Ops Agent
    participant LLM as LLM Engine
    U->>A: Upload Contract
    A->>LLM: Extract Clauses (Pydantic)
    LLM-->>A: Structured JSON
    A->>A: Calculate Risk Scores
    A-->>U: Risk Assessment Report
""",
        "workflow": """
flowchart LR
    Start([Upload]) --> Ingest[Ingestion]
    Ingest --> Parse[Parsing]
    Parse --> Score[Scoring]
    Score --> Review[Expert Review]
    Review --> End([Approval])
"""
    }

    image_dir = "images"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    for name, code in diagrams.items():
        print(f"Generating {name} diagram...")
        encoded = base64.b64encode(code.encode()).decode()
        url = f"https://mermaid.ink/img/{encoded}"
        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                filename = f"{image_dir}/{name}-diagram.png"
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Saved {filename}")
            else:
                print(f"Error {response.status_code} for {name}")
        except Exception as e:
            print(f"Failed to generate {name}: {e}")

if __name__ == "__main__":
    generate_diagrams()
