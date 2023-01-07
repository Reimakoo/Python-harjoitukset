var names = [];

for (var i = 0; i < 6; i++) {
  names.push(prompt("Enter the name of dog " + (i + 1) + ":"));
}
names.sort();
names.reverse();

var ul = document.createElement("ul");
for (var i = 0; i < names.length; i++) {
  var li = document.createElement("li");
  li.textContent = names[i];
  ul.appendChild(li);
}
var el = document.getElementById("names");
el.appendChild(ul);