# abortListener Method

```py
from PyEventsEmitter import EventEmitter, AbortSignal

emitter = EventEmitter()

emitter.addAbortListener(AbortSignal(), lambda x: print(x))
```