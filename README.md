# Yatzy playing algorithm
Heuristic-based algorithm for playing Scandinavian Yatzy (5 dice, 15 turns, max score is 374).

## Solver 2 algorithm
1. For each of the 15 things that are possible to aim for, estimate an **expected score** if aiming for that.
2. From the expected score, subtract a **cost function**. (The cost function is what you hope to get for each combination, kind of.)
3. Multiply the difference by a **weight function**. This helps to prioritize e.g. the upper half, to get the bonus.
4. Use the max value to determine which dice to save.

Average score: 229

Overall, Solver 2 plays decently, probably better than many humans, but sometimes makes really stupid decisions.

## Demo
Super simple website where you can see it play: [yatzy-solver.fly.dev](https://yatzy-solver.fly.dev/).
