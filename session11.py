import math

import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        self._side_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def count_vertices(self):
        return self._n
    
    @property
    def count_edges(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._R
    
    @property
    def interior_angle(self):
        return (self._n - 2) * 180 / self._n

    @property
    def side_length(self):
        if self._side_length is None:
            self._side_length = 2 * self._R * math.sin(math.pi / self._n)
        return self._side_length
    
    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self._R * math.cos(math.pi / self._n)
        return self._apothem
    
    @property
    def area(self):
        if self._area is None:
            self._area = self._n / 2 * self.side_length * self.apothem
        return self._area
    
    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self._n * self.side_length
        return self._perimeter
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented


class Polygons:
    """
    A class representing a collection of polygons with varying numbers of sides.
    """
    def __init__(self, m, R):
        """
        Initializes a Polygons instance.
        """
        if m < 3:
            raise ValueError('m must be greater than or equal to 3')
        self._m = m
        self._R = R

    def __len__(self):
        """
        Returns the number of polygons in the collection.
        """
        return self._m - 2

    def __repr__(self):
        """
        Provides a string representation of the Polygons instance.
        """
        return f'Polygons(m={self._m}, R={self._R})'

    def __getitem__(self, s):
        """
        Returns the polygon at the specified index.
        """
        if s < 0 or s >= len(self):
            raise IndexError('Index out of range')
        n = s + 3
        return Polygon(n, self._R)

    @property
    def max_efficiency_polygon(self):
        """
        Returns the polygon with the highest area-to-perimeter ratio.
        """
        max_ratio = float('-inf')
        best_polygon = None
        for n in range(3, self._m + 1):
            polygon = Polygon(n, self._R)
            ratio = polygon.area / polygon.perimeter
            if ratio > max_ratio:
                max_ratio = ratio
                best_polygon = polygon
        return best_polygon

    def __iter__(self):
        """
        Returns an iterator for the polygons collection.
        """
        return PolygonsIterator(self._m, self._R)


class PolygonsIterator:
    """
    An iterator for the Polygons class.
    """
    def __init__(self, m, R):
        """
        Initializes a PolygonsIterator instance.
        """
        self._current = 3
        self._m = m
        self._R = R

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next polygon in the sequence.
        """
        if self._current <= self._m:
            polygon = Polygon(self._current, self._R)
            self._current += 1
            return polygon
        else:
            raise StopIteration

if __name__=="__main__":

    polygons = Polygons(5, 10)
    for polygon in polygons:
        print(polygon)