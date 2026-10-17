---
title: Tech Interview Study List — Detailed Engineering Notes
updated: 2026-10-17
source: "Tech Interview Study List by codersoni.pdf, uploaded 2026-10-17"
status: living-document
---

# Tech Interview Study List — Detailed Engineering Notes

This guide expands the uploaded 10-page checklist into a practical learning path. The PDF is a topic inventory, not a complete course. This file preserves its six main groups—Git, system design, Linux, JavaScript, AWS, and AI/ML—and adds explanations, implementation cues, examples, and exercises. The original checklist is attributed to its creator; these explanations are study notes.

## Recommended chronological order
1. Git and collaborative workflow.
2. Linux and shell fundamentals.
3. JavaScript language and asynchronous runtime.
4. TypeScript and Node.js.
5. System design fundamentals.
6. Databases, caching, messaging, and distributed systems.
7. AWS/cloud architecture and operations.
8. AI/ML and LLM application engineering.
9. End-to-end design drills and mock interviews.

## 1. Git: commands and collaboration

### Mental model
Git records snapshots as commits. A branch is a movable reference to a commit; a remote is another repository location. Working tree, staging area, and commit history are different states.

### Commands to practise
~~~bash
git init
git clone <repository-url>
git status
git add <path>
git commit -m "feat: validate order input"
git push
git fetch
git pull --rebase
git branch
git switch -c feature/order-validation
git merge main
git rebase main
git log --oneline --graph --decorate
git diff
git stash
git restore <path>
git revert <commit>
git reset --soft HEAD~1
git reset --mixed HEAD~1
git reset --hard HEAD~1
git cherry-pick <commit>
git tag v1.0.0
git reflog
git blame <path>
git show <commit>
git bisect start
git clean -n
git worktree add ../hotfix hotfix/urgent
~~~

### What the commands mean
- **Inspect:** status, log, diff, show, blame.
- **Collaborate:** add, commit, push, fetch, pull.
- **Branching:** branch, switch, merge, rebase, cherry-pick.
- **Undo:** restore discards working-tree changes; revert creates a new inverse commit; reset moves the branch pointer and can discard work.
- **Recover:** reflog can reveal previous local HEAD positions.
- **Debug history:** bisect locates a regression by testing commits.
- **Advanced:** worktree checks out multiple branches in separate directories; submodules pin another repository; clean removes untracked files.

### Branching, conflicts, and review
Short-lived branches and trunk-based development support fast feedback. Pull requests should explain intent, implementation, tests, risks, migrations, and rollback. Resolve conflicts by understanding both sides, not blindly accepting one. Do not rewrite shared history casually.

### Interview traps
- fetch downloads remote references; pull fetches and integrates.
- merge preserves branch topology; rebase replays commits onto a new base.
- reset --hard may destroy uncommitted work; inspect status and reflog before destructive recovery.
- .gitignore does not untrack files already committed. Never commit secrets.

### Exercise
Create a feature branch, make two commits, introduce a bug, use git bisect, revert the bad change, then resolve a merge conflict. Explain the difference between reverting and resetting.

## 2. Linux and shell fundamentals

### Mental model
Processes execute programs; files, permissions, sockets, mounts, signals, environment variables, and logs are the main operational interfaces.

### Commands grouped by purpose
~~~bash
# Files and navigation
pwd; ls -la; cd path; mkdir -p logs; touch app.log
cp source.txt backup.txt; mv old.txt new.txt; rm -i file.txt
cat file.txt; less file.txt; head -n 20 file.txt; tail -f app.log
grep -R "ERROR" logs/; find . -name "*.log"; wc -l app.log

# Processes, disk, memory, ports
ps aux; top; kill -TERM <pid>; df -h; du -sh .
free -h; lsof -i :3000; ss -lntp

# Text, archives, networking
sort names.txt | uniq
cut -d, -f1 data.csv
tar -czf backup.tar.gz data/
curl -I https://example.com
ping example.com; traceroute example.com
ssh user@host; scp file.txt user@host:/tmp/

# Services and environment
export NODE_ENV=production
printenv
systemctl status service-name
journalctl -u service-name --since "1 hour ago"
crontab -e
~~~

### Permissions
Unix permissions apply to owner/group/other. 755 means owner can read/write/execute and others can read/execute; 644 means owner can read/write and others can read. Execute on a directory means traversal. Avoid chmod 777 as a generic fix.

