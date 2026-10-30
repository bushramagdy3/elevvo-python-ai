"""Calculate the average of a non-empty sequence of numeric scores."""


def calculate_average(scores):
    """Return the arithmetic mean, rejecting an empty sequence."""
    if not scores:
        raise ValueError("At least one score is required.")

    return sum(scores) / len(scores)


def main():
    """Display the average for a sample set of scores."""
    scores = [80, 90, 100]
    average = calculate_average(scores)
    print(f"Average score: {average:.2f}")


if __name__ == "__main__":
    main()
