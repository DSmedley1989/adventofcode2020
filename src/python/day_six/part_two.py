from part_one import test_input_raw, problem_input, group_answers, parse_input

def num_in_group(group_answers_raw):
    return len([ answers for answers in group_answers_raw.split('\n') if answers != ''])

def questions_answered_by_all(group_answers_raw):
    groups_answers = group_answers(group_answers_raw)
    num = num_in_group(group_answers_raw)

    answered_by_all = 0

    for answer, times_answered in groups_answers.items():
        if times_answered == num:
            answered_by_all += 1

    return answered_by_all

if __name__ == "__main__":
    test_groups = [g for g in test_input_raw.split('\n\n') if g != '']

    test_result = 0

    for group in test_groups:
        test_result += questions_answered_by_all(group)

    if test_result != 6:
        print("TEST FAILURE!")
        exit()

    problem_groups = [g for g in problem_input.split('\n\n') if g != '']

    problem_answer = 0

    for group in problem_groups:
        problem_answer += questions_answered_by_all(group)

    print(problem_answer)
