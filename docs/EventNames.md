# event_names Method

```py
from PyEventsEmitter import EventEmitter

emitter = EventEmitter()

emitter.on("my_event", lambda x: print(x))
print(emitter.event_names())
```