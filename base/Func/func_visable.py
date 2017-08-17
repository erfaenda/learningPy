def space_ship(cans):
    total_cans = 0
    for week in range(1,52):
        total_cans = total_cans + cans
        print('Неделя %s, банок: %s' % (week, total_cans))

space_ship(2)