### Shell scripting
Use variables, quoting, loops, conditions, functions, and exit codes. Quoting prevents unwanted word splitting. Example:
~~~bash
#!/usr/bin/env bash
set -euo pipefail
: "\${APP_ENV:?APP_ENV must be set}"
echo "Deploying safely"
~~~
Understand the consequences of set -e and pipeline failures rather than copying them blindly.

### Production troubleshooting sequence
1. Is the process running? Check ps/systemctl.
2. Is the port listening? Check ss/lsof.
3. Can the host resolve/reach the dependency? Check DNS/curl.
4. Is disk or memory exhausted? Check df/free/top.
5. What do logs and exit codes say? Check journalctl/tail.
6. What changed recently? Review deployment, config, and dependency history.

Never run destructive commands on an unfamiliar host; inspect dry-run options first.

## 3. JavaScript: language fundamentals

### Values, scope, functions, and objects
Master var/let/const, primitive/reference values, coercion, truthiness, equality, scope/hoisting, closures, this, prototypes, classes, constructor functions, arrays, destructuring, spread/rest, callbacks, higher-order functions, currying, composition, call/apply/bind, optional chaining, nullish coalescing, immutability, Map/Set/WeakMap/WeakSet, and Symbols.

~~~js
const makeCounter = () => {
  let count = 0;
  return () => ++count;
};
const next = makeCounter();
console.log(next()); // 1
console.log(next()); // 2
~~~

The returned function closes over count. Closures are useful for encapsulated state, but can retain large objects unintentionally. Arrow functions capture lexical this; ordinary functions receive this based on how they are called.

### Arrays and copying
~~~js
const activeNames = users
  .filter(user => user.active)
  .map(user => user.name);
const label = config.title ?? "Untitled";
~~~
Spread makes a shallow copy; nested objects remain shared. structuredClone supports many structured values but not every value such as functions. Use immutability deliberately, especially when state updates rely on reference changes.

### Async JavaScript
Understand callbacks, promises, async/await, event loop, microtasks/macrotasks, Promise.all/race/allSettled/any, generators/iterators, debounce/throttle, and memoization.

~~~js
async function loadProfile(id) {
  const response = await fetch("/api/profiles/" + encodeURIComponent(id));
  if (!response.ok) throw new Error("HTTP " + response.status);
  return response.json();
}
~~~

Promise.all rejects when one input rejects, but does not automatically cancel other work. allSettled waits for every result. race settles with the first settled promise; any fulfills with the first fulfilled promise or rejects if all reject.

### Event-loop interview example
~~~js
console.log("A");
setTimeout(() => console.log("timer"), 0);
Promise.resolve().then(() => console.log("microtask"));
console.log("B");
// Typical browser output: A, B, microtask, timer
~~~
Know runtime-specific details instead of assuming one simplified event-loop model covers browsers and every Node.js phase.

### Browser/platform concepts
- DOM manipulation and event handling: learn capturing, target, bubbling, and event delegation.
- Fetch and JSON: handle non-2xx responses, network errors, cancellation, and schema validation.
- localStorage/sessionStorage/cookies: storage lifetime and security differ. JavaScript can read localStorage; HttpOnly cookies cannot be read by client JS.
- CORS: browser response-sharing policy, not authentication.
- Regex and Date/Intl: validate carefully and format locale/time zones intentionally.
- Service workers: request interception, offline cache, lifecycle, and cache versioning.
- Web workers: off-main-thread computation with message passing.
- Garbage collection/memory leaks: monitor retained objects, listeners, timers, and unbounded caches.
- Strict mode and modules: understand scope and module semantics.
- Polyfills: reproduce specified behavior, including edge cases; avoid overwriting built-ins casually.

### Debounce vs throttle
Debounce runs after calls pause; useful for search input. Throttle limits execution frequency; useful for scroll/resize events. Memoization caches a function's result for a key; bound the cache if inputs are unbounded.

### Exercise
Implement debounce, a concurrency-limited mapper, and a memoizer with a bounded cache. Test empty inputs, rejection, cancellation, and repeated keys.

## 4. TypeScript and Node.js

### TypeScript
Learn primitives, unions, narrowing, interfaces/type aliases, generics, utility types, discriminated unions, strict mode, async return types, and module resolution.
~~~ts
type Result<T> =
  | { ok: true; value: T }
  | { ok: false; error: string };

