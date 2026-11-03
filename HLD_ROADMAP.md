# High-Level Design (HLD) Roadmap

> **Phase 3: HLD concepts (Days 29–52)** → **Phase 4: HLD interview problems (Days 53–62)**
> Follows [LLD_ROADMAP.md](LLD_ROADMAP.md). Track daily progress in [PROGRESS.md](PROGRESS.md).
> Stack for practicals: **Python 3.12 (FastAPI)** for services · **Docker Compose** for Redis, Postgres, Kafka (Redpanda), nginx, MinIO, Prometheus and Grafana · **Locust** (Python) for load tests · **single-file HTML/JS** for interactive visualisations

---

## How every topic is taught

The method is the same as in LLD. Every concept goes through these 5 steps, simplest first:

| Step | What | Example (Caching) |
|---|---|---|
| **1. Real-life analogy** | One everyday situation that *is* the concept | Keeping a water bottle on your desk instead of walking to the kitchen every time |
| **2. Tiny example** | ≤ 30 lines, runs with one command | A Python `dict` in front of a function that sleeps for 1 second; the second call is instant |
| **3. Practical build** | A real setup that works like production, only smaller | FastAPI + Redis (Docker) in front of a slow endpoint |
| **4. Visualise** | See it happen: a chart, an animated HTML page, or a diagram | Hit/miss ratio and latency chart; 🌐 `viz/cache.html` |
| **5. Push** | Notes, code, compose file and visual go to GitHub | `day-35: caching + cdn` |

> **Rule:** if you can't explain the concept with the analogy in 2 sentences, we don't move on.

---

## Why this order

Every *sequenced* source agrees on the same arc: system-design-primer, karanpratapsingh/system-design, awesome-system-design-resources, chapter 1 of Alex Xu Vol 1, and Hello Interview's Core Concepts. The arc is:

**fundamentals & networking → building blocks in the request path → data layer → distributed-systems theory → async & messaging → architecture & reliability → specialised structures → problems**

The sources disagree on two points. Here is how this roadmap settles them:

| Disagreement | Our choice | Why |
|---|---|---|
| Where to teach **CAP** | Inside the data-layer week, after replication and sharding (karanpratapsingh's order). Not on day 1 as theory (the primer's order) | CAP only makes sense once you have *seen* replicas disagree |
| How to handle **back-of-envelope estimation** | Learn it early (Alex Xu). In interviews keep it to ~2 min, and only when it changes the design (Hello Interview) | Indian interviews usually still expect a quick estimate |

**ByteByteGo's system-design-101** is a set of visual cheat-sheets, not a course. Use it for **revision and visual inspiration**, not as the order to follow.

---

## Source key

