# ALU AirBnB Clone

The AirBnB clone project is a step-by-step rebuild of the AirBnB web
application. This first stage delivers the data model and the command-line
interpreter that will be reused by the storage engine, the API, and the web
front-end in later stages.

## Description of the command interpreter

The console is a small REPL (read-eval-print loop) built on top of Python's
`cmd` module. It allows you to create, retrieve, update, and destroy the
objects that make up the application (users, places, cities, states,
amenities, reviews) and to persist them to a JSON file.

### How to start it

Clone the repository and launch the console from the project root:

```
$ git clone https://github.com/<your-user>/alu-AirBnB_clone.git
$ cd alu-AirBnB_clone
$ ./console.py
(hbnb)
```

In non-interactive mode you can pipe commands to it:

```
$ echo "help" | ./console.py
```

### How to use it

Once the `(hbnb)` prompt appears, type `help` to list the available
commands. The most common ones are:

| Command                    | Effect                                            |
| -------------------------- | ------------------------------------------------- |
| `create <Class>`           | Create a new instance and print its id            |
| `show <Class> <id>`        | Print the string representation of an instance    |
| `destroy <Class> <id>`     | Delete an instance and save the change            |
| `all [<Class>]`            | List every instance, optionally filtered by class |
| `update <Class> <id> ...`  | Update an attribute of an instance                |
| `quit` / `EOF`             | Leave the interpreter                             |

### Examples

```
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {...}
(hbnb) all BaseModel
(hbnb) quit
$
```

## Repository layout

```
models/        Data model classes (BaseModel and its subclasses)
tests/         Unit tests mirroring the models/ package
AUTHORS        Contributors to the repository
```

## Running the tests

```
$ python3 -m unittest discover tests
```

## Authors

See the [AUTHORS](AUTHORS) file.
