raw_users = ["anna", "bob", "anna", "carl", "bob", "dave"]

unique_users = set(raw_users)
normalized_users = set(user.upper() for user in unique_users)
feature_dictionary = {user: len(user) for user in normalized_users}

print(f"#1: {unique_users}")

print(f"#2: {normalized_users}")

print(f"#3: {feature_dictionary}")
