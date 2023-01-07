var numbers = [];

while (true) {
  var num = parseInt(prompt("Enter a number:"));

  if (numbers.indexOf(num) >= 0) {
    console.log("The number " + num + " has already been given.");
    break;
  }
  numbers.push(num);
}

numbers.sort(function(a, b) {
  return a - b;
});

console.log("Numbers:", numbers);