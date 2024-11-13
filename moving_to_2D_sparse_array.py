class Sparse2DArray:
    def __init__(self, rows, cols, values=None):
        self._data = {} # Dictionary to store non-zero values
        self._rows = rows
        self._cols = cols
    
    # Initialize with given values (a 2D lsit), if provided
    if values:
        for row in range(rows):
            for col in range(col):
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
    
    