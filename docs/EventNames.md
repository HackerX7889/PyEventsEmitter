# event_names Method

```py
from PyEventsEmitter import EventEmitter

emitter = EventEmitter({ "captureRejections": True })

emitter.on("my_event", lambda x: print(x))
print(emitter.event_names())
```