# Async javascript

## Iterator pattern

1. `producer` - `consumer` pair.
1. `consumer` requests info from `producer` until the `producer`
    1. runs out of data OR
    1. throws an error.
1. There is an explicit way to indicate completion

```javascript
const it = [1, 2, 3].iterator()

console.log(it.next()) // { value: 1, done: false }
console.log(it.next()) // { value: 2, done: false }
console.log(it.next()) // { value: 3, done: false }
console.log(it.next()) // { done: true }
```

## Observer pattern

How events work: `consumer` hands the `producer` a `callback`. When `producer` is ready, it pushes information to the `consumer`, via the callback, one at a time.

```javascript
// the addEventListener method is an observer
const d = document.getElementById('mouse-position')
const next = e => {
    console.log('mouse moves', e)
    const p = document.createElement('p')
    p.innerHTML = `Mouse is at: (${e.screenX}, ${e.screenY})`
    d.appendChild(p)
};

document.addEventListener('mousemove', next)
document.removeEventListener('mousemove', next) // do this to cleanup
```

1. The `iterator` and `observer` patterns are asymmetrical.
1. In the observer pattern, there is no way for the `producer` to tell the `consumer` that

    1. there is no more data
    1. an error has occurred.
    1. For the `consumer` to stop receiving data

1. An `iterable` is something you can ask an `iterator` from.
1. The opposite of an `iterable` is an `observable`.

```javascript
Observable === Collection + Time // collection that arrives over time
```

## The `Observer` object

```javascript
      const mouseMoves = Observable.fromEvent(document, 'mousemove')

      const sub = mouseMoves.forEach({
        onNext: e => console.log(e),
        onError: err => console.log(err),
        onCompleted: () => console.log('done')
      })
      sub.dispose()
```

### Converting `Event`s to `Observable`s

```javascript
Observable.fromEvent = (dom, eventName) => {
  // returning observable object
  return {
    forEach: observer => {
      const handler = e => observer.onNext(e);
      dom.addEventListener(eventName, handler);

      //return Subscription object
      return {
        dispose: () => {
          dom.removeEventListener(eventName, handler)
        }
      }
    }
  }
}
```

1. `Hot Observable` - Emits data whether you're listening or not e.g mousemoves
1. `Cold Observable` - Must be listened to to emit data
1. `dispose` doesn't trigger `onCompleted`

### Mousedrags collection

```javascript
const getElementDrags = elmt => {
  elmt.mouseDowns = Observable.fromEvent(elmt, 'mousedown');
  elmt.mouseUps = Observable.fromEvent(elmt, 'mouseup')
  elmt.mouseMoves = Observable.fromEvent(elmt, 'mousemove')

  return elmt.mouseDowns
    .map(md => document.mouseMoves.takeUntil(document.mouseUps))
    .concatAll();
};

getElementDrags(image)
    .forEach(pos => image.position = pos);
```

### Problem solving steps

1. What collections do I have?
1. What collections do I want?
1. How do I get from what I have to what I want?
1. What am I going to do with the data that comes with what I want?

### `filter` implementation

```javascript
Array.prototype.filter = function (predicateFunction) {
    var results = [];
    this.forEach(function (itemInArray) {
        if (predicateFunction(itemInArray)) {
            results.push(itemInArray)
        }
    });
    return results;
};
```

### `map` implementation

```javascript
Array.prototype.map = function (projectionFunction) {
    var results = [];
    this.forEach(function (itemInArray) {
        results.push(projectionFunction(itemInArray))
    });
    return results;
};

console.log(JSON.stringify([1, 2, 3].map(function (x) { return x + 1; }))) //'[2,3,4]'
```

### `concatAll` implementation

```javascript
Array.prototype.concatAll = function () {
    var results = [];
    this.forEach(function (subArray) {
        subArray.forEach(i => { results.push(i) })
    });
    return results;
};

console.log(JSON.stringify([[1, 2, 3], [4, 5, 6], [7, 8, 9]].concatAll())); // "[1,2,3,4,5,6,7,8,9]"
console.log([1, 2, 3].concatAll()); // throws an error because this is a one-dimensional array
```

### `zip` implementation

```javascript
Array.zip = function (left, right, combinerFunction) {
    var counter,
        results = [];

    for (counter = 0; counter < Math.min(left.length, right.length); counter++) {
        results.push(combinerFunction(left[counter], right[counter]));
    }
    return results;
};
// JSON.stringify(Array.zip([1,2,3],[4,5,6], function(left, right) { return left + right })) === '[5,7,9]'
```

### `reduce` implementation

**Note**: This reduce implementation returns an Array of length 1. JavaScript implementation returns a scalar

