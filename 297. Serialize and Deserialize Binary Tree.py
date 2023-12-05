# dfs
class Codec:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("#")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = deque(data.split(","))
        def dfs():
            val = vals.popleft()
            if val == "#":
                return None
            
            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()


# bfs
class Codec:
    def serialize(self, root):
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("#")
        
        return ",".join(res)
  
    def deserialize(self, data):
        if not data or data == "#":
            return None 
            
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        queue = deque([root])
  
        i = 1
        while queue:
            node = queue.popleft()
            if vals[i] != "#":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
  
            if vals[i] != "#":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
  
        return root
  
