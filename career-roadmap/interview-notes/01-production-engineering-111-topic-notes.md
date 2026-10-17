---
title: Production Engineering & System Design — 111 Topic Notes
updated: 2026-10-17
source: Code Baithak Instagram carousel screenshots supplied by the user
---

# Production Engineering & System Design: 111 Topic Notes

These notes expand the 111-item checklist into practical engineering concepts. For every topic, focus on the failure/problem it solves, a real application, and the implementation trade-off. Code examples use TypeScript/SQL-style pseudocode; validate, test, and instrument any production adaptation.

## Study method
1. Explain the concept in plain language.
2. Build a small local example.
3. Test a failure case.
4. Discuss correctness, latency, security, availability, and cost.
5. Revisit the interview prompts at the end.

## I. API reliability and application behavior

### 1. Idempotency keys
Repeated delivery of the same command should create one logical effect. For payment/order APIs, accept an Idempotency-Key, persist it under a unique constraint with a request fingerprint and result, and return the saved result on replay. Reject the same key with a different payload. An in-memory map fails across replicas/restarts.

### 2. Rate limiting
Bound request volume per user, IP, API key, or route. Use token bucket when controlled bursts are acceptable; sliding windows for more precise rolling limits. Shared Redis-backed counters coordinate replicas. Return HTTP 429 and Retry-After. IP-only limits can harm users behind NAT; combine identity and risk signals.

### 3. Reverse proxies
A reverse proxy receives public traffic and forwards it to private services; it can terminate TLS, route, compress, and enforce limits. Example: Nginx routes /api to Node.js. Trust forwarded client-IP headers only from known proxies, and set body-size and timeout limits.

### 4. Connection pooling
Reuse a bounded set of database connections instead of opening one per request. Example: PostgreSQL pool with max=10, short connection timeout, and idle timeout. Capacity must account for replicas: 10 connections × 20 replicas = 200 possible connections. Pool exhaustion can queue requests; oversized pools can overwhelm the database.

### 5. N+1 queries
Fetching a list and then issuing one query per row causes N+1 round trips. Example: 100 posts plus 100 author lookups. Fix with a join, eager loading, or batched DataLoader-style requests. Verify query counts and plans; avoid replacing N+1 with a huge join that duplicates excessive data.

### 6. Caching strategies
Cache-aside reads cache then source on miss; write-through updates cache with the source; write-behind queues source writes and risks lag/loss. Cache public product details, not highly sensitive balances by default. Define TTL, staleness tolerance, invalidation, cache key, and stampede behavior before implementation.

### 7. Cache invalidation
Remove or refresh stale values after source changes. Options: TTL, explicit delete, versioned keys, or event-driven invalidation. Example: after product 123's price commits, invalidate product:123. If invalidation fails after commit, stale data remains; use an outbox/retry or a short TTL where appropriate.

### 8. Load balancing
Distribute requests among healthy instances using round-robin, least-connections, weights, or hashing. Example: three stateless API replicas behind a load balancer. Health checks must reflect readiness, not merely process existence. Sticky sessions can cause uneven load and reduce failover flexibility.

### 9. API gateways
Central entry point for routing, quotas, authentication integration, request shaping, and analytics. Route /v1/orders to order service. Keep domain/business rules in services; a gateway should not become a single bottleneck or duplicate every business rule.

### 10. Timeouts
Set a deadline for every network/database operation so slow dependencies cannot hold resources forever. Allocate an overall request budget across DB and downstream calls; propagate deadlines and use AbortController for fetch. Separate connection and total timeouts. Longer timeouts can worsen resource exhaustion.

### 11. Retries
Retry transient failures only when the operation is safe to repeat. Retrying a read after connection reset may be safe; retrying a payment POST without idempotency may double-charge. Cap attempts, respect Retry-After, enforce a deadline, and retry at one appropriate layer to avoid retry storms.

### 12. Exponential backoff
Increase retry delay after each failure and add random jitter. Example: ceiling = min(2000 ms, 100 ms × 2^attempt), then choose a random delay below that ceiling. This spreads clients out after an outage. Keep retries within the total deadline and cap them.

### 13. Circuit breakers
Closed allows requests; open fails fast after repeated failures; half-open permits limited recovery probes. If recommendations time out, show popular items instead. A breaker complements timeouts and bulkheads; it does not fix the failing dependency or guarantee a safe fallback.

