# listner_count Method

```py
from PyEventEmitter import EventEmitter

emitter = EventEmitter()

emitter.on("my_event", lambda x: print(x))
print(emitter.listener_count("my_event"))
```