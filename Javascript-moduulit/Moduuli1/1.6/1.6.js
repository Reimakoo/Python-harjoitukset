function squareRoot() {
  let confirmCalculation = confirm("Should I calculate the square root?");

  if (confirmCalculation) {
    let num = prompt("Enter a number:");

    num = Number(num);

    if (num < 0) {
      document.write("The square root of a negative number is not defined.");
    } else {
      let sqrt = Math.sqrt(num);
      document.write(`The square root of ${num} is ${sqrt}.`);
    }
  } else {
    document.write("The square root is not calculated.");
  }
}
squareRoot();