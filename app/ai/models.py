from dataclasses import dataclass


@dataclass(slots=True)
class AIAnalysis:
    category: str
    department: str
    priority: str
    sentiment: str
    summary: str
    draft_reply: str