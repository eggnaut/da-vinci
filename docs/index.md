# EggEngine
A framework/library written with and for Python.

## Features
EggEngine comes with 7 Python modules ready to use!

1. `data`
2. `debug`
3. `encrypt`
4. `files`
5. `image`
6. `module`
7. `turtl`
8. `ui` (experimental)

## Setup
This will install Python modules (or dependencies) that are required to allow all features of EggEngine to work as intended.

1. Create a new Python file, you can name it anything you want.
2. Copy the folder `EggEngine` into the same diredctory.
3. In the Python file, add the following line:
```python
from EggEngine import module
```
- Or (not recommended) alternative:
```python
import EggEngine.module
```
4. Next, add these line:
```python
module.dependencies()
```
- If you used the alternative, add this line:
```python
EggEngine.module.dependencies()
```
5. You're ready to use EggEngine!

## Quick start

Obviously, the first step would be to download the repository or from the latest release. Then, follow these steps:

1. Copy the folder `EggEngine` into your project folder.
2. In your Python file(s), add the following line: 
```python 
from EggEngine import <module you want to use>
```
-  For example, if I want to use the `data` module from `EggEngine`, I would add this line of code:
```python
from EggEngine import data
```
- When calling functions, this is what it would look like:
```python
data.function()
```
-  Another (not recommended) alternative:
```python
import EggEngine.<module you want to use>
```
- Following my example from earlier, this is what it would look like:
```python
import EggEngine.data
```
- The downside to this import statement is when calling functions, you must type out the parent module, then the module, and finally the function like this:
```python
EggEngine.data.function()
```
3. Now you're ready to start using EggEngine in your project!
