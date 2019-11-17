# sass

## BEM (Block Element Modifier) architecture

1. Elements defined inside a block have regular class names
1. Double underscores, `__`, indicate an element is being defined inside a block
1. Dash, `-`, indicates a modifier

```html
<div class="textfield">
    <label for="first-name" class="textfield__label">
    First Name
    <label>
    <input name="first-name" type="email" class="textfield__input" />
    <span class="textfield__validation-error">
    Must be two characters or longer
    <span>
<div>
```

```scss
.textfield {
    &__input { }
    &__label { }
    &__validation-error { }
}
```

1. `@mixin` defines re-usable blocks
1. `@extends` defines style that will not be repeated in the importing components.
1. `%placeholder` exists solely to be extended from. This is unlike extends that can be used on their own.

## Building tiny classes

```scss
$increments: 5 10 15 20 25;
$directions: t b l r;
$dir_maps: (t: top, l: left, r: right, b: bottom,);

@each $n in $increments {
    @each $dir in $directions {
        .m-#{$dir}-#{$n} {
            margin-#{map-get($dir_maps, $dir)}: #{$n}px;
        }

        .p-#{$dir}-#{$n} {
            padding-#{map-get($dir_maps, $dir)}: #{$n}px;
        }
    }
}

// alternative solution

// @each $n in $increments {
//     .m-t-#{$n} {
//         margin-top: #{$n}px;
//     }
//     .m-b-#{$n} {
//         margin-bottom: #{$n}px;
//     }
//     .m-l-#{$n} {
//         margin-left: #{$n}px;
//     }
//     .m-r-#{$n} {
//         margin-right: #{$n}px;
//     }
//     .p-t-#{$n} {
//         padding-top: #{$n}px;
//     }
//     .p-b-#{$n} {
//         padding-bottom: #{$n}px;
//     }
//     .p-l-#{$n} {
//         padding-left: #{$n}px;
//     }
//     .p-r-#{$n} {
//         padding-right: #{$n}px;
//     }
// }
```
