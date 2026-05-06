# learning machines raw 🔩

**Started: May 2, 2026. Day 1 was hello world. It gets deeper from here.**

I don't use tutorials. I build things from scratch, break them, and figure out what's happening underneath. Every file here is something I wrote myself and understood myself.

Goal: systems engineer. Distributed systems, bare metal performance, understanding the machine at every layer.

---

## what i built

### `analyse.py` — string analyser *(day 2)*
Full string analysis engine. No built-in shortcuts.

- letter counter without `len()` — manual loop
- vowel and consonant counter
- palindrome checker
- most frequent character using nested loops — O(n²), my first real algorithm
- case detection using raw ASCII values with `ord()` — 65-90 uppercase, 97-122 lowercase
- unique character frequency map
- edge case handling for empty strings

I wanted to know what `len()` actually does. So I didn't use it.

---

### `calculator.py` — interactive calculator *(day 3)*
First real interactive project. Takes user input, handles operations, loops until exit.

---

### `studentregister.py` — student register *(day 5)*
Student register built using lists, not a database.

- walrus operator `:=` for clean input handling
- duplicate roll number detection
- `enumerate()` to track positions
- `zip()` to pair names with roll numbers

---

### `shoppingcart.py` — shopping cart simulator *(day 6)*
Most complex project so far. Combines everything learned.

- `defaultdict(list)` to group items by category
- walrus operator `:=` in while condition
- `Counter` for item frequency
- `most_common(2)` to find top 2 items
- reused my own `flatten()` function from recursion day

---

## what i learned

### `first.py` *(day 1)*
Hello world. Variables. The beginning.

### `functions.py` *(day 4)*
How functions actually work — `*args`, `**kwargs`, default parameters, return values.

### `legb.py` *(day 4)*
Python's scope resolution — Local, Enclosing, Global, Built-in. Why Python finds variables in the order it does.

### `nested.py` *(day 4)*
Nested functions, closures, how inner functions capture outer scope.

### `recursion.py` *(day 5)*
Factorial using recursion. Understanding base case and recursive case.

### `nested.py` — array flattening *(day 5)*
Spent 3 hours figuring out how to flatten `[1,[2,3],4,5]` without any hints. When it clicked I realised this is the same logic your file system uses — every folder inside a folder inside a folder.

### `deepcopy.py` *(day 5)*
Deep vs shallow copy. `isinstance()` for type validation. Discovered `bool` is a subclass of `int` in Python — had to explicitly reject it.

### `while.py` *(day 3)*
While loops, nested for loops, `break`, `continue`, `pass`, string iteration.

### `datastructures.py` *(day 6)*
Sets, dict methods (`keys()`, `values()`, `items()`), `Counter`, list/dict/set comprehensions, slicing, `[::-1]` creates a new list not mutate, starred unpacking with `*b`.

---

## follow the journey

Twitter: [@pistabarfy](https://twitter.com/pistabarfy)

posting everything raw as I learn it.

---

*insha allah, the machine will make sense.*