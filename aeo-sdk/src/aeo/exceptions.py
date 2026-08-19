class AEOError(Exception):
    """Base exception for all AEO errors."""
    pass

class ConfigurationError(AEOError):
    """Raised when configuration is invalid."""
    pass

class PolicyError(AEOError):
    """Raised for policy-related errors."""
    pass

class CacheError(AEOError):
    """Raised when caching operations fail."""
    pass

class EvaluationError(AEOError):
    """Raised when an action evaluation fails."""
    pass

class IntegrationError(AEOError):
    """Raised for framework integration errors."""
    pass

class BudgetError(AEOError):
    """Raised when budget constraints are violated."""
    pass
