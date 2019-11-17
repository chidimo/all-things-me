# CSS

## `position`: default (`static`)

1. `block`  elements start on new lines and take up the full width available to them
1. `inline`  elements take up only as much space as they need and do not start on new lines
1. `inline-block`  elements can display side-by-side but still can have width and height properties, which regular inline elements cannot
1. `relative`: relative to where it would normally be (requires offset values of top, right, bottom, left).
1. `absolute`: set relative to their nearest explicitly positioned ancestor. If you haven't explicitly set any positioning values on previous elements, the absolutely positioned element will appear relative to the edges of the document.
1. `fixed`: set relative to the entire viewport

## `box-sizing`: default (`content-box`)

1. `box-sizing: {border-box}`: measure box from item border
1. `box-sizing: {content-box}`: measure box from content. Includes `padding` and `border`, but not `margin`.

## `margin`

1. Set in `pixels`: unchanging
1. Set in `em/rem`: relative to the element's text size
1. Set in `%`: relative to the width of the element's container.

## `padding`

1. Set in `pixels`: unchanging
1. Set in `em/rem`: relative to the element's text size
1. Set in `%`: relative to the width of the containing element.

## Flexbox: 1D layouts

1. `justify-content`: align along the main axis.
1. `align-items`: align along the cross axis.
1. `align-self`: align a single element.
1. `align-content`  : align multiple rows or columns along the cross-axis
1. `flex-basis`: control each item's space up along the container's main axis.
1. `flex-grow`: make elements bigger than the ones next to them.
1. `flex-shrink`: reduce the size of certain elements when there's not enough space.
1. `order`: reorder elements in your layout without touching the HTML

## Grid: 2D layout