### 14. Race conditions
Concurrent interleaving causes an invalid result. Two requests may both read stock=1 and oversell. Use atomic updates or transactions:
~~~sql
UPDATE inventory SET quantity = quantity - 1
WHERE product_id = $1 AND quantity > 0
RETURNING quantity;
~~~
Check whether a row was returned. Do not perform a read-check-write sequence without a concurrency guarantee.

### 15. Deadlocks
Transactions wait for locks held by one another. A locks account A then B; another locks B then A. Acquire locks in a consistent order, keep transactions short, index predicates, and retry the entire transaction when the database reports a deadlock—not merely the last statement.

### 16. Memory leaks
Objects remain reachable and cannot be reclaimed. Example: a global array stores every request for debugging. Monitor heap/RSS over time, take heap snapshots, inspect retained objects, remove listeners/timers, and bound caches. High memory alone is not proof of a leak; compare workload and GC behavior.

### 17. Webhooks
A provider sends an event to your endpoint. Verify signatures over the raw body, check timestamps/replay, persist a unique event ID, acknowledge quickly, and process asynchronously. Delivery may be duplicated, late, or out of order. Make handlers idempotent and verify authoritative provider state for sensitive transitions.

### 18. CORS
Browser policy determines which origins may read cross-origin responses; it is not authentication. Allow explicit origins and required methods/headers. Credentialed requests cannot use wildcard origin. CORS does not generally prevent CSRF; cookie-authenticated state changes still need appropriate CSRF defenses.

### 19. Secrets management
Keep credentials outside source control; use managed secret stores or deployment injection, least privilege, separate environments, audit, and rotation. Never log tokens or passwords. Environment variables reduce accidental commits but do not by themselves provide governance, rotation, or protection from a compromised process.

## II. Databases and distributed data

### 20. Database indexing
Indexes trade storage/write overhead for faster selected reads. A B-tree on (customer_id, created_at DESC) can help fetch newest orders per customer. Use EXPLAIN (ANALYZE, BUFFERS) on realistic data. Indexes are not automatically useful for every column or low-selectivity query.

### 21. Query optimization
Reduce scanned rows, unnecessary columns, repeated queries, sorting, and bytes transferred. Reproduce the slow query, inspect its plan, adjust indexes/query shape/statistics, benchmark, and watch regressions. Keyset pagination over an indexed cursor can outperform large OFFSET pagination.

### 22. Read replicas
Replicate data to read-only copies for read scale or reporting. Writes go to primary; reports use replicas. Asynchronous lag can hide a just-written record. Route read-after-write traffic to primary or use a consistency-aware strategy.

### 23. Database migrations
Versioned schema/data changes. Prefer expand → deploy compatible code → backfill → switch usage → contract. Add a nullable column before requiring it everywhere. Large-table locks, long backfills, and rollback compatibility must be planned.

### 24. Schema versioning
Track evolving payload/database contracts and preserve compatibility. Events may carry schemaVersion=2. Prefer additive changes, validation, deprecation windows, and consumer compatibility tests. A version field alone does not make a breaking change safe.

### 25. Optimistic locking
Assume conflicts are uncommon and detect them through a version:
~~~sql
UPDATE documents SET body=$1, version=version+1
WHERE id=$2 AND version=$3;
~~~
Zero affected rows means another writer changed the record. Reload or ask the user to resolve the conflict. Useful for forms and collaborative edits with relatively low contention.

### 26. Pessimistic locking
Lock data before changing it. SELECT ... FOR UPDATE can protect a wallet row while validating and recording a transfer in a short transaction. Useful under high contention; long transactions increase lock waits and deadlock risk.

### 27. Distributed locks
Coordinate workers across processes using a lease/owner token and safe release. Example: only one reconciliation job runs at once. Lease expiry, pauses, and partitions can create stale owners; critical systems may need fencing tokens. A simple Redis lock is not a universal correctness guarantee.

### 28. Sharding
Split records across database servers using a shard key such as customer_id. It can increase capacity, but cross-shard joins/transactions and rebalancing are harder. Poor keys create hot shards or force common queries to scatter across all shards.

