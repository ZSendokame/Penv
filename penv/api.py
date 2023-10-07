import os
from ast import literal_eval
from typing import Any


class Enviroment:
    def __init__(self, env: os.PathLike = '.env') -> None:
        self.env = {**os.environ, **self.__parse__(env)}

    def get(self, key: str, default: Any = None) -> Any:
        return self.env.get(key, default)

    def __parse__(self, file: str) -> dict:
        file = open(file, 'r')
        enviroment = {}

        for line in file.read().split('\n'):
            key, value = line.split('=', 1)
            value = literal_eval(value)

            if isinstance(value, str):
                value = value.format(**enviroment)

            enviroment[key] = value

        file.close()

        return enviroment
