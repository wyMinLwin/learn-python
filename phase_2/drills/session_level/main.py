# ### Given
#
# ```python
# records = [
#     ("alice", 24),
#     ("bob", 17),
#     ("charlie", 24),
#     ("alice", 30),
#     ("bob", 17)
# ]
# ```
#
# ### Tasks
#
# 1. Remove **duplicate records**
# 2. Create a dictionary where:
#
#    * key = name
#    * value = **set of ages** for that name
# 3. Create another dictionary containing **only users aged 18+**
# 4. Use:
#
#    * tuple unpacking
#    * sets
#    * **dict comprehensions**
#
# ### Expected Output Shape
#
# ```python
# {
#     "alice": {24, 30},
#     "charlie": {24}
# }
# ```

records = [("alice", 24), ("bob", 17), ("charlie", 24), ("alice", 30), ("bob", 17)]

unique_records = set(records)
users = dict()

for name, age in unique_records:
    users[name] = users.get(name, set()) | {age}

adults = {
    name: ages
    for name, ages in users.items()
    if all(age >= 18 for age in ages)
}

print(f"#1 : {unique_records}")
print(f"#2 : {users}")
print(f"#3: {adults}")
