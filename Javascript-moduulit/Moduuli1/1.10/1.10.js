function diceProbability() {
  let numDice = prompt("Enter the number of dice:");
  let targetSum = prompt("Enter the sum of the eye numbers:");

  numDice = Number(numDice);
  targetSum = Number(targetSum);

  let totalRolls = 0;
  let targetRolls = 0;

  for (let i = 0; i < 10000; i++) {
    let rollSum = 0;
    for (let j = 0; j < numDice; j++) {
      rollSum += Math.floor(Math.random() * 6) + 1;
    }

    if (rollSum === targetSum) {
      targetRolls++;
    }
    totalRolls++;
  }

  let probability = (targetRolls / totalRolls) * 100;

  document.write(`Probability to get sum ${targetSum} with ${numDice} dice is ${probability.toFixed(2)}%.`);
}

diceProbability();