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

<h3 align="center" style="font-weight:bold">Advent of Code 2022</h3>

  <p align="center">
    <a href="https://www.smarty.com/advent-of-code" style="font-style: italic">Image from smarty.com</a>
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