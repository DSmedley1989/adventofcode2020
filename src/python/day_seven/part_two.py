from part_one import problem_input, parse_ruleset, Rule

test_input_raw = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

def get_bag_contents(bag_ruleset, rule):
    further_bags_required = []

    bag_contents = bag_ruleset[rule.key]

    for new_rule in bag_contents.contents:
        rule_to_add = new_rule.copy()
        rule_to_add.multiply_by(rule.quantity)

        further_bags_required.append(rule_to_add)

    return further_bags_required

def find_total_bag_contents(bag_ruleset, initial_bag_key):
    bag_totals = {}

    contents_to_check = get_bag_contents(bag_ruleset, Rule(1, initial_bag_key))

    while len(contents_to_check) > 0:
        rule_to_check = contents_to_check.pop(0)

        existing_bag_total = bag_totals.get(rule_to_check.key) or 0

        bag_totals[rule_to_check.key] = existing_bag_total + rule_to_check.quantity

        new_contents_to_check = get_bag_contents(bag_ruleset, rule_to_check)

        contents_to_check.extend(new_contents_to_check)

    return bag_totals

if __name__ == "__main__":
    test_ruleset = parse_ruleset(test_input_raw)

    test_bag_contents = find_total_bag_contents(test_ruleset, 'shiny gold bag')

    test_total_bags = 0

    for _, quantity in test_bag_contents.items():
        test_total_bags += quantity

    if test_total_bags != 126:
        print("TEST FAILURE!")
        print(test_bag_contents)
        exit()

    problem_ruleset = parse_ruleset(problem_input)

    problem_bag_contents = find_total_bag_contents(problem_ruleset, 'shiny gold bag')

    problem_total_bags = 0

    for _, quantity in problem_bag_contents.items():
        problem_total_bags += quantity

    print(problem_total_bags)
