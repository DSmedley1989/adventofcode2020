

class Seat:

    @staticmethod
    def to_number(b_str, zero_char, one_char):
        digits = []

        for d in b_str:
            if d == zero_char:
                digits.append('0')
            elif d == one_char:
                digits.append('1')

        return int(''.join(digits), 2)

    @staticmethod
    def parse(input_str):
        row_str = input_str[:7]
        seat_str = input_str[7:]

        return Seat(Seat.to_number(row_str, 'F', 'B'), Seat.to_number(seat_str, 'L', 'R'))

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def get_id(self):
        return (self.row * 8) + self.column

test_row_string_1 = 'BFFFBBFRRR'
test_row_string_2 = 'FFFBBBFRRR'
test_row_string_3 = 'BBFFBBFRLL'
test_row_1 = Seat(70, 7)
test_row_2 = Seat(14, 7)
test_row_3 = Seat(102, 4)

problem_input_raw = None

with open('./data/day_five_part_one.txt', 'r') as file:
    problem_input_raw = file.read()

seats = [
    Seat.parse(seat_str.strip()) for seat_str in problem_input_raw.split('\n') if seat_str != ''
]

if __name__ == '__main__':
    # Test things

    if Seat(44, 5).get_id() != 357:
        print("Seat ID test failure!")
        exit()

    if Seat.parse(test_row_string_1).get_id() != test_row_1.get_id():
        print("Seat parsing failure!")
        exit()

    if Seat.parse(test_row_string_2).get_id() != test_row_2.get_id():
        print("Seat 2 parsing failure!")
        exit()

    if Seat.parse(test_row_string_3).get_id() != test_row_3.get_id():
        print("Seat 3 parsing failure!")
        exit()


    highest_id = 0

    for seat in seats:
        if seat.get_id() > highest_id:
            highest_id = seat.get_id()

    print(highest_id)
