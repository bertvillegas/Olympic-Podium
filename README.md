# Olympic-Podium
Olympic Podium
Instructions
Write a function called podium that takes:

A list of tuples called scores.
Each tuple will be of the format (str, int), where the string is the name of a person and the integer is the score that they got.

Your function should return a list of the top 3 (person, score) tuples ordered from highest score to lowest score (in other words, the gold, silver, and bronze medalists).

If there is a tie, the person who appears in the scores list first should appear in the returned list first.

Assumptions: len(scores) >= 3

No name will appear in the list more than once

Scores will be integers - but they could be negative, 0, or positive

Example: podium([('Mikayla', 20), ('Kevin', 25), ('Tristan', 10), ('Moe', 30)])
should return

[('Moe', 30), ('Kevin', 25), ('Mikayla', 20)]

because Moe, Kevin, and Mikayla are the 3 highest scorers in order from highest score to lowest score.

