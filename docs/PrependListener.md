# prependListener Method

```py
from PyEventsEmitter import EventEmitter

emitter = EventEmitter()

emitter.prependListener("my_event", lambda x: print(x))
emitter.emit("my_event", "Hello, world!")
```