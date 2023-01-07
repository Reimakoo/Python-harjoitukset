var year = parseInt(prompt("Enter a year:"));

if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
  var result = year + " is a leap year.";
} else {
  var result = year + " is not a leap year.";
}

var el = document.getElementById("result");

el.textContent = result;