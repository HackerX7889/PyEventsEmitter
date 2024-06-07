# Off Method Usage

```py
from PyEventsEmitter import EventEmitter

emitter = EventEmitter()

emitter.on("my_event", lambda x: print(x))
emitter.off("my_event", lambda x: print(x))
```