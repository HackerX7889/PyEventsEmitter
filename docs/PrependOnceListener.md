# prependOnceLitner Method

```py
from PyEventsEmitter import EventEmitter

emitter = EventEmitter({ "captureRejections": True })

emitter.prependOnceListener("my_event", lambda x: print(x))
emitter.emit("my_event", "Hello, world!")
```