from datadog_checks.base import AgentCheck

METRICS = {
    "uptime": AgentCheck.gauge,
    "asserts.msg": AgentCheck.rate,
    "asserts.regular": AgentCheck.rate,
    "asserts.rollovers": AgentCheck.rate,
    "asserts.user": AgentCheck.rate,
    "asserts.warning": AgentCheck.rate,
    "backgroundFlushing.average_ms": AgentCheck.gauge,
    "backgroundFlushing.flushes": AgentCheck.rate,
    "backgroundFlushing.last_ms": AgentCheck.gauge,
    "backgroundFlushing.total_ms": AgentCheck.gauge,
    "tcmalloc.generic.current_allocated_bytes": AgentCheck.gauge,
    "tcmalloc.generic.heap_size": AgentCheck.gauge,
    "tcmalloc.tcmalloc.aggressive_memory_decommit": AgentCheck.gauge,
    "tcmalloc.tcmalloc.central_cache_free_bytes": AgentCheck.gauge,
    "tcmalloc.tcmalloc.current_total_thread_cache_bytes": AgentCheck.gauge,
    "tcmalloc.tcmalloc.max_total_thread_cache_bytes": AgentCheck.gauge,
    "tcmalloc.tcmalloc.pageheap_free_bytes": AgentCheck.gauge,
    "tcmalloc.tcmalloc.pageheap_unmapped_bytes": AgentCheck.gauge,
    "tcmalloc.tcmalloc.thread_cache_free_bytes": AgentCheck.gauge,
    "tcmalloc.tcmalloc.transfer_cache_free_bytes": AgentCheck.gauge,
    "tcmalloc.tcmalloc.spinlock_total_delay_ns": AgentCheck.gauge,
}

CASE_SENSITIVE_METRIC_NAME_SUFFIXES = {
    r'\.R\b': ".shared",
    r'\.r\b': ".intent_shared",
    r'\.W\b': ".exclusive",
    r'\.w\b': ".intent_exclusive",
}
