# Times Puzzle (UE4/5 Prototype)

This is a small **Unreal Engine C++ prototype** that generates multiplication
puzzle rounds. It fairly cycles through factor pairs and presents them in a
game-like way, similar to a crossword but with numbers.

## Features
- Fair selection of products by least-used factor pairs
- Shuffles numbers to include the correct factors and distractors
- Validates guesses and updates usage counts
- Exposed to Blueprints via `UTestActorComponent`:
  - `GetNumbers(int& product, int size)`
  - `CheckFactors(int a, int b)`
  - `AllNumbersUsed()`

## Source Layout
```
Source/Times/
├─ Times.Build.cs
├─ Times.h
├─ Times.cpp
├─ TestActorComponent.h
├─ TestActorComponent.cpp
├─ TestGameModeBase.h
├─ TestGameModeBase.cpp
├─ TImesPlayTest.h   # capital I
└─ TImesPlayTest.cpp
```

## How to Build
1. Create a blank **C++ Unreal project** in UE 4.27+ or UE5.x.
2. Copy the `Source/Times` folder into your project’s `Source` directory.
3. Regenerate project files and build from the Unreal Editor or IDE.
4. Add the `UTestActorComponent` to an actor in your level.

## How to Play
- Call `GetNumbers(product, 9)` to create a puzzle round.
- Present the numbers in UI.
- On user selection, call `CheckFactors(a, b)` to validate.
- Continue until `AllNumbersUsed()` returns true.

## Roadmap
- Port logic to **FastAPI** backend
- Add a simple web UI to play the puzzle
- Unit tests for fairness and distribution

---

Unreal Engine © Epic Games. This repository only contains original C++ logic —
no proprietary Epic assets are included.