### 29. Partitioning
Divide one logical table into partitions, often by date or key range. Monthly event partitions make retention/deletion efficient. Partitioning is not necessarily sharding: partitions may be on one server. Ensure predicates enable partition pruning.

### 30. Replication
Maintain data copies for availability, reads, and recovery. Synchronous replication can improve durability at latency cost; asynchronous replication is faster but may lose recent writes on failover. Understand lag, split-brain prevention, failover, and restore procedures.

### 31. Leader election
Choose a coordinator for writes/tasks. Robust distributed election uses quorum/epochs and fencing to prevent a stale leader from continuing work. A process merely believing it is leader is insufficient during network partitions.

### 32. CAP theorem
During a network partition, a distributed system must trade off strong consistency for an operation versus availability of every request. Partition tolerance is unavoidable in a networked system. CAP does not mean a database permanently picks any two in all situations. Banking writes may fail closed; feeds may serve stale data.

### 33. Eventual consistency
Replicas can temporarily disagree but converge if updates stop and replication proceeds. Define acceptable staleness, conflict resolution, and read-your-writes behavior. “Eventually” needs a convergence mechanism; it is not a guarantee that data becomes correct by magic.

### 34. Distributed transactions
Coordinate operations across services/stores. Two-phase commit coordinates prepare/commit but introduces coordinator/availability complexity. A Saga sequences local transactions with compensating actions. Compensation is a new business action, not a magical rollback of an external payment or shipment.

### 35. Saga pattern
Persist a workflow such as create order → reserve stock → charge payment → confirm. If payment fails, release stock. Make each step idempotent, record workflow state, define timeout/retry paths, and support compensation failure/manual recovery.

### 36. Message queues
Buffer work and decouple request latency from processing. An API can enqueue invoice generation and return 202 Accepted. Define delivery semantics, acknowledgements, visibility timeout, ordering, retries, queue-age alerts, and capacity. Queues cannot solve a permanently slower consumer without scaling or load shedding.

### 37. Pub/Sub
Publish events to a topic so independent subscriptions receive them. OrderPlaced can trigger email, analytics, and inventory. Queues often distribute work among competing consumers; pub/sub fans events out to independent subscribers. Handle duplicate delivery, event schema evolution, and lag.

### 38. Event-driven architecture
Services react to events rather than making every downstream call synchronously. This decouples scaling but complicates tracing, replay, and consistency. Use event IDs, correlation IDs, compatible schemas, idempotent consumers, and an outbox when database commits and event publication must stay aligned.

### 39. Dead-letter queues
Store messages that repeatedly fail. Alert on DLQ growth, preserve event IDs and sanitized failure reasons, fix the cause, and replay safely with idempotency. A DLQ without an owner and replay runbook becomes a graveyard for lost business work.

### 40. Backpressure
Slow producers or limit acceptance when consumers cannot keep up. Use bounded queues, flow control, concurrency limits, load shedding, or 429/503. Unbounded buffering converts overload into memory exhaustion and extreme latency.

### 41. Cron jobs
Scheduled cleanup, reports, and reconciliation need time-zone rules, missed-run handling, overlap prevention, idempotency, retries, metrics, and alerts. Multiple replicas may run the same schedule; use a scheduler or distributed coordination if single execution matters.

## III. Security and network protocols

### 42. SQL injection
Untrusted input changes SQL meaning. Parameterize values and allow-list identifiers such as sort columns:
~~~ts
const result = await pool.query(
  "SELECT id, email FROM users WHERE email = $1", [email]
);
~~~
Avoid string concatenation and hand-written escaping.

### 43. XSS
Attacker-controlled content executes in another user's browser. Stored, reflected, and DOM-based XSS require context-aware output encoding, safe templates, sanitization for allowed rich HTML, CSP, and avoiding unsafe DOM sinks. Render comments as text, not executable HTML.

### 44. CSRF
A browser with ambient credentials is tricked into an unwanted state-changing request. Use SameSite cookies, anti-CSRF tokens, Origin/Referer checks where appropriate, and never mutate state on GET. CORS alone is not a general CSRF defense.

### 45. SSRF
An attacker makes the server request an unintended internal URL. URL-preview endpoints are a classic risk. Allow-list schemes/hosts, block loopback/private/link-local addresses, re-check DNS results and redirects, enforce egress controls, and set timeouts. Beware DNS rebinding.

