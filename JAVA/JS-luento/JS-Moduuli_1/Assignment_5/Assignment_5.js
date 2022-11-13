/*let v = parseInt(prompt("Anna vuosiluku:"));
if ((v % 4 == 0 && v % 100 != 0) || (v % 400 == 0 ))
{
    kohde.innerHTML = "Vuosi on karkausvuosi";
}
else {
    kohde.innerHTML = 'Vuosi ei ole karkausvuosi';
}
*/
let v
let kohde = document.querySelector('#kohde')
let alku = parseInt(prompt("Anna alkuvuosi!"));
let loppu = parseInt(prompt("Anna loppuvuosi!"));

let html = '<ul>';
for (let v = alku; v <= loppu; v++);
{
    if ((v % 4 == 0 && v % 100 != 0) || (v % 400 == 0 ))
    {
        html += '<li>';
        html += v;
        html += '</li>'
    }
}
html += '</ul>'

html = kohde.innerHTML