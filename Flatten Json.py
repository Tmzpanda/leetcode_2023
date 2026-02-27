"""
input:
{
  "user": {
    "name": "Gemini",
    "address": { "city": "NYC" }
  },
  "active": 1,
}

output:
{
  "user.name": "Gemini",
  "user.address.city": "NYC",
  "active": 1
}

"""
# recursion 
def flatten_json(obj):
    res = {}
    
    def recurse(item, prefix):
        for k, v in item.items():
            new_k = f"{prefix}.{k}" if prefix else k
    
            if isinstance(v, dict):
                recurse(v, new_k)
            else:
                res[new_k] = v

    recurse(obj, "")
    return res

# stack
def flatten_json(obj):
    res = {}
    stack = [(obj, "")]
    
    while stack:
        item, path = stack.pop()
        for k, v in item.items():
            new_k = f"{path}.{k}" if path else k
            
            if isinstance(v, dict) and v:
                stack.append((v, new_k))
            else:
                res[new_k] = v
                
    return res