### 46. OAuth 2.0
Delegated authorization lets a client obtain scoped access without collecting the user's password for the target service. Public web/mobile clients should use Authorization Code with PKCE and exact redirect URIs. OpenID Connect adds identity on top of OAuth. Never embed client secrets in public apps.

### 47. JWT rotation
JWTs are signed claims, not encrypted by default. Use short-lived access tokens, refresh-token rotation/reuse detection, and planned signing-key rotation. Validate signature, issuer, audience, expiry, and allowed algorithm. A valid signature alone does not prove the token is meant for your service.

### 48. IAM
Identity and Access Management defines who can do what to which resource. Use least privilege, scoped roles, temporary credentials, separate service identities, and audit. A report worker should access its report bucket, not administer the whole cloud account.

### 49. TLS
TLS protects data in transit and authenticates servers when certificate validation is performed. Use modern TLS, valid certificate chain/hostname, automated renewal, and verified service-to-service connections. TLS cannot protect plaintext after it reaches a compromised endpoint.

### 50. Encryption at rest
Encrypt database volumes, object storage, backups, and disks; govern keys, rotation, audit, and access separately. Application-level field encryption may be needed for specific threats. Encryption does not stop an authorized compromised application from reading plaintext.

### 51. Encryption in transit
Protect service-to-service and client-to-service traffic with authenticated encryption. Internal networks are not automatically trusted. TLS must validate peers; disabling certificate validation defeats important guarantees.

### 52. WAF
A Web Application Firewall filters suspicious HTTP traffic using managed rules and custom policy. It can reduce common exploit traffic but cannot replace secure code, authorization, or patching. Tune false positives and monitor bypasses.

### 53. DDoS protection
Combine provider edge mitigation, CDN caching, WAF, per-route quotas, connection limits, autoscaling, and incident runbooks. Autoscaling alone can scale costs faster than attack traffic disappears. Protect expensive endpoints more strictly than static assets.

### 54. WebSockets
Persistent full-duplex connection for chat/live updates. Authenticate the handshake, authorize each channel/action, use heartbeats and reconnect jitter, cap message size, and handle backpressure. Long-lived connections require connection and fan-out capacity planning.

### 55. Server-Sent Events
SSE streams server-to-browser events over HTTP; client-to-server actions use normal requests. Good for progress updates and notifications. Use event IDs/reconnect behavior and heartbeats; configure proxies to avoid buffering.

### 56. Long polling
Client request waits for an event or timeout, then client starts another request. Useful when persistent push is unavailable, but creates more request overhead. Bound waiting requests and use jittered reconnects.

### 57. gRPC
Typed RPC commonly using Protocol Buffers and HTTP/2. Useful for internal service calls and streaming. Define deadlines, compatible schemas, authorization, and observability. Browser support, debugging, and load balancing need deliberate design.

### 58. HTTP/2 and HTTP/3
HTTP/2 multiplexes streams over TCP; HTTP/3 uses QUIC over UDP and can reduce transport-level head-of-line effects. Protocol changes do not fix slow SQL or application work; measure end-to-end latency.

### 59. TCP vs UDP
TCP provides reliable ordered bytes and congestion control; UDP datagrams leave delivery/order behavior to the application/protocol. HTTPS commonly uses TCP with HTTP/1.1 or HTTP/2; HTTP/3 uses QUIC over UDP. UDP is not automatically faster for every workload.

### 60. DNS
DNS maps names to records such as A/AAAA, CNAME, MX, and TXT. Debug resolver result, delegation, TTL, authoritative records, and local caches. DNS changes are not instantaneous global switches; plan TTL and rollback before moving a service.

## IV. Delivery, infrastructure, and concurrency

### 61. Docker
Package an application into a reproducible image. Use multi-stage builds, pinned base images, a minimal runtime, non-root user, .dockerignore, scanning, and secrets outside the image. A container shares the host kernel and is not a VM.

### 62. Kubernetes
Orchestrates containers through desired state, scheduling, services, deployments, and recovery. Know Pod, Deployment, Service, ConfigMap, Secret, Ingress/Gateway, Job, and CronJob. It adds operational complexity; use it when benefits justify it.