function unwrap<T>(result: Result<T>): T {
  if (!result.ok) throw new Error(result.error);
  return result.value;
}
~~~
Types disappear at runtime. Validate request bodies using runtime schemas; a TypeScript assertion is not validation.

### Node.js
Study event loop, modules, fs, streams, buffers, EventEmitter, npm scripts, HTTP, environment configuration, process signals, graceful shutdown, and package managers.
~~~js
import { createServer } from "node:http";
const server = createServer((req, res) => {
  res.writeHead(200, { "content-type": "application/json" });
  res.end(JSON.stringify({ ok: true }));
});
server.listen(process.env.PORT || 3000);
~~~
Avoid blocking the event loop with expensive synchronous work. Use streams for large files, bound concurrency, handle rejected promises, and close servers/database pools gracefully.

## 5. System design: problem-solving framework

### A repeatable interview sequence
1. Clarify users, core features, traffic, latency, availability, consistency, privacy, and budget.
2. Estimate QPS, storage, bandwidth, cache size, and growth; state assumptions.
3. Define APIs and data model.
4. Draw the simplest architecture that meets requirements.
5. Find bottlenecks and failure modes.
6. Add caches, queues, replicas, shards, or regions only when justified.
7. Discuss security, observability, cost, trade-offs, and future evolution.

### Architecture and scaling
- **Client-server:** clients request; server enforces business rules and accesses data.
- **Vertical/horizontal scaling:** bigger instance versus more instances.
- **Load balancing:** routes traffic; health checks and algorithm matter.
- **Monolith/microservices:** monolith simplifies local calls/deployment; services enable independent ownership/scaling but add network and operational failure modes.
- **API design:** REST, GraphQL, and gRPC have different caching, client flexibility, schema, streaming, and tooling trade-offs.
- **API gateway:** routing, policy, auth integration, quotas, and analytics.
- **Service discovery:** locate dynamic instances; health and authorization remain separate.
- **CDN/edge caching:** reduce origin load/latency; define cache key and protect private responses.
- **Fault tolerance/high availability:** redundancy, independent failure domains, tested failover, and graceful degradation.
- **Back-of-the-envelope estimates:** show assumptions and units; include peak factor, replication, and overhead.

### Data and consistency
- **SQL vs NoSQL:** choose based on relationships, query patterns, transactions, schema, and operations—not fashion.
- **Indexing/query optimization:** use explain plans; indexes speed some reads but cost storage and writes.
- **Sharding vs replication:** sharding splits data; replication copies it.
- **CAP/consistency/quorum:** understand partition trade-offs and read-after-write behavior.
- **ACID vs BASE:** transaction guarantees versus availability-oriented eventual convergence; not a simple SQL/NoSQL binary.
- **Isolation levels:** know read committed, repeatable read, serializable and database-specific behavior; dirty/non-repeatable/phantom reads and write skew.
- **Normalization/denormalization:** reduce update anomalies versus duplicate data for read efficiency.
- **Cache eviction:** LRU, LFU, FIFO each encode different assumptions; define TTL and invalidation too.
- **Caching patterns:** cache-aside, write-through, write-behind; write-behind risks lag/loss.
- **Idempotency:** repeated command has one logical effect.
- **Database partitioning:** split a table by key/time for manageability and pruning.
- **Distributed locks:** lease/ownership/fencing; not a magic global mutex.
- **Object storage:** durable blobs plus metadata, lifecycle, and signed URLs.
- **Search:** inverted index, tokenization, ranking, freshness, and eventual indexing.
- **Geospatial indexing:** geohash/quadtree/spatial indexes reduce candidates before exact distance checks.
- **Data lakes/warehouses/ETL:** raw and curated data, transformation, lineage, quality, governance, freshness.
- **Unique IDs:** UUID or time/worker/sequence schemes; consider collision, ordering, coordination, and privacy.

