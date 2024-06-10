# remove_all_listners Method

```py
from PyEventsEmitter import EventEmitter

emitter = EventEmitter({ "captureRejections": True })

emitter.on("my_event", lambda x: print(x))
emitter.remove_all_listeners("my_event")
```