### 63. Helm charts
Package Kubernetes manifests as templates and values. Render and inspect the generated YAML, validate in CI, and keep templates understandable. Complex templating can hide dangerous changes.

### 64. Service discovery
Find service instances dynamically, e.g. Kubernetes DNS. Discovery tells you where to connect, not whether a request is healthy or authorized. Add health checks, deadlines, and secure identity.

### 65. CI/CD
CI validates changes; delivery/deployment automates release preparation or rollout. Pipeline: lint/typecheck → tests → build → security checks → staging → smoke test → controlled production. A green build does not prove production safety; migrations and rollback need planning.

### 66. Build caching
Reuse outputs when inputs have not changed. Cache package downloads and Docker layers, but ensure keys include all relevant inputs. Wrong keys serve stale artifacts; untrusted PRs must not poison trusted release caches.

### 67. Infrastructure as Code
Version-controlled declarations make infrastructure repeatable and reviewable. Review plans, separate environments/state, secure secrets, pin providers, and detect drift. State may contain sensitive data, so protect access and storage.

### 68. Terraform
Declarative IaC workflow: init → fmt/validate → plan → review → apply. Use modules carefully, lock state, and inspect destructive replacements. Never blindly apply a plan that replaces a production database or exposes a resource.

### 69. Feature flags
Deploy code separately from enabling it. Ramp a new checkout from internal users to a small percentage. Define ownership, expiry, default behavior, and audit. Permanent flags multiply test complexity; remove them.

### 70. Blue-green deployment
Run old and new environments side-by-side and switch traffic after validation. Rollback is fast if data/schema remain compatible. Database migrations must support both versions during transition.

### 71. Canary releases
Send a small share of traffic to a new version, compare error rate and p99 latency, then ramp gradually. A small sample can hide rare errors; segment by route, region, tenant, or device where useful.

### 72. Rolling deployments
Replace instances gradually while preserving capacity. Tune maxUnavailable/maxSurge, readiness, graceful shutdown, and backward-compatible schemas/messages. Old and new code often run simultaneously.

### 73. Rollbacks
Return to a known-good artifact/configuration. Keep immutable artifacts and define triggers/runbooks. Data migrations may not be reversible; a forward fix or compensating migration can be safer.

### 74. Health checks
Liveness asks whether a process should restart; readiness asks whether it should receive traffic; startup gives slow initialization time. Avoid making liveness fail on a temporary dependency outage, which can restart every replica.

### 75. Liveness and readiness probes
Configure separate paths, thresholds, timeouts, and startup probes. Readiness failure should normally remove traffic, not necessarily kill the process. Overly aggressive probes can amplify load spikes.

### 76. Dependency hell
Conflicting/incompatible dependencies cause build and runtime failures. Use lockfiles, reproducible installs, automated updates, SBOM and vulnerability scans. A lockfile gives repeatability, not proof of safety.

### 77. API versioning
Evolve public contracts without breaking clients. URI versions are one option; additive compatible changes may avoid a new version. Track deprecation dates and actual usage. Too many versions increase maintenance.

### 78. Semantic versioning
Under SemVer, MAJOR signals incompatible API changes, MINOR backward-compatible functionality, PATCH backward-compatible fixes. Labels are meaningful only when maintainers follow a clear compatibility contract.

### 79. Garbage collection
Runtime reclaims unreachable memory but incurs CPU/pause costs. Node's V8 cannot reclaim objects still retained by a global cache. Track heap, allocation rate, GC pauses, and retention; remove unnecessary references rather than blindly forcing GC.

### 80. Thread safety
Concurrent access must preserve invariants. Use locks, atomics, immutable messages, actor ownership, or database transactions. Node's main JS thread does not eliminate async race conditions, worker_threads, or external-service concurrency.

## V. Scaling, latency, and recovery

### 81. Autoscaling
Adjust capacity from CPU, request rate, or queue depth. Define min/max, warm-up, stabilization, and scale-down policy. CPU alone misses DB saturation and queue backlog.

### 82. Horizontal scaling
Add instances. Stateless API replicas scale well when sessions/shared state are externalized and jobs are idempotent. More app replicas do not automatically scale a database or third-party API.

