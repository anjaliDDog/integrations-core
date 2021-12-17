# (C) Datadog, Inc. 2019-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

CHECK_NAME = 'cilium'
NAMESPACE = 'cilium.'
CILIUM_VERSION = os.getenv('CILIUM_VERSION')

AGENT_DEFAULT_METRICS = [
    'cilium.agent.api_process_time.seconds.count',
    'cilium.agent.api_process_time.seconds.sum',
    'cilium.agent.bootstrap.seconds.count',
    'cilium.agent.bootstrap.seconds.sum',
    'cilium.controllers.failing.count',
    'cilium.controllers.runs_duration.seconds.count',
    'cilium.controllers.runs_duration.seconds.sum',
    'cilium.endpoint.count',
    'cilium.endpoint.regeneration_time_stats.seconds.count',
    'cilium.endpoint.regeneration_time_stats.seconds.sum',
    'cilium.endpoint.state',
    'cilium.event_timestamp',
    'cilium.identity.count',
    'cilium.ip_addresses.count',
    'cilium.k8s_client.api_latency_time.seconds.count',
    'cilium.k8s_client.api_latency_time.seconds.sum',
    'cilium.nodes.managed.total',
    'cilium.policy.count',
    'cilium.policy.endpoint_enforcement_status',
    'cilium.policy.max_revision',
    'cilium.policy.regeneration_time_stats.seconds.count',
    'cilium.policy.regeneration_time_stats.seconds.sum',
    'cilium.process.max_fds',
    'cilium.process.open_fds',
    'cilium.process.resident_memory.bytes',
    'cilium.process.start_time.seconds',
    'cilium.process.virtual_memory.bytes',
    'cilium.process.virtual_memory.max.bytes',
    'cilium.triggers_policy.update_folds',
    'cilium.unreachable.health_endpoints',
    'cilium.unreachable.nodes',
]

ADDL_AGENT_METRICS = [
    'cilium.triggers_policy.update_call_duration.seconds.count',
    'cilium.triggers_policy.update_call_duration.seconds.sum',
    'cilium.triggers_policy.update.total',
    'cilium.subprocess.start.total',
    'cilium.process.cpu.seconds.total',
    'cilium.policy.regeneration.total',
    'cilium.policy.l7_denied.total',
    'cilium.policy.l7_forwarded.total',
    'cilium.policy.l7_parse_errors.total',
    'cilium.policy.l7_received.total',
    'cilium.policy.import_errors.count',
    'cilium.nodes.all_datapath_validations.total',
    'cilium.nodes.all_events_received.total',
    'cilium.kubernetes.events_received.total',
    'cilium.kubernetes.events.total',
    'cilium.k8s_client.api_calls.count',
    'cilium.ipam.events.total',
    'cilium.fqdn.gc_deletions.total',
    'cilium.forward_bytes.total',
    'cilium.forward_count.total',
    'cilium.errors_warning.total',
    'cilium.endpoint.regenerations.count',
    'cilium.drop_bytes.total',
    'cilium.drop_count.total',
    'cilium.datapath.conntrack_gc.key_fallbacks.total',
    'cilium.datapath.conntrack_gc.runs.total',
    'cilium.controllers.runs.total',
    'cilium.bpf.map_ops.total',
    'cilium.datapath.conntrack_gc.duration.seconds.count',
    'cilium.datapath.conntrack_gc.duration.seconds.sum',
    'cilium.datapath.conntrack_gc.entries',
    'cilium.datapath.errors.total',
]

OPERATOR_METRICS = [
    'cilium.operator.process.cpu.seconds',
    'cilium.operator.process.max_fds',
    'cilium.operator.process.open_fds',
    'cilium.operator.process.resident_memory.bytes',
    'cilium.operator.process.start_time.seconds',
    'cilium.operator.process.virtual_memory.bytes',
    'cilium.operator.process.virtual_memory_max.bytes',
    # 'cilium.operator.identity_gc.entries',    # v1.10
    # 'cilium.operator.identity_gc.runs',       # v1.10
    # 'cilium.operator.num_ceps_per_ces.sum',   # v1.11
    # 'cilium.operator.num_ceps_per_ces.count', # v1.11
    # 'cilium.operator.ces.queueing_delay.seconds.sum',     # v1.11
    # 'cilium.operator.ces.queueing_delay.seconds.count',   # v1.11
    # 'cilium.operator.ces.sync_errors.total',              # v1.11
]

