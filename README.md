A small class which loads .env files. It has default type-casting for every standard type, and it also supports variables. 100% Standard.<br>
It's essentially a ``Dotenv``, or ``Environs`` but more limited. It's also faster than ``Dotenv`` loading files, do the benchmark!

# How to install
No plans on adding it to PyPI, so GitHub will be the source.
```sh
pip install git+https://github.com/ZSendokame/Penv.git  # That's all!
```

# Basic use
```python
""" Example .env:
protocol="http"
port=5000
domain="localhost"
url="{protocol}://{domain}:{port}"
"""

import penv

env = penv.Enviroment('.env')

print(env.get('url'))  # -> "http://localhost:5000"
```

It's worth noting that ``port`` has no quotes and it's a number, therefore, it will be an INT. Penv needs an strict syntax, but it will not be harder than before. Also, no use for ``os`` here, and it will still merge both your systems' enviroment variables and the files' variables (**File variables *will* override your systems' variables**).