from enum import Enum

class ActionType(str, Enum):
    LLM = "LLM"
    TOOL = "TOOL"
    RETRIEVAL = "RETRIEVAL"
    DATABASE = "DATABASE"
    HTTP = "HTTP"
    AGENT = "AGENT"
    A2A = "A2A"
    MCP = "MCP"
    CODE = "CODE"
    MEMORY = "MEMORY"
    CUSTOM = "CUSTOM"
