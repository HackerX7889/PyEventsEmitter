# abortListener Method

```py
from PyEventEmitter import EventEmitter, AbortSignal

emitter = EventEmitter()

emitter.addAbortListener(AbortSignal(), lambda x: print(x))
```