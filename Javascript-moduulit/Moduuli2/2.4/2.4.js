var numbers = [];
while (true) {
  var num = parseInt(prompt("Enter a number (0 to end):"));
  if (num == 0) {
    break;
  }
  numbers.push(num);
}

numbers.sort(function(a, b) {
  return a - b;
});
numbers.reverse();
for (var i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}