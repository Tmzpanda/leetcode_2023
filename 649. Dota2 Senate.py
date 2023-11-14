def predictPartyVictory(senate: str) -> str:
    r_positions, d_positions = deque(), deque()
    for index, char in enumerate(senate):
        if char == 'R':
            r_positions.append(index)
        else:
            d_positions.append(index)

    next_position = len(senate)
    while r_positions and d_positions:
        if r_positions[0] < d_positions[0]:
            r_positions.append(next_position)
        else:
            d_positions.append(next_position)

        r_positions.popleft()
        d_positions.popleft()
        next_position += 1

    return 'Radiant' if r_positions else 'Dire'
