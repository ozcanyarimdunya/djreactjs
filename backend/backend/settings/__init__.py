from .base import *
from .common import *

DEVELOPMENT = True

if DEVELOPMENT:
    from .dev import *
else:
    from .prod import *
