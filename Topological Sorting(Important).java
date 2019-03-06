/*
Topological Sorting problem
Given an directed graph, a topological order of the graph nodes is defined as follow:
*For each directed edge A -> B in graph, A must before B in the order list.
*The first node in the order can be any node in the graph with no nodes direct to it
Find any topological order for the given graph
You can assume that there is at least noe topological order in the graph
*/
//Solution
 /**
  * Definition for Directed graph.
  class DirectedGraphNode {
      int label;
      ArrayList<DirectedGraphNode> neighbors;
      DirectedGraphNode(int x) { 
          label = x; neighbors = new ArrayList<DirectedGraphNode>();
        }
  };
  */
public class Solution {
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {
        ArrayList<DirectedGraphNode> order = new ArrayList<>();

        if (graph == null) {
            return order;
        }

        //1. count indegree(入度)
        Map<DirectedGraphNode, Integer> indegree = getIndegree(graph);

        //2. topological sorting - bfs
        Queue<DirectedGraphNode> queue = new LinkedList<>();

        //start nodes
        //Topological Sorting start with node which have 0 indegree
        //find node with 0 indegree, delete from graph, put it into the sort queue, neighbor nodes' indegree-1,
        for (DirectedGraphNode node : graph) {
            if (indegree.get(node) == 0) {
                queue.offer(node);  //to be deleted queue, delete node with 0 indegree from the origin graph every step.
                order.add(node);
            }
        }

        while (!queue.isEmpty()) {
            DirectedGraphNode node = queue.poll();
            for (DirectedGraphNode neighbor : node.neighbors) {
                //node -> neighbor
                indegree.put(neighbor, indegree.get(neighbor)-1);
                if (indegree.get(neighbor) == 0) {
                    queue.offer(neighbor);
                    order.add(neighbor);
                }
            }
        }

        if (order.size() == graph.size()) {
            return order;
        }

        return null;
    }

    private Map<DirectedGraphNode, Integer> getIndegree(ArrayList<DirectedGraphNode> graph) {
        Map<DirectedGraphNode, Integer> indegree = new HashMap<>();
        for (DirectedGraphNode node : graph) {
            indegree.put(node,0);
        }

        for (DirectedGraphNode node : graph) {
            for (DirectedGraphNode neighbor : node.neighbors) {
                indegree.put(neighbor, indegree.get(neighbor)+1);
            }
        }

        return indegree;
    }
}

/**
 * 判断图里有没有环（不可拓扑排序）
 * order为空或者order.size()小于graph.size()
 * 环状结构内所有点入度都大于等于1，无法取出到order中，有残留点在图中
 */