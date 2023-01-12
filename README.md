# EggEngine
A custom framework/engine written with and for Python.

## Features:
EggEngine comes with 7 Python modules ready to use!
1. `data`
2. `debug`
3. `encrypt`
4. `files`
5. `image`
6. `module`
7. `turtl`

## Quick start:

Obviously, the first step would be to download the source code from this repository. Then, follow these steps:

1. Copy the folder `engine` into your project folder.
2. In your Python file, add the following line: 
```python 
from engine import <module you want to use>
```
-  For example, if I want to use the `data` module from `engine`, I would add this line of code:
```python
from engine import data
```
- When calling functions, this is what it would look like:
```python
data.function()
```
-  Another (not recommended) alternative:
```python
import engine.<module you want to use>
```
- Following my example from earlier, this is what it would look like:
```python
import engine.data
```
- The downside to this import statement is when calling functions, you must type out the parent module, then the module, and finally the function like this:
```python
engine.data.function()
```
3. Now you're ready to start using EggEngine!
