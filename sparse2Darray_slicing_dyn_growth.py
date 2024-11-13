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
            row_slice, col_slice = index
            
            # Handle row and column slicing
            if isinstance(row_slice, slice) or isinstance(col_slice, slice):
                return self._slice_2d(row_slice, col_slice)
            else:
                row, col = row_slice, col_slice
                if row >= self._rows or col >= self._cols:
                    raise IndexError("Index out of range")
                return self._data.get((row, col), 0)
        else:
            raise TypeError("Index should be a tuple of (row, col)")

    def _slice_2d(self, row_slice, col_slice):
        # Normalize row and column slices to valid ranges
        row_range = range(*row_slice.indices(self._rows))
        col_range = range(*col_slice.indices(self._cols))
        
        # Create the sliced subarray as a 2D list
        sliced_values = []
        for row in row_range:
            sliced_row = []
            for col in col_range:
                sliced_row.append(self._data.get((row, col), 0))
            sliced_values.append(sliced_row)
        
        # Return a new Sparse2DArray with the sliced portion
        new_rows = len(sliced_values)
        new_cols = len(sliced_values[0]) if sliced_values else 0
        return Sparse2DArray(new_rows, new_cols, sliced_values)

    def __setitem__(self, index, value):
        row, col = index
        if row >= self._rows or col >= self._cols:
            raise IndexError("Index out of range")
        if value != 0:
            self._data[(row, col)] = value
        elif (row, col) in self._data:
            del self._data[(row, col)]

    def __delitem__(self, index):
        row, col = index
        if (row, col) in self._data:
            del self._data[(row, col)]

    def append_row(self, new_row=None):
        """Appends a new row to the end of the array."""
        new_row_values = new_row or [0] * self._cols
        if len(new_row_values) != self._cols:
            raise ValueError("New row must have the same number of columns")
        for col, value in enumerate(new_row_values):
            if value != 0:
                self._data[(self._rows, col)] = value
        self._rows += 1

    def append_column(self, new_col=None):
        """Appends a new column to the right of the array."""
        new_col_values = new_col or [0] * self._rows
        if len(new_col_values) != self._rows:
            raise ValueError("New column must have the same number of rows")
        for row, value in enumerate(new_col_values):
            if value != 0:
                self._data[(row, self._cols)] = value
        self._cols += 1

    def __str__(self):
        result = []
        for row in range(self._rows):
            current_row = []
            for col in range(self._cols):
                current_row.append(self._data.get((row, col), 0))
            result.append(current_row)
        return str(result)

# Example usage:
sparse_2d = Sparse2DArray(3, 3, [[0, 1, 0], [0, 0, 0], [3, 0, 0]])

# Accessing elements
print(sparse_2d[0, 1])  # Should print 1

# Slicing rows and columns
sub_array = sparse_2d[0:2, 0:2]
print(sub_array)  # Should print a 2x2 subarray

# Append a new row
sparse_2d.append_row([5, 0, 0])
print(sparse_2d)

# Append a new column
sparse_2d.append_column([0, 7, 0, 0])
print(sparse_2d)