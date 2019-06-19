import java.util.LinkedList;
import java.util.Queue;

//problem 200 Number of Islands
class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        
        int nr = grid.length;
        int nc = grid[0].length;
        int num_islands = 0;
        
        for (int r = 0; r < nr; ++r) {
            for (int c = 0; c < nc; ++c) {
                if (grid[r][c] == '1') {
                    ++num_islands;
                    grid[r][c] = '0';   //visited
                    Queue<Coordinate> neighbors = new LinkedList<>();
                    neighbors.add(new Coordinate(r,c));
                    while (!neighbors.isEmpty()) {
                        Coordinate id = neighbors.remove();
                        int row = id.x;
                        int col = id.y;
                        if (row-1 >= 0 && grid[row-1][col] == '1') {
                            neighbors.add(new Coordinate(row-1,col));
                            grid[row-1][col] = '0';
                        }
                        if (row+1 < nr && grid[row+1][col] == '1') {
                            neighbors.add(new Coordinate(row+1,col));
                            grid[row+1][col] = '0';
                        }
                        if (col-1 >= 0 && grid[row][col-1] == '1') {
                            neighbors.add(new Coordinate(row,col-1));
                            grid[row][col-1] = '0';
                        }
                        if (col+1 < nc && grid[row][col+1] == '1') {
                            neighbors.add(new Coordinate(row,col+1));
                            grid[row][col+1] = '0';
                        }
                    }
                }
            }
        }
        return num_islands;
    }
}
class Coordinate {
    int x,y;
    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
}