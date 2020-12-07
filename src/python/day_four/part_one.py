test_input_raw = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

problem_input_raw = None

with open('./data/day_four_part_one.txt', 'r') as file:
    problem_input_raw = file.read()

def parse_passport(passport_string):
    passport = {}

    passport_args = []

    for row in passport_string.split('\n'):
        passport_args.extend(
            [ elem.strip() for elem in row.split(' ') ]
        )

    for arg in passport_args:
        split = arg.split(':')
        passport[split[0].strip()] = split[1].strip()

    return passport

def parse_passports(passports_string):
    return [ parse_passport(passport_string.strip()) for passport_string in passports_string.split('\n\n') ]

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def validate_passport(passport):
    for field in required_fields:
        if field not in passport:
            return False

    return True

def count_valid_passports(passports):
    valid = 0

    for passport in passports:
        if validate_passport(passport):
            valid += 1

    return valid

if __name__ == '__main__':
    test_passports = parse_passports(test_input_raw)
    test_valid_passports = count_valid_passports(test_passports)

    if test_valid_passports != 2:
        print('TEST FAILURE! %d != 2' % test_valid_passports)
        exit()

    problem_passports = parse_passports(problem_input_raw)

    print(count_valid_passports(problem_passports))
