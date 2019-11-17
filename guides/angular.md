# Angular.io

1. `npm install @angular/cli@7.1.2`
1. `ng new ng-fundamentals`

## Bootstrapping the angular app

### Flow

1. `webpack`: bootstraps the app module through the entry point (`projects -> <app-name> -> architect -> build -> options -> main`) settings of the `angular.json` file
1. The `src/main.ts` bootstraps the app with the `<AppModule>` from `src/app/app.module.ts`. Every angular app has an `<AppModule>`, which is responsible for making `Angular` aware of our `<AppComponent>`.
    1. The `<AppModule>` is itself bootstrapped with the `<AppComponent>` from `src/app/app.component.ts` file
    1. The `<AppComponent>` has a selector property that tells `Angular` the `HTML` tag to use in displaying the component in the `src/index.html` file
1. Angular loads the `src/index.html` file and it in turn loads our `<AppComponent>`
1. **Summary**: `webpack` -> `main.ts` -> `app.module.ts` -> `app.component.ts`

## The `<AppModule>`

1. The `<AppModule>` is bootstrapped with the follow default settings: `declarations`, `imports`, `providers` and `bootstrap`. All are arrays.
    1. `declarations`: every component must be declared here
    1. `imports`: used for importing other modules
    1. `providers`: every service must be added here

## Adding assets

The assets folder is specified in the `projects -> <app-name> -> architect -> build -> options -> assets` array of the `angular.json` settings.
There's also settings for app-wide `styles` and `scripts`
