var num1 = parseInt(prompt("Enter the first integer:"));
var num2 = parseInt(prompt("Enter the second integer:"));
var num3 = parseInt(prompt("Enter the third integer:"));

var sum = num1 + num2 + num3;
var product = num1 * num2 * num3;
var average = (num1 + num2 + num3) / 3;

var sumEl = document.getElementById("sum");
var productEl = document.getElementById("product");
var averageEl = document.getElementById("average");

sumEl.textContent = "Summa: " + sum;
productEl.textContent = "Tulo: " + product;
averageEl.textContent = "Keskiarvo: " + average;