OPERATOR_AWS_METRICS_PRE_1_8 = [
    'cilium.operator.eni.k8s_sync.duration.seconds.count',
    'cilium.operator.eni.aws_api_duration.seconds.count',
    'cilium.operator.eni.deficit_resolver.latency.seconds.count',
    'cilium.operator.eni.k8s_sync.latency.seconds.sum',
    'cilium.operator.eni.deficit_resolver.latency.seconds.sum',
    'cilium.operator.eni.deficit_resolver.duration.seconds.sum',
    'cilium.operator.eni.deficit_resolver.queued.total',
    'cilium.operator.eni.ips.total',
    'cilium.operator.eni.k8s_sync.folds',
    'cilium.operator.eni.k8s_sync.duration.seconds.sum',
    'cilium.operator.eni.k8s_sync.latency.seconds.count',
    'cilium.operator.eni.available',
    'cilium.operator.eni.ec2_resync.latency.seconds.count',
    'cilium.operator.eni.interface_creation_ops',
    'cilium.operator.eni.ec2_resync.folds',
    'cilium.operator.eni.ec2_resync.duration.seconds.count',
    'cilium.operator.eni.deficit_resolver.duration.seconds.count',
    'cilium.operator.eni.deficit_resolver.folds',
    'cilium.operator.eni.ec2_resync.duration.seconds.sum',
    'cilium.operator.eni.nodes.total',
    'cilium.operator.eni.ec2_resync.latency.seconds.sum',
    'cilium.operator.eni.aws_api_duration.seconds.sum',
    'cilium.operator.eni.ec2_resync.queued.total',
    'cilium.operator.eni.available.ips_per_subnet',
    'cilium.operator.eni.k8s_sync.queued.total',
    'cilium.operator.eni.resync.total',
]

OPERATOR_AWS_METRICS_1_8 = [
    'cilium.operator.ec2.api.duration.seconds.sum',
    'cilium.operator.ec2.api.duration.seconds.count',
    'cilium.operator.ipam.available',
    'cilium.operator.ipam.available.ips_per_subnet',
    'cilium.operator.ipam.deficit_resolver.duration.seconds.sum',
    'cilium.operator.ipam.deficit_resolver.duration.seconds.count',
    'cilium.operator.ipam.deficit_resolver.folds',
    'cilium.operator.ipam.deficit_resolver.latency.seconds.sum',
    'cilium.operator.ipam.deficit_resolver.latency.seconds.count',
    'cilium.operator.ipam.deficit_resolver.queued.total',
    'cilium.operator.ipam.ips',
    'cilium.operator.ipam.k8s_sync.duration.seconds.sum',
    'cilium.operator.ipam.k8s_sync.duration.seconds.count',
    'cilium.operator.ipam.k8s_sync.folds',
    'cilium.operator.ipam.k8s_sync.latency.seconds.sum',
    'cilium.operator.ipam.k8s_sync.latency.seconds.count',
    'cilium.operator.ipam.k8s_sync.queued.total',
    'cilium.operator.ipam.nodes',
    'cilium.operator.ipam.resync.duration.seconds.sum',
    'cilium.operator.ipam.resync.duration.seconds.count',
    'cilium.operator.ipam.resync.folds',
    'cilium.operator.ipam.resync.latency.seconds.sum',
    'cilium.operator.ipam.resync.latency.seconds.count',
    'cilium.operator.ipam.resync.queued.total',
    'cilium.operator.ipam.resync.total',
]

# Not currently tested
ADDL_OPERATOR_AWS_METRICS = [
    'cilium.operator.ec2.api.rate_limit.duration.seconds.sum',
    'cilium.operator.ec2.api.rate_limit.duration.seconds.count',
    'cilium.operator.ipam.allocation_ops',
    'cilium.operator.ipam.release_ops',
    'cilium.operator.ipam.interface_creation_ops',
]
