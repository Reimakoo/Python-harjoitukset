'use strict';

let kohde = document.querySelector('#kohde')

let eka = parseInt(prompt("Anna eka"))
let toka =parseInt(prompt("Anna toka"))
let kolmas = parseInt(prompt("Anna kolmas!"))

let summa = eka + toka + kolmas
let tulo = eka * toka * kolmas
let ka = summa / 3

let assignment_3;
assignment_3 =
    'summa = ' + summa +
    ', tulo = ' + tulo +
    ', keskiarvo = ' + ka;

kohde.innerHTML = assignment_3
console.log(assignment_3)