## Goal-1 
Refactor the `Polygon` class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our `Polygon` class "immutable").

## Solution-1
To refactor the Polygon class so that the calculated properties are lazy properties, we can use Python's functools.lru_cache decorator to cache the results of the properties, or manually implement caching using instance variables. For simplicity and clarity, I'll use manual caching with instance variables.

1. Added Caching Attributes: Added private attributes (_side_length, _apothem, _area, and _perimeter) to store the calculated values.

2. Checked for Cache: Each property method now checks if its cached value is None. If it is None, it computes the value and stores it in the corresponding private attribute. If it's not None, it simply returns the cached value.

This way, each property is only computed once and the result is reused, making the properties lazy and efficient in terms of recalculation.

## Goal-2
Refactor the `Polygons` (sequence) type, into an **iterable**. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.


## Solution-2
Remove the list-based storage mechanism and instead generate each polygon on-the-fly. Here’s how we can achieve this:

1. Remove the internal list: Instead of storing polygons in a list, generate them on-the-fly.
2. Implement lazy iteration: The iterator should compute polygons as needed rather than storing them.

### Polygons Class:

__getitem__ Method: Computes the Polygon object directly using the index, where the index s corresponds to a polygon with n = s + 3.
max_efficiency_polygon Property: Iterates over the possible number of sides, computes each Polygon, and keeps track of the one with the highest area-to-perimeter ratio.
__iter__ Method: Returns an instance of PolygonsIterator, which will handle lazy evaluation.

### PolygonsIterator Class:

__init__ Method: Initializes the iterator with the starting number of sides (3) and the maximum number of sides (m).
__next__ Method: Computes the next polygon on-the-fly and advances the state of the iterator. When all polygons are exhausted, it raises StopIteration.
With these changes, the Polygons class and its iterator no longer use an internal list to store polygons, thereby achieving lazy computation and iteration.