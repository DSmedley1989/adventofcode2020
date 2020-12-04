problem_input = None

with open("./data/day_one_part_one.txt", "r") as file:
    problem_input = [int(n) for n in file.read().split("\n") if n != ""]

def find_and_multiply(numbers):
    numbers.sort()
    result = None
    for n in numbers:
        for x in range(len(numbers) - 1, 0, -1):
            m = numbers[x]

            if m + n == 2020:
                result = m * n
            elif m + n < 2020:
                break
            else:
                continue

        if result is not None:
            break

    return result


test_input = [
    1721,
    979,
    366,
    299,
    675,
    1456
]

test_output = 514579

if __name__ == "__main__":

    if find_and_multiply(test_input) != test_output:
        print("TEST FAILED!")
        exit()


    answer = find_and_multiply(problem_input)

    print(answer)
