# yatzy_solver
Implemented a heuristic-based algorithm for playing Scandinavian Yatzy (5 dice, 15 turns, max score is 374).

# Solver 2 algorithm:
1. For each of the 15 things that are possible to aim for, estimate an **expected score** if aiming for that.
2. From the expected score, subtract a **cost function**. (The cost function is what you hope to get for each combination, kind of.)
3. Multiply the difference by a **weight function**. This helps to prioritize e.g. the upper half, to get the bonus.
4. Use the max value to determine which dice to save.

Average score: 229

Overall, Solver 2 plays decently, probably better than many humans, but worse than experienced humans, because it makes really stupid decisions sometimes. For an example game, see solvers/solver2/example_game.txt
