function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}

var ul = document.createElement("ul");

while (true) {
  var roll = rollDice();
  if (roll == 6) {
    break;
  }

  var li = document.createElement("li");
  li.textContent = roll;
  ul.appendChild(li);
}
var el = document.getElementById("rolls");

el.appendChild(ul);