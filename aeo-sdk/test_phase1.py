import sys
from datetime import datetime
from pprint import pprint

from aeo import AEO, AEOConfig
from aeo.actions.action import ExecutionAction
from aeo.actions.types import ActionType
from aeo.runtime.context import TaskContext, AgentState

def main():
    print("--- 1. Initialize AEO Optimizer ---")
    config = AEOConfig(enabled=True, dry_run=True)
    optimizer = AEO(config)
    print(f"Optimizer initialized with config:\n{config.model_dump_json(indent=2)}\n")

    print("--- 2. Create Task Context & State ---")
    task_context = TaskContext(
        task_id="task-001",
        task="Summarize user profile",
        budget=0.10
    )
    agent_state = AgentState(
        messages=[{"role": "user", "content": "What is the status of my order?"}]
    )
    
    print("--- 3. Create a Proposed Action ---")
    proposed_action = ExecutionAction(
        action_id="act-123",
        action_type=ActionType.LLM,
        name="generate_summary",
        arguments={"prompt": "Summarize user profile"},
        model="gpt-4o-mini"
    )
    print(f"Action: {proposed_action.model_dump_json(indent=2)}\n")

    print("--- 4. Evaluate the Action ---")
    decision = optimizer.evaluate_action(
        task_context=task_context,
        agent_state=agent_state,
        proposed_action=proposed_action
    )
    
    print("--- 5. Evaluation Decision ---")
    print(decision.model_dump_json(indent=2))
    
    print("\n--- Test Complete ---")
    print("Phase 1 test succeeded! The core models and default decision engine are working.")

if __name__ == "__main__":
    main()