### Messaging and distributed workflows
- **Queues (Kafka/RabbitMQ/SQS concepts):** decouple producers/consumers; design delivery, ack, retry, ordering, replay, and idempotency.
- **Pub/Sub/event-driven systems:** independent consumers react to events; use event IDs, correlation, schema evolution, and outbox patterns.
- **Distributed transactions:** two-phase commit versus Saga; compensation is a new action.
- **Consensus/leader election:** Raft/Paxos concepts, quorum, terms, and split-brain prevention.
- **CQRS/event sourcing:** separate read/write models or persist domain events only when benefits justify added complexity.
- **Retries/backoff/circuit breakers/backpressure:** prevent cascading failures and retry storms.
- **Bloom filters:** probabilistic membership test with possible false positives; useful to avoid expensive absent-key lookups.
- **Gossip/heartbeats:** spread membership/liveness information; missing heartbeat does not prove a node is dead.
- **WebSockets/SSE/long polling:** bidirectional persistent channel, server-to-client stream, or repeated wait/reconnect.
- **Rate-limiting algorithms:** fixed window, sliding log/window, token bucket, and leaky bucket trade simplicity, accuracy, and burst tolerance.
- **SLA/SLO/SLI:** contractual promise, internal target, and measurement.
- **RPO/RTO and multi-region:** acceptable data-loss window and recovery time; regional failover must be tested.

### Example design: URL shortener
Requirements: create short link, redirect quickly, optional expiry and analytics. API: POST /links returns code; GET /{code} redirects. Store code, destination, owner, creation time, and expiry with a unique code constraint. Cache popular codes, queue analytics asynchronously, validate destinations, rate-limit abuse, and define deletion/privacy behavior. Discuss collision handling, read/write ratio, hot keys, multi-region reads, and cache invalidation.

### Example design: chat
Use WebSockets for active connections, durable message storage, per-conversation authorization, message IDs/order rules, push notifications for offline recipients, and catch-up after reconnect. Socket delivery does not equal durable delivery.

### Example design: news feed
Fan-out-on-write suits ordinary accounts with many reads; fan-out-on-read may suit huge-follower accounts. Hybrid approaches reduce write amplification. Add ranking, cursor pagination, cache invalidation, and privacy/block filtering.

### Example design: ride-sharing
Use geospatial candidate search followed by exact ETA/ranking, atomic driver assignment, explicit trip state, location freshness, idempotent payments, and strict location access/retention controls.

### Example design: video streaming
Upload to object storage, transcode asynchronously, distribute renditions via CDN, use adaptive bitrate, and monitor startup/rebuffering. Separate metadata/control plane from media delivery and account for egress cost.

### Example design: notifications/rate limiter
Use durable queues, user channel preferences, provider throttling, retries, DLQ, deduplication, and delivery telemetry. Choose rate limiter algorithm based on burst tolerance, accuracy, and storage cost.

## 6. AWS and cloud fundamentals

Service features and prices change; check official docs and pricing before deploying. Learn purpose, security boundary, failure modes, and cost model for each service.

### Compute and containers
- **EC2:** virtual machines, AMIs, instance types, security groups, attached disks, patching.
- **Lambda:** event-driven functions, concurrency, duration, cold starts, and retry semantics.
- **ECS/Fargate:** container orchestration with less cluster management.
- **EKS:** managed Kubernetes control plane; workload operations remain.
- **Elastic Beanstalk:** managed application deployment abstraction and customization trade-offs.

### Storage and databases
- **S3:** object storage, bucket policies, versioning, lifecycle, storage classes, replication, presigned URLs.
- **EBS:** block volumes, snapshots, and performance classes.
- **RDS/Aurora:** managed relational database, backups, failover, replicas, connection limits, maintenance.
- **DynamoDB:** key-value/document store; design partition/sort keys around access patterns.
- **ElastiCache:** Redis/Memcached; cache invalidation and failover still matter.
- **Redshift/Athena:** analytical warehouse/query over data; control scan and storage cost.

### Networking and edge
- **VPC:** subnets, route tables, internet/NAT gateways, and private/public resources.
- **Security Groups vs NACLs:** stateful interface-level rules versus stateless subnet-level rules.
- **Route 53:** DNS and routing policies; health checks and TTLs.
- **Elastic Load Balancing:** listener/routing/health-check layer.
- **CloudFront:** CDN cache policies, origin access, TLS, invalidation, and egress.
- **Regions/AZs/edge locations:** different failure and latency scopes; multi-AZ is not multi-region.

