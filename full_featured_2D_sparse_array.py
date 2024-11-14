class Sparse2DArray:
    def __init__(self, rows, cols, values=None):
        self.rows = rows
        self.cols = cols
        self.data = {}
        if values:
            for r, row in enumerate(values):
                for c, value in enumerate(row):
                    if value != 0:
                        self.data[(r, c)] = value

    # Get an element, supports slicing
    def __getitem__(self, indices):
        if isinstance(indices[0], slice) or isinstance(indices[1], slice):
            row_slice = indices[0] if isinstance(indices[0], slice) else slice(indices[0], indices[0] + 1)
            col_slice = indices[1] if isinstance(indices[1], slice) else slice(indices[1], indices[1] + 1)

            sliced_array = []
            for r in range(*row_slice.indices(self.rows)):
                row_data = []
                for c in range(*col_slice.indices(self.cols)):
                    row_data.append(self.data.get((r, c), 0))
                sliced_array.append(row_data)

            return sliced_array
        else:
            row, col = indices
            if not (0 <= row < self.rows and 0 <= col < self.cols):
                raise IndexError("Index out of bounds.")
            return self.data.get((row, col), 0)

    # Set an element, removes zero entries from the dictionary
    def __setitem__(self, indices, value):
        row, col = indices
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("Index out of bounds.")
        if value == 0:
            self.data.pop((row, col), None)
        else:
            self.data[(row, col)] = value

    # Append a new row
    def append_row(self, row):
        if len(row) != self.cols:
            raise ValueError("Row length must match the number of columns.")
        for c, value in enumerate(row):
            if value != 0:
                self.data[(self.rows, c)] = value
        self.rows += 1

    # Append a new column
    def append_column(self, column):
        if len(column) != self.rows:
            raise ValueError("Column length must match the number of rows.")
        for r, value in enumerate(column):
            if value != 0:
                self.data[(r, self.cols)] = value
        self.cols += 1

    # Check if a value exists in the array
    def __contains__(self, value):
        return value in self.data.values() or (value == 0 and (self.rows * self.cols != len(self.data)))

    # Concatenate two sparse arrays (row-wise or column-wise)
    def __add__(self, other):
        if not isinstance(other, Sparse2DArray):
            raise ValueError("Can only concatenate Sparse2DArray objects.")
        
        # Concatenate row-wise if the number of columns matches
        if self.cols == other.cols:
            new_array = Sparse2DArray(self.rows + other.rows, self.cols)
            for (r, c), value in self.data.items():
                new_array[r, c] = value
            for (r, c), value in other.data.items():
                new_array[r + self.rows, c] = value
            return new_array
        # Concatenate column-wise if the number of rows matches
        elif self.rows == other.rows:
            new_array = Sparse2DArray(self.rows, self.cols + other.cols)
            for (r, c), value in self.data.items():
                new_array[r, c] = value
            for (r, c), value in other.data.items():
                new_array[r, c + self.cols] = value
            return new_array
        else:
            raise ValueError("Incompatible dimensions for concatenation.")

    # Compare the size of two arrays
    def __lt__(self, other):
        if not isinstance(other, Sparse2DArray):
            return NotImplemented
        return (self.rows * self.cols) < (other.rows * other.cols)

    def __gt__(self, other):
        if not isinstance(other, Sparse2DArray):
            return NotImplemented
        return (self.rows * self.cols) > (other.rows * other.cols)

    # Return the total number of elements in the array
    def __len__(self):
        return self.rows * self.cols

# Example usage
if __name__ == "__main__":
    sa = Sparse2DArray(3, 3, [[1, 0, 0], [0, 0, 3], [0, 0, 0]])
    
    # Access elements
    print(sa[0, 0])  # Output: 1
    print(sa[1, 2])  # Output: 3
    print(sa[2, 2])  # Output: 0
    
    # Set elements
    sa[2, 2] = 5
    print(sa[2, 2])  # Output: 5
    
    # Append rows and columns
    sa.append_row([0, 0, 6])
    print(sa[3, 2])  # Output: 6
    
    sa.append_column([0, 0, 0, 9])
    print(sa[3, 3])  # Output: 9
    
    # Slicing
    print(sa[0:2, 0:2])  # Output: [[1, 0], [0, 0]]
    
    # Contains check
    print(5 in sa)  # Output: True
    print(7 in sa)  # Output: False
    
    # Concatenation
    sa2 = Sparse2DArray(2, 3, [[7, 8, 9], [4, 5, 6]])
    new_array = sa + sa2
    print(new_array[4, 2])  # Output: 9