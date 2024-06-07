# Event Emitter

### Overview
------------

The Event Emitter (PyEventsEmitter) is a powerful tool for managing event listeners and emitting events in your application. It provides a range of methods for adding, removing, and checking listeners, as well as emitting events with arguments.

## Installation

```sh
pip install PyEventsEmitter
```

### Initialization
-----------------

### `__init__(options: Optional[Dict[str, Any]] | None) -> None`
Initializes a new instance of the Event Emitter class. The `options` parameter is an optional dictionary containing configuration options for the Event Emitter. If provided, the `captureRejections` flag is set to the value of the 'captureRejections' key in the `options` dictionary. If the 'captureRejections' key is not present in the `options` dictionary, or if `options` is `None`, the `captureRejections` flag is set to `False`.

### `events` and `captureRejections` Attributes
-----------------------------------------

- `events`: A dictionary storing event listeners.
- `captureRejections`: A flag indicating whether the Event Emitter captures and emits rejections.

### Methods
---------

### `on(event_name: str, listener: Callable[..., None]) -> None`
Adds a listener to the specified event.

### `off(event_name: str, listener: Callable[..., None]) -> None`
Removes a listener from the specified event.

### `emit(event_name: str, *args: Any) -> self`
Emits an event with the given name and arguments.

### `once(event_name: str, listener: Callable[..., None]) -> self`
Adds a listener to the specified event that will be executed only once.

### `listeners(event_name: str) -> List[Callable[..., None]]`
Returns a list of listeners for the specified event name.

### `listener_count(event_name: str) -> int`
Returns the number of listeners for the specified event name.

### `remove_listener(event_name: str, listener: Callable[..., None]) -> self`
Removes a listener from the specified event.

### `remove_all_listeners(event_name: Optional[str] = None) -> self`
Removes all listeners for the specified event or all events if no event name is provided.

### `set_max_listeners(n: int) -> self`
Sets the maximum number of listeners for the event emitter.

### `get_max_listeners() -> int`
Returns the maximum number of listeners for the event emitter.

### `prependListener(event_name: str, listener: Callable[..., None]) -> self`
Adds a listener to the beginning of the listeners array for the specified event.

### `prependOnceListener(event_name: str, listener: Callable[..., None]) -> self`
Adds a one-time listener function to the beginning of the listeners array for the specified event.

### `event_names() -> List[str]`
Returns a list of event names.

### `addAbortListener(signal: AbortSignal, resource: Callable[[str], None]) -> Disposable`
Adds an abort listener to the event emitter.

### `captureRejection() -> bool`
Gets the current setting for capturing rejection events.

### `defaultMaxListeners() -> int`
Returns the default maximum number of listeners allowed per event.