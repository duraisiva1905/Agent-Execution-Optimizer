"""
AEO - Agent Execution Optimizer
"""
from .config.settings import AEOConfig
from .runtime.optimizer import AEO

__all__ = ["AEO", "AEOConfig"]
__version__ = "0.1.0"
