## Usage with Custom Data Types 

```py
from enum import Enum
from typing import NamedTuple

# Define an Enum class for grades
class Grades(Enum):
    A = "best"
    B = "avg"
    C = "bad"

# Define a NamedTuple class for data
class Data(NamedTuple):
    name: str
    age: int
    male: bool
    grade: Grades

# Import the PyEventsEmitter class
from PyEventsEmitter import EventEmitter

# Create an instance of the EventEmitter class
emitter = EventEmitter({'captureRejections': True})

# Define a function to test the event emitter
def test():
    # Create an instance of the Data class
    info = Data(
        age=25,
        name="John",
        male=True,
        grade=Grades.A
    )

    # Define a listener function
    def listner(data: Data):
        print(data.age)
        print(data.name)
        print(data.male)
        print(data.grade)

        # Your own logic

    # Add the listener to the event emitter
    emitter.on("name", lambda data: listner(data))

    # Emit the event with the data
    emitter.emit("name", info)

# Run the test function
test()
```