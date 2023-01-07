var numParticipants = parseInt(prompt("Enter the number of participants:"));
var names = [];

for (var i = 0; i < numParticipants; i++) {
  names.push(prompt("Enter the name of participant " + (i + 1) + ":"));
}
names.sort();

var ol = document.createElement("ol");
for (var i = 0; i < names.length; i++) {
  var li = document.createElement("li");
  li.textContent = names[i];
  ol.appendChild(li);
}
var el = document.getElementById("names");

el.appendChild(ol);