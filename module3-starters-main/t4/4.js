'use strict';
let element = document.getElementById('target')

const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

for (let i = 0; i !== students.length; i++) {
  let student_value = document.createElement('option')
  student_value.innerText = students[i].name
  student_value.value = students[i].id
  element.appendChild(student_value)
}