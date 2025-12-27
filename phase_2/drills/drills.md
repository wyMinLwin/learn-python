# 🧠 Python Data Structures Drills (Easy → Hard)

This drill set covers:

* Lists
* Tuples
* Dictionaries
* Sets
* Indexing & slicing
* **List / Dict comprehensions (IMPORTANT)**

Do these drills **in order**. Avoid shortcuts. Write loop versions first if needed, then refactor to comprehensions.

---

## 🟢 Event Metrics Slice — User Activity Snapshot

### Scenario

You are given a small batch of **event metrics** collected from a mobile app. Each number represents the number of actions a user performed in a session.

```python
event_counts = [3, 6, 9, 12, 15, 18]
```

### Tasks

1. Extract the **first 3 sessions** (early users) using slicing
2. Extract the **last 2 sessions** (most recent users) using slicing
3. Store the event counts as an **immutable snapshot** (tuple)
4. Deduplicate the event counts to get **unique activity levels** (set)
5. Build a list of **high-activity sessions (>10 events)** using a **list comprehension only**

### Concepts Covered

* Lists
* Tuples
* Sets
* Indexing & slicing
* List comprehension

---

## 🟡 User Identity Normalization — Dedup & Feature Mapping

### Scenario (FAANG-style)

You are cleaning **raw user identity data** before storing it in a user-profile service. Usernames may appear multiple times and must be normalized.

```python
raw_users = ["anna", "bob", "anna", "carl", "bob", "dave"]
```

### Tasks

1. Remove duplicate user records
2. Normalize all usernames to **uppercase**
3. Build a **feature dictionary** where:

   * key = normalized username
   * value = length of the username
4. Use **comprehensions only** (no manual loops)

### What This Simulates

* Data deduplication in ingestion pipelines
* User identity normalization
* Feature extraction for ranking or ML models

### Expected Output Shape

```python
{
    "ANNA": 4,
    "BOB": 3,
    "CARL": 4,
    "DAVE": 4
}
```

### Concepts Covered

* Sets (deduplication)
* Dictionaries
* List comprehension
* Dict comprehension

---

## 🟠 User Age Aggregation — Session-Level Analytics

### Given

```python
records = [
    ("alice", 24),
    ("bob", 17),
    ("charlie", 24),
    ("alice", 30),
    ("bob", 17)
]
```

### Tasks

1. Remove **duplicate records**
2. Create a dictionary where:

   * key = name
   * value = **set of ages** for that name
3. Create another dictionary containing **only users aged 18+**
4. Use:

   * tuple unpacking
   * sets
   * **dict comprehensions**

### Expected Output Shape

```python
{
    "alice": {24, 30},
    "charlie": {24}
}
```

### Concepts Covered

* Tuples & unpacking
* Sets
* Dictionaries
* Dict comprehensions
* Filtering logic

---

## 🔴 Text Signal Extraction — Feature Engineering Pipeline

### Given

```python
text = "ai will change the world but python will power ai"
```

### Tasks

1. Split the text into words
2. Create a **dictionary** where:

   * key = word
   * value = **tuple** `(count, length)`
3. Ignore words shorter than **3 characters**
4. Use:

   * indexing or slicing at least once
   * **dict comprehension**
   * set or tuple where appropriate

### Expected Output Shape

```python
{
    "change": (1, 6),
    "world": (1, 5),
    "python": (1, 6),
    "power": (1, 5)
}
```

### Constraints

* ❌ no manual loops
* ✅ comprehensions only
* ✅ clean, Pythonic code

---

## 🎯 Completion Criteria

If you can solve **Text Signal Extraction — Feature Engineering Pipeline** cleanly without loops, your Python data-structure fundamentals are solid and AI-ready.

Refactor aggressively. Readability > cleverness.

