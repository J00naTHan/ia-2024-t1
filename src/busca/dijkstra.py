"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""

from heapq import heapify, heappush, heappop
from queue import deque

from util import reverse_path


def dijkstra(Grafo, start, goal):
  """Busca em graph, um caminho entre start e goal usando Dijkstra."""
  dist, prev, Q = {}, {}, deque()
  for nodo in Grafo.nodos:
    dist[nodo] = float('inf')
    prev[nodo] = None
    Q.appendleft(nodo)
  dist[start] = 0

  while Q:
    #u = nodo com menor custo que existe em Q (no caso de uma iteração que está em start, u seria o próprio, pois ele tem custo 0, enquanto os outros tem custo infinito)
    Q.pop(u)

  # u == goal para baixo não existe no pseudocódigo do professor
  if u == goal:
    analisados = 0
    for key in prev.keys():
      if prev[key] != None
	    analisados += 1
    return (analisados, dist, [prev #falta recuperar o caminho])

  for v in Graph.vizinhos(u):
    if v in Q:
      alt = dist[u] + Graph.arestas[u][v]
      if alt < dist[v]:
        dist[v] = alt
        prev[v] = u
