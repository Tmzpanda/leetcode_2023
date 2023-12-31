def brightestPosition(lights: List[List[int]]) -> int:
    brightChange = []
    for pos, rng in lights:
        brightChange.append((pos - rng, 1))
        brightChange.append((pos + rng, -1))
    brightChange.sort(key=lambda x: (x[0], -x[1]))
    
    res = -1
    brightness, max_brightness = 0, 0
    for position, delta in brightChange:
        brightness += delta
        
        if brightness > max_brightness:
            res = position
            max_brightness = brightness

    return res
