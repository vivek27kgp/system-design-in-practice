# Low-Level Design (LLD) Roadmap

> **Phase 1: LLD concepts (Days 1–17)** → **Phase 2: LLD interview problems (Days 18–28)**
> Language: **Python 3.12** (`abc`, `dataclasses`, `enum`, type hints, `threading`) · Tests: **pytest** · Diagrams: **Mermaid** (GitHub renders it natively) · Console visuals: **rich**
> Then continue to [HLD_ROADMAP.md](HLD_ROADMAP.md). Track daily progress in [PROGRESS.md](PROGRESS.md).

---

## How every topic is taught

Every concept goes through the same 5 steps, simplest first:

| Step | What | Example (Strategy pattern) |
|---|---|---|
| **1. Real-life analogy** | One everyday situation that *is* the concept | Google Maps: same trip, but you choose car, bike or walk, and the route changes |
| **2. Tiny example** | ≤ 30 lines, runs with one command, no frameworks | `Navigator(route_strategy=Walk()).route("A", "B")` |
| **3. Practical build** | A small but realistic program, with tests | Payment checkout where UPI, card and wallet are swappable strategies |
| **4. Visualise** | See it work: a diagram plus a console demo that prints each step | Mermaid class diagram + a `rich` table showing which strategy ran |
| **5. Push** | Notes, code, tests and diagram go to GitHub | `day-08: strategy + observer` |

> **Rule:** if you can't explain the concept with the analogy in 2 sentences, we don't move on.

---

## Why this order (and why the repos you found disagreed)

The repos you found are different *kinds* of resource:

| Resource | What it really is | Use it for |
|---|---|---|
| ByteByteGo `system-design-101` | A collection of visual HLD cheat-sheets with **no sequence** | Revision & visual ideas (HLD phase) |
| `system-design-primer` | An HLD concept index with almost no LLD | HLD phase |
| GeeksforGeeks | Encyclopedia-style articles of uneven quality | One-off definitions only |
| `awesome-low-level-design`, AlgoMaster, Hello Interview | **Sequenced LLD curricula** | ✅ The spine of this roadmap |

The current LLD curricula all agree on this order:

**OOP → class relationships → design principles → SOLID → UML → design patterns → concurrency → interview framework → problems**

Each step uses vocabulary from the step before it:
- You can't judge "Open/Closed" until you understand polymorphism.
- Patterns are just principles applied to recurring situations.
- Concurrency comes last because interviewers ask you to make a *working* design thread-safe; they don't expect you to start with it.

---

## Source key (open these alongside each day)

All the concepts are language-agnostic. Where a source's code is in Java, read it for the *idea* and write your own in Python.

