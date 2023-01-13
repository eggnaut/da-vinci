# EggEngine
A custom framework/library written with and for Python.

## Socials

![GitHub Repo stars](https://img.shields.io/github/stars/eggnaut/EggEngine?logo=Github&style=for-the-badge) ![GitHub watchers](https://img.shields.io/github/watchers/eggnaut/EggEngine?logo=Github&style=for-the-badge) ![GitHub followers](https://img.shields.io/github/followers/eggnaut?logo=Github&style=for-the-badge)

## Downloads

![GitHub all releases](https://img.shields.io/github/downloads/eggnaut/EggEngine/total?style=for-the-badge) ![GitHub repo size](https://img.shields.io/github/repo-size/eggnaut/EggEngine?style=for-the-badge) ![GitHub](https://img.shields.io/github/license/eggnaut/EggEngine?style=for-the-badge)

## Developers

![GitHub issues](https://img.shields.io/github/issues/eggnaut/EggEngine?style=for-the-badge) ![GitHub closed issues](https://img.shields.io/github/issues-closed/eggnaut/EggEngine?style=for-the-badge)

![GitHub pull requests](https://img.shields.io/github/issues-pr/eggnaut/EggEngine?style=for-the-badge) ![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/eggnaut/EggEngine?style=for-the-badge)

![GitHub language count](https://img.shields.io/github/languages/count/eggnaut/EggEngine?style=for-the-badge) ![GitHub top language](https://img.shields.io/github/languages/top/eggnaut/EggEngine?style=for-the-badge)

![GitHub last commit](https://img.shields.io/github/last-commit/eggnaut/EggEngine?style=for-the-badge) ![GitHub contributors](https://img.shields.io/github/contributors/eggnaut/EggEngine?style=for-the-badge)

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
3. Now you're ready to start using EggEngine!
