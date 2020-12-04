problem_input = None

with open("./data/day_one_part_one.txt", "r") as file:
    problem_input = [int(n) for n in file.read().split("\n") if n != ""]

def find_and_multiply(numbers, target_sum):
    numbers.sort()
    result = None
    for n in numbers:
        for x in range(len(numbers) - 1, 0, -1):
            m = numbers[x]

            if m + n == target_sum:
                result = m * n
            elif m + n < target_sum:
                break
            else:
                continue

        if result is not None:
            break

    return result

def find_three_and_multiply(numbers):
    numbers.sort()

    for i in range(0, len(numbers) - 1):
        nums = numbers[:]
        n = nums.pop(i)
        target = 2020 - n
        result = find_and_multiply(nums, target)

        if result is not None:
            return n * result


test_input = [
    1721,
    979,
    366,
    299,
    675,
    1456
]

test_output = 241861950

if __name__ == "__main__":

    if find_three_and_multiply(test_input) != test_output:
        print("TEST FAILED!")
        exit()


    answer = find_three_and_multiply(problem_input)

    print(answer)
