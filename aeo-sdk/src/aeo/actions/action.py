from typing import Any, Dict, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .types import ActionType

class ExecutionAction(BaseModel):
    action_id: str
    action_type: ActionType
    name: str
    arguments: Dict[str, Any]
    model: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    parent_action_id: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
