event_counts = [3, 6, 9, 12, 15, 18]

# 1
print(f"#1: ", event_counts[0:3])

# 2
print(f"#2: ", event_counts[-2:])

# 3
print(f"#3: ", tuple(event_counts))

# 4
print(f"#4: ", set(event_counts))

# 5
print(f"#5: ", [e for e in event_counts if e > 10])
