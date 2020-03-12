# React notes

1. What is `React`? It is a **D**eclarative, **E**fficient, and **F**lexible `JavaScript` library for building user interfaces.
1. `React Component Class` (RCC) or `React Component Type` (RCT).
1. Component parameters are called props
1. `render` method should return a `React element`. A `React element` is a `JavaScript` object.
1. It is possible to use `JSX` or `React.createElement`
1. `JavaScript` expressions can be put inside braces (`{}`) in `JSX`.
1. Components can have `state` by setting `this.state`.
1. `this.state` should be considered **private** to the Component it's defined in.
1. **All** RCCs that have a `constructor` should start it with `super(props)`
1. When you call `setState` in a component, `React` automatically updates the child components inside of it too.
1. **Lifting state**. The technique of maintaining the state of a _child_ component inside its _parent_.
1. **To collect data from multiple children, or to have two child components communicate with each other, you need to declare the shared state in their parent component instead. The parent component can pass the state back down to the children by using props; this keeps the child components in sync with each other and with the parent component.**

1. To render multiple items in React, we can use an array of React elements.
1. **It’s strongly recommended that you assign proper keys whenever you build dynamic lists.** If you don’t have an appropriate key, you may want to consider restructuring your data so that you do.

## Passing data between `React` components (from child to parent and vice versa)

1. <https://medium.com/@ruthmpardee/passing-data-between-react-components-103ad82ebd17>
1. [React JS Tutorial 10: Passing data from child to parent components](https://www.youtube.com/watch?v=AnRDdEz1FJc)

`App.js`

```javascript
class App extends Component {
  constructor(props) {
    super(props);
    this.state = { someStateVariable: "" };
    this.callbackFromParentToChild = this.callbackFromParentToChild.bind(this); // IMPORTANT
  }

  // get some value from the child component
  // this callback belongs to the child's context so we have to bind it to
  // this parent's context using this line in the constructor
  // this.callbackFromParentToChild = this.callbackFromParentToChild.bind(this)

  callbackFromParentToChild(value_from_child_to_parent) {
    this.setState({ someStateVariable: value_from_child_to_parent });
  }

  renderChildComponent() {
    return country_denominations.map(denomination => (
      <ChildComponent
        callback_from_parent_to_child={this.callbackFromParentToChild}
      />
    ));
  }
}
```

`ChildComponent.jsx`

```javascript
export default class ChildComponent extends Component {
  computeValueToBePassedToParent() {
    value_from_child_to_parent = ""; // perform some computation
    this.props.callback_from_parent_to_child(value_from_child_to_parent); // pass the total back to the parent's callback
  }
}
```

## Exercise: Translating `React` code to `python`

```javascript
// Task.jsx. How each item of the task is rendered
import React, { Component } from "react";

export default class Task extends Component {
  render() {
    return (
      <li>
        {this.props.item_id} - {this.props.task.text}
      </li>
    );
  }
}

// App.js
import React, { Component } from "react";
import Task from "./Task.jsx";

export default class App extends Component {
  getTasks() {
    return [
      { _id: 1, text: "Task 1" },
      { _id: 2, text: "Task 2" },
      { _id: 3, text: "Task 3" }
    ];
  }

  renderTasks() {
    // In this mapping, each item of getTasks() is referred to by the name instance_identifier
    return this.getTasks().map(instance_identifier => (
      // Initialize the Task class with two items: key and task.
      // Try to access key with {this.props.key} results in an error saying that key is not a prop. Perhaps it's used internally
      <Task
        key={instance_identifier._id}
        item_id={instance_identifier._id}
        task={instance_identifier}
      />
    ));
  }

  render() {
    return (
      <div className="container">
        <header>
          <h1>Meteor todo</h1>
        </header>

        <ul>{this.renderTasks()}</ul>
      </div>
    );
  }
}
```

Translated to python, it becomes

```python
# Task.py
from react import React, Component

class Task(Component):
    def __init__(self, task_instance):
        """This corresponds roughly to where the props is initialized in React

        task_instance is the javascript task object
        """
        self.task_dict = task_instance.task_dict
        self.item_id = task_instance.item_id

    def render(self):
        return f'<li>{self.task_dict.text} - {self.item_id}</li>'

# App.py
from react import React, Component
from .Task import Task

class App(Component):

    def getTasks(self):
        return [{_id: 1, text:'Task 1'}, {_id: 2, text:'Task 2'}, {_id: 3, text:'Task 3'}]

    def renderTasks(self):
        """
        Each item of getTasks() is mapped to Task().
        The list item instances are named with lambda functions in python
        """
        return map(lambda task_instance: Task(task_instance), self.getTasks())

    def render(self):
        return f'
            <div className="container">
                <header>
                    <h1>Meteor todo</h1>
                </header>

                <ul>
                {self.renderTasks()}
                </ul>
            </div>
        '
```
