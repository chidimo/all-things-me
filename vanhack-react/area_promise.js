// Complete the calculateArea function below.
// It returns a Promise which on success, returns area of the shape, and on failure returns [-1].

let calculateArea = (shape, values) => {
    const valid_shapes = ['square', 'rectangle', 'circle', 'triangle']
    if (!valid_shapes.includes(shape)) {
        return Promise.reject([-1])
    }
    const round2dp = value => Math.round(value * 100) / 100
    const areas = {
        square: side => round2dp(side * side),
        rectangle: (length, breadth) => round2dp(length * breadth),
        circle: radius => round2dp(3.14 * radius * radius),
        triangle: (base, height) => round2dp(0.5 * base * height)
    }

    const f = areas[shape]
    const [side1, side2] = values
    if (side2) return Promise.resolve(f(side1, side2))
    else return Promise.resolve(f(side1))
}

// Complete the generateArea function below.
// It returns a Promise which on success, returns an array of areas of all the shapes and on failure, returns [-1].

let getAreas = async (shapes, values_arr) => {
    const areas = []
    const l = shapes.length
    for (let i = 0; i < l; i += 1) {
        const area = await calculateArea(shapes[i], values_arr[i])
        if (area === -1) { console.log(area); return Promise.reject(area) }
        else areas.push(area)
    }
    return Promise.reject(areas)
}

console.log('square', calculateArea('square', [5]))
console.log('circle', calculateArea('circle', [4]))
console.log('circle', calculateArea('red', [4]).then(k => k).catch(err => err))
console.log('rectangle', calculateArea('rectangle', [4, 5]))
console.log('triangle', calculateArea('triangle', [4, 5]))
console.log("**********************")


console.log(getAreas(['square', 'circle', 'triangle'],
    [[5], [3], [3, 8]])
    .then(res => res)
    .catch(err => err)
)

console.log(getAreas(['black', 'square', 'circle'],
    [[1], [2], [3]])
    .then(res => res)
    .catch(err => err)
)