### Identity, security, and management
- **IAM:** policies, roles, trust, temporary credentials, least privilege.
- **KMS/Secrets Manager:** key lifecycle/encryption and managed secret storage/rotation.
- **Cognito:** user identity/authentication features; application authorization still matters.
- **Shared Responsibility Model:** provider secures cloud infrastructure; customer responsibilities vary by service and include data, identities, configuration, and application security.
- **Well-Architected Framework:** operational excellence, security, reliability, performance, cost optimization, sustainability.

### Messaging, workflows, analytics, and delivery
- **SQS:** durable queue, visibility timeout, DLQ, standard/FIFO behavior, idempotent consumers.
- **SNS:** publish/subscribe fan-out.
- **EventBridge:** event routing and rules.
- **Step Functions:** durable workflows with retry/catch and visible state.
- **Kinesis:** streaming ingestion, partition keys, throughput.
- **API Gateway:** API entry, auth integration, throttling, routing.
- **CloudWatch:** logs, metrics, alarms, dashboards.
- **CloudFormation/Terraform:** IaC, state, plans, drift, secrets.
- **CodePipeline/CodeBuild/CodeDeploy:** CI/CD components; compare with GitHub Actions.
- **AWS CLI/SDKs:** repeatable automation using roles/profiles; never commit access keys.
- **Cost management:** tags, budgets, Cost Explorer, pricing model, idle-resource cleanup.

### Cloud practical lab
Deploy a small HTTPS API, least-privilege identity, managed database, object storage, queue + worker, logs/alarms, and budget alert. Document assumptions, security, restore, and teardown. Do not leave paid resources running accidentally.

## 7. AI/ML and LLM engineering

### Classical ML foundations
- **ML basics:** define target, features, baseline, split, metric, and intended use.
- **Supervised vs unsupervised:** labeled prediction vs structure discovery.
- **Neural networks/deep learning:** layered parameterized models trained with gradients.
- **Train/validation/test:** train parameters, tune on validation, estimate final performance on held-out test. Avoid user/time/location leakage.
- **Overfitting/underfitting:** poor generalization from excessive complexity or insufficient capacity/learning.
- **Loss/gradient descent:** objective and parameter updates; know learning-rate effects.
- **Regression/classification:** continuous value vs class/probability.
- **Feature engineering:** transformations, missing data, encoding, scaling, and point-in-time correctness.
- **Bias-variance:** balance systematic error and sample sensitivity.
- **Regularization:** L1/L2, dropout, early stopping; tune without contaminating test.
- **Cross-validation:** repeated splits; use grouped/time-aware splits when random split leaks information.
- **Metrics:** precision/recall/F1/AUC for classification; MAE/RMSE for regression; choose by error cost.
- **Trees/Random Forest/Gradient Boosting:** splits, bagging, sequential boosting and trade-offs.
- **K-Means/PCA:** clustering/dimensionality reduction; scale features and validate assumptions.
- **Backpropagation/activations/optimizers:** gradients, nonlinearities, SGD/Adam, learning-rate schedules.
- **CNN/computer vision and RNN/LSTM:** spatial feature learning and sequence models; compare with current alternatives.
- **Transfer learning:** reuse pretrained representations.
- **RLHF:** preference feedback in alignment pipelines; understand reward model and policy-optimization limits.

