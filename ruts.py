from typing import Union
import re


def __check_rut_format(rut: Union[str, int]):
    regex = r"^(\d{1,3}(\.?\d{3}){1,2})(-?\d|k|K)?$"
    return re.match(regex, rut)


def __clean_rut(rut: Union[str, int]):
    return re.sub(r"\.|(-[\dkK])", "", rut)
