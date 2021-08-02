import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
public class StronglyConnectedComponents {

    public  static List<List<Integer>> scc(int students,List<List<Integer>> knows) {
        int [][] graph=new int[students][students];
        for(List<Integer> list : knows){
            graph[list.get(0)][list.get(1)]=1;
        }

        boolean[] visited_vert = new boolean[graph.length];

        Stack<Integer> stack = new Stack<>();

        for (int vertex = 0; vertex < graph.length; vertex++) {
            if (!visited_vert[vertex]) {
                DFSGraph(graph, visited_vert, stack, vertex);
            }
        }

        int[][] rev_graph = get_rev_graph(graph);

        List<List<Integer>> components = new ArrayList<>();

        visited_vert = new boolean[graph.length];

        while (!stack.isEmpty()) {
            int vertex = stack.pop();
            if (!visited_vert[vertex]) {
                List<Integer> component = new ArrayList<>();
                DFSrev_graph(rev_graph, visited_vert, component, vertex);
                components.add(component);
            }
        }

        return components;
    }

    private static void DFSGraph(int[][] graph, boolean[] visited_vert, Stack<Integer> stack, int vertex) {
        visited_vert[vertex] = true;

        for (Integer adjacentVertex : get_adj_vertices(graph, vertex)) {
            if (!visited_vert[adjacentVertex]) {
                DFSGraph(graph, visited_vert, stack, adjacentVertex);
            }
        }

        stack.push(vertex);
    }

    private static void DFSrev_graph(int[][] graph, boolean[] visited_vert, List<Integer> list, int vertex) {
        visited_vert[vertex] = true;
        list.add(vertex);

        for (Integer adjacentVertex : get_adj_vertices(graph, vertex)) {
            if (!visited_vert[adjacentVertex]) {
                DFSrev_graph(graph, visited_vert, list, adjacentVertex);
            }
        }

    }

    private static List<Integer> get_adj_vertices(int[][] graph, int source) {
        List<Integer> adj_vertices = new ArrayList<>();

        for (int vertex = 0; vertex < graph.length; vertex++) {
            if (graph[source][vertex] == 1) {
                adj_vertices.add(vertex);
            }
        }

        return adj_vertices;
    }

    private static int[][] get_rev_graph(int[][] graph) {
        int[][] rev_graph = new int[graph.length][graph.length];

        for (int row = 0; row < graph.length; row++) {
            for (int col = 0; col < graph[row].length; col++) {

                if (graph[row][col] == 1) {
                    rev_graph[col][row] = 1;
                }
            }
        }
        return rev_graph;
    }
}




