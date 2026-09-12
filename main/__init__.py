# Copyright (c) Microsoft. All rights reserved.

"""Orchestration patterns for Microsoft Agent Framework.

This package provides high-level builders for the Magentic One pattern for sophisticated multi-agent orchestration
"""

import importlib.metadata

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"  # Fallback for development mode

from ._magentic import (
    MAGENTIC_MANAGER_NAME,
    ORCH_MSG_KIND_INSTRUCTION,
    ORCH_MSG_KIND_NOTICE,
    ORCH_MSG_KIND_TASK_LEDGER,
    ORCH_MSG_KIND_USER_TASK,
    MagenticAgentExecutor,
    MagenticBuilder,
    MagenticContext,
    MagenticManagerBase,
    MagenticOrchestrator,
    MagenticOrchestratorEvent,
    MagenticOrchestratorEventType,
    MagenticPlanReviewRequest,
    MagenticPlanReviewResponse,
    MagenticProgressLedger,
    MagenticProgressLedgerItem,
    MagenticResetSignal,
    StandardMagenticManager,
)
from ._orchestration_request_info import AgentRequestInfoResponse
from ._orchestration_state import OrchestrationState
from ._orchestrator_helpers import clean_conversation_for_handoff, create_completion_message

__all__ = [
    "MAGENTIC_MANAGER_NAME",
    "ORCH_MSG_KIND_INSTRUCTION",
    "ORCH_MSG_KIND_NOTICE",
    "ORCH_MSG_KIND_TASK_LEDGER",
    "ORCH_MSG_KIND_USER_TASK",
    "AgentOrchestrationOutput",
    "AgentRequestInfoResponse",
    "MagenticAgentExecutor",
    "MagenticBuilder",
    "MagenticContext",
    "MagenticManagerBase",
    "MagenticOrchestrator",
    "MagenticOrchestratorEvent",
    "MagenticOrchestratorEventType",
    "MagenticPlanReviewRequest",
    "MagenticPlanReviewResponse",
    "MagenticProgressLedger",
    "MagenticProgressLedgerItem",
    "MagenticResetSignal",
    "OrchestrationState",
    "StandardMagenticManager",
    "TerminationCondition",
    "__version__",
    "clean_conversation_for_handoff",
    "create_completion_message",
]