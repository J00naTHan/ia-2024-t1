"""Implementação do algoritmo A*."""

def heuristic(a, b):
  return abs(a.lat - b.lat) + abs(a.lon - b.lon)

def a_star(graph, start, goal):
  """Busca em graph, um caminho entre start e goal usando A*."""
  frontier = PriorityQueue()
  frontier.put(0, start)
  came_from = {start: None}
  cost_so_far = {start: 0}

  while not frontier.empty():
    current = frontier.get()

    if current == goal:
      if came_from[current] is None:
        return [current]
      parent = came_from[current]
      path = [current, parent]
      while parent != start:
        parent = came_from[parent]
        path.append(parent)
      return (len(came_from.keys()), cost_so_far[current], reversed(path))

    for next in graph.neighbors(current):
      new_cost = cost_so_far[current] + graph.cost(current, next)
      if next not in cost_so_far or new_cost < cost_so_far[next]:
         cost_so_far[next] = new_cost
         priority = new_cost + heuristic(goal, next)
         frontier.put(next, priority)
         came_from[next] = current
