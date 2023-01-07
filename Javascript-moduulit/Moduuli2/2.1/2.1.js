var numbers = [];

for (var i = 0; i < 5; i++) {
  numbers.push(parseInt(prompt("Enter a number:")));
}
for (var i = numbers.length - 1; i >= 0; i--) {
  console.log(numbers[i]);
}