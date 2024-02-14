def graphSnowfall(t):
    numbers_file = open(t, "r")
    numbers = []
    for number in numbers_file.readlines():
        numbers.append(int(number.strip()))
    numbers_file.close()

    # check the 10cm max range
    max_number = max(numbers)
    max_number = round((max_number / 10) + 0.1) * 10

    max_range = max_number
    print(max_range)

    size = int(max_range / 10)
    print(size)
    occurrences = [0] * size

    print(occurrences)

    values = ["0-10", "11-20", "21-30", "31-40", "41-50"]  # x-values, adjust string values given max_range value

    for number in numbers:  # depending on max_range value we got, update if needed
        if 0 <= number <= 10:
            occurrences[0] += 1
        elif 11 <= number <= 20:
            occurrences[1] += 1
        elif 21 <= number <= 30:
            occurrences[2] += 1
        elif 31 <= number <= 40:
            occurrences[3] += 1
        elif 41 <= number <= 50:
            occurrences[4] += 1

    print(occurrences)

    plt.bar(values, occurrences)
    plt.yticks(range(max(occurrences) + 1)),  # Set y-axis tick labels to integers
    plt.title("Snowfall accumulation for given days aggregated based on a 10cm range")
    plt.xlabel("cms")
    plt.ylabel("# of occurrences")
    plt.show()





