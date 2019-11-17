# React dev environment setup

## Setup react test and CI/CD with jest and react testing library

### Resource

1. <https://testing-library.com/docs/react-testing-library/setup>

1. `yarn add jest jest-dom coveralls @babel/core @babel/cli @babel/preset-env @babel/preset-react @testing-library/react -D`

1. Create `.babelrc` with the following content

        {
            "presets": ["@babel/preset-env", "@babel/preset-react"]
        }

1. Setup CI/CD with `.coveralls.yml` and `.travis.yml`. [Instructions](express-setup.md#test-and-cicd)