### 83. Vertical scaling
Give one machine more CPU, memory, or I/O. It can be the simplest fix for database saturation, but has cost/size ceilings and retains a single-node failure domain.

### 84. CDN
Edge network serves content close to users. Hashed static assets can use long immutable TTLs. Set Cache-Control and correct cache keys. Accidentally caching personalized responses publicly can leak data.

### 85. Edge caching
Cache eligible responses near users. Cache public product descriptions, not private account pages. Define cache key, cookies/query handling, purge strategy, and acceptable staleness; key mistakes can cross-serve users.

### 86. Cost optimization
Attribute cost with tags and unit metrics; right-size, remove idle resources, set budgets, and review spend. Measure cost per 1,000 requests or per job, not only total bill. Cheapest infrastructure can be costly in incidents or engineering time.

### 87. Cold starts
A function/container initializes after inactivity or scaling. Reduce package size, safely reuse clients, and provision warm capacity only when justified by latency goals. Keeping everything warm can erase serverless savings.

### 88. Serverless limits
Functions have duration, memory, concurrency, payload, and networking limits. Long jobs should use durable queues/workflows and checkpointed steps. Serverless still needs security, monitoring, retries, and cost controls.

### 89. Latency
Time from defined start to completion. Break it into DNS/connect/TLS, queue wait, app, database, and downstream time. Tracing may reveal one 900 ms dependency inside a 1-second request. Average latency hides tail pain.

### 90. Throughput
Completed work per time, e.g. requests/second. Concurrency can raise throughput until saturation; beyond that it may only increase queues and latency. Benchmark realistic payloads, cache rates, and dependencies.

### 91. p99 latency
99% of measured requests finish at or below this value; 1% are slower. Track by endpoint/region and set SLOs. Percentiles depend on sample size and aggregation; do not average p99 values from hosts.

### 92. Tail latency
Slowest fraction of requests, caused by queueing, GC, network variance, hot keys, or slow fan-out dependencies. Use deadlines, bounded queues, caching, and fewer dependencies. Hedged requests can double load and worsen overload.

### 93. Network partitions
Nodes cannot communicate reliably while they may still run. Define which operations reject, which may serve stale data, quorum behavior, and split-brain prevention. A timeout cannot tell whether a remote operation failed or succeeded but its response was lost.

### 94. Clock skew
Machine clocks differ, so timestamps do not always establish order. Synchronize clocks, use monotonic clocks for durations, and use versions/sequence numbers for ordering. Wall-clock time is not distributed consensus.

### 95. Multi-region deployment
Multiple regions can improve latency/resilience but complicate replication, residency, conflicts, routing, and failover. Choose active-active or active-passive based on requirements. Global deployment adds cost and operational complexity.

### 96. Failover
Switch to a healthy standby/route. Define detection, promotion authority, fencing, routing, data-loss window, capacity, and return-to-normal procedure. Noisy health checks or stale standbys can make automatic failover worse.

### 97. Backups
Protect against deletion, corruption, ransomware, and infrastructure loss. Use automated encrypted backups, separate access/account, retention, and restore drills. A successful backup job is not proof a restore works.

### 98. Disaster recovery
RPO is acceptable data-loss window; RTO is acceptable recovery time. Agree business targets, design for them, and test restore/failover. A written target that has never been tested is not a recovery capability.

### 99. Chaos engineering
Controlled experiments test resilience hypotheses, e.g. stop one staging replica and verify error/latency targets. Define blast radius, owner, abort condition, telemetry, and rollback. Randomly breaking production is not disciplined chaos engineering.

## VI. Observability and production operations

### 100. Logging
Record discrete events for debugging/audit. Prefer structured logs with timestamp, severity, service/version, request ID, and safe context. Never log passwords, tokens, card data, or unnecessary personal data. Excessive logs cost money and expose information.

### 101. Monitoring
Collect signals for known failure modes and trends: request/error rate, latency, saturation, queue age, DB connections, dependency health. Dashboards need owners and response actions; otherwise they are decoration.

### 102. Distributed tracing
Follow a request through services using trace/span IDs and standard context propagation. A checkout trace may reveal that inventory takes 900 ms. Correlate logs and traces, sample thoughtfully, and never put secrets in span attributes.

### 103. Metrics
Counters count events, gauges represent current values, histograms measure distributions. Track HTTP errors and duration histograms by bounded labels. Raw user IDs or full URLs create dangerous high cardinality.

