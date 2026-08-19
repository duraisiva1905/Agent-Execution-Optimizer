from pydantic import BaseModel, Field

class AEOConfig(BaseModel):
    enabled: bool = Field(default=True, description="Enable or disable the optimizer entirely.")
    dry_run: bool = Field(default=True, description="If True, evaluate decisions but do not enforce them (SKIP/REUSE/STOP).")
    cache_enabled: bool = Field(default=True, description="Enable caching for actions.")
    cache_ttl: int = Field(default=300, description="Default cache time-to-live in seconds.")
    context_optimization: bool = Field(default=True, description="Enable context optimization/deduplication.")
    early_exit: bool = Field(default=False, description="Enable early exit policies.")
    model_substitution: bool = Field(default=False, description="Enable model substitution policies.")
    trajectory_recording: bool = Field(default=True, description="Record execution trajectories.")
    max_budget_usd: float | None = Field(default=None, description="Maximum budget allowed for the task.")
    optimization_budget_usd: float = Field(default=0.001, description="Maximum overhead budget for optimization per action.")