```javascript
Array.prototype.reduce = function (combiner, initialValue) {
    var counter, accumulatedValue;

    // If the array is empty, do nothing
    if (this.length === 0) {
        return this;
    }
    else {
        // If the user didn't pass an initial value, use the first item.
        if (arguments.length === 1) {
            counter = 1;
            accumulatedValue = this[0];
        }
        else if (arguments.length >= 2) {
            counter = 0;
            accumulatedValue = initialValue;
        }
        else {
            throw "Invalid arguments.";
        }

        // Loop through the array, feeding the current value and the result of
        // the previous computation back into the combiner function until
        // we've exhausted the entire array and are left with only one value.
        while (counter < this.length) {
            accumulatedValue = combiner(accumulatedValue, this[counter])
            counter++;
        }

        return [accumulatedValue];
    }
};

// [1,2,3].reduce(function(accumulatedValue, currentValue) { return accumulatedValue + currentValue; }); === [6];
// [1,2,3].reduce(function(accumulatedValue, currentValue) { return accumulatedValue + currentValue; }, 10); === [16];

```

### Combining `map` and `concatAll` to flatten a list

This example demonstrates both a *naive* and a *better* solution

```javascript
const movieLists = [
    {
        name: "Instant Queue",
        videos: [
            {
                "id": 70111470,
                "title": "Die Hard",
                "boxarts": [
                    { width: 150, height: 200, url: "http://cdn-0.nflximg.com/images/2891/DieHard150.jpg" },
                    { width: 200, height: 200, url: "http://cdn-0.nflximg.com/images/2891/DieHard200.jpg" }
                ],
                "url": "http://api.netflix.com/catalog/titles/movies/70111470",
                "rating": 4.0,
                "bookmark": []
            },
            {
                "id": 654356453,
                "title": "Bad Boys",
                "boxarts": [
                    { width: 200, height: 200, url: "http://cdn-0.nflximg.com/images/2891/BadBoys200.jpg" },
                    { width: 150, height: 200, url: "http://cdn-0.nflximg.com/images/2891/BadBoys150.jpg" }

                ],
                "url": "http://api.netflix.com/catalog/titles/movies/70111470",
                "rating": 5.0,
                "bookmark": [{ id: 432534, time: 65876586 }]
            }
        ]
    },
    {
        name: "New Releases",
        videos: [
            {
                "id": 65432445,
                "title": "The Chamber",
                "boxarts": [
                    { width: 150, height: 200, url: "http://cdn-0.nflximg.com/images/2891/TheChamber150.jpg" },
                    { width: 200, height: 200, url: "http://cdn-0.nflximg.com/images/2891/TheChamber200.jpg" }
                ],
                "url": "http://api.netflix.com/catalog/titles/movies/70111470",
                "rating": 4.0,
                "bookmark": []
            },
            {
                "id": 675465,
                "title": "Fracture",
                "boxarts": [
                    { width: 200, height: 200, url: "http://cdn-0.nflximg.com/images/2891/Fracture200.jpg" },
                    { width: 150, height: 200, url: "http://cdn-0.nflximg.com/images/2891/Fracture150.jpg" },
                    { width: 300, height: 200, url: "http://cdn-0.nflximg.com/images/2891/Fracture300.jpg" }
                ],
                "url": "http://api.netflix.com/catalog/titles/movies/70111470",
                "rating": 5.0,
                "bookmark": [{ id: 432534, time: 65876586 }]
            }
        ]
    }
];

// naive solution using indexing
const naive = movieLists
    .map(m => {
        return m.videos.map(v => {
            return {
                id: v.id,
                title: v.title,
                boxart: v.boxarts.filter(b => b.width === 150)[0]['url']
            }
        })
    }).concatAll()

// improved solution. Hold off building the object
// until we have everything we need in scope
// a map inside a map is a perfect candidate for concatAll
const better = movieLists
    .map(m => {
        return m.videos.map(v => {
            return v.boxarts
                .filter(b => (b.width === 150))
                .map(a => ({ id: v.id, title: v.title, boxart: a.url }))
        }
        ).concatAll()
    }
    ).concatAll()

console.log(JSON.stringify(naive) === JSON.stringify(better))

  // Use one or more map, concatAll, and filter calls to create an array with the following items
  // [
  // {"id": 675465,"title": "Fracture","boxart":"http://cdn-0.nflximg.com/images/2891/Fracture150.jpg" },
  // {"id": 65432445,"title": "The Chamber","boxart":"http://cdn-0.nflximg.com/images/2891/TheChamber150.jpg" },
  // {"id": 654356453,"title": "Bad Boys","boxart":"http://cdn-0.nflximg.com/images/2891/BadBoys150.jpg" },
  // {"id": 70111470,"title": "Die Hard","boxart":"http://cdn-0.nflximg.com/images/2891/DieHard150.jpg" }
  // ];

```