### LLM and generative AI concepts
- **Tokenization/embeddings:** tokens represent text units; embeddings map content into vectors.
- **Transformers/attention:** contextual representations and attention computation.
- **LLMs:** probabilistic generation, not automatically a verified database.
- **Prompt engineering:** clear instructions, context, examples, constraints, and evaluation; prompts alone are not a security boundary.
- **Fine-tuning:** adjust behavior with curated examples; distinguish full fine-tuning from parameter-efficient methods.
- **RAG:** retrieve relevant documents, supply grounded context, generate, cite, and evaluate retrieval and answer quality.
- **Vector databases:** store embeddings/metadata; evaluate recall, filters, latency, freshness, and cost.
- **AI agents/tool use:** model selects tools within a bounded workflow; validate arguments and authorize every action in code.
- **Evaluation/benchmarks:** representative tasks, edge cases, regression tests, latency, and cost; avoid benchmark overfitting.
- **Safety/alignment/responsible AI:** mitigate harm, bias, privacy risk, and misuse; document residual risks.
- **Deployment/inference:** batching, caching, quantization, throughput, latency, model/version management.
- **Context window/temperature/top-k/top-p:** context limit and sampling controls; randomness settings do not ensure truth.
- **Hallucinations:** unsupported outputs; mitigate with retrieval, tools, constrained outputs, verification, and uncertainty.
- **Zero-shot/few-shot/reasoning-oriented prompts:** instruction-only or examples; evaluate outputs rather than assuming a generated explanation is correct.
- **LoRA/PEFT:** train adapters or a subset of parameters at lower cost.
- **Quantization/distillation:** reduce model size/compute or train a smaller student; measure quality loss.
- **Chunking/reranking/hybrid search:** split documents, retrieve candidates, rerank, combine lexical/vector signals, and evaluate context relevance.
- **Function calling/structured outputs:** validate schema and semantics; valid JSON may still be wrong.
- **MCP:** protocol for connecting AI apps to tools/context servers; treat tool results as untrusted and enforce permissions at the host.
- **Multi-agent systems:** use only when independent roles justify orchestration overhead; bound loops and budgets.
- **Multimodal models:** text/image/audio/video inputs; evaluate each modality and privacy implications.
- **Diffusion/generative models:** iterative denoising for generated content; evaluate conditioning and safety.
- **Prompt injection/guardrails:** separate trusted instructions from retrieved content, minimize privileges, validate inputs/outputs, and require confirmation for high-impact actions.
- **Data leakage/quality:** provenance, duplicates, missing values, label correctness, temporal splits, and privacy controls.
- **MLOps/LLMOps:** version data/models/prompts, track experiments, deploy reproducibly, monitor drift/quality/cost, and roll back.

### RAG implementation blueprint
~~~text
Ingestion: normalize documents -> chunk with overlap -> attach source/date/access metadata
           -> embed chunks -> store vectors and lexical index

Question: authenticate user -> filter documents by permissions
          -> retrieve lexical + vector candidates -> rerank
          -> build bounded context -> generate answer
          -> validate citations/schema -> record safe metrics and feedback
~~~

Never treat retrieval as authorization. A user must not receive a chunk they could not access in the source system. Evaluate retrieval recall, answer relevance, groundedness, citation correctness, and unanswerable-question behavior.

## 8. Interview implementation exercises

1. **Git/Linux:** resolve conflict, find a regression, diagnose a process that cannot bind to a port.
2. **JavaScript:** implement debounce, concurrency-limited mapping, and bounded memoization.
3. **Node/TypeScript:** build a validated REST API with structured errors, tests, request IDs, and graceful shutdown.
4. **Database:** design orders/inventory; demonstrate constraints, transactions, indexes, and EXPLAIN.
5. **System design:** URL shortener, chat, news feed, ride-sharing, video, notification service, rate limiter.
6. **Cloud:** deploy least-privilege service with secrets, alarms, backup/restore, and teardown.
7. **AI:** compare a baseline model, build a small RAG evaluation set, test prompt injection and authorization boundaries.

## 9. Self-assessment rubric

- **0 — Unseen:** cannot define the problem.
- **1 — Explain:** explain concept and trade-offs.
- **2 — Implement:** build a working example and test failure cases.
- **3 — Operate:** secure, deploy, observe, and debug it.
- **4 — Interview-ready:** compare alternatives, estimate capacity/cost, and defend decisions with assumptions.

Do not mark a topic complete merely because you watched a video. Use code, tests, and verbal explanation as evidence.

## Official reference starting points
- Git: https://git-scm.com/docs
- Linux man-pages: https://man7.org/linux/man-pages/
- JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript
- TypeScript: https://www.typescriptlang.org/docs/
- Node.js: https://nodejs.org/docs/latest/api/
- PostgreSQL: https://www.postgresql.org/docs/current/
- AWS: https://docs.aws.amazon.com/
- Kubernetes: https://kubernetes.io/docs/
- OWASP: https://cheatsheetseries.owasp.org/
- Google SRE books: https://sre.google/books/
- scikit-learn: https://scikit-learn.org/stable/user_guide.html
- PyTorch: https://pytorch.org/docs/stable/
- Hugging Face: https://huggingface.co/docs
- OpenTelemetry: https://opentelemetry.io/docs/

## Source checklist coverage
The uploaded PDF's major groups are all represented: Git; System Design (including classic design problems); Linux; JavaScript; AWS; AI/ML and LLMs. Use the PDF for exact checklist wording and this guide as the working explanation/implementation companion.
