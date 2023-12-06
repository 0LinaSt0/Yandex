import heapq
from typing import Union, List

from .vertises import *


__all__ = ['Dijkstras']


class Dijkstras:

    def __dist_definer(cls, dist: Union[int, float]):
        return (0 if dist == float('inf') else dist)

    def __get_next_vertex(
        cls, track_vertices: List[VertexInfo], refers_dists: List[Dists]
    ) -> int:

        next_vertex = -1

        if len(refers_dists):
            for elem in refers_dists:
                n_vertex = elem.n_vertex
                # print(f'num_v: {n_vertex} -> {track_vertices[n_vertex].dist()}')
                if ((track_vertices[n_vertex].is_visited is False) & \
                    (track_vertices[n_vertex].dist() != float('inf'))
                ):
                    next_vertex = n_vertex
                    track_vertices[n_vertex].is_visited = True
                    break

        return next_vertex

    def define_distance(
        cls, adj_graph: Vertices, v_from: int, v_to: int
    ) -> int:
        track_vertices = [0] + [
            VertexInfo(idx) for idx in range(1, adj_graph.v_count + 1)
        ]
        # print('\n'.join(map(lambda x: x.get_info(), track_vertices[1:])))
        refers_dists = []

        track_vertices[v_from].dist.dist = 0

        while v_from > 0:
            for v_neighbor, weight in adj_graph.get_item(v_from):
                # print(v_neighbor, weight)
                is_updated = track_vertices[v_neighbor].update_prev_vertex(
                    v_from, (track_vertices[v_from].dist() + weight)
                )

                if is_updated:
                    heapq.heappush(
                        refers_dists, track_vertices[v_neighbor].dist
                    )
                # print(refers_dists)

            v_from = cls.__get_next_vertex(track_vertices, refers_dists)

        # print(
        #     '\n'.join((map(lambda x: x.get_info(), track_vertices[1:]))),
        #     track_vertices[v_to].dist(),
        #     sep='\n\n'
        # )

        return cls.__dist_definer(track_vertices[v_to].dist())
