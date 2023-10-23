from tsp_solver import TSPSolver
from graph import UndirectedGraph

if __name__ == "__main__":
     graph = UndirectedGraph()
     graph.add_nodes(
          ["1", "2", "3", "4"]
     )

     graph.add_edges(
          [
               ("1", "4", 20), ("1", "3", 15), ("4", "3", 30), ("2", "3", 35), ("1", "2", 10), ("2", "4", 25)
          ]
     )
     
     solver = TSPSolver(graph)
     cost, _, path = solver.solve()
     
     print("Minimum-cost tour:", path)
     print("Cost:", cost)

     graph.plot_overlay_TSP(solver)