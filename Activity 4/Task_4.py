# Belief Revision Simulation
# Topic: Non-Monotonic Reasoning
# Course: CSST101

# Default rule: "If an animal is a bird, assume it can fly."

def can_fly(animal):
    birds = ["sparrow", "eagle", "parrot", "penguin", "ostrich"]
    exceptions = ["penguin", "ostrich"]

    print("Reasoning process:")
    if animal.lower() in birds:
        print(f"1. {animal.capitalize()} is a bird.")
        print("2. By default, birds can fly.")
        if animal.lower() in exceptions:
            print(f"3. However, {animal.capitalize()} is an exception.")
            print(f"4. Therefore, {animal.capitalize()} cannot fly.")
            return False
        else:
            print(f"3. No exception found for {animal.capitalize()}.")
            print(f"4. Therefore, {animal.capitalize()} can fly.")
            return True
    else:
        print(f"1. {animal.capitalize()} is not a bird.")
        print(f"2. No rule applies for non-birds.")
        return None

# Ask user for input
animal_name = input("Enter the name of an animal: ")
result = can_fly(animal_name)

if result is True:
    print(f"\nConclusion: {animal_name.capitalize()} can fly.")
elif result is False:
    print(f"\nConclusion: {animal_name.capitalize()} cannot fly.")
else:
    print(f"\nConclusion: Unable to determine flying ability.")
