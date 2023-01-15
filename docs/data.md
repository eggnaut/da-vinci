# Usage 
```py
from EggEngine import data # or 
import EggEngine.data
```

Includes many useful functions related to data and data storage within Python, mainly lists and 2D lists (arrays).

Made by @eggnaut

---

## sort

Sorts any Python list using the selection sort algorithm.

**Syntax**
```py
sort(target)
```

**Args**
```text
target (list): any list with any values that needs to be sorted.
```

**Returns**
```text
new (list): the same items as the orginal list, but sorted using the selection sort algorithm.
```

---

## generateList

Generates a prefilled Python list with random integer items.

**Syntax**
```py
generateList(length, startVal, endVal)
```

**Args**
```text
length (int): how many items in the list
startVal (int): the start point for the range of random integers
endVal (int): the end point for the range of random int
```

**Returns**
```text
new (list): a list with random integer items.
```

---

## generateArray

Generates a prefilled 2D Python list (array) with random integer items.

**Syntax**
```py
generateArray(rows, cols, startVal, endVal)
```

**Args**
```text
rows (int): how many rows (lists) you want in the array
cols (int): how many columns (items) you want in each row (list)
startVal (int): the start point for the range of random integers
endVal (int): the end point for the range of random integers
```

**Returns**
```text
new (list): a 2D Python list (array) with random integer items.
```

---

## loopArray

Loops through a 2D Python list (array) and finds all items in it.

**Syntax**
```py
loopArray(array)
```

**Args**
```text
array (list): the 2D Python list (array) which the function will search through
```

**Returns**
```text
cells (list): a list filled with tuples as items. Each tuple follows this format: row (list) index, cell (item) index, cell (item's value)
```

---

## findCell

Gives the exact coordinates of an item within a 2D Python list (array) in the form of a row index and column index.

**Syntax**
```py
findCell(array, cell)
```

**Args**
```text
array (list): any 2D Python list (array) that contains items with any type of value.
cell (any): the item you are looking for within the array
```

**Returns**
```text
coordinate: the position of the cell within the array as (row index, column index)
```
