# abortListener Method

```py
from PyEventsEmitter import EventEmitter, AbortSignal

emitter = EventEmitter({ "captureRejections": True })

emitter.addAbortListener(AbortSignal(), lambda x: print(x))
```