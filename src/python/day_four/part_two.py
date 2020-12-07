from part_one import required_fields, problem_input_raw, parse_passports, validate_passport
import re

invalid_passports_raw = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

valid_passports_raw = """
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

def validate_birth_year(year):
    y = int(year)
    return y >= 1920 and y <= 2002

def validate_issue_year(year):
    y = int(year)
    return y >= 2010 and y <= 2020

def validate_expiration_year(year):
    y = int(year)
    return y >= 2020 and y <= 2030

def validate_height(height):
    exp = re.match(r'^([0-9]*)(in|cm)$', height)

    if exp is None:
        return False

    num = int(exp.group(1))
    unit = exp.group(2)

    if unit == 'cm':
        return num >= 150 and num <= 193
    elif unit == 'in':
        return num >= 59 and num <= 76
    else:
        return False

def validate_hair_colour(colour):
    return re.match(r'^#[0-9a-f]{6}$', colour) is not None

def validate_eye_colour(colour):
    return colour in [
        'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
    ]

def validate_passport_id(pass_id):
    return re.match(r'[0-9]{9}$', pass_id)

validations = {
    'byr': validate_birth_year,
    'iyr': validate_issue_year,
    'eyr': validate_expiration_year,
    'hgt': validate_height,
    'hcl': validate_hair_colour,
    'ecl': validate_eye_colour,
    'pid': validate_passport_id
}

def validate_fields(passport):
    for field in required_fields:
        if not validations[field](passport[field]):
            return False

    return True

if __name__ == '__main__':
    invalid_passports = parse_passports(invalid_passports_raw)
    valid_passports = parse_passports(valid_passports_raw)

    test_invalid_count = 0
    test_valid_count = 0

    for passport in invalid_passports:
        if not validate_fields(passport):
            test_invalid_count += 1

    for passport in valid_passports:
        if validate_fields(passport):
            test_valid_count += 1

    if test_invalid_count != 4 or test_valid_count != 4:
        print("TEST FAILURE!")
        print(test_invalid_count)
        print(test_valid_count)
        exit()

    valid_count = 0

    pass_with_fields = [
        passport for passport in parse_passports(problem_input_raw) if validate_passport(passport)
    ]

    for passport in pass_with_fields:
        if validate_fields(passport):
            valid_count += 1

    print(valid_count)
