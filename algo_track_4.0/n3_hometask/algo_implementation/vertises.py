from dataclasses import dataclass, field
from abc import ABC, abstractclassmethod
from typing import Dict, Iterator, Tuple, List, Union
from copy import deepcopy


__all__ = [
    'Vertices', 'VerticesList', 'VerticesMatrix', 'Dists', 'VertexInfo'
]


@dataclass
class Vertices(ABC):
    vertices: Union[
        Dict[int, List[Tuple[int]]],
        List[List[int]]
    ] = field(init=False, repr=False)
    v_count: int = field(init=False, repr=False)

    def __init__(self):
        pass

    def __call__(self) -> Union[Dict[int, List[Tuple[int]]],List[List[int]]]:
        return self.vertices

    @abstractclassmethod
    def get_item(self, n_vertex: int) -> Tuple[int, int]:
        ...

    @abstractclassmethod
    def get_invers_item(self, n_vertex: int) -> Tuple[int, int]:
        ...


@dataclass
class VerticesList(Vertices):
    '''
    Class for representation graph as an adjacency list:
    {
        from_vertex: [(to_vertex, weight), ...]
        ...
    }

    Parameters
    ----------
    matrix_graph : Tuple[List[List[int]], int], default=None
        The parameter contains a tuple with two values:
        - the adjacency matrix of graph
        - the count of vertices

    Attributes
    ----------
    vertices : Dict[int, List[Tuple[int]]]
        Adjacency list of vertices in dict representation
    inverse_vertices : Dict[int, List[Tuple[int]]]
        Adjacency list of vertices with inverse edges in dict representation
    v_count : int
        A count of the vertices in graph

    Raises
    ------
    ValueError
        If the vertices list have been set already
    '''

    vertices: Dict[int, List[Tuple[int]]] = field(init=False, repr=False)
    inverse_vertices: Dict[int, List[Tuple[int]]] = field(init=False, repr=False)
    v_count: int = field(init=False, repr=False)

    def __init__(self, matrix_graph: Tuple[List[List[int]], int] = None):
        if matrix_graph is not None:
            self.set_vertices(matrix_graph)
            self.v_count = matrix_graph[1]
        else:
            self.vertices = {}
            self.inverse_vertices = {}
            self.v_count = 0

    def __set_by_vertex(
        self,
        set_to: Dict[int, List[Tuple[int]]],
        v_from: int,
        v_to: int,
        weight: int
    ):
        v_key = set_to.get(v_from)
        if v_key:
            set_to[v_from].append((v_to, weight))
        else:
            set_to[v_from] = [(v_to, weight)]

    def set_vertex(self, v_from: int, v_to: int, weight: int):
        '''
        Sets vertex v_from with a new dependent with vertex
        v_to and the weight forward and inverse way

        Parameters
        ----------
        v_from : int
        v_to : int
        weight : int
        '''

        if weight:
            self.__set_by_vertex(self.vertices, v_from, v_to, weight)
            self.__set_by_vertex(self.inverse_vertices, v_to, v_from, weight)
            self.v_count = v_from

    def set_vertices(self, matrix_graph: Tuple[List[List[int]], int]):
        '''
        Sets vertices from the adjacency matrix of graph with vertices
        if list haven't been set yet

        Parameters
        ----------
        matrix_graph : Tuple[List[List[int]], int], default=None
            The parameter contains a tuple with two values:
            - the adjacency matrix of graph
            - the count of vertices

        Raises
        ------
        ValueError
            If the vertices list have been set already
        '''
        if len(self.vertices) > 0:
            raise ValueError('Vertices list have been set already')

        c_vertices = matrix_graph[1]

        for v_from in range(1, c_vertices + 1):
            for v_to in range(1, c_vertices + 1):
                self.set_vertex(
                    v_from, v_to, matrix_graph[0][v_from - 1][v_to - 1]
                )

    def __neighbors_generator(
        self, vertices: Dict[int, List[Tuple[int]]], n_vertex: int
    ) -> Iterator[Tuple[int, int]]:
        neighbors = vertices.get(n_vertex)
        if neighbors:
            for neighbor in neighbors:
                v_to, weight = neighbor
                yield v_to, weight

    def get_item(self, n_vertex: int) -> Iterator[Tuple[int, int]]:
        return self.__neighbors_generator(self.vertices, n_vertex)

    def get_invers_item(self, n_vertex: int) -> Iterator[Tuple[int, int]]:
        return self.__neighbors_generator(self.inverse_vertices, n_vertex)


