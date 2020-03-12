# Redux notes

## The store

```
1. store = state tree + interactions

1. ways of interacting with state tree

	Getting the state

	Listening for state changes

	Updating the state
```

## Store rules

1. Only an event can change the state of the store
1. The function that returns the new, updated, state must be a `pure function`

### Pure function

1. Returns same result for the same set of arguments every single time
1. It's return value is STRICTLY dependent on its arguments. No outside values is accessed
1. Does NOT produce any side effects. No interaction with the outside world e.g. making network requests, mutating its internal state. What about logging to the console?

## Terminology

1. `store` An object that keeps track of our state
1. `Action` A state manipulation function that is called by a component
1. `Reducer` A function that applies an action to the state and returns a new updated _copy_ of the state. `reducer(previous-state, action) --> new-state`. Reducers are passed to the store during store initialization.
1. `subscribe` A store function that provides a way to listen on state changes within the store.
1. `dispatch` A store function that provides a way to pass an action to the store.
