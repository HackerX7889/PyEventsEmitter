# Once Method Usage

```py
from PyEventsEmitter import EventEmitter

emitter = EventEmitter({ 'captureRejections': True })

emitter.emit("foo", 15)

emitter.once("foo", lambda x: print(x)) # Output: 15
```