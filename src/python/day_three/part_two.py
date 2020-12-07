from part_one import test_input, problem_input, Slope, count_trees_on_slope

def check_paths_for_slope(slope, paths):
    result = 1

    for path in paths:
        tree_count = count_trees_on_slope(slope, path[0], path[1])
        result *= tree_count

    return result

if __name__ == '__main__':

    paths_to_check = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]

    test_slope = Slope(test_input)
    test_result = 336

    if check_paths_for_slope(test_slope, paths_to_check) != test_result:
        print("TEST FAILURE!")
        exit()

    problem_slope = Slope(problem_input)

    print(check_paths_for_slope(problem_slope, paths_to_check))
