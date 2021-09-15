from unittest import TestCase
from graph.DFS import dfs

graph = {1: [3],
         2: [3, 4],
         3: [1, 2, 4, 5],
         4: [3],
         5: [3, 2, 6],
         6: []
         }


class TesDFS(TestCase):
    def testDFS(self):
        visited = list()
        dfs(graph, 1, visited)
        self.assertEqual(len(visited), len(graph.keys()))

