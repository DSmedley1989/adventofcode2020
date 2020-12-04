test_input = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]

test_output = 1

puzzle_input = None

with open('./data/day_two_part_one.txt', 'r') as f:
    puzzle_input = [str(row).strip() for row in f.read().split('\n') if row != ""]

def parse_and_validate(line):
    rule_and_pw = line.split(":")
    rule = rule_and_pw[0].strip()
    pw = rule_and_pw[1].strip()

    range_and_char = rule.split(" ")
    valid_range = range_and_char[0].split("-")
    first_index = int(valid_range[0])
    second_index = int(valid_range[1])

    check_char = range_and_char[1]

    first_char_matches = pw[first_index - 1] == check_char
    second_char_matches = pw[second_index - 1] == check_char

    return first_char_matches != second_char_matches

def count_valid(lines):
    return len([line for line in lines if parse_and_validate(line)])

if count_valid(test_input) != test_output:
    print("TEST FAILURE")
    exit()

print(count_valid(puzzle_input))
