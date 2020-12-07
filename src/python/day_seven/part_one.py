import re

test_input_raw = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

problem_input = None

with open('./data/day_seven_part_one.txt', 'r') as file:
    problem_input = file.read()

MASTER_RULE_PATTERN = r'^([a-z\s]+)s contain (([0-9]+ [a-z\s]+(, |\.))*)$'
EMPTY_BAG_PATTERN = r'^([a-z\s]+)s contain no other bags.$'
EXTRACT_RULE_PATTERN = r'^([0-9]+) ([a-z\s]+?)s?\.?$'

master_rule = re.compile(MASTER_RULE_PATTERN)
empty_bag = re.compile(EMPTY_BAG_PATTERN)
extract_rule = re.compile(EXTRACT_RULE_PATTERN)

class Rule:

    @staticmethod
    def parse(rule_str):
        m = extract_rule.match(rule_str)

        if m is not None:
            quantity = int(m.group(1))
            key = m.group(2)
            return Rule(quantity, key)
        else:
            return None

    def __init__(self, quantity, key):
        self.quantity = quantity
        self.key = key

    def copy(self):
        return Rule(self.quantity, self.key)

    def multiply_by(self, factor):
        self.quantity *= factor


class BagContents:
    def __init__(self, rules):
        self.contents = rules
        self.keys = [rule.key for rule in rules]

    def contains(self, key):
        return key in self.keys

def parse_bag_rules(bag_rules_str):
    e = empty_bag.match(bag_rules_str)

    if e is not None:
        return e.group(1), []

    m = master_rule.match(bag_rules_str)

    if m is not None:
        bag_key = m.group(1)
        rules = m.group(2).split(', ')

        parsed_rules = []
        for rule in rules:
            maybe_parsed = Rule.parse(rule)

            if maybe_parsed is not None:
                parsed_rules.append(maybe_parsed)

        return bag_key, parsed_rules

def parse_ruleset(ruleset_str):
    rulebook = {}

    for rule_str in ruleset_str.split('\n'):
        if rule_str != '':
            bag_key, parsed_rules = parse_bag_rules(rule_str)

            rulebook[bag_key] = BagContents(parsed_rules)

    return rulebook

def find_bags_containing(bag_ruleset, desired_bag_key):
    bags_that_contain = []

    for bag_key, rules in bag_ruleset.items():
        if rules.contains(desired_bag_key):
            bags_that_contain.append(bag_key)

    return bags_that_contain

def find_nested_bags_containing(bag_ruleset, desired_bag_key):
    bags_that_contain = set([])

    bags_to_check = find_bags_containing(bag_ruleset, desired_bag_key)

    while len(bags_to_check) > 0:
        bag = bags_to_check.pop(0)

        bags_that_contain.add(bag)

        new_bags_to_check = find_bags_containing(bag_ruleset, bag)

        bags_to_check.extend(new_bags_to_check)

    return bags_that_contain

if __name__ == "__main__":

    test_ruleset = parse_ruleset(test_input_raw)

    test_bags_containing = find_nested_bags_containing(test_ruleset, 'shiny gold bag')

    if len(test_bags_containing) != 4:
        print("TEST FAILURE!")
        print(test_bags_containing)
        exit()

    problem_ruleset = parse_ruleset(problem_input)

    problem_bags_containing = find_nested_bags_containing(problem_ruleset, 'shiny gold bag')

    print(len(problem_bags_containing))
