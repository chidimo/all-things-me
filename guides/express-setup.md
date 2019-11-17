# `Express` setup

## `Babel`

```cmd
yarn add @babel/cli @babel/core @babel/plugin-transform-runtime @babel/preset-env @babel/register @babel/runtime @babel/node --dev
```

## Component functions

1. `@babel/cli` - Allows the use of `Babel` from the terminal. Available as `./node_modules/.bin/babel`. Used in build script.
1. `@babel/core` - core `Babel` functionality. Required installation.
1. `@babel/node` - *works exactly the same as the Node.js CLI, with the added benefit of compiling with Babel presets and plugins before running it*. Required for use with `nodemon` as `"nodemon --exec babel-node ./src/bin/www"`. This forces `nodemon` to run `babel-node ./src/bin/www.js` instead of running the start script.
1. `@babel/plugin-transform-runtime` - helps avoid duplication in compiled output
1. `@babel/preset-env` - collection of plugins. plugins are responsible for carrying out code transformations
1. `@babel/register` - compile files on the fly. Specified as a requirement during tests.
1. `@babel/runtime` - used in conjunction with `@babel/plugin-transform-runtime`

## `eslint`

```cmd
yarn add eslint --dev
```

```cmd
./node_modules/.bin/eslint --init`
```

Follow the on-screen instructions. On windows, do this in `powershell`.

Add a linting to start scripts `"lint": "./node_modules/.bin/eslint ./src"`

## `CORS`, `dotenv`, `express-validator`

```cmd
yarn add cors dotenv express-validator
```

Create a `.env` file and add it to `.gitignore`

```javascript
// app.js

import cors from 'cors';
import dotenv from 'dotenv';
import validator from 'express-validator';

app.use(validator());
app.use(cors('*'));
dotenv.config();
```

## Test and CI/CD

```cmd
yarn add mocha chai sinon nyc sinon-chai supertest coveralls --dev
```

1. `mocha` - test runner
1. `chai` - for assertions
1. `sinon` - for spying, stubbing, and mocking
1. `nyc` - for coverage reporting
1. `sinon-chai` - extends `chai`'s assertions
1. `supertest` - a helper library used to make http calls to out API during tests
1. `coveralls` - for uploading test coverage to <https://coveralls.io>

```json
// package.json
{
    "scripts": {
        "test": "nyc --reporter=html --reporter=text --reporter=lcov mocha -r @babel/register src/**/*.test.js",
        "coverage": "nyc report --reporter=text-lcov | coveralls"
    }
}
```

Requiring `babel-register` instructs `node` to transform files before running tests.

### Minimal `travis-ci` setup

```yaml
# .travis.yml

language: node_js
matrix:
  include:
  - node_js: '10'
  - node_js: '12'
cache:
  directories: node_modules
after_success: yarn coverage
script:
  - yarn test
```

### Minimal `AppVeyor` setup

```yaml
# appveyor.yml

environment:
    matrix:
    - nodejs_version: "10"
install:
    - ps: Install-Product node $env:nodejs_version
    - npm install
test_script:
    - node --version
    - npm --version
    - yarn test
build: off
```

### Minimal `coveralls` setup

```yaml
# .coveralls.yml

repo_token: get-this-from-repo-settings-on-coveralls.io
service_name: travis-ci
```

### Minimal `codeclimate` setup

```yaml
# .codeclimate.yml

version: "2" # required to adjust maintainability checks

plugins:
  duplication:
    enabled: true
  eslint:
    enabled: true
    channel: eslint-5
exclude_patterns:
  - node_modules/
  - build/
```
## Setup mock API

```cmd
yarn add @babel/core @babel/cli @babel/node @babel/preset-env json-server json-schema-faker faker chance --dev
```

1. Put mock data files inside a `mockapi/` folder.

    1. Declare `json` schema for random data using `json-schema-faker`
    1. Serve generated data with `json server`

1. `faker` and `chance` are used to extend `json-schema-faker`
