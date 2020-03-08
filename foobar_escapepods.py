"""
  Escape Pods
  You've blown up the LAMBCHOP doomsday device and broken the bunnies out of Lambda's prison,
  and now you need to escape from the space station as quickly and as orderly as possible!
  The bunnies have all gathered in various locations throughout the station,
  and need to make their way towards the seemingly endless amount of escape pods positioned
  in other parts of the station.
  You need to get the numerous bunnies through the various rooms to the escape pods.
  Unfortunately, the corridors between the rooms can only fit so many bunnies at a time.
  What's more, many of the corridors were resized to accommodate the LAMBCHOP,
  so they vary in how many bunnies can move through them at a time.
  <p>
  Given the starting room numbers of the groups of bunnies,
  the room numbers of the escape pods,
  and how many bunnies can fit through at a time in each direction of every corridor in between,
  figure out how many bunnies can safely make it to the escape pods at a time at peak.
  <p>
  Write a function solution(entrances, exits, path) that takes
  an array of integers denoting where the groups of gathered bunnies are,
  an array of integers denoting where the escape pods are located,
  and an array of an array of integers of the corridors,
  returning the total number of bunnies that can get through at each time step as an int.
  The entrances and exits are disjoint and thus will never overlap.
  The path element path[A][B] = C describes that the corridor going from A to B can fit C bunnies at each time step.
  There are at most 50 rooms connected by the corridors and at most 2000000 bunnies that will fit at a time.
  <p>
  For example, if you have:
  entrances = [0, 1]
  exits = [4, 5]
  path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
  ]
  <p>
  Then in each time step, the following might happen:
  0 sends 4/4 bunnies to 2 and 6/6 bunnies to 3
  1 sends 4/5 bunnies to 2 and 2/2 bunnies to 3
  2 sends 4/4 bunnies to 4 and 4/4 bunnies to 5
  3 sends 4/6 bunnies to 4 and 4/6 bunnies to 5
  <p>
  So, in total, 16 bunnies could make it to the escape pods at 4 and 5 at each time step.
  (Note that in this example, room 3 could have sent any variation of 8 bunnies to 4 and 5,
  such as 2/6 and 6/6, but the final solution remains the same.)
  <p>
  Languages
  =========
  <p>
  To provide a Java solution, edit Solution.java
  To provide a Python solution, edit solution.py
  <p>
  Test cases
  ==========
  Your code should pass the following test cases.
  Note that it may also be run against hidden test cases not shown here.
  <p>
  -- Java cases --
  Input:
  Solution.solution({0, 1}, {4, 5}, {{0, 0, 4, 6, 0, 0}, {0, 0, 5, 2, 0, 0}, {0, 0, 0, 0, 4, 4}, {0, 0, 0, 0, 6, 6}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})
  Output:
  16
  <p>
  Input:
  Solution.solution({0}, {3}, {{0, 7, 0, 0}, {0, 0, 6, 0}, {0, 0, 0, 8}, {9, 0, 0, 0}})
  Output:
  6
  <p>
  -- Python cases --
  Input:
  solution.solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])
  Output:
  6
  <p>
  Input:
  solution.solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
  Output:
  16
 """

# The Ford Fulkerson Method 最大流问题
#https://github.com/vitaminac/blog/blob/f6185a02fcdc12a67cc02bfed436817d0e8d2ac9/source/_posts/Google-Foobar-Escape-Pods.md#the-ford-fulkerson-method

import collections
def solution(entrances, exits, path):
    # Your code here
    def transform(entrances,exits,path):        # add a new single entrance and a single exit
        newpath = [[0]*(n+2) for _ in range(n+2)]   # newpath will be (n+2)x(n+2) large
        for i in range(n):
            for j in range(n):
                newpath[i+1][j+1] = path[i][j]
        for entrance in entrances:
            newpath[0][entrance+1] = float('inf')
        for ex in exits:
            newpath[ex+1][n+1] = float('inf')
        return newpath

    def bfs(residual_net):
        m = len(residual_net)
        parents = [-1]*m
        queue = collections.deque([0])
        while queue and parents[-1] == -1:
            u = queue.popleft()
            for i in range(m):
                if residual_net[u][i] > 0 and parents[i] == -1:
                    queue.append(i)
                    parents[i] = u
        route = []
        u = parents[-1]
        while u != 0:
            if u == -1:
                return None
            route.append(u)
            u = parents[u]
        return route[-1::-1]

    n = len(path)
    maxflow = 0
    residual_net = transform(entrances,exits,path)
    while bfs(residual_net):
        route = bfs(residual_net)
        minflow = float('inf')
        u = 0
        for v in route:
            minflow = min(minflow,residual_net[u][v])
            u = v
        maxflow += minflow
        u = 0
        for v in route:
            residual_net[u][v] -= minflow
            residual_net[v][u] += minflow
            u = v
        
    return maxflow


print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))
print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))