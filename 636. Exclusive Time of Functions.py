def exclusiveTime(n: int, logs: List[str]) -> List[int]:
    stack = []
    res = [0] * n 
    for log in logs:
        i = int(log.split(':')[0])
        action = log.split(':')[1]
        time = int(log.split(':')[2])

        if action == 'start':
            if stack:
                res[stack[-1]] += time-prev_time
            stack.append(i)
            prev_time = time
        
        else:
            res[stack.pop()] += time-prev_time+1
            prev_time = time+1

    return res
