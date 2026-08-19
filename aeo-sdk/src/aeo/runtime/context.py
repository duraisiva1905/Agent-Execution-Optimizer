from typing import Any, Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field

class TaskContext(BaseModel):
    task_id: str
    task: str
    agent_id: Optional[str] = None
    framework: Optional[str] = None
    success_criteria: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    budget: Optional[float] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class AgentState(BaseModel):
    messages: List[Dict[str, Any]] = Field(default_factory=list)
    variables: Dict[str, Any] = Field(default_factory=dict)
    tool_results: Dict[str, Any] = Field(default_factory=dict)
    intermediate_results: List[Any] = Field(default_factory=list)
    memory: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
