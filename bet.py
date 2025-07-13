# Initial crash data
crash_history = [
    2.56, 4.67, 18.98, 2.26, 2.86, 1.12, 1.41, 2.75,
    11.42, 1.69, 1.90, 3.21, 2.59, 1.24, 1.15, 4.04
]

# Predict next crash value range
def predict_next(history):
    if len(history) < 16:
        return "Not enough data to predict."

    last16 = history[-16:]
    low_count = sum(1 for x in last16 if x < 1.5)

    avg = sum(last16) / len(last16)

    if low_count >= 2:
        return "High"
    elif avg > 5:
        return "Low"
    else:
        return "Medium"

# Get float safely from user
def get_float_input(prompt):
    while True:
        val = input(prompt)
        if val.lower() == 'q':
            return None
        try:
            return float(val)
        except ValueError:
            print("Invalid input. Enter a number or 'q' to quit.")

# Append new value to file
def append_to_file(value):
    with open("history.txt", "a") as file:
        file.write(f"{value},  ")

# Main loop
def main():
    print(" Crash Game Predictor Started!")
    print("Type 'q' anytime to quit.\n")

    while True:
        prediction = predict_next(crash_history)
        print(f"\n My Prediction for next round: {prediction} crash")

        feedback = input("Was I correct? (y/n): ").strip().lower()
        if feedback == 'q':
            print("Exiting... ")
            break
        elif feedback in ['y', 'n']:
            actual = get_float_input("Enter actual crash point: " if feedback == 'y' else "Oops! What was the actual crash point? ")
            if actual is None:
                break
            crash_history.append(actual)
            append_to_file(actual)
            print("Updated with actual crash point.")
        else:
            print(" Please type 'y', 'n', or 'q'.")

if __name__ == "__main__":
    main()