| Key | Source | Best for |
|---|---|---|
| **KP** | [karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design) (~47k ⭐) | **Main free spine**: a sequenced 5-chapter "book" |
| **AX1 / AX2** | Alex Xu, *System Design Interview* Vol 1 / Vol 2 ([ByteByteGo](https://bytebytego.com)) | **Industry-standard problem walkthroughs**. Vol 1's chapter order runs easy → hard |
| **HI** | [Hello Interview: System Design](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction) + [YouTube](https://www.youtube.com/@hello_interview) | **The interview layer**: delivery framework, key technologies, 16 free problem breakdowns |
| **SDP** | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) (~376k ⭐) | Concept reference; latency and powers-of-two tables |
| **DDIA** | *Designing Data-Intensive Applications*, **2nd ed.** (Kleppmann & Riccomini, 2026) | Real depth on replication, partitioning, transactions, consistency, consensus and streams. Read the matching chapters only |
| **BBG** | [ByteByteGo system-design-101](https://github.com/ByteByteGoHq/system-design-101) + [ByteByteGo YouTube](https://www.youtube.com/channel/UCkXHjz_uUmrPJps7YxJXEyg) | Visual revision and ideas for your own diagrams |
| **GS** | [Gaurav Sen](https://www.youtube.com/@gkcs) (YouTube) | Intuition, with great analogies, for consistent hashing, sharding and queues |
| **JH** | [Jordan has no life](https://www.youtube.com/@jordanhasnolife5163) (YouTube) | DDIA-style depth once the basics are clear |
| **AB** | [Arpit Bhayani](https://arpitbhayani.me) (YouTube: @AsliEngineering) | How databases and real systems actually work inside |
| **HN** | Hussein Nasser (YouTube) | Backend fundamentals: TCP, HTTP/1-2-3, TLS, proxies |
| **AS** | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) (~43k ⭐) | Curated links, plus problems sorted by difficulty |
| **SCL** | [binhnguyennus/awesome-scalability](https://github.com/binhnguyennus/awesome-scalability) (~75k ⭐) | Index of real engineering-blog articles ("how company X did it") |
| **MIT** | [MIT 6.5840 Distributed Systems](https://pdos.csail.mit.edu/6.824/index.html) | Raft lecture now; labs after this plan |
| **CC** | Concept && Coding HLD series (YouTube) | Hindi/English; continues from the LLD phase |

> **Real-world reading:** on each problem day, read one engineering-blog post about the system you're designing (find it via SCL). For example, [How Discord stores trillions of messages](https://discord.com/blog/how-discord-stores-trillions-of-messages) on chat day.

---

## Daily loop & repo layout

The loop is the same as LLD:
1. Analogy + tiny example
2. Learn
3. **Build something that runs**
4. **Visualise it**
5. Notes + 5 interview Qs
6. Commit `day-NN: <topic>`
7. Tick [PROGRESS.md](PROGRESS.md)

```
hld/
├── dayNN-<topic>/           # README (analogy, notes, diagram, interview Qs) + example.py + code + docker-compose.yml
└── problems/<name>/         # design doc using the framework + mini prototype
docs/                        # 🌐 GitHub Pages: gallery of interactive visualisations
└── viz/<topic>.html         #    e.g. consistent-hashing.html, rate-limiter.html
```

The **`docs/` visualisation gallery** becomes a live site at `<username>.github.io/<repo>`, which you can link on your resume.

> ⚠️ **Install Docker Desktop before Day 34.** From then on, Redis, Postgres, Kafka and nginx run in containers.

---

## PHASE 3: HLD Concepts (Days 29–52)

### Week 5: Foundations & the request path

| Day | Topic | 🧠 Simple real-life example | 🛠️ Build (practical) | 👀 Visualise | 📚 Study from |
|---|---|---|---|---|---|
| **29** | **Scalability vocabulary:** vertical vs horizontal, latency vs throughput, availability "nines", SLA/SLO/SLI; "scale from zero to millions" | **Vertical**: a bigger kitchen. **Horizontal**: more kitchens. **Latency vs throughput**: a highway's speed limit vs its number of lanes. **99.9%** uptime = ~8.7 hours down per year | A tiny FastAPI server, load-tested with Locust; record p50, p95 and p99 | Latency histogram chart | AX1 ch.1, KP ch.I, SDP |
| **30** | **Back-of-envelope estimation:** latency numbers, powers of two, QPS, storage, bandwidth | Estimating how many cups of chai your city drinks per day from population × habits | Estimate WhatsApp's QPS and storage by hand, then verify with a script | 🌐 `viz/estimator.html`: DAU → QPS → storage calculator | AX1 ch.2, SDP (appendix) |
| **31** | **Networking:** OSI/TCP-IP, TCP vs UDP, DNS, HTTP/1.1 → 2 → 3, TLS | **TCP** = registered post with acknowledgement. **UDP** = a live cricket stream (a dropped frame is just skipped). **DNS** = your phone's contacts (name → number). **TLS** = a sealed envelope plus a verified ID | TCP and UDP echo servers in Python with a packet-loss mode; trace DNS with `nslookup` | Mermaid sequence diagrams of the DNS, TCP and TLS handshakes | HN, KP ch.I |
| **32** | **API design:** REST vs gRPC vs GraphQL; pagination, versioning, status codes, idempotency keys | **REST** = ordering from a fixed restaurant menu. **GraphQL** = a buffet where you pick exactly what you want. **gRPC** = a walkie-talkie with a fixed, compact protocol | The same "bookstore" API in REST (FastAPI) and gRPC; compare payload size and latency | Comparison chart | HI (API design), KP ch.III |
| **33** | **Real-time communication:** short polling, long polling, SSE, WebSockets | **Polling** = a kid asking "are we there yet?" every minute. **Long polling** = a waiter standing at your table until you decide. **SSE** = a radio broadcast. **WebSocket** = a phone call | One FastAPI server exposing all 4 methods | 🌐 A browser page with 4 panes showing messages and request counts live | KP ch.III, HI |
| **34** | **Load balancing:** L4 vs L7, algorithms (round robin, weighted, least connections, IP hash), health checks, reverse proxy, API gateway | **Load balancer** = a toll plaza sending cars to the shortest queue. **Reverse proxy** = an office receptionist. **API gateway** = a building's security desk that checks your ID and directs you | Your own Python LB over 3 backends, then nginx in Docker; kill a backend and watch failover | 🌐 `viz/load-balancer.html`: animated request routing per algorithm | KP ch.I, SDP, BBG |
| **35** | **Caching & CDN:** cache-aside, write-through, write-back, write-around; LRU/LFU; TTL & invalidation; **stampede** | **Cache** = a water bottle on your desk. **CDN** = Amazon's local warehouses near you. **Stampede** = everyone rushing into a shop the moment it opens | Redis in front of a slow endpoint; measure hit ratio; reproduce a stampede, then fix it with a lock | Hit/miss and latency chart; 🌐 `viz/cache.html` | HI (Caching, Redis), KP ch.I |

### Week 6: The data layer

| Day | Topic | 🧠 Simple real-life example | 🛠️ Build | 👀 Visualise | 📚 Study from |
|---|---|---|---|---|---|
| **36** | **Databases:** SQL vs NoSQL (key-value, document, wide-column, graph), ACID vs BASE, data modelling, normalisation vs denormalisation | **SQL** = an Excel sheet with strict columns. **Document DB** = a folder of forms, each filled differently. **ACID** = a bank transfer that happens fully or not at all | The same e-commerce model in Postgres and MongoDB (Docker); compare the queries | ER diagram (Mermaid `erDiagram`) | HI (Data modelling), KP ch.II, DDIA (data models) |
| **37** | **Indexing & storage engines:** B-tree vs LSM tree, `EXPLAIN ANALYZE`, composite indexes | **Index** = the index at the back of a book. **B-tree vs LSM** = a librarian who shelves each book immediately vs one who drops books in a tray and sorts the tray later | 1M rows in Postgres, timed with and without an index; a **mini LSM tree** in Python | Query plans; LSM levels diagram | DDIA (storage), AB, HI |
| **38** | **Transactions & isolation levels:** dirty reads, lost updates, write skew; optimistic vs pessimistic locking | Two people editing the same Google Sheet cell. **Pessimistic** = locking the meeting room. **Optimistic** = a Wikipedia "edit conflict" warning | Reproduce a lost update with 2 concurrent sessions, then fix it with `SELECT … FOR UPDATE` and with a version column | Timeline of the two sessions interleaving | DDIA (transactions), KP ch.II |
| **39** | **Replication:** leader-follower, multi-leader, leaderless; sync vs async; replication lag; read-your-writes | **Replication** = photocopies of one notice pinned in every building. **Lag** = some copies get updated late | Postgres primary + replica in Docker; measure lag; reproduce a stale read | Sequence diagram of a write flowing to the replica | DDIA (replication), KP ch.II |
| **40** | **Sharding** (range, hash, directory), hotspots, resharding + **consistent hashing** with virtual nodes | **Sharding** = splitting a phone directory into A–M and N–Z volumes. **Consistent hashing** = guests at a round table; one guest leaves and only their neighbour's share changes | A consistent-hash ring in Python; measure keys moved on adding a node vs `mod N` | 🌐 `viz/consistent-hashing.html`: interactive ring | AX1 ch.5, GS, DDIA (partitioning) |
| **41** | **CAP → PACELC → consistency models**; quorums (N, R, W) | Two bank branches lose their phone line: either stop serving customers (consistency) or serve and risk mismatched balances (availability). **Quorum** = a majority vote | Python sim of 3 replicas: cut the network, tune R and W, and see stale vs unavailable | 🌐 `viz/quorum.html` | AX1 ch.6, KP ch.II, DDIA (consistency) |
| **42** | **Unique IDs** (UUID, Snowflake) · **blob storage** (S3/MinIO, presigned URLs) · **search** (inverted index, Elasticsearch) | **Snowflake** = a token number built from time + counter + counter ID. **Blob storage** = a cloakroom (hand over the bag, get a ticket). **Inverted index** = searching recipes by ingredient | Snowflake ID generator; MinIO presigned upload; a mini search engine | Snowflake bit layout; inverted-index diagram | AX1 ch.7, HI (Elasticsearch) |

### Week 7: Async & distributed systems

| Day | Topic | 🧠 Simple real-life example | 🛠️ Build | 👀 Visualise | 📚 Study from |
|---|---|---|---|---|---|
| **43** | **Message queues vs pub-sub**; delivery guarantees (at-most-once, at-least-once, exactly-once); **Kafka** (topics, partitions, consumer groups, offsets) | **Queue** = a post box. **Pub-sub** = a newspaper subscription. **Kafka partitions** = multiple supermarket checkout lines, each keeping its own order | Redpanda/Kafka in Docker; producer + consumer group; kill a consumer and watch the rebalance | Partition → consumer assignment, before and after | HI (Kafka), KP ch.III, AX2 |
| **44** | **Event-driven architecture**, event sourcing, CQRS, stream basics (windows) | **Event sourcing** = a bank passbook (every transaction) vs storing only the balance. **CQRS** = separate "order here" and "pickup here" counters | Event-sourced bank account with projections; a per-minute click counter | Event log → projections diagram | KP ch.III, DDIA (streams), JH |
| **45** | **Microservices:** monolith vs microservices, service discovery, gateway, sync vs async calls | **Monolith** = one big restaurant. **Microservices** = a food court of independent stalls. **Service discovery** = the mall directory board | 2 FastAPI services + a gateway in `docker-compose` | Architecture diagram | KP ch.III–IV, BBG |
| **46** | **Rate limiting:** token bucket, leaky bucket, fixed window, sliding log, sliding-window counter; distributed limiting with Redis | **Token bucket** = a club bouncer handing out entry passes that refill each minute. **Leaky bucket** = a funnel that drains at a steady rate | All 5 algorithms + a Redis-backed limiter as middleware | 🌐 `viz/rate-limiter.html`: bucket filling and draining | AX1 ch.4, HI (Rate Limiter) |
| **47** | **Idempotency & distributed transactions:** 2PC, **saga**, **outbox**, distributed locks (+ fencing tokens) | **Idempotency** = pressing the lift button 5 times still calls one lift. **Saga** = a trip booking where, if the flight fails, you cancel the hotel. **2PC** = a wedding: both must say "I do" or nothing happens | An order → payment → inventory saga with compensations; idempotency-key middleware | Saga sequence diagram (success + failure paths) | KP ch.II–IV, DDIA (transactions) |
| **48** | **Consensus & coordination:** Raft (leader election, log replication), ZooKeeper/etcd, split brain | **Raft** = a class electing a monitor by majority vote. **Split brain** = two people both thinking they're captain | Play with the [Raft visualisation](https://raft.github.io/); a leader-election sim in Python with node crashes | 🌐 `viz/leader-election.html` | MIT (Raft lecture), DDIA (consensus), JH |
| **49** | **Reliability:** timeouts, retries + exponential backoff + **jitter**, circuit breaker, bulkhead, disaster recovery (RPO/RTO) | **Jitter** = after a network outage, everyone redials at the same instant unless they wait random amounts. **Circuit breaker** = your home's electrical fuse. **Bulkhead** = a ship's watertight compartments | A circuit breaker around a flaky service; compare retry storms with and without jitter | Retry-spike chart; circuit-breaker state diagram | KP ch.IV, SCL (Netflix posts) |

### Week 8a: Finishing touches

| Day | Topic | 🧠 Simple real-life example | 🛠️ Build | 👀 Visualise | 📚 Study from |
|---|---|---|---|---|---|
| **50** | **Observability** (logs, metrics, traces, p99, alerts) + **security** (authN vs authZ, sessions vs JWT, OAuth2/OIDC, TLS/mTLS) | **Observability** = a car dashboard. **AuthN vs authZ** = showing your ID at the gate vs which floors your badge opens. **JWT** = a signed concert wristband. **OAuth** = giving a valet a car key that only drives, not opens the boot | Prometheus + Grafana on the Day 45 services; JWT auth at the gateway | Grafana dashboard screenshot; OAuth sequence diagram | KP ch.IV, BBG |
| **51** | **Probabilistic & geo structures:** Bloom filter, count-min sketch, HyperLogLog, geohash, quadtree | **Bloom filter** = a bouncer who can say "definitely not on the list" or "maybe". **HyperLogLog** = estimating a crowd's size without counting everyone. **Geohash** = PIN codes for the planet. **Quadtree** = splitting a map into finer grids where it's crowded | Implement each in Python; measure error rate vs memory used | 🌐 `viz/quadtree.html` + `viz/bloom-filter.html` | AX2 (proximity), HI (deep dives), AB |
| **52** | **The HLD interview framework + common patterns:** scaling reads, scaling writes, contention, real-time updates, large blobs, long-running tasks | A rehearsed recipe beats improvising | Write `hld/hld-interview-playbook.md` (below); watch one full Hello Interview walkthrough | Template diagram | HI (Delivery framework & patterns), AX1 ch.3 |

**HLD interview playbook (Day 52)**

This 45-minute format merges the Alex Xu and Hello Interview frameworks.

| Step | What to do | Time |
|---|---|---|
| 1 | **Requirements:** 3 core functional requirements, plus 3–5 quantified non-functional ones (scale, latency, consistency vs availability, durability) | ~5 min |
| 2 | **Estimation:** QPS, storage, bandwidth, only as much as the design needs | ~2 min |
| 3 | **Core entities and data model** | ~3 min |
| 4 | **API:** REST by default; take the user from the auth token | ~5 min |
| 5 | **High-level design:** satisfy each API one by one with a box diagram | ~10–15 min |
| 6 | **Deep dives:** meet the non-functional requirements by working through bottlenecks, scaling, caching, sharding, consistency and failure modes | ~10 min |
| 7 | **Wrap-up:** trade-offs, what you'd monitor, what's next | ~2 min |

---

## PHASE 4: HLD Interview Problems (Days 53–62)

Do these steps for every problem, in `hld/problems/<name>/`:

1. **Your own design first.** Follow the playbook with a 45-minute timer. Draw the diagram in Excalidraw or Mermaid.
2. **Compare** with HI, AX1 or AX2, and write down what you missed.
3. **Build a mini prototype, starting simple.** Begin with the 🌱 version, then grow it one commit at a time, so you prove the design by running it.
4. **Read one real engineering-blog post** on that system (via SCL).

The problems go easy → hard, and the most frequently asked ones (Tier 1) come first.

| Day | Problem | Tier | Core lessons | 🌱 Start simple → ⬆️ grow the prototype | 📚 Study from |
|---|---|---|---|---|---|
| **53** | **URL Shortener** (Bitly) | 1 | ID generation, base62, read-heavy caching, 301 vs 302 | 🌱 Python dict in memory → ⬆️ FastAPI + Postgres → Redis cache → Locust load test | AX1 ch.8, HI |
| **54** | **Distributed KV store / cache** + **Rate limiter** (full design) | 1–2 | Consistent hashing, quorums, gossip; distributed rate limiting | 🌱 One-node dict server → ⬆️ 3 nodes on a hash ring (Day 40 code) → replication with quorum | AX1 ch.4, 6 |
| **55** | **Typeahead / autocomplete** | 1 | Trie + top-K, precomputation | 🌱 Trie over 100 words → ⬆️ top-5 by frequency → API + search box UI with live suggestions | AX1 ch.13 |
| **56** | **Notification system** + **Web crawler** | 1 | Queues, retries, dedup, politeness, Bloom filter | 🌱 Crawl 1 site, single-threaded → ⬆️ async workers → politeness delay → Bloom-filter dedup | AX1 ch.9–10 |
| **57** | **News feed / Instagram** | 1 | Fan-out on write vs read, the celebrity problem | 🌱 Feed = SQL query over the people you follow → ⬆️ precomputed Redis timelines → hybrid for celebrities; compare latencies | AX1 ch.11, HI (FB News Feed) |
| **58** | **Chat (WhatsApp)** | 1 | WebSockets, presence, delivery receipts, ordering | 🌱 2 browser tabs chatting over a WebSocket → ⬆️ online status → ✓✓ receipts → stored history | AX1 ch.12, HI (WhatsApp), Discord blog |
| **59** | **YouTube/Netflix** + **Dropbox/Google Drive** | 1 | Upload pipeline, transcoding, adaptive bitrate, CDN; chunking, dedup, sync | 🌱 Upload a whole file → ⬆️ split into chunks → hash-based dedup → resume an interrupted upload | AX1 ch.14–15, HI (YouTube, Dropbox) |
| **60** | **Ticketmaster/BookMyShow** + **Leaderboard / Top-K** | 2 | Contention, seat holds with TTL, idempotency; Redis sorted sets | 🌱 Book a seat in Postgres → ⬆️ 100 concurrent buyers (watch it break) → Redis hold with TTL; live leaderboard | HI (Ticketmaster, Top-K), AX2 (leaderboard) |
| **61** | **Uber / Yelp (proximity)** | 1–2 | Geohash/quadtree, high-frequency location updates, matching | 🌱 Nearest driver by brute force over 100 points → ⬆️ geohash index → 10k moving drivers on a map visual | AX2 (proximity), HI (Uber, Yelp) |
| **62** | **Payment system** + 🎯 **2 timed mock interviews** + final revision | 2 | Idempotency, double-entry ledger, reconciliation, saga | 🌱 A pay API → ⬆️ idempotency key (double click = one charge) → ledger table → reconciliation script | AX2 (payment, wallet); mocks: Exponent / HI / peer |

### Bonus problems (after Day 62, or on catch-up days)

Google Docs (OT vs CRDT) · Job scheduler · Ad-click aggregator · Metrics monitoring · Distributed message queue · S3-like object storage · Hotel reservation · Google Maps · Stock exchange · Digital wallet · Tinder · LeetCode (online judge) · **LLM/ChatGPT serving** (an emerging question in 2026)

---

## Phase checkpoints

| After | You should be able to |
|---|---|
| Day 35 | Trace a request from the browser through DNS, the load balancer, the app and the cache, explaining each hop with its analogy and its failure modes |
| Day 42 | Pick a database and justify the choice; explain replication, sharding and CAP using your own demo |
| Day 49 | Explain Kafka, sagas and Raft, and when you'd use each |
| Day 52 | Run the 45-minute framework on any prompt |
| Day 62 | Design 12+ classic systems from memory, each backed by a running prototype in your repo |

## After the plan (optional deep-end)

- MIT 6.5840 labs (MapReduce → Raft → sharded KV)
- The rest of DDIA (2nd ed.)
- Hello Interview's deep dives (vector DBs, time-series DBs, change data capture)
- Alex Xu Vol 2 in full
