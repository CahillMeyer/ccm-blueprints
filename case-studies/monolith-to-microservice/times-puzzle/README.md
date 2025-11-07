# Case Study: Monolith to Microservice (Strangler Fig Pattern)
### Project: The "Times Puzzle"

This repository is a tangible case study demonstrating the **Strangler Fig Pattern** for legacy modernization. It simulates the process of extracting a single piece of business logic from an older, monolithic application into a modern, independent microservice.

### The Scenario

We have a hypothetical legacy system, a **C++ command-line tool** (`times-puzzle-legacy/`), that solves a "Times Puzzle". This tool is critical, but it's difficult to maintain, integrate with new web applications, or scale.

The goal is *not* a full, high-risk rewrite. Instead, we strategically "strangle" the monolith by identifying its core logic (the puzzle solver) and extracting it into a new, modern service (`times-puzzle-modern/`).

---

### 1. The Legacy Monolith (`/times-puzzle-legacy`)

* **Tech:** C++
* **Role:** Simulates the original, aging application. It contains all logic: UI (command-line), business logic (the solver), and data handling, all tightly coupled in one executable.

### 2. The Modern Microservice (`/times-puzzle-modern`)

* **Tech:** Python, FastAPI, Docker
* **Role:** This is the new, extracted component.
    * **Isolated Logic:** The core "puzzle-solving" algorithm has been isolated and rewritten in Python for clarity and maintainability.
    * **API-fication:** This logic is wrapped in a high-performance **FastAPI** REST API.
    * **Scalable:** The service is containerized with **Docker**, ready to be deployed to any modern cloud (like AWS) and scale independently.

### Strategic Value (Why this matters)

This pattern demonstrates the core of my **Legacy Modernization Strategy**:

1.  **De-Risk the Project:** We don't touch the stable, working monolith. We build *around* it.
2.  **Incremental Value:** The new microservice can be used *immediately*—both by new web clients and even by the original C++ app (which could be refactored to call this API instead of its internal function).
3.  **Future-Proof:** The legacy app can now be slowly and safely decommissioned, one piece at a time.