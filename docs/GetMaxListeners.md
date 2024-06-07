# get_max_listeners Method

```py
from PyEventEmitter import EventEmitter

emitter = EventEmitter()

emitter.set_max_listeners(93)
print(emitter.get_max_listeners())
```

## or

```py
import random

def random_int():
    return random.randint(20, 50)

from PyEventEmitter import EventEmitter

emitter = EventEmitter()

emitter.set_max_listeners(random_int())
print(emitter.get_max_listeners())
```