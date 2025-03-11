ages = [22, 25, 19, 34, 23, 18]
policy_violated = False
for age in ages:
    if age < 21:
        policy_violated = True

if policy_violated:
    print(f"Policy violation found at")
else:
    print("No policy violations detected.")
