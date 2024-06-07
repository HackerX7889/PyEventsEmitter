# Listners Method

```py
from PyEventsEmitter import EventEmitter

emitter = EventEmitter({ "captureRejections": True })

emitter.on("my_event", lambda x: print(x))
print(emitter.listeners("my_event"))
```