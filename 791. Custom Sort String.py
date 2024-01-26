def customSortString(self, order: str, s: str) -> str:
  
    index_dict = {char: i for i, char in enumerate(order)}
    return ''.join(sorted(s, key=lambda x: index_dict.get(x, len(order))))
