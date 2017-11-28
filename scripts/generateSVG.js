generateSVG = (input, cellSize=50) => {
  svg = `<svg width="${cellSize}" height="${cellSize}"><circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" /></svg>`
  return svg
}

$( 'body' ).append(generateSVG(1));

// getCaseMaxLength = (cases) => {
//   l = 0
//   for (case in cases):
//     if (cases[case].length > l) {
//       l = cases[case].length
//     }
//   return l
// }
y = [1,2,3,4,5,6,7,8,9,0]
y.slice(y.length - 3,y.length)
console.log(y)
