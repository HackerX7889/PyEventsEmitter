# remove_listner Method

```py
from PyEventsEmitter import EventEmitter

emitter = EventEmitter({ "captureRejections": True })

emitter.on("my_event", lambda x: print(x))
emitter.remove_listener("my_event", lambda x: print(x))
```