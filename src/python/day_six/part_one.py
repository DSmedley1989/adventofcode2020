test_input_raw = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""

test_expected_result = 11

problem_input = None

with open('./data/day_six_part_one.txt', 'r') as file:
    problem_input = file.read()

def group_answers(group_answers_raw):
    results = {}

    for answers in group_answers_raw.split('\n'):
        if answers == '':
            continue

        for answer in answers.strip():
            previous_result = results.get(answer) or 0
            results[answer] = previous_result + 1

    return results

def parse_input(input_str):
    return [ group_answers(answers) for answers in input_str.split('\n\n')]

if __name__ == '__main__':
    test_answers = parse_input(test_input_raw)

    test_result = 0

    for answers in test_answers:
        test_result += len(answers)

    if test_result != test_expected_result:
        print("TEST FAILURE!")
        exit()

    problem_answers = parse_input(problem_input)

    problem_result = 0

    for answers in problem_answers:
        problem_result += len(answers)

    print(problem_result)
