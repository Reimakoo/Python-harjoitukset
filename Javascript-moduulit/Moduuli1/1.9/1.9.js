var num = parseInt(prompt("Enter an integer:"));

var isPrime = true;
for (var i = 2; i < num; i++) {
  if (num % i == 0) {
    isPrime = false;
    break;
  }
}

var el = document.getElementById("result");
if (isPrime) {
  el.textContent = num + " is a prime number.";
} else {
  el.textContent = num + " is not a prime number.";
}

