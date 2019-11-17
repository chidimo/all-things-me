# ES6 notes

## Resources

1. ES6 In Depth <https://ponyfoo.com/articles/tagged/es6-in-depth>
1. ES6 Promises <https://ponyfoo.com/articles/es6-promises-in-depth>
1. EX6 Generators <https://ponyfoo.com/articles/es6-generators-in-depth>

## Promises

1. A promise can only follow one branch. The `resolve` or the `rejection` branch.
1. `.then` and `.catch` return **a new promise every time**
1. You can save a reference to any point in the promise chain. You may then tack more promises on top of it.
1. Promises work like a tree where you add branches where and when you need them.
1. `Promise.race()` returns the first `Promise` to resolve.

```javascript
fetch('foo')
  .then(res => res.a.prop.that.does.not.exist)
  .catch(err => console.error(err.message))
// <- 'Cannot read property "prop" of undefined'
```

In the above scenario, the `.catch()` acts on the `Promise` returned by the `.then()` call.

```javascript
const p = fetch('foo').then(res => res.a.prop.that.does.not.exist)
p.catch(err => console.error(err.message))
p.catch(err => console.error(err.message))
```

In the above scenario, the two `.catch()`s acts on a single `Promise` object, `p`.

