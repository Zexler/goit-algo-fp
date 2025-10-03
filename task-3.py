import heapq


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        if weight is None:
            weight = 0
        self.vertices[from_vertex].append((to_vertex, weight))
        self.vertices[to_vertex].append((from_vertex, weight))

    def dijkstra(self, start_vertex):
        distances = {vertex: float("infinity") for vertex in self.vertices}
        distances[start_vertex] = 0

        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


def main():
    metro_graph = Graph()

    metro_graph.add_vertex("Майдан Незалежності")
    metro_graph.add_vertex("Хрещатик")
    metro_graph.add_vertex("Золоті ворота")
    metro_graph.add_vertex("Університет")
    metro_graph.add_vertex("Театральна")
    metro_graph.add_vertex("Палац Спорту")
    metro_graph.add_vertex("Арсенальна")
    metro_graph.add_vertex("Дніпро")
    metro_graph.add_vertex("Лівобережна")
    metro_graph.add_vertex("Дарниця")
    metro_graph.add_vertex("Позняки")
    metro_graph.add_vertex("Вокзальна")
    metro_graph.add_vertex("Політехнічний інститут")

    metro_graph.add_edge("Майдан Незалежності", "Хрещатик", 1)
    metro_graph.add_edge("Хрещатик", "Золоті ворота", 1)
    metro_graph.add_edge("Майдан Незалежності", "Університет", 2)
    metro_graph.add_edge("Університет", "Театральна", 1)
    metro_graph.add_edge("Театральна", "Золоті ворота", 2)
    metro_graph.add_edge("Золоті ворота", "Політехнічний інститут", 3)
    metro_graph.add_edge("Політехнічний інститут", "Вокзальна", 1)
    metro_graph.add_edge("Майдан Незалежності", "Дарниця", 3)
    metro_graph.add_edge("Дарниця", "Лівобережна", 1)
    metro_graph.add_edge("Лівобережна", "Дніпро", 2)
    metro_graph.add_edge("Дніпро", "Арсенальна", 2)
    metro_graph.add_edge("Майдан Незалежності", "Палац Спорту", 2)
    metro_graph.add_edge("Палац Спорту", "Золоті ворота", 2)
    metro_graph.add_edge("Майдан Незалежності", "Позняки", 2)

    start_vertex = "Майдан Незалежності"
    shortest_distances = metro_graph.dijkstra(start_vertex)

    print("\nНайкоротші відстані від станції 'Майдан Незалежності':")
    print("Станція                 | Відстань")
    print("------------------------|----------")
    for station, dist in sorted(shortest_distances.items()):
        d = "∞" if dist == float("infinity") else str(dist)
        print(f"{station:<24} | {d}")


if __name__ == "__main__":
    main()
