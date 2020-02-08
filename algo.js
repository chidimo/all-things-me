/**
 *
@param
 {string} initial
 *
@param
 {string} goal
 *
@return
 {number}
 */

function minimumConcat(initial, goal) {
    const map = new Map();
      for (let i = 0; i < initial.length; i++) {
          if (map.get(initial[i])) {
              const arr = map.get(initial[i]);
              arr.push(i);
              map.set(initial[i], arr);
          } else {
              map.set(initial[i], [i]);
          }
      }
      let occurrences = 0;
      for (let i = 0; i < goal.length; i++) {
          const indexes = map.get(goal[i]);
          if (indexes === void 0) return -1;
          occurrences++;
          let max = 0;
          indexes.forEach(index => {
              let j = 0;
              let ignore = 0;
              while(initial[index + j + ignore] !== void 0) {
                  if(goal[i + j] !== initial[index + j + ignore]) {
                      ignore++;
                  } else {
                      max = Math.max(max, j++);
                  }
              }
          });
          i += max;
      }
      return occurrences;
  }

  var initial = readline();
  var goal = readline();
  print(minimumConcat(initial, goal));

  /**
   *
  @param
   {character[][]} matrix
   *
  @return
   {number}
   */
  var maximalRectangle = function(grid) {
    // your code here
  for (let i = 0; i < grid.length; i++) {
      for (let j = 0; j < grid[0].length; j++) {
        grid[i][j] = parseInt(grid[i][j]);
      }
    }

    let row = grid[0];
    let max = largestRectangleArea(grid[0])

    for (let i = 1; i < grid.length; i++) {

      for (let j = 0; j < grid[0].length; j++) {
        if (grid[i][j] === 0) {
          row[j] = 0;
        } else {
          row[j] += 1;
        }
      }

      let currMax = largestRectangleArea(row);
      if (currMax > max) {
        max = currMax;
      }
    }

    return max;

  };

  function largestRectangleArea(arr) {
    if (arr == null || arr.length == 0) {
      return 0;
    }
    var stack = [];

    var max = 0;
    var i = 0;

    while (i < arr.length) {
      if (stack.length == 0 || arr[i] >= arr[stack[stack.length - 1]]) {
        stack.push(i);
        i++;
      } else {
        var p = stack.pop();
        var h = arr[p];
        var w = stack.length == 0 ? i : i - stack[stack.length - 1] - 1;
        max = Math.max(h * w, max);
      }
    }

    while (stack.length != 0) {
      var p = stack.pop();
      var h = arr[p];
      var w = stack.length == 0 ? i : i - stack[stack.length - 1] - 1;
      max = Math.max(h * w, max);
    }

    return max;
  }

  let height = parseInt(readline());
  let width =  parseInt(readline());
  let matrix = [];
  for (var i = 0; i < height; i++) {
    matrix[i] = (readline() || "").split("");
  }

  print(maximalRectangle(matrix));

  /**
   *
  @param
   {character[][]} grid
   *
  @return
   {number}
   */
  function numOffice(grid) {
      let result = 0;
      //Put your code here.
       let counter = 0;

    function dfs(grid, i, j) {
      if (i < 0 || i > grid.length - 1 || j < 0 || j > grid[0].length - 1) {
        return;
      }

      if (grid[i][j] === '0') {
        return;
      }

      grid[i][j] = '0';

      dfs(grid, i - 1, j);
      dfs(grid, i + 1, j);
      dfs(grid, i, j - 1);
      dfs(grid, i, j + 1);
    }

    for (let i = 0; i < grid.length; i++) {
      for (let j = 0; j < grid[0].length; j++) {

        if (grid[i][j] === '1') {
          dfs(grid, i, j)
          counter++;
        }

      }
    }

    return counter;

  };

  let height = parseInt(readline());
  let width =  parseInt(readline());
  let grid = [];
  for (var i = 0; i < height; i++) {
    grid[i] = (readline() || "").split("");
  }

  print(numOffice(grid));
