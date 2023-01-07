function rollDice(numSides) {
  return Math.floor(Math.random() * numSides) + 1;
}

var max = parseInt(prompt("Enter the maximum number on the dice:"));

var ul = document.createElement("ul");

while (true) {
  var roll = rollDice(max);
  if (roll == max) {
    break;
  }

  var li = document.createElement("li");
  li.textContent = roll;
  ul.appendChild(li);
}

var el = document.getElementById("rolls");
el.appendChild(ul);