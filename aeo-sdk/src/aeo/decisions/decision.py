from enum import Enum
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field

class DecisionType(str, Enum):
    EXECUTE = "EXECUTE"
    SKIP = "SKIP"
    REUSE = "REUSE"
    SUBSTITUTE = "SUBSTITUTE"
    STOP = "STOP"

class ActionDecision(BaseModel):
    decision: DecisionType
    reason: str
    rule_name: str
    confidence: float
    estimated_cost: Optional[float] = None
    estimated_savings: Optional[float] = None
    optimizer_cost: Optional[float] = None
    action_id: str
    source_action_id: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
