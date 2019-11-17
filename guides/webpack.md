# Webpack

## Resources

1. <https://webpack.js.org/guides/getting-started/>
1. <https://medium.com/code-oil/burning-questions-with-answers-to-why-webpack-dev-server-live-reload-does-not-work-6d6390277920>
1. `npx webpack` uses `./src/index.js` as the default entry point and outputs a `./dist/main.js` file.
1. To use `webpack-dev-servr`, install and configure it in `webpack.config.js`

`yarn add webpack webpack-cli webpack-dev-server`

```javascript
// webpack.config.js

const path = require('path');

module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist')
    },
    watch: true,
    watchOptions: {
        ignored: /node_modules/
    },

    devServer: {
        // location of static html files.
        // The main html file referencing the bundled file should be placed here
        // to enable live reloading
        contentBase: './UI',
        // where the in-memory bundled js file should be served.
        // Reference /dist/bundle.js in html file <script> tag
        // A useful strategy is to set output.path and publicPath to the same
        // directory so that the bundle reference in the html file will be the same
        publicPath: '/dist/',
        watchContentBase: true,
        compress: true,
    }
}
```

## Multiple entry points and bundles

the bundles are referenced in the html as `dist/index.bundle.js` and `dist/users.bundle.js`

```javascript
const path = require('path');

module.exports = {
    entry: {
        index: './src/index.js',
        users: './src/users.js'
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'dist')
    },
}
```

## Loaders

A loader applies a transformation to files before bundling. For ES6 syntax support use `babel-loader`. See setup section of <https://babeljs.io>

1. Install `babel` dependencies: `yarn add babel-loader @babel/core @babel/preset-env -D`
1. Configure module key in webpack config
1. Add `.babelrc` with ES6 preset
