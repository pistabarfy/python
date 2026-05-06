# learning machines raw 🔩

**Started: May 2, 2026. Day 1 was hello world. It gets deeper from here.**

I'm learning Python from the ground up — not surface level, not tutorials, not copy paste.
I learn by building things from scratch and understanding what's actually happening under the hood.
Every file in here is something I wrote myself, figured out myself, broke myself.

Goal: systems engineer. Distributed systems, bare metal performance, understanding the machine.
This repo documents the journey from zero.

---

## what's here

### `analyse.py` — string analyser *(day 2)*
Built a full string analysis engine from scratch. No built-in shortcuts.

- letter counter (manual loop, no `len()`)
- word counter
- vowel and consonant counter
- palindrome checker
- most frequent character finder (nested loops, O(n²))
- case detection using **raw ASCII values with `ord()`** — 65-90 uppercase, 97-122 lowercase
- unique character frequency map
- full edge case handling for empty strings

Most people would do `len(text)` and call it a day.
I wanted to know what `len()` is actually doing. So I wrote it myself.

### `calculator.py *day 3*`
Basic calculator. First real project.

### `functions.py`
Learning how functions actually work — scope, return values, how Python handles calls.

### `legb.py *day 4*`
Python's scope resolution — Local, Enclosing, Global, Built-in.
Understanding why Python looks up variables the way it does.

### `nested.py`
Nested functions and closures. How inner functions capture outer scope.

### `first.py`
Where it all started.

---

## the approach

No shortcuts. No `import this_does_everything`.
If I can build it manually first, I build it manually.
That's how you actually learn what the language is doing.

When I use a built-in later, I'll already know what it replaced.

---

## what's coming

- SQL fundamentals
- Backend basics
- Systems programming
- Going deeper into how Python executes code
- Distributed systems concepts

---

## follow the journey

Twitter: [@pistabarfy](https://twitter.com/pistabarfy)

posting everything raw as I learn it. the confusion, the breakthroughs, the weird stuff I find.

---

*insha allah, the machine will make sense.*
