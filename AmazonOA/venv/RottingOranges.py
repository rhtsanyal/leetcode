class Solution:
    def buildGraph(self,grid):
        graph = {}
        total_oranges = 0
        already_added = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    total_oranges+=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    key = str(i) + ',' + str(j)
                    if key not in graph:
                        graph[key] = set()
                    if i+1 < len(grid):
                        if grid[i+1][j] == 1:
                             dest = str(i+1) + ',' + str(j)
                             if dest not in already_added:
                                graph[key].add(dest)
                                already_added(dest)
                    if i-1 >= 0:
                        if grid[i-1][j] == 1:
                            dest = str(i-1) + ',' + str(j)
                            if dest not in already_added:
                                graph[key].add(dest)
                                already_added.add(dest)
                    if j+1 < len(grid[0]):
                        if grid[i][j+1] == 1:
                            dest = str(i) + ',' + str(j+1)
                            if dest not in already_added:
                                graph[key].add(dest)
                                already_added.add(dest)
                    if j-1 >=0:
                        if grid[i][j-1] == 1:
                            dest = str(i) + ',' + str(j-1)
                            if dest not in already_added:
                                graph[key].add(dest)
                                already_added.add(dest)
        return graph,total_oranges
    def BFSFromVertex(self,v,visited,q,graph,minutes):
        while len(q) > 0:
            curr =  q.pop(0)
            fresh_oranges_found = False
            if curr in graph:
                for i in graph[curr]:
                    if i not in visited:
                        fresh_oranges_found = True
                        q.append(i)
                        visited.add(i)
            if fresh_oranges_found:
                minutes.append(1)
    def orangesRotting(self, grid):
        graph,total_oranges= self.buildGraph(grid)
        visited = set()
        minutes = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q = [str(i) + ',' + str(j)]
                    visited.add(q[0])
                    self.BFSFromVertex(q[0],visited,q,graph,minutes)
        if len(visited) == total_oranges:
            return len(minutes)
        return -1

input = [[1,2,1,1,2,1,1]]

print(Solution().orangesRotting(input))