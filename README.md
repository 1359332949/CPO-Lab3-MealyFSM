# GROUP-123456 - lab 3 - variant 3

We design an embedded domain-specific language(eDSL) or a simple text parser for Mealy finite state machine(MealyFSM).
And provide a complex example with a physical system controller crossroad with
a traffic light.

## Project structure

- `Interpreter.py` -- implementation of `Interpreter` class.
   Stateless.
- `Interpreter.py` -- unit tests for `Interpreter`.

## Features

- unittest: `test_aspect_oriented_valid` and 'test_interpreter'

## Contribution

- 212320030 Guo Haodong -- writes the main code of this lab.
- 212320028 Yang Junyan -- writes the test.

## Changelog

- 14.06.2022 - 0
  - first commit.

## Design notes

- Input data control
- Design mealy finite state machine
- StateMachine Visualization

### Input data control
```
    def typecheck(*type_args: Any, **type_kwargs: Any) -> Any:
        """
        This function is a decorator used to check the input parameter type
        :param type_args:One or more unnamed parameters passed in.
        :param type_kwargs:One or more parameters with parameter names passed in.
        :return:An example of a decorator used to check the input type.
        """
        def decorator(func):
            sig = signature(func)
            bound_types = sig.bind_partial(*type_args, **type_kwargs).arguments

            @wraps(func)
            def wrapper(*args, **kwargs):
                bound_values = sig.bind(*args, **kwargs)
                for name, value in bound_values.arguments.items():
                    if name in bound_types:
                        if not isinstance(value, bound_types[name]):
                            logger.error('\nArgument {} must be {}'.format(
                                name, bound_types[name]))
                            raise TypeError(
                                '\nArgument {} must be {}'.format(
                                    name, bound_types[name]))
                return func(*args, **kwargs)
            return wrapper
        return decorator
```
### Design mealy finite state machine
- We design a state transition table for the interpreter, and details please check `Interpreter.py`.
### StateMachine Visualization
- generates `log.txt`, `test_picture.gv` and `test_picture.gv.pdf` that descript a whole process for Traffic light for this MealyFSM.
```
    def create_graph(self) -> None:
        """
        This function creates a visual state transition diagram.
        You need to explicitly call create_action_table before use
        :return: None
        """
        logger.info("Create a viz graph.")
        g = Digraph('test_picture')
        for i in self.state_list:
            g.node(self.state_list[i], self.state_list[i])
        for t in self.trans_list:
            g.edge(str(t[0]), str(t[2]), label=str(t[1]) + "/" + str(t[3]) + " latency:" + str(t[4]))
        g.view()
```
