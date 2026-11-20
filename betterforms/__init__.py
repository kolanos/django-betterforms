from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version('django-betterforms')
except PackageNotFoundError:
    __version__ = None