### 104. Alerts
Notify a responsible person when action is needed. Good alerts are actionable, owned, linked to runbooks, and based on user impact/risk. Alert fatigue makes real incidents easier to miss.

### 105. Observability
Infer internal state from logs, metrics, traces, and other outputs. Instrument user journeys, dependencies, correlation IDs, and safe context. More telemetry alone does not make a system diagnosable.

### 106. SLIs
Service Level Indicators are measurements such as successful-request ratio, latency threshold, or data freshness. Define numerator, denominator, exclusions, window, and user impact precisely.

### 107. SLOs
Service Level Objectives are target values for SLIs, e.g. 99.9% of eligible requests succeed within 300 ms over 30 days. They guide reliability investment and release decisions. Define measurement carefully.

### 108. Error budgets
Allowed unreliability implied by an SLO. A 99.9% success target permits 0.1% unsuccessful requests in its measurement window. Rapid budget burn can trigger a pause on risky releases and reliability work; do not treat the budget as a target to waste.

### 109. Production incidents
A material degradation in service, data integrity, security, or customer experience. Detect → declare severity → assign incident commander → mitigate → communicate → recover → verify → learn. Restore service before pursuing perfect root-cause certainty.

### 110. On-call
Staffed incident response outside normal hours. Provide fair rotations, escalation, runbooks, sensible paging, handoffs, and follow-up. Pages should contain impact, reason, dashboard, runbook, and next action; warning spam creates burnout.

### 111. Postmortems
Blameless review of impact, timeline, contributing factors, detection/response, and prioritized actions with owners/dates. “Be more careful” is not an actionable fix. Improve systems and controls rather than searching for an individual to blame.

## End-to-end lab: resilient order API

~~~text
Client
  -> HTTPS reverse proxy / load balancer
  -> Node.js API + rate limiter
  -> PostgreSQL (pool, constraints, transactions)
  -> outbox table -> worker/queue -> email/webhook provider
  -> structured logs + metrics + traces + alerts
~~~

Build POST /orders with validation and an Idempotency-Key. In one database transaction, enforce inventory invariants, create the order, and write an outbox event. A worker publishes events with bounded retries/backoff; repeated failures enter a DLQ with a safe replay procedure. Add correlation IDs and never log secrets.

### Test scenarios
- Duplicate request with same key returns one order.
- Two concurrent requests cannot oversell one item.
- Transaction failure does not leave partial order state.
- Provider timeout does not cause duplicate side effects.
- Duplicate/out-of-order webhook is handled safely.
- Slow database call respects deadline.
- Load test reports throughput, p50/p95/p99, error rate, and DB saturation.
- Restore a backup into isolation and verify the application can use it.

### Interview questions
1. Why is a unique DB constraint stronger than an in-memory key check?
2. What if the DB commits but event publication fails?
3. Which errors are safe to retry?
4. How do you prevent a retry storm?
5. How do you find N+1 queries?
6. How do liveness and readiness differ?
7. How do you prove backups are restorable?
8. Which checkout SLI reflects user experience?
9. When is a modular monolith better than microservices?
10. What changes in multi-region operation?

## Quick revision map
- Correctness: idempotency, races, locks, transactions, schema evolution.
- Resilience: timeouts, retries, backoff, circuit breakers, backpressure, failover.
- Scale: pools, indexes, caching, load balancing, queues, autoscaling.
- Security: SQL injection, XSS, CSRF, SSRF, OAuth, IAM, TLS, secrets.
- Delivery: Docker, CI/CD, IaC, feature flags, canary, rollback, probes.
- Operations: logs, metrics, traces, SLI/SLO, error budgets, incidents, postmortems.

## Primary references
- Node.js: https://nodejs.org/docs/latest/api/
- PostgreSQL: https://www.postgresql.org/docs/current/
- MDN: https://developer.mozilla.org/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- RFC Editor: https://www.rfc-editor.org/
- Kubernetes: https://kubernetes.io/docs/
- Docker: https://docs.docker.com/
- Terraform: https://developer.hashicorp.com/terraform/docs
- OpenTelemetry: https://opentelemetry.io/docs/
- Google SRE books: https://sre.google/books/
