class SparseArray:
    def __init__(self, values):
        self._data = {}  # Store non-zero values in a dictionary
        self._length = len(values)  # The total length of the array
        
        # Initialize the array with non-zero values
        for index, value in enumerate(values):
            if value != 0:
                self._data[index] = value

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if index >= self._length or index < 0:
            raise IndexError("Index out of range")
        
        return self._data.get(index, 0)  # Return 0 if index not found

    def __setitem__(self, index, value):
        if index >= self._length or index < 0:
            raise IndexError("Index out of range")
        
        if value != 0:
            self._data[index] = value
        elif index in self._data:
            del self._data[index]  # Remove the key if we're setting it to 0

    def __delitem__(self, index):
        if index >= self._length or index < 0:
            raise IndexError("Index out of range")
        
        # Remove the value at the index (if present), and shift all items to the left
        if index in self._data:
            del self._data[index]
        
        # Shift all elements after the deleted one
        keys_to_update = [k for k in self._data.keys() if k > index]
        for key in keys_to_update:
            self._data[key - 1] = self._data.pop(key)
        
        # Decrease the virtual length
        self._length -= 1

    def append(self, value):
        if value != 0:
            self._data[self._length] = value
        self._length += 1

    def __contains__(self, value):
        # Check if value exists in the sparse array
        return value == 0 or value in self._data.values()

    def __add__(self, other):
        if not isinstance(other, SparseArray):
            raise ValueError("Can only concatenate with another SparseArray")
        
        new_values = [self[i] for i in range(self._length)] + [other[i] for i in range(len(other))]
        return SparseArray(new_values)

    def __lt__(self, other):
        if not isinstance(other, SparseArray):
            return NotImplemented
        return len(self) < len(other)

    def __gt__(self, other):
        if not isinstance(other, SparseArray):
            return NotImplemented
        return len(self) > len(other)

    def __eq__(self, other):
        if not isinstance(other, SparseArray):
            return NotImplemented
        return len(self) == len(other)

    def __str__(self):
        return str([self[i] for i in range(self._length)])

# Example Usage
my_array = SparseArray([0, 7, 0, 5, 0, 6, 0, 0, 0, 4, 13, 0, 0])
print(len(my_array))  # Should print 13
print(my_array[3])    # Should print 5
del my_array[0]
print(my_array[0])    # Should print 7
my_array.append(10)
print(my_array)  # Should print [7, 0, 5, 0, 6, 0, 0, 0, 4, 13, 0, 0, 10]