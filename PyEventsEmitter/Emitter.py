from typing import Any, Callable, List, Optional, Dict
from .utils import DEFAULT_LISTNER_COUNT, AbortSignal, Disposable

class EventEmitter:
    def __init__(self, options: Optional[Dict[str, Any]] | None) -> None:
        """
        Initializes a new instance of the EventEmitter class.

        Args:
            options `(Optional[Dict[str, Any]]):` An optional dictionary containing configuration options for the EventEmitter.
                The possible keys and their corresponding values are:
                - 'captureRejections' (bool): If True, the EventEmitter will capture and emit rejections. Defaults to False.

        Initializes the `events` dictionary to store event listeners, and the `captureRejections` flag to indicate whether
        rejections should be captured and emitted. If `options` is provided, the `captureRejections` flag is set to the
        value of the 'captureRejections' key in the `options` dictionary. If the 'captureRejections' key is not present
        in the `options` dictionary, or if `options` is None, the `captureRejections` flag is set to False.
        """
        self.events: dict[str, List[Callable[..., None]]] = {}
        self.captureRejections: bool = options.get('captureRejections', False) if options else False

    def on(self, event_name: str, listener: Callable[..., None]) -> None:
        """
        Adds a listener to the specified event.

        Args:
            event_name (str): The name of the event to listen to.
            listener `(Callable[..., None]):` The function to be called when the event is emitted.

        Returns:
            None: This function does not return anything.

        This function adds a listener to the specified event. If the event does not exist in the `events` dictionary,
        it is created as an empty list. The listener function is then appended to the list of listeners for that event.
        """
        if event_name not in self.events:
            self.events[event_name] = []
        self.events[event_name].append(listener)

    def off(self, event_name: str, listener: Callable[..., None]) -> None:
        """
        Removes a listener from the specified event.

        Args:
            event_name (str): The name of the event.
            listener `(Callable[..., None]):` The function to be removed as a listener.

        Returns:
            None: This function does not return anything.

        This function removes a listener from the specified event. If the event exists in the `events` dictionary and the listener is present in the list of listeners for that event, it is removed from the list.
        """
        if event_name in self.events:
            self.events[event_name].remove(listener)

    def emit(self, event_name: str, *args: Any):
        """
        Emits an event with the given name and arguments.

        Args:
            event_name (str): The name of the event to emit.
            *args (Any): The arguments to pass to the event listeners.

        Returns:
            self: The current instance of the class.

        This function emits an event with the given name and arguments. It checks if the event name exists in the `events` dictionary. If it does, it iterates over the list of listeners for that event and calls each listener with the provided arguments.

        Example:
        ```py
            emitter = EventEmitter()
            
            emitter.emit('my_event', 'Hello, world!')
            
            emitter.on('my_event', lambda x: print(x)) # Output: Hello, world!
        ```
        """
        if event_name in self.events:
            for listener in self.events[event_name]:
                listener(*args)
        return self

    def once(self, event_name: str, listener: Callable[..., None]):
        """
        Adds a listener to the specified event that will be executed only once.

        Args:
            event_name (str): The name of the event to listen to.
            listener (Callable[..., None]): The function to be called when the event is emitted.

        Returns:
            self: The current instance of the class.

        This function adds a listener to the specified event that will be executed only once. If the event does not exist in the `events` dictionary,
        it is created as an empty list. The listener function is then appended to the list of listeners for that event. The listener will be removed after it is called.

        Example:
        ```py
            emitter = EventEmitter()
            
            def my_listener(arg: str):
                print(arg)
            
            emitter.once('my_event', my_listener)
            
            emitter.emit('my_event', 'Hello, world!') # Output: Hello, world!
            emitter.emit('my_event', 'Goodbye, world!') # No output
        ```
        """
        def wrapper(*args: Any):
            """
            A wrapper function that removes a listener from the event and calls the listener with the provided arguments.

            Args:
                *args (Any): The arguments to pass to the listener function.

            Returns:
                None
            """
            self.remove_listener(event_name, wrapper)
            listener(*args)
        self.on(event_name, wrapper)
        return self

    def listeners(self, event_name: str) -> List[Callable[..., None]]:
        """
        Returns a list of listeners for the specified event name.

        Args:
            event_name (str): The name of the event.

        Returns:
            `List[Callable[..., None]]:` A list of listener functions for the event. If the event does not exist, an empty list is returned.
        """
        return self.events.get(event_name, [])

    def listener_count(self, event_name: str) -> int:
        """
        Returns the number of listeners for the specified event name.

        Args:
            event_name (str): The name of the event.

        Returns:
            int: The number of listeners for the event.
        """
        return len(self.listeners(event_name))

    def remove_listener(self, event_name: str, listener: Callable[..., None]):
        """
        Removes a listener from the specified event.

        Args:
            event_name (str): The name of the event.
            listener (Callable[..., None]): The function to be removed as a listener.

        Returns:
            self: The current instance of the class.

        This function removes a listener from the specified event. It calls the `off` method with the `event_name` and `listener` arguments to remove the listener from the event.
        """
        self.off(event_name, listener)
        return self

    def remove_all_listeners(self, event_name: Optional[str] = None):
        """
        Removes all listeners for the specified event or all events if no event name is provided.

        Args:
            event_name (Optional[str]): The name of the event. If not provided, all events will be removed.

        Returns:
            self: The current instance of the class.

        This function removes all listeners for the specified event if `event_name` is provided. If `event_name` is not provided, all events and their listeners will be removed.
        """
        if event_name:
            del self.events[event_name]
        else:
            self.events.clear()
        return self

    def set_max_listeners(self, n: int):
        """
        Set the maximum number of listeners for the event emitter.

        Args:
            n (int): The maximum number of listeners.

        Returns:
            self: The current instance of the class.

        This function sets the maximum number of listeners for the event emitter. It takes an integer `n` as an argument, which represents the maximum number of listeners. The function assigns the value of `n` to the `_max_listeners` attribute of the event emitter object. It then returns the current maximum number of listeners.

        Example:
        ```py
            emitter = EventEmitter()
            emitter.set_max_listeners(10)  # Set the maximum number of listeners to 10
            current_max_listeners = emitter.set_max_listeners(20)  # Set the maximum number of listeners to 20 and get the current maximum number of listeners
        ```
        """
        self._max_listeners = n
        return self

    def get_max_listeners(self) -> int:
        """
        Returns the maximum number of listeners for the event emitter.

        Returns:
            int: The maximum number of listeners. If the event emitter has a `_max_listeners` attribute, it returns that value. Otherwise, it returns the default listener count which is `10`.
        """
        return self._max_listeners if hasattr(self, '_max_listeners') else self.defaultMaxListeners()

    def prependListener(self, event_name: str, listener: Callable[..., None]):
        """
        Adds a listener to the beginning of the listeners array for the specified event.

        Parameters:
            event_name (str): The name of the event to listen for.
            listener (Callable[..., None]): The function to be called when the event is emitted.

        Returns:
            self: The current instance of the class.

        This function adds a listener to the beginning of the listeners array for the specified event. If the event does not exist in the `events` dictionary, it is created. The listener is then inserted at the beginning of the listeners array for the specified event.

        Example:
        ```py
            emitter = EventEmitter()
            
            def listener():
                print("Listener called")
                
            emitter.prependListener("event", listener())
            
            emitter.emit("event")  # Output: "Listener called"
        ```
        """
        if event_name not in self.events:
            self.events[event_name] = []
        self.events[event_name].insert(0, listener)
        return self

    def prependOnceListener(self, event_name: str, listener: Callable[..., None]):
        """
        Adds a one-time listener function to the beginning of the listeners array for the specified event.

        Parameters:
            event_name (str): The name of the event.
            listener (Callable[..., None]): The function to be called when the event is emitted.

        Returns:
            self: The current instance of the class.

        This function adds a one-time listener function to the beginning of the listeners array for the specified event. 
        The listener will be automatically removed after it is called. If the event does not exist in the `events` dictionary, 
        it is created. The listener is then inserted at the beginning of the listeners array for the specified event.

        Example:
        ```py
            emitter = EventEmitter()
            
            def listener():
                print("Listener called")
                
            emitter.prependOnceListener("event", listener())
            
            emitter.emit("event")  # Output: "Listener called"
        ```
        """
        def wrapper(*args: Any):
            """
            A wrapper function that removes a listener from the event and calls the listener with the provided arguments.

            Args:
                *args (Any): The arguments to pass to the listener function.

            Returns:
                None
            """
            self.off(event_name, wrapper)
            listener(*args)
        self.prependListener(event_name, wrapper)
        return self

    def event_names(self) -> List[str]:
        """
        Returns a list of event names.

        This function returns a list of event names by retrieving the keys from the `events` dictionary.

        Returns:
            List[str]: A list of event names.
        """
        return list(self.events.keys())

    def addAbortListener(self, signal: AbortSignal, resource: Callable[[str], None]) -> Disposable:
        """
        Adds an abort listener to the event emitter.

        This method creates a new instance of the AbortListener class and adds it as a listener to the event emitter. The AbortListener class is responsible for checking if the provided AbortSignal is aborted and calling the resource function if it is.

        Args:
            signal (AbortSignal): The AbortSignal object to listen for abort events.
            resource (Callable[[str], None]): The function to be called when the AbortSignal is aborted. This function takes a string parameter representing the event.

        Returns:
            Disposable: The AbortListener instance that was added to the event emitter.
        """
        class AbortListener(Disposable):
            def __init__(self, signal: AbortSignal, resource: Callable[[str], None]) -> None:
                """
                Initializes a new instance of the AbortListener class.

                Args:
                    signal (AbortSignal): The abort signal object.
                    resource (Callable[[str], None]): The resource function to be called if the signal is aborted.

                Returns:
                    None
                """
                self.signal: AbortSignal = signal
                self.resource: Callable[[str], None] = resource

            def __call__(self, event: str):
                """
                Call the resource function if the signal is aborted.

                This method checks if the signal is aborted and if so, it calls the resource function with the provided event.

                Parameters:
                    event (str): The event to pass to the resource function.

                Returns:
                    None
                """
                if self.signal.aborted:
                    self.resource(event)

        return AbortListener(signal, resource)

    def captureRejection(self):
        """
        Gets the current setting for capturing rejection events.

        This function retrieves the flag indicating whether the EventEmitter instance is configured to capture rejection events.

        Returns:
            bool: True if rejection events are captured; False otherwise.
        """
        return self.captureRejection

    def defaultMaxListeners(self):
        """
        Returns the default maximum number of listeners allowed per event.

        This function provides the default maximum number of listeners that can be registered for a single event type before warnings are issued.

        Returns:
            int: The default maximum number of listeners.
        """
        return DEFAULT_LISTNER_COUNT