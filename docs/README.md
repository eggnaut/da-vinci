# EggEngine
A framework/library written with and for Python.

Currently in development.

## Socials:

![GitHub Repo stars](https://img.shields.io/github/stars/eggnaut/EggEngine?color=yellow&logo=Github&style=for-the-badge) ![GitHub watchers](https://img.shields.io/github/watchers/eggnaut/EggEngine?color=orange&logo=Github&style=for-the-badge)
## Download:

![GitHub all releases](https://img.shields.io/github/downloads/eggnaut/EggEngine/total?style=for-the-badge) ![GitHub repo size](https://img.shields.io/github/repo-size/eggnaut/EggEngine?style=for-the-badge) ![GitHub](https://img.shields.io/github/license/eggnaut/EggEngine?style=for-the-badge)

## Developers:

![GitHub issues](https://img.shields.io/github/issues/eggnaut/EggEngine?color=green&style=for-the-badge) ![GitHub closed issues](https://img.shields.io/github/issues-closed/eggnaut/EggEngine?color=red&style=for-the-badge)

![GitHub pull requests](https://img.shields.io/github/issues-pr/eggnaut/EggEngine?color=green&style=for-the-badge) ![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/eggnaut/EggEngine?color=red&style=for-the-badge)

![GitHub language count](https://img.shields.io/github/languages/count/eggnaut/EggEngine?style=for-the-badge) ![GitHub top language](https://img.shields.io/github/languages/top/eggnaut/EggEngine?logo=Python&logoColor=yellow&style=for-the-badge)

![GitHub last commit](https://img.shields.io/github/last-commit/eggnaut/EggEngine?style=for-the-badge) ![GitHub contributors](https://img.shields.io/github/contributors/eggnaut/EggEngine?style=for-the-badge)

## Features:
EggEngine comes with 9 Python modules ready to use!
1. `data`
2. `debug`
3. `encrypt`
4. `files`
5. `image`
6. `module`
7. `turtl`
8. `ui` (experimental)
9. `entities` (experimental)

Note: modules marked with 'experimental' may not function properly and may contain bugs.

## Setup:
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
4. Next, add this line:
```python
module.dependencies()
```
- If you used the alternative, add this line:
```python
EggEngine.module.dependencies()
```
5. Run/execute the Python file.
6. You're ready to use EggEngine!
7. You can now delete this file.

## Integration:

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
