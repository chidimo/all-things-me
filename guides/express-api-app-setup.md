# Setup `express` API project

1. Start project with `express <project-name>`. We won't be using `express`'s view engine.
1. Create `.editorconfig` file in project root
1. Create `.gitignore` file in project root and add `node_modules/`
1. Delete `public/` and `views/` folder.
1. Delete view engine setup, static path setup, and error handling setup from `app.js`.
1. Delete `http-errors` and `jade` from `package.json`.
1. Delete `routes/users.js` and remove `users` route from `app.js`.
1. Update `/` route in `app.js` to return `json` response.
1. Navigate to the folder on `cmd` and install dependencies with `yarn install`
1. Create a folder `src/` project and move `bin/`, `routes/` and `app.js` inside. Now our structure looks like this

        Project/
            node_modules/
            src/
                bin/
                routes/
                app.js
            .gitignore
            package.json
            yarn.lock

1. Edit the start script in `package.json` to be `"node ./src/bin/www"`
1. Install `nodemon` and create `devstart` script and set it to `"nodemon ./src/bin/www"`
1. Setup `Babel`. [Instructions](express-setup.md#babel)
1. Setup linting with `ESLint`. [Instructions](express-setup.md#eslint)
1. Convert all files to `ES6` syntax.
1. Configure `start`, `dev-start`, and `build` scripts.
1. Now set start script in `package.json` to be `"node ./build/bin/www"`
1. Configure `CORS`, `dotenv`, and `express-validator`. [Instructions](express-setup.md#cors-dotenv-express-validator)
1. Optionally install and configure `localtunnel` (for sharing WIP) and `npm-run-all` (for running parallel tasks)
1. Setup testing and `CI/CD`. [Instructions](express-setup.md#test-and-cicd).
1. Setup mock API [Instructions](express-setup.md#setup-mock-api)
1. Setup swagger documentation
1. Update existing starter kits. Options are `Yeoman`, `Github`
