'use strict'
function sayHello() {
    console.log('moi!');
}

const interval = setInterval(sayHello, 1000);
clearInterval(interval)