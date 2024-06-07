# Listners Method

```py
from PyEventEmitter import EventEmitter

emitter = EventEmitter()

emitter.on("my_event", lambda x: print(x))
print(emitter.listeners("my_event"))
```