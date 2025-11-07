# Case Study: Monolith to Microservice (Strangler Fig Pattern)
### Project: The "Times Puzzle"

This directory is a tangible case study demonstrating the **Strangler Fig Pattern** for legacy modernization. It simulates the process of extracting a single piece of business logic from an older, monolithic application—in this case, a **C++ Unreal Engine prototype**—into a modern, independent microservice.

### The Scenario

We have a hypothetical legacy component, a **C++ Unreal Engine prototype** (`unreal-engine/`), that contains critical business logic for a "Times Puzzle." This logic is "trapped" within the C++ game framework, making it impossible to integrate with new web applications or scale independently.

The goal is *not* a full, high-risk rewrite. Instead, we strategically "strangle" the monolith by identifying its core logic (the `TImesPlayTest` solver) and extracting it into a new, modern microservice (`fastapi-backend/`).

---

### 1. The Legacy Component (`unreal-engine/`)

* **Tech:** C++ (Unreal Engine)
* **Role:** Simulates the original, aging component. It contains the core business logic (the puzzle solver) tightly coupled with the Unreal game framework (e.g., `UTestActorComponent`). This makes the logic difficult to access from outside the game engine.

### 2. The Modern Microservice (`fastapi-backend/`)

* **Tech:** Python, FastAPI, Docker
* **Role:** This is the new, extracted component.
    * **Isolated Logic:** The core "puzzle-solving" algorithm from `TImesPlayTest.cpp` has been ported to clean, maintainable Python (`logic.py`).
    * **API-fication:** This logic is wrapped in a high-performance **FastAPI** REST API, making it accessible to any modern web or mobile application.
    * **Scalable:** The service is containerized with **Docker**, ready to be deployed to any modern cloud (like AWS) and scale independently of the original monolith.

### Strategic Value (Why this matters)

This pattern demonstrates the core of my **Legacy Modernization Strategy**:

1.  **De-Risk the Project:** We don't touch the stable, working monolith. We build *around* it.
2.  **Incremental Value:** The new microservice can be used *immediately*—both by new web clients and even by the original C++ app (which could be refactored to call this API instead of its internal function).
3.  **Future-Proof:** The legacy app can now be slowly and safely decommissioned, one piece at a time.