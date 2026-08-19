from typing import Any

from .runtime import AEORuntime
from ..config.settings import AEOConfig
from ..runtime.context import TaskContext, AgentState
from ..actions.action import ExecutionAction
from ..decisions.decision import ActionDecision

class AEO:
    """Agent Execution Optimizer Facade."""
    def __init__(self, config: AEOConfig | None = None):
        self.config = config or AEOConfig()
        self.runtime = AEORuntime(self.config)

    def evaluate_action(
        self,
        task_context: TaskContext,
        agent_state: AgentState,
        proposed_action: ExecutionAction
    ) -> ActionDecision:
        """Manually evaluate an action's necessity and safety."""
        return self.runtime.evaluate_action(
            task_context=task_context,
            agent_state=agent_state,
            proposed_action=proposed_action
        )

    def wrap(self, agent: Any) -> Any:
        """Wrap an agent to transparently optimize its execution."""
        # Phase 1: Just return the agent unmodified as a placeholder
        # True auto-instrumentation will be built in subsequent phases
        return agent
