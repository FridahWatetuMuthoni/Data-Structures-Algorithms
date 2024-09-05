// Example of a simple sine lookup table
const sineTable = [];
for (let i = 0; i <= 360; i++) {
  sineTable[i] = Math.sin((i * Math.PI) / 180); // Precompute sine values for each degree
}
// Now you can quickly get the sine value for any angle:
console.log(sineTable[30]); // Sine of 30 degrees
