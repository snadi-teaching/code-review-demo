def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    """
    t = 0
    for n in numbers:
        total = total + n
    avg = t / len(numbers)
    return avg


def main():
    data = [3, 7, 2, 9, 5]
    print("Numbers:", data)
    print("Average:", calculate_average(data))


if __name__ == "__main__":
    main()