| Key | Source | Best for |
|---|---|---|
| **AL** | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) (~28k ⭐) | **Main spine.** Concepts, concurrency, and 30+ problems with **Python solutions** |
| **AM** | [AlgoMaster LLD](https://algomaster.io/learn/lld/how-to-learn-lld) | Structured lessons (freemium) and a [concurrency module](https://algomaster.io/learn/lld/handling-concurrency) |
| **HI** | [Hello Interview LLD](https://www.hellointerview.com/learn/low-level-design) | The interviewer's view: delivery framework, which patterns actually matter |
| **RG** | [refactoring.guru](https://refactoring.guru/design-patterns/catalog) | **Best daily pattern reference**: illustrations, real-world analogies, **Python code** for every pattern |
| **PP** | [faif/python-patterns](https://github.com/faif/python-patterns) | Idiomatic Python implementations of the patterns |
| **HF** | *Head First Design Patterns*, 2nd ed. (O'Reilly) | Book for real intuition (Java code, but the ideas are what matter) |
| **CC** | [Concept && Coding: LLD Basics to Advanced](https://www.youtube.com/playlist?list=PL6W8uoQQ2c61X_9e6Net0WdYZidm7zooW) (YouTube, Hindi/English) | Pattern and problem walkthroughs, popular for Indian interviews (Java code) |
| **OK** | [Christopher Okhravi: Design Patterns](https://www.youtube.com/playlist?list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc) (YouTube) | *Why* each pattern exists; follows Head First chapter by chapter |
| **SC** | [sudoCode: LLD Primer](https://www.youtube.com/playlist?list=PLTCrU9sGybupCpY20eked6blbHI4zZ55k) (YouTube) | Short, beginner-friendly basics |
| **DP** | [design-patterns-for-humans](https://github.com/kamranahmedse/design-patterns-for-humans) (~49k ⭐) | Each pattern explained in plain English with a real-world example |
| **WT** | [workat.tech Machine Coding](https://workat.tech/machine-coding) | How the Indian machine-coding round works (Flipkart, Swiggy, Uber…) |
| **GK** | [Grokking OOD (mirror)](https://github.com/tssovi/grokking-the-object-oriented-design-interview) | UML-heavy case studies for 16 classic problems |
| **KL** | [kumaransg/LLD](https://github.com/kumaransg/LLD) | Company-tagged machine-coding problems (Flipkart, Navi, Udaan…) |
| **PT** | [Python Tutor](https://pythontutor.com) | Visualises objects and references step by step (great for Days 1–2) |

---

## Daily loop (≈2–3 hrs)

1. **Analogy + tiny example** (15 min): understand the idea in plain words first.
2. **Learn** (45 min): read or watch the day's sources.
3. **Build**: the practical, plus `pytest` tests.
4. **Visualise**: a Mermaid diagram in the README, plus a demo script that prints each step.
5. **Note**: write the day's `README.md` with the analogy, key ideas, the diagram, mistakes you made, and **5 interview questions with answers**.
6. **Commit & push**: `git commit -m "day-NN: <topic>"`, then tick the day in [PROGRESS.md](PROGRESS.md).

### Repo layout (set up on Day 1)

```
lld/
├── requirements.txt          # pytest, rich
└── dayNN_<topic>/            # a Python package; run from repo root: python -m lld.dayNN_<topic>.demo
    ├── __init__.py
    ├── README.md             # analogy → notes → Mermaid diagram → interview Qs
    ├── example.py            # the tiny ≤30-line example
    ├── <build>.py            # the practical
    ├── demo.py               # run me: prints the visual step-by-step walkthrough
    └── test_<build>.py       # pytest
```

---

## PHASE 1: LLD Concepts (Days 1–17)

### Week 1: Foundations

| Day | Topic | 🧠 Simple real-life example | 🛠️ Build (practical) | 👀 Visualise | 📚 Study from |
|---|---|---|---|---|---|
| **1** | **Setup + OOP pillars:** class vs object; encapsulation, abstraction, inheritance, polymorphism; Python `abc`, `@dataclass`, `Enum`, `__eq__`/`__hash__`, `@property` | A **car**: you press the pedal (*abstraction*) without seeing the engine, which is sealed inside (*encapsulation*). Every vehicle has wheels (*inheritance*). "Horn" sounds different on a bike and a truck (*polymorphism*) | Git repo, venv, `requirements.txt`, root README. `Shape` → `Circle`/`Rectangle` (`area()` polymorphism); a `BankAccount` that blocks a negative balance | Run the objects through **Python Tutor**; Mermaid class diagram | AL (OOP), SC, RG |
| **2** | **Class relationships:** association, aggregation, composition, dependency; **composition over inheritance** | **Teacher–Student** (association: they know each other). **Team–Players** (aggregation: players survive if the team breaks up). **House–Rooms** (composition: no house, no rooms). **Driver uses a taxi** (dependency) | Refactor an inheritance mess (`FlyingDuck`, `RubberDuck`…) into composition with pluggable behaviours | Mermaid diagram showing every arrow type, before and after | AL (Class Relationships), HF ch.1 |
| **3** | **Design principles:** DRY, KISS, YAGNI, Law of Demeter, coupling vs cohesion, **code smells** | **DRY**: writing your address in 5 forms when one saved profile would do. **YAGNI**: buying a 10-seater car "just in case". **Demeter**: you pay the shopkeeper; you don't hand them your wallet | Take a deliberately messy 150-line "God class" order processor and refactor it in small commits | Before/after diagram + a smell → fix table | AM, RG ([code smells](https://refactoring.guru/refactoring/smells)) |
| **4** | **SOLID (1):** SRP, OCP, LSP | **SRP**: a chef cooks; they don't also do the accounting. **OCP**: a phone gets new apps without being opened up. **LSP**: a toy duck that needs batteries isn't a real substitute for a duck | One "bad" and one "fixed" version per principle (discount calculator for OCP; Rectangle/Square for LSP) | Diagram per principle | AL (SOLID), CC (SOLID) |
| **5** | **SOLID (2):** ISP, DIP + **dependency injection** | **ISP**: a short menu per need, not one giant form. **DIP**: your laptop depends on the *socket standard*, not on the power plant, so any plug that fits works | A notification service where Email, SMS and WhatsApp senders are injected; tests use a fake sender | Dependency arrows before and after inverting them | AL, HI (Design Principles) |
| **6** | **UML that interviews use:** class (first), sequence, state, use-case (briefly) | **Class diagram** = a house blueprint. **Sequence diagram** = ordering at a restaurant (you → waiter → kitchen → waiter → you). **State diagram** = a traffic light | Model an ATM withdrawal in all 3 diagrams, then code its card-session states | 3 Mermaid diagrams (`classDiagram`, `sequenceDiagram`, `stateDiagram-v2`) | GK (UML), AL (UML) |
| **7** | **Week 1 review + mini-project** | A **library**: members borrow and return books, with late fees | Small and complete, with tests, using everything from Days 1–6 | Full class diagram + a demo run | Self-review against the SOLID checklist |

### Week 2: Design patterns (each tied to an everyday example)

> **Calibration from Hello Interview:** interviewers really probe about **5 patterns**, and most good designs use 0–2 of them. Learn all the ⭐ must-knows, but never force a pattern into a design. ◽ = nice-to-know.

| Day | Patterns | 🧠 Simple real-life example | 🛠️ Build (practical) | 👀 Visualise | 📚 Study from |
|---|---|---|---|---|---|
| **8** | ⭐ **Strategy**, ⭐ **Observer** | **Strategy**: Google Maps with car, bike or walk; same trip, swappable route logic. **Observer**: YouTube's 🔔 subscribe bell; one upload notifies every subscriber | Checkout with UPI/card/wallet strategies; stock-price alerts to multiple subscribers | Class diagrams; a `rich` console log of notifications fanning out | HF ch.1–2, OK ep 1–2, RG |
| **9** | ⭐ **Factory** (Simple + Factory Method), ◽ Abstract Factory, ⭐ **Singleton** (and why DI is usually better) | **Factory**: at a pizza shop you say "Margherita" and they build it. **Abstract Factory**: an IKEA *collection*, where chair, table and lamp all match one style. **Singleton**: a country has exactly one president | Vehicle factory; light/dark UI theme family; a config holder written as a Singleton and then with DI | Diagrams; a demo where 2 threads break a naive Singleton | HF ch.4–5, RG, DP |
| **10** | ⭐ **Builder**, ◽ Prototype | **Builder**: ordering at Subway, step by step (bread → filling → sauce → done). **Prototype**: photocopy a filled form and change only the name | An `HttpRequest` builder with validation; cloning document templates | Builder-chain diagram | RG, PP |
| **11** | ⭐ **Decorator**, ⭐ **Adapter**, ⭐ **Facade** | **Decorator**: coffee + milk + sugar, each layer adding cost. **Adapter**: an Indian-to-UK travel plug adapter. **Facade**: a hotel reception desk, one counter for many services | Coffee pricing with add-ons; wrap a "legacy" payment API; a `start_movie()` home-theatre facade | Wrapper-nesting diagram | HF ch.3, 7; OK |
| **12** | ⭐ **State**, ⭐ **Command** | **State**: a traffic light, which behaves differently in red, yellow and green. **Command**: TV remote buttons and **Ctrl+Z** (each action is an object, so it can be undone) | Order lifecycle (placed → paid → shipped → delivered); a text editor with undo/redo | **State diagram** + the undo stack printed live | HF ch.6, 10; CC (vending machine) |
| **13** | ⭐ **Chain of Responsibility**, ⭐ **Template Method**, ◽ Iterator, ◽ Composite, ◽ Proxy | **CoR**: customer support escalation, L1 → L2 → manager. **Template**: making tea vs coffee (same steps, different ingredients). **Iterator**: the TV "next channel" button. **Composite**: folders inside folders. **Proxy**: a security guard who checks before letting you in | Logger levels (CoR); data export pipeline (Template); folder size calculator (Composite); caching proxy | A request flowing through the chain; folder tree printout | RG, HF ch.8–9, 11 |
| **14** | ◽ Mediator, Memento, Bridge, Flyweight, Visitor + **anti-patterns** + a **pattern-picking cheat sheet** | **Mediator**: air traffic control. **Memento**: a game save point. **Flyweight**: every "a" on screen shares one font object. **Bridge**: any remote works with any TV brand | One tiny example each + `pattern-cheatsheet.md` ("if the problem says X → think of Y") | Comparison table | RG, DP |

### Week 3a: Concurrency for LLD

> Engineers at 2–5 YOE are expected to discuss concurrency; at your level it sets you apart. In Python we also cover **what the GIL does and doesn't protect you from**: `count += 1` can still race.

| Day | Topic | 🧠 Simple real-life example | 🛠️ Build | 👀 Visualise | 📚 Study from |
|---|---|---|---|---|---|
| **15** | **Correctness:** threads, race conditions, the GIL, `threading.Lock`/`RLock`, atomic operations, thread-safe collections | **Race condition**: a joint bank account with ₹100, and two people withdraw ₹100 at two ATMs at the same moment. **Lock**: the single bathroom key at a café | A counter that gives the wrong total under 100 threads, fixed with a lock; a thread-safe bank account | `rich` timeline of thread interleavings (who read, who wrote, when) | AL (Concurrency), AM (concurrency module), HI |
| **16** | **Coordination and scarcity:** `Condition`, `Semaphore`, **producer-consumer** with `queue.Queue`, `ThreadPoolExecutor`, reader-writer, **deadlock** (cause and prevention) | **Producer-consumer**: a chef puts dishes on a counter with 5 slots and waiters take them. **Semaphore**: a parking lot with 10 spots. **Thread pool**: a call centre with 5 agents. **Deadlock**: two cars facing each other on a one-lane bridge | Your own bounded blocking queue; a DB connection pool using `Semaphore`; trigger a deadlock and then fix it with lock ordering | Live console bar of queue fill level and blocked/waiting threads | AL (concurrency problems), AM |
| **17** | **The LLD interview framework and the machine-coding round** | A rehearsed recipe beats improvising | Write `lld-interview-playbook.md` (below); warm up with **Tic-Tac-Toe** in 45 min | — | HI (Delivery Framework), WT |

**LLD interview playbook (Day 17)**

| Step | What to do | Time |
|---|---|---|
| 1 | Clarify requirements and scope: what's in, what's out | 3–5 min |
| 2 | Identify the core entities (nouns) and actions (verbs) | ~5 min |
| 3 | Define the relationships and draw the class diagram | ~10 min |
| 4 | Define the public APIs (method signatures) | ~5 min |
| 5 | Code the core flow first, then edge cases. Keep it runnable with a `demo.py` | Most of the time |
| 6 | Cover extensions ("add a new X"), concurrency, and tests | ~10 min |

**Machine-coding round** (Flipkart, Swiggy, Uber, CRED, Navi, Udaan…):
- **Format:** 90–120 minutes. The code must run, using in-memory storage and no UI. A code review follows.
- **What they judge:** separation of concerns, extensibility, and explicitly modelled states.

---

## PHASE 2: LLD Interview Problems (Days 18–28)

Rules for every problem:
- **Start simple, then grow.** Get the smallest version (🌱 column) working first, then add features one commit at a time. That's also the right approach in the interview.
- **Time-box it.** 90 min to code, then 30 min to review.
- **Required outputs:**
  - a requirements list
  - a Mermaid class diagram
  - runnable code with `demo.py`
  - pytest tests
  - a README covering trade-offs and "what if" extensions
- **Compare only after your own attempt.** Check AL, CC or HI afterwards.

The problems are ordered by **interview frequency** (Tier 1 first), after one easy warm-up.

| Day | Problem | Tier | 🌱 Start with the simplest version | Key patterns and concepts | ⬆️ Then add |
|---|---|---|---|---|---|
| **18** | **Parking Lot** | 1 | 1 floor, cars only, park/leave | Strategy (spot allocation, pricing), Factory, Enum | Floors, vehicle types, hourly pricing, a **thread-safe last spot** |
| **19** | **Snake & Ladder** + Connect Four | 1 | 2 players, fixed board, one die | Game loop, board/player separation | Configurable board, pluggable dice strategy |
| **20** | **Vending Machine** (+ coffee machine variant) | 1 | 1 product, exact coins only | **State** pattern (the centrepiece) | Multiple products, change-making, refunds |
| **21** | **LRU Cache** + **Logging framework** | 1 / 2 | `get`/`put` with capacity; logger with 2 levels | HashMap + doubly linked list; Chain of Responsibility | Thread safety + TTL; multiple log sinks (file, console) |
| **22** | **Elevator system** | 1 | 1 lift, requests served in order | State, Strategy (SCAN/LOOK scheduling), Command | Multiple lifts + a dispatcher |
| **23** | **Splitwise** | 1 | Equal split among friends, show balances | Strategy (equal/exact/percent) | **Debt simplification** (minimise the number of transactions) |
| **24** | **BookMyShow** | 1 | 1 show, pick a seat, book it | Entity modelling, booking states | **Seat locking**: 2 users want the same seat; hold with a timeout |
| **25** | **Rate Limiter** + **Pub-Sub / message queue** | 2 | Fixed window, 1 user; 1 topic, 1 subscriber | Strategy (token bucket, sliding window); Observer; concurrency | Per-user limits; multiple subscribers; at-least-once delivery |
| **26** | **Food delivery (Swiggy/Zomato)** or **ATM** | 2 | Place an order → deliver it; withdraw cash | Order state machine, Strategy (rider assignment), Observer | Coupons; cash dispenser via CoR (₹500 → ₹200 → ₹100) |
| **27** | **Chess** | 1 | Board + pawns only, valid moves | Polymorphic pieces, Command (move history) | All pieces, check detection, undo |
| **28** | 🎯 **Mock machine-coding round** (90 min, unseen problem): Ride-sharing (Uber), Hotel booking, or a problem from KL | 2 | Your call: that's part of the test | Everything | Self-review against the [checklist](#self-review-checklist) |

### Bonus problems (catch-up days / weekends; Tier 2–3)

Library Management · Hotel Booking · Car Rental · Notification System · Inventory Management (Zepto) · Digital Wallet / Payment Gateway · Amazon Locker · File System (Composite) · Task Scheduler · Stock Brokerage · Event Calendar (Flipkart) · Cricinfo · Stack Overflow · Thread-safe blocking queue

### Self-review checklist

- [ ] Each class has one reason to change (SRP).
- [ ] New types plug in without editing existing code (OCP). Ask yourself "add a new X".
- [ ] Code depends on abstractions (ABC/Protocol), with dependencies injected rather than created inside.
- [ ] States are modelled explicitly (Enum or State pattern), not as boolean flags.
- [ ] There's no business logic in `demo.py`/the controller.
- [ ] Edge cases are handled: invalid input, empty or full, concurrency.
- [ ] It runs end-to-end and the tests pass.
- [ ] Names read like the domain: `ParkingSpot`, not `data2`.

---

## Phase checkpoints

| After | You should be able to |
|---|---|
| Day 7 | Explain every SOLID principle with its real-life analogy, spot violations, and draw a class diagram for any small system |
| Day 14 | Hear "undo", "notify", "swap algorithm" or "wrap" and name the matching pattern, with its analogy |
| Day 17 | Make an existing design thread-safe, and walk through the interview framework |
| Day 28 | Solve an unseen LLD problem in 90 minutes with runnable, tested, extensible code |

➡️ **Next:** [HLD_ROADMAP.md](HLD_ROADMAP.md) (Day 29 onwards)
