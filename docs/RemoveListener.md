# remove_listner Method

```py
from PyEventsEmitter import EventEmitter

emitter = EventEmitter()

emitter.on("my_event", lambda x: print(x))
emitter.remove_listener("my_event", lambda x: print(x))
```