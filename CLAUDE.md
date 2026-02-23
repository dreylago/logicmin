# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**logicmin** is a Python library for Boolean logic minimization using the Quine-McCluskey algorithm. It takes truth tables as input and produces minimized Sum-of-Products (SOP) expressions, with output in algebraic notation, VHDL, or Verilog syntax. It also supports finite-state machine (FSM) minimization with D and JK flip-flops.

## Commands

```bash
# Install in development mode
pip install -e .

# Run all tests (execfile-based, runs all examples)
python logicmin/tests/test_examples.py

# Run a single example
python logicmin/examples/full-adder.py
```

There is no linter, formatter, or CI configured.

## Architecture

The minimization pipeline flows: **TT (truth table) → prime implicants → PIT solver → Sol → expression output**.

### Core Modules

- **`tt.py`** — `TT` class: entry point. Users define truth tables with `add(input_bits, output_bits)`, then call `solve()` which returns a `MultiSol`.
- **`logic.py`** — The minimization engine. `prime_implicants()` implements Quine-McCluskey cube merging. `solve_PIT()` solves the Prime Implicant Table using essential row selection and dominated row elimination.
- **`cube.py`** — `Cube` class: represents a product term as a pair of bitmasks (`t` for true, `f` for false). Provides `varstr()`, `vhdl()`, `verilog()` methods for rendering in different syntaxes. Also contains free functions for cube manipulation (`combinable`, `combine`, `CombToCube`, etc.).

### Solution & Output

- **`sol.py`** — `Sol(SOP)`: wraps minimization results (cubes, cost, minimality flag) with `printSol()` for formatted output.
- **`sop.py`** — `SOP`: creates expression objects via `expr(xnames, syntax)`, dispatching to the appropriate renderer.
- **`expr2l.py`** — `Expr2L`: base expression renderer (algebraic: `.` for AND, `+` for OR, `'` for NOT).
- **`expr2vhdl.py`** — `Expr2VHDL(Expr2L)`: VHDL syntax (`and`/`or`/`not`).
- **`expr2verilog.py`** — `Expr2Verilog(Expr2L)`: Verilog syntax (`&`/`|`/`~`).
- **`multisol.py`** — `MultiSol`: container for multiple output solutions, handles `printN()` with named inputs/outputs.

### FSM Support

- **`fsm.py`** — `FSM` class: state machine minimization. Users define states and transitions, assign binary codes, then solve with `solveD()` (D flip-flops) or `SolveJK()` (JK flip-flops). Internally builds a `TT` and delegates to the same minimization pipeline.

## Conventions

- Python 2/3 compatible (uses `future` package). Tabs for indentation in most files; `logic.py` and `expr2l.py` use spaces.
- Adding a new output syntax: add a `Cube` method in `cube.py`, create an `Expr2*` subclass of `Expr2L`, and register it in `SOP.expr()` in `sop.py`.
- Tests work by executing example scripts and asserting they don't crash (no assertion-based unit tests).
