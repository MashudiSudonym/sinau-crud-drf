from .production import *

try:
    from .production import *
except:
    from .local import *
