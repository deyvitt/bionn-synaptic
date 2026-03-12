from .synaptic_visualization import SynapticVisualizer
from .metaCognitive_enhancer import (
      MetaCognitiveAnalyzer,
      integrate_with_aggregator,
      get_enhanced_insights
     )
from .emrgnt_learner import EmergentSemanticLearner
from .synaptic_config import SynapticConfig, DEFAULT_CONFIG

__all__ = [
    'SynapticVisualizer',
    'MetaCognitiveAnalyzer',
    'EmergentSemanticLearner',
    'SynapticConfig',
    'DEFAULT_CONFIG',
    'integrate_with_aggregator',    
    'get_enhanced_insights'         
]

# Constants
from .constants import (
    # Domain keywords
    DOMAIN_KEYWORDS,
    
    # Connection thresholds
    STRONG_CONNECTION_THRESHOLD,
    WEAK_CONNECTION_THRESHOLD,
    PRUNING_THRESHOLD,
    COLLABORATIVE_THRESHOLD,
    COMPETITIVE_THRESHOLD,
    SEQUENTIAL_WINDOW,
    
    # Time constants
    SESSION_TIMEOUT_HOURS,
    PRUNING_CHECK_INTERVAL,
    ACTIVITY_TRACE_WINDOW,
    PERFORMANCE_HISTORY_SIZE,
    
    # Visualization
    COLOR_MAP,
    NODE_SIZES,
    FIGURE_SIZE,
    DPI,
    ANIMATION_FPS,
    
    # Confidence levels
    CONFIDENCE_LEVELS,
    CONSENSUS_LEVELS,
    
    # STDP parameters
    STDP_TAU,
    STDP_MAX_TIME_DIFF,
    
    # Pattern matching
    MIN_PATTERN_LENGTH,
    MAX_PATTERN_LENGTH,
    PATTERN_QUALITY_THRESHOLD,
    
    # Error messages
    ERROR_MESSAGES,
    
    # File paths
    DEFAULT_FILE_PATHS,
    
    # Performance metrics
    METRIC_NAMES,
    TREND_THRESHOLDS,
    
    # Special constants
    EPSILON,
    
    # Default values
    DEFAULT_LEARNING_RATE,
    DEFAULT_CONSENSUS_THRESHOLD,
    DEFAULT_HISTORY_SIZE,
    DEFAULT_EMBEDDING_DIM,
    DEFAULT_HIDDEN_DIM,
)

# Update __all__ to include constants
__all__.extend([
    'DOMAIN_KEYWORDS',
    'STRONG_CONNECTION_THRESHOLD',
    'WEAK_CONNECTION_THRESHOLD',
    'PRUNING_THRESHOLD',
    'COLLABORATIVE_THRESHOLD',
    'COMPETITIVE_THRESHOLD',
    'SEQUENTIAL_WINDOW',
    'SESSION_TIMEOUT_HOURS',
    'PRUNING_CHECK_INTERVAL',
    'ACTIVITY_TRACE_WINDOW',
    'PERFORMANCE_HISTORY_SIZE',
    'COLOR_MAP',
    'NODE_SIZES',
    'FIGURE_SIZE',
    'DPI',
    'ANIMATION_FPS',
    'CONFIDENCE_LEVELS',
    'CONSENSUS_LEVELS',
    'STDP_TAU',
    'STDP_MAX_TIME_DIFF',
    'MIN_PATTERN_LENGTH',
    'MAX_PATTERN_LENGTH',
    'PATTERN_QUALITY_THRESHOLD',
    'ERROR_MESSAGES',
    'DEFAULT_FILE_PATHS',
    'METRIC_NAMES',
    'TREND_THRESHOLDS',
    'EPSILON',
    'DEFAULT_LEARNING_RATE',
    'DEFAULT_CONSENSUS_THRESHOLD',
    'DEFAULT_HISTORY_SIZE',
    'DEFAULT_EMBEDDING_DIM',
    'DEFAULT_HIDDEN_DIM',
])
# Types
from .types import (
    ConnectionType,
    SynapticConnection,
    LearningMetrics,
    ClusterPerformance,
    VNIContribution,
    ConsensusResult,
    ConflictAnalysis,
    SynapticInsights,
    PerformanceTrend,
    PatternRecord
)

# Update __all__ to include types
__all__.extend([
    'ConnectionType',
    'SynapticConnection',
    'LearningMetrics',
    'ClusterPerformance',
    'VNIContribution',
    'ConsensusResult',
    'ConflictAnalysis',
    'SynapticInsights',
    'PerformanceTrend',
    'PatternRecord',
])
# Memory classes
from .vni_memory import (
    VniMemory,
    MemoryVersion,
    MemoryEntry,
    MemoryCluster,
    # Add any other classes exported by vni_memory.py
)

__all__.extend([
    'VniMemory',
    'MemoryVersion',
    'MemoryEntry',
    'MemoryCluster',
])

# Reasoning output structures
from .reasoning_output import ReasoningOutput, VNIOpinion

__all__.extend([
    'ReasoningOutput',
    'VNIOpinion',
])
