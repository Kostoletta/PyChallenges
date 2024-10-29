# Store Class

## Overview

The `Store` class provides two implementations for managing collections of values:

### Unique Value Store

- **Functionality**: Stores values without allowing duplicates.
- **Operations**:
  - **Add**: Insert a value only if it doesn’t already exist in the store.
  - **Delete**: Remove a specified value from the store.
  - **Get Random**: Retrieve a random value from the store.

### Duplicate Value Store

- **Functionality**: Allows storing values with duplicates.
- **Operations**:
  - **Add**: Insert a value, permitting multiple occurrences.
  - **Delete**: Remove one instance of a specified value, preserving other occurrences.
  - **Get Random**: Retrieve a random value from the store.

## Features

- Both implementations allow constant time \(O(1)\) operations for adding, deleting, and retrieving random values, making them efficient for dynamic data management.

## Usage

To use the `Store` class, simply initialize an instance and call the appropriate methods to manage your collection of values.

### Example

```python
# Initialize the Store
my_store = Store()

# Add values
my_store.add(5)
my_store.add(10)

# Delete a value
my_store.delete(5)

# Get a random value
random_value = my_store.get_random()

# Print the random value
print(random_value)
```
