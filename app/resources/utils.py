from functools import partial


def base_url(name):
    return partial("{base}{}".format, base=name)
