# AEO — Agent Execution Optimizer

A framework-independent execution-control and optimization SDK for AI agents.

## Overview

AEO reduces unnecessary agent execution while preserving task success, output quality, and safety. The fundamental optimization unit is the agent execution trajectory rather than merely an individual LLM request.

## Installation

```bash
pip install aeo-sdk
```

## Quickstart

```python
from aeo import AEO, AEOConfig

config = AEOConfig(
    enabled=True,
    dry_run=True,
    cache_enabled=True,
    context_optimization=True,
)

optimizer = AEO(config)

optimized_agent = optimizer.wrap(agent)
result = optimized_agent.run(task)
```

## Features
- Duplicate Request Detection
- Result Reuse via Exact Caching
- Token Budget Enforcement
- Deterministic Early Exit
- Trajectory Recording

## Documentation
Please refer to the `docs/` folder for comprehensive documentation on architecture, policies, benchmarks, and integrations.

## License
MIT License
