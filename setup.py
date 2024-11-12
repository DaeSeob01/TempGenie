
---

#### setup.py

```python
from setuptools import setup, find_packages

setup(
    name='tempgenie',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'tempgenie = tempgenie.main:main',
        ],
    },
)
