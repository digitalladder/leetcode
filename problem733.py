#problem 733 / flood fill
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        n = len(image)
        m = len(image[0])
        color = image[sr][sc]
        if color == newColor:           #一定要检查这一步，没有这一步会导致 bfs 无限运行下去
            return image
        queue = collections.deque()
        queue.append((sr,sc))
        while queue:
            r,c = queue.popleft()
            image[r][c] = newColor
            for nr,nc in {(r,c+1),(r,c-1),(r+1,c),(r-1,c)}:
                if 0 <= nr < n and 0 <= nc < m:
                    if image[nr][nc] == color:
                        queue.append((nr,nc))
        return image