@dataclass
class VerticesMatrix(Vertices):
    '''
    Class for representation graph as an adjacency matrix:
    {
        [[adj_weight, ..., adj_weight]
        ...]
    }
    Be carefull, the class expected that the names of the vertices
    if from 1 to n

    Parameters
    ----------
    v_count : int
        A count of the vertices in graph
    matrix_graph : List[List[int]]
        The adjacency graph in List[List] representation with weights

    Attributes
    ----------
    vertices : List[List[int]]
        Adjacency list of vertices in matrix List[List] representation
    v_count : int
        A count of the vertices in graph
    '''

    vertices: List[List[int]] = field(init=False, repr=False)
    v_count: int = field(init=False, repr=False)

    def __init__(self, v_count: int, adj_matrix: List[List[int]]):
        self.v_count = v_count
        self.vertices = deepcopy(adj_matrix)

    def __idx(self, vertex: int) -> int:
        '''
        Returns the index of vertex in the adjacency of graph
        '''

        return vertex - 1

    def reset_vertex_weight(self, v_from: int, v_to: int, weight: int):
        '''
        Resets the dependent between v_from and v_to vertices with a new weight
        if the vertices in the adjacency of graph

        Parameters
        ----------
        v_from : int
        v_to : int
        weight : int

        Raises
        ------
        IndexError
            If the one or both vertices isn't in list
        '''
        try:
            self.vertices[self.__idx(v_from)][self.__idx(v_to)] = weight
        except:
            raise IndexError(f'Vertex {v_from} or/and {v_to} isn\'t in graph')

    def get_item(self, n_vertex: int) -> Iterator[Tuple[int, int]]:
        for to_idx, weight in zip(
            range(0, self.v_count), self.vertices[n_vertex - 1]
        ):
            if weight:
                yield (to_idx + 1), weight

    def get_invers_item(self, n_vertex: int) -> Iterator[Tuple[int, int]]:
        for to_idx in range(0, self.v_count):
            weight = self.vertices[to_idx][n_vertex - 1]
            if weight:
                yield (to_idx + 1), weight


@dataclass
class Dists(dict):
    n_vertex: int = field(init=False, repr=False)
    dist: Union[float, int] = float('inf')

    def __init__(self, n_vertex: int):
        self.n_vertex = n_vertex

    def __call__(self) -> Union[float, int]:
        return self.dist

    def __lt__(self, other: 'Dists') -> bool:
        return self.dist < other.dist

    def get_attributes(self) -> str:
        return f'n_vertex: {self.n_vertex} dist: {self.dist}'


@dataclass
class VertexInfo:
    n_vertex: int = field(init=False, repr=False)
    is_visited: bool = False
    dist: Dists = field(init=False, repr=False)
    v_prev: int = -1

    def __init__(self, n_vertex: int):
        self.n_vertex = n_vertex
        self.dist = Dists(n_vertex)

    def get_info(self) -> str:
        return f'n_vertex: {self.n_vertex} '\
            f'is_visited: {self.is_visited} '\
            f'dist: {self.dist()} '\
            f'v_prev: {self.v_prev}'


    def update_prev_vertex(self, v_from: int, weight: int) -> bool:
        is_udated = False

        if self.dist() > weight:
            self.dist.dist = weight
            self.v_prev = v_from
            is_udated = True

        return is_udated
