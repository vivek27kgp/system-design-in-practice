# System Design in Practice

**Learning system design by building it.** Every concept, from OOP to distributed consensus, comes with a real-life analogy, runnable Python code, tests and a visual demo. One topic a day.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/tests-pytest-0A9EDC?logo=pytest&logoColor=white)
![Progress](https://img.shields.io/badge/progress-Day%201%20%2F%2062-blueviolet)

---

## 🧭 The method

Every topic goes through the same five steps:

| | Step | Example (Caching) |
|---|---|---|
| 🧠 | **Real-life analogy** | A water bottle on your desk instead of walking to the kitchen |
| ⚡ | **Tiny example** (≤ 30 lines) | A `dict` in front of a slow function |
| 🛠️ | **Practical build + tests** | FastAPI + Redis in front of a slow endpoint |
| 👀 | **Visualise** | Hit/miss and latency charts, diagrams, interactive pages |
| 🚀 | **Ship** | Notes, code and diagrams committed here |

## 🗺️ Roadmap

| Phase | Days | Focus | Plan |
|---|---|---|---|
| 1 · LLD concepts | 1–17 | OOP, SOLID, UML, design patterns, concurrency | [LLD_ROADMAP.md](LLD_ROADMAP.md) |
| 2 · LLD problems | 18–28 | Parking Lot, Elevator, Splitwise, BookMyShow, Chess… | [LLD_ROADMAP.md](LLD_ROADMAP.md#phase-2-lld-interview-problems-days-1828) |
| 3 · HLD concepts | 29–52 | Networking, caching, databases, sharding, Kafka, Raft… | [HLD_ROADMAP.md](HLD_ROADMAP.md) |
| 4 · HLD problems | 53–62 | URL shortener, WhatsApp, YouTube, Uber, payments… | [HLD_ROADMAP.md](HLD_ROADMAP.md#phase-4-hld-interview-problems-days-5362) |

📈 **Daily progress:** [PROGRESS.md](PROGRESS.md)

## 📂 What's inside

| Day | Topic | Folder |
|---|---|---|
| 01 | OOP pillars: encapsulation, abstraction, inheritance, polymorphism | [lld/day01_oop_pillars](lld/day01_oop_pillars/) |

## ▶️ Run it yourself

```bash
git clone https://github.com/vivek27kgp/system-design-in-practice.git
cd system-design-in-practice
python -m venv .venv
.venv\Scripts\activate          # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt

python -m pytest                              # run every test
python -m lld.day01_oop_pillars.demo          # run a day's visual demo
```

## 📚 Main references

- LLD: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design), [refactoring.guru](https://refactoring.guru/design-patterns), [Hello Interview LLD](https://www.hellointerview.com/learn/low-level-design)
- HLD: [karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design), Alex Xu's *System Design Interview* Vol 1 and 2, [Hello Interview](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction), *Designing Data-Intensive Applications* (2nd ed.)

The full source list, and the reasons for this order, are in each roadmap.
