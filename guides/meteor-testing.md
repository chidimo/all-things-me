# Meteor testing

## Resources

1.  <https://github.com/meteortesting/meteor-mocha/blob/master/README.md#run-app-tests>

        setx TEST_WATCH 1
        meteor test --driver-package meteortesting:mocha
        meteor test --full-app --driver-package meteortesting:mocha
        meteor test --once --full-app --driver-package meteortesting:mocha

        meteor add meteortesting:mocha johanbrook:publication-collector xolvio:cleaner dburles:factory
        meteor npm install --save-dev faker jsdom chai sinon enzyme enzyme-adapter-react-16
        meteor npm install @babel/core babel-loader @babel/preset-env @babel/preset-react @babel/register --save-dev

create a top-level `.babelrc` file and populate it with

```json
{
    "presets": ["@babel/preset-react", "@babel/preset-env"]
}
```

create a `tests/setup.js` file and populate it with

```javascript
/* setup.js */

const { JSDOM } = require("jsdom");

const jsdom = new JSDOM("<!doctype html><html><body></body></html>");
const { window } = jsdom;

function copyProps(src, target) {
    Object.defineProperties(target, {
        ...Object.getOwnPropertyDescriptors(src),
        ...Object.getOwnPropertyDescriptors(target)
    });
}

global.window = window;
global.document = window.document;
global.navigator = {
    userAgent: "node.js"
};
global.requestAnimationFrame = function(callback) {
    return setTimeout(callback, 0);
};
global.cancelAnimationFrame = function(id) {
    clearTimeout(id);
};
copyProps(window, global);

console.log("Setup ready");
```
