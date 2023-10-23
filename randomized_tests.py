import unittest 
import random

from graph import UndirectedGraph
from tsp_solver import TSPSolver, BruteForceTSPSolver

SEED = 40
random.seed(SEED)

class RandomizedUnitTests(unittest.TestCase):
    TRIALS = 10
    SMALL = 5
    MED = 10
    LARGE = 15

    def generate_random_graph(self, size):
        graph = UndirectedGraph()
        graph.add_nodes(
            [str(i) for i in range(size)]
        )

        for i in range(size):
            for j in range(i + 1, size):
                graph.add_edge(str(i), str(j), weight = random.randint(1, 100))
        return graph
    
    def __test_small_graph(self):
        graph = self.generate_random_graph(self.SMALL)
        solver = TSPSolver(graph)
        solver_cost, *_ = solver.solve()

        brute_force = BruteForceTSPSolver(graph)
        brute_force_cost, *_ = brute_force.solve()

        return solver_cost, brute_force_cost

    def __test_med_graph(self):
        graph = self.generate_random_graph(self.MED)
        solver = TSPSolver(graph)
        solver_cost, *_ = solver.solve()

        brute_force = BruteForceTSPSolver(graph)
        brute_force_cost, *_ = brute_force.solve()

        return solver_cost, brute_force_cost
    
    def test_trials(self):
        solver_costs = []
        brute_force_costs = []

        for _ in range(self.TRIALS):
            x, y = self.__test_small_graph()
            solver_costs.append(x)
            brute_force_costs.append(y)
        
        self.assertEqual(solver_costs, brute_force_costs)


if __name__ == "__main__":
    unittest.main()