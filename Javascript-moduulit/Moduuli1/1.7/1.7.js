function rollDice() {
  let numDice = prompt("Enter the number of dice to roll:");

  numDice = Number(numDice);

  let rollSum = 0;

  for (let i = 0; i < numDice; i++) {
    rollSum += Math.floor(Math.random() * 6) + 1;
  }

  console.log(`The sum of the dice rolls is ${rollSum}.`);
}

rollDice();