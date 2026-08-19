from typing import Protocol, Optional, runtime_checkable, Any
from .decision import ActionDecision
from ..runtime.context import TaskContext, AgentState
from ..actions.action import ExecutionAction

class EvaluationContext:
    def __init__(
        self,
        task_context: TaskContext,
        agent_state: AgentState,
        proposed_action: ExecutionAction,
        execution_history: list = None,
        available_tools: dict = None,
        cache: Any = None,
        budget: Any = None
    ):
        self.task_context = task_context
        self.agent_state = agent_state
        self.proposed_action = proposed_action
        self.execution_history = execution_history or []
        self.available_tools = available_tools or {}
        self.cache = cache
        self.budget = budget

@runtime_checkable
class DecisionRule(Protocol):
    name: str

    def evaluate(self, context: EvaluationContext) -> Optional[ActionDecision]:
        """Evaluate the proposed action and return a decision, or None to pass to the next rule."""
        ...
