def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    distances = [[float('inf')]*n for _ in range(n)]
    for i, j, w in edges:
        distances[i][j] = w
        distances[j][i] = w
    for i in range(n):
        distances[i][i] = 0

    for via in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][via] + distances[via][j])

    count_dict = defaultdict(int)
    for i in range(n):
        for distance in distances[i]:
            if distance <= distanceThreshold:
                count_dict[i] += 1

    cities_with_min_neighbors = [city for city, count in count_dict.items() if count == min(count_dict.values())]
    return max(cities_with_min_neighbors)
