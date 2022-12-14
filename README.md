<!-- PROJECT SHIELDS -->
<div align="center">

  [![Contributors][contributors-shield]][contributors-url]
  [![Forks][forks-shield]][forks-url]
  [![Stargazers][stars-shield]][stars-url]
  [![Issues][issues-shield]][issues-url]

  <br />

  <!-- PROJECT LOGO -->
  <a href="https://github.com/elijahw0lf/adventofcode-2022">
    <img src="https://i.imgur.com/6wJjrqO.png" alt="Logo" width="600">
  </a>

<h3 align="center"><b>Advent of Code 2022</b></h3>

  <p align="center">
    <a href="https://www.smarty.com/advent-of-code"><i>Image from smarty.com</i></a>
  </p>
</div>

<br />

<!-- PROJECT INTRODUCTION -->
# What Is This?

<p>This repo holds solutions to puzzles from <a href="https://adventofcode.com">Advent of Code</a>, an advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language. These are my solutions in Python, with no external modules.</p>

<p>A new puzzle is released every day and we must wait for that day to start before we can access it. The solutions are stored into folders that indicate the puzzle date ranging from 01 to 25. I'll try to add some info about each puzzle below but each solution should explain itself between the provided comments and the code itself.</p>

<p>If you have any questions, my contact details are located at the bottom of this readme. Best of luck with your coding journey, and Merry Christmas!</p>

<br />

<!-- PROJECT NOTES -->
# Puzzles
### <b>Dec 1st</b>
<p>As we start out with the puzzles, it appears they incrementally grow in difficulty and so I'll take the opportunity to put a fun spin on this puzzle. There's many ways to accomplish this task, I decided to make an Elf class that would let me hold the Elf's calorie total and conveniently store a method to add food items.</p>

<p>As luck would have it, I actually decided to print out the top 3 calorie totals amongst all the elves, purely because the output of just one elf's calorie total made the terminal look pretty bare. It was easy to do because the elf objects were stored in a list which could then be sorted, so the top 3 calorie totals were the elf objects at indexes 0, 1 and 2 of the list.</p>

<p>When part two was revealed and it asked for the total of the top 3, I just added a line of code to add & print it. I hope that this luck continues as I move through the puzzles, time will tell! This was a fun challenge and a perfect warm-up for the next puzzles.</p>
<br />

---
<br />

### <b>Dec 2nd</b>
<p>This puzzle of scissors, paper, rock was fun and presented a lot of room for creativity. I didn't want to base everything on conditional statements (ie: if statements) which is tempting with this kind of puzzle.</p>

<p>Even though I already used classes, I used them again here because it's so handy to eliminate repeat code. For part one, I typed out the logic (who would win in each scenario) and found a pattern that could be repeated, the only problem was finding which of the two players won in that scenario - and I didn't want to use if statements after coming this far!</p>

<p>By storing the players in a list, I could sort it and find the winner that way. It came in handy for part two where I could use a 3d dictionary to determine the user's correct move and the rest of the code from part one could be repeated, so that went into a function.</p>

<p>I wonder how many people used switches instead of conditional statements, I was tempted to use them here but they're a relatively new addition to Python. In the spirit of sharing, I felt it was better to avoid them so anybody who clones my repo wouldn't be forced to use a later version of python just because of switch, but it would work perfectly here.</p>
<br />

---
<br />

### <b>Dec 3rd</b>
<p>For this puzzle I was more focused on a method to find a common letter between multiple strings that didn't involve looping through the string contents. Not to throw shade at that approach, it's absolutely a valid way to find the result, this was to push me out of my safe zone and to start thinking about features of other data types.</p>

<p>Lately I've been using sets (which I never used before), there is a lot of power in set functions - depending on your needs. I always thought sets and tuples were the same, or at least that they were so similar it didn't really matter. It's really awesome to think about the expanded number of tools we walk away with when we challenge ourselves with puzzles like Advent of Code!</p>

<p>Anyway, about the code; originally I had used a class again, to accept a string and break it down into the bag compartments, typecast to sets, etc. I've learned my lesson and decided not to write anything fancy or to go into great detail with comments until I saw part two.</p>

<p>This paid off as the class was useless to the approach needed for part two and I trashed it for two simple loops in the main function. This is a good lesson that I need to learn, to code more swiftly in the moment and loop back at the end for finishing touches instead of trying to make it perfect on the first pass.</p>
<br />

---
<br />

### <b>Dec 8th</b>
<p>This was my first puzzle and I spent a little too much time on the first part (not knowing there was a second part to the puzzles). The first half uses a function to search for visible trees in a row and re-uses the same function to search a column.</p>

<p>All visible trees are found when looking left to right. Then visible trees from right to left, stopping at the tallest tree discovered from our search from left to right. We can do this because no trees will be visible from that point onwards when looking from right to left, they're all smaller than that tree.</p>

<p>Columns are handled in the same way, we just mark visible trees as either x or y coordinates depending on whether we searched a row or a column. As we search rows and columns, the coordinates of visible trees are stored in a set to eliminate duplicates and that set's length equals all visible <i>internal</i> trees. We can just then add all trees from the edges of the grid to find the total. I used the coordinates from the set to print the tree grid with colors to show visible trees for a little flair.</p>

<p>The second part was quite rushed and was solved in the most basic way. Using nested for loops, we iterate over internal trees (ie: not edge trees). For each tree, there are 4 infinite loops to search in each direction until a tree of equal or taller height is found. At the end, the scenic score is calculated and the highest score is remembered for the solution. I'm positive there's a more graceful way to calculate this (and faster than 4 infinite loops), I look forward to learning how others solved this part of the puzzle!</p>

<br />

<!-- PROJECT LICENSE -->
# License
Distributed under the Mozilla Public License. See `LICENSE` for more information.

<br />

<!-- PROJECT DETAILS -->
# Contact
Elijah Wolf - <a href="mailto:elijah@w0lf.dev">elijah@w0lf.dev</a><br />
Repo Link: [https://github.com/elijahw0lf/adventofcode-2022](https://github.com/elijahw0lf/adventofcode-2022)

<!-- PROJECT RESOURCES -->
[contributors-shield]: https://img.shields.io/github/contributors/elijahw0lf/adventofcode-2022.svg?style=for-the-badge
[contributors-url]: https://github.com/elijahw0lf/adventofcode-2022/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/elijahw0lf/adventofcode-2022.svg?style=for-the-badge
[forks-url]: https://github.com/elijahw0lf/adventofcode-2022/network/members
[stars-shield]: https://img.shields.io/github/stars/elijahw0lf/adventofcode-2022.svg?style=for-the-badge
[stars-url]: https://github.com/elijahw0lf/adventofcode-2022/stargazers
[issues-shield]: https://img.shields.io/github/issues/elijahw0lf/adventofcode-2022.svg?style=for-the-badge
[issues-url]: https://github.com/elijahw0lf/adventofcode-2022/issues