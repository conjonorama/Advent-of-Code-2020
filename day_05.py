# Part 1

def get_seat_info(txt):
    """
    Returns row, column, and seat ID
    >>> get_seat_info('BFFFBBFRRR')
    (70, 7, 567)
    """

    row = int(txt[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(txt[-3:].replace('L', '0').replace('R', '1'), 2)

    seat_id = row * 8 + col

    return row, col, seat_id

def test_file():
    largest_id = 0
    for line in open('input_05.txt', encoding='utf8'):    
        row, col, seat_id = get_seat_info(line.strip())
        if seat_id > largest_id:
            largest_id = seat_id
    print(largest_id)



def find_row():
    d = {}
    for line in open('input_05.txt', encoding='utf8'):
        row, col, seat_id = get_seat_info(line.strip())
        d[row] = d.get(row, 0) + 1
    
    t = []
    for k, v in d.items():
        if v < 8:
            t.append((k, v))
    for line in open('input_05.txt', encoding = 'utf8'):
        row, col, seat_id = get_seat_info(line.strip())
        if row == 79:
            print(row, col, seat_id)

def find_seat():
    seats = {get_seat_info(line.strip())[2]
            for line in open('input_05.txt', encoding='utf8')}
    all_seats = set(range(min(seats), max(seats) + 1))
    return all_seats - seats


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # test_file()
    find_row()
    print(find_seat())

