python的递归模版：

def dfs(node, visited):
    if node in visited#terminator
        #alder visited
        return

        visited add(node)


        #process current node here.

        for next_node in node chilchildren():
            if not next_node in visited:
                dfs(next_node, visited)

递归的时候几个要点：
1.人肉递归
2.找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）
3.数学归纳法思维

BFS代码：
def BFS(graph,start,end):
    
    queue = []
    queue.append([start])
    
    visited = set() #和数中的BFS的最大区别
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes=generate_related_nodes(node)
        queue push(nodes)
        
  
