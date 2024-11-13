

Sparse2DArray: Efficient 2D Array with Slicing and Dynamic Growth

Overview

The Sparse2DArray class implements a memory-efficient 2D array, where only non-zero elements are stored in memory. This class supports Pythonic operations like slicing, element access, and dynamic growth through row and column appending. The class is designed to handle large arrays where most of the values are zeros (referred to as sparse arrays), allowing for efficient storage and manipulation.

Key Features

	•	Efficient Storage: Only stores non-zero elements, reducing memory usage.
	•	2D Slicing: Supports row and column slicing for sub-array extraction.
	•	Dynamic Growth: Allows appending rows and columns dynamically, updating the array’s dimensions.
	•	Intuitive API: Supports typical list operations like indexing, length retrieval, and appending.

Table of Contents

	•	Installation
	•	Usage
	•	Initialization
	•	Accessing Elements
	•	Slicing
	•	Appending Rows
	•	Appending Columns
	•	Deleting Elements
	•	Example
	•	Contributing
	•	License

Installation

You can include Sparse2DArray in your Python project by simply copying the class code into your project. There are no external dependencies required.

# If you're using this as a standalone script, just include it directly in your project.


Usage

Initialization

To create a Sparse2DArray, initialize it with the number of rows and columns, and optionally, with a 2D list of values.

sparse_array = Sparse2DArray(3, 3, [[0, 1, 0], [0, 0, 0], [3, 0, 0]])



Accessing Elements

You can access individual elements using standard Python indexing. If the element is not explicitly stored (i.e., it’s a zero), the array will return 0 by default.

value = sparse_array[0, 1]  # Returns 1
empty_value = sparse_array[2, 2]  # Returns 0 (as it's a sparse value)



Slicing

The Sparse2DArray supports slicing for both rows and columns:

sub_array = sparse_array[0:2, 1:3]  # Slices a 2x2 subarray
print(sub_array)  # Prints the sliced sub-array

Slicing is very useful when you need to extract smaller sections of the array without affecting the original array.



Appending Rows

You can append a new row to the end of the array using the append_row() method:

sparse_array.append_row([5, 0, 0])  # Appends a new row

The new row should have the same number of columns as the existing array.



Appending Columns

You can append a new column to the right of the array using the append_column() method:

sparse_array.append_column([0, 7, 0, 0])  # Appends a new column

The new column should have the same number of rows as the existing array.



Deleting Elements

You can delete elements from the array by using the del keyword:

del sparse_array[0, 1]  # Removes the element at row 0, column 1

After deleting, accessing that element will return 0 as it’s now a sparse value.




Example

# Create a 3x3 sparse array
sparse_array = Sparse2DArray(3, 3, [[0, 1, 0], [0, 0, 0], [3, 0, 0]])
print(sparse_array)

# Accessing elements
print(sparse_array[0, 1])  # Should print 1
print(sparse_array[2, 2])  # Should print 0 (sparse)

# Slicing a subarray
sub_array = sparse_array[0:2, 0:2]
print(sub_array)  # Should print a 2x2 subarray

# Appending a new row
sparse_array.append_row([5, 0, 0])
print(sparse_array)  # Should now have an additional row

# Appending a new column
sparse_array.append_column([0, 7, 0, 0])
print(sparse_array)  # Should now have an additional column

# Deleting an element
del sparse_array[0, 1]
print(sparse_array[0, 1])  # Should print 0 as the element is now sparse



Contributing

Contributions to extend or improve the Sparse2DArray class are welcome. You can fork the repository and create a pull request with your changes. Please include tests for any new features.



License

This project is licensed under the MIT License.



By using the Sparse2DArray, you can efficiently store and manipulate sparse data without wasting memory. The class is flexible and extensible, making it a great choice for handling large datasets with mostly empty values.