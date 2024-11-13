class Sparse2DArray:
    def __init__(self, rows, cols, values=None):
        self._data = {}  # Dictionary to store non-zero values
        self._rows = rows
        self._cols = cols

        # Initialize with given values (a 2D list), if provided
        if values:
            for row in range(rows):
                for col in range(cols):
                    if values[row][col] != 0:
                        self._data[(row, col)] = values[row][col]

    def __len__(self):
        return self._rows * self._cols

    def __getitem__(self, index):
        if isinstance(index, tuple):
            row, col = index
            if row >= self._rows or col >= self._cols:
                raise IndexError("Index out of range")
            return self._data.get((row, col), 0)
        else:
            raise TypeError("Index should be a tuple of (row, col)")

    def __setitem__(self, index, value):
        row, col = index
        if row >= self._rows or col >= self._cols:
            raise IndexError("Index out of range")
        if value != 0:
            self._data[(row, col)] = value
        elif (row, col) in self._data:
            del self._data[(row, col)]

    def __str__(self):
        result = []
        for row in range(self._rows):
            current_row = []
            for col in range(self._cols):
                current_row.append(self._data.get((row, col), 0))
            result.append(current_row)
        return str(result)

# Example usage of 2D SparseArray:
sparse_2d = Sparse2DArray(3, 3, [[0, 1, 0], [0, 0, 0], [3, 0, 0]])
print(sparse_2d)  # Should print a 3x3 grid
print(sparse_2d[0, 1])  # Should print 1
sparse_2d[2, 0] = 0  # Remove the non-zero value
print(sparse_2d)  # Should print the updated grid