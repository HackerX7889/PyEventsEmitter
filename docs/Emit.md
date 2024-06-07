# Emit Method Usage

```py
from PyEventEmitter import EventEmitter

emitter = EventEmitter()

emitter.on("my_event", lambda x: print(x))
emitter.emit("my_event", "Hello, world!")
```