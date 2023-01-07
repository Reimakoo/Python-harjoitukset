var name = prompt("Enter your name:");
var houseNumber = Math.floor(Math.random() * 4) + 1;

var house;
switch (houseNumber) {
  case 1:
    house = "Gryffindor";
    break;
  case 2:
    house = "Slytherin";
    break;
  case 3:
    house = "Hufflepuff";
    break;
  case 4:
    house = "Ravenclaw";
    break;
}
var el = document.getElementById("result");
el.textContent = name + ", you are " + house + ".";