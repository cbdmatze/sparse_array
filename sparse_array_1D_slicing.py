class SparseArray:
    def __init__(self, values):
        self._data = {}
        self._length = len(values)
        for index, value in enumerate(values):
            if value != 0:
                self._data[index] = value

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if isinstance(index, slice):
            # If index is a slice, handle it by creating a sublist and return a new SparseArray
            start, stop, step = index.indices(self._length)  # Normalize slice values
            sliced_values = [self[i] for i in range(start, stop, step)]
            return SparseArray(sliced_values)
        if index >= self._length or index < 0:
            raise IndexError("Index out of range")
        return self._data.get(index, 0)

    def __setitem__(self, index, value):
        if index >= self._length or index < 0:
            raise IndexError("Index out of range")
        if value != 0:
            self._data[index] = value
        elif index in self._data:
            del self._data[index]

    def __delitem__(self, index):
        if index >= self._length or index < 0:
            raise IndexError("Index out of range")
        if index in self._data:
            del self._data[index]
        keys_to_update = [k for k in self._data.keys() if k > index]
        for key in keys_to_update:
            self._data[key - 1] = self._data.pop(key)
        self._length -= 1

    def append(self, value):
        if value != 0:
            self._data[self._length] = value
        self._length += 1

    def __contains__(self, value):
        return value == 0 or value in self._data.values()

    def __add__(self, other):
        new_values = [self[i] for i in range(self._length)] + [other[i] for i in range(len(other))]
        return SparseArray(new_values)

    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __eq__(self, other):
        return len(self) == len(other)

    def __str__(self):
        return str([self[i] for i in range(self._length)])

# Example Usage
my_array = SparseArray([0, 7, 0, 5, 0, 6, 0, 0, 0, 4, 13, 0, 0])
print(my_array[1:5])  # Should return a new SparseArray with values [7, 0, 5, 0]