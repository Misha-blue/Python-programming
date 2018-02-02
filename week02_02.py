import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        json_dict = json.dumps(func(*args, **kwargs))
        return json_dict

    return wrapped


@to_json
def get_data(param):
    return {
        'data': param
    }


@to_json
def get_data_second(first_param, second_param):
    return {
        'data': {first_param: second_param}
    }