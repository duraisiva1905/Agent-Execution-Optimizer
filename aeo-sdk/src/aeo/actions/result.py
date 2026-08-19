from typing import Any, Dict, Optional
from datetime import datetime
from pydantic import BaseModel, Field

class ExecutionResult(BaseModel):
    action_id: str
    output: Any
    success: bool = True
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    latency: Optional[float] = None  # in seconds
    estimated_cost: Optional[float] = None # in USD
    metadata: Dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
