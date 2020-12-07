from part_one import seats

def sort_by_id(seat):
    return seat.get_id()

if __name__ == '__main__':

    mid_row_seats = [
        seat for seat in seats if (seat.row > 0 and seat.row < 127)
    ]

    mid_row_seats.sort(key=sort_by_id)

    previous_seat = None
    missing_id = None

    for seat in mid_row_seats:

        if previous_seat is None:
            previous_seat = seat
            continue

        if seat.get_id() - previous_seat.get_id() > 1:
            missing_id = seat.get_id() - 1
            break

        previous_seat = seat

    print(missing_id)
