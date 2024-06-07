# remove_all_listners Method

```py
from PyEventEmitter import EventEmitter

emitter = EventEmitter()

emitter.on("my_event", lambda x: print(x))
emitter.remove_all_listeners("my_event")
```