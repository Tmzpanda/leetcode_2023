from itertools import combinations
from collections import defaultdict
def mostVisitedPattern(username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    activities = []
    for user, web, time in zip(username, website, timestamp):
        activities.append((user, web, time))
    activities.sort(key=lambda x:x[2])
    
    userToWebs = defaultdict(list)
    for user, web, time in activities:
        userToWebs[user].append(web)
        
    patternCount = defaultdict(int)
    for user in userToWebs:
        patterns = set(combinations(userToWebs[user], 3))
        for pattern in patterns:
            patternCount[pattern] += 1
            
    largest = max(patternCount.values())
    res = []
    for pattern, count in patternCount.items():
        if count == largest:
            res.append(pattern)
    res.sort()
    
    return res[0]
