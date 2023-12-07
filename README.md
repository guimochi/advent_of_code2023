# [Advent of code 2023](https://adventofcode.com/2023)

A daily updated repository of my Python solutions for the Advent of Code challenges. This project reflects my journey of learning Python and enhancing my problem-solving skills, one puzzle at a time.<br>
For each puzzle, I will give my personal difficulty, how I proceeded to solve it and what I learned from it.

## Calendar

| Mon         | Tue         | Wed         | Thu         | Fri         | Sat         | Sun         |
|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
|             |             |             |             | [1](#day-1) | [2](#day-2) | [3](#day-3) |
| [4](#day-4) | [5](#day-5) | [6](#day-6) | [7](#day-7) | 8           | 9           | 10          |
| 11          | 12          | 13          | 14          | 15          | 16          | 17          |
| 18          | 19          | 20          | 21          | 22          | 23          | 24          |
| 25          | 26          | 27          | 28          | 29          | 30          | 31          |

## [Day 1](https://github.com/guimochi/advent_of_code2023/tree/main/day1)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day1/part1.py)

#### Difficulty: ⭐️☆☆☆☆

#### Duration: 5 minutes

This was really easy.
I read the file line by line.
For each line, I save the digits in an array.
I get the first and last digit and merged them together to create a number.
And add this number to a sum through each iteration.

#### Learned concepts

- List comprehension
- with to close a resource automatically

### [Part 2](https://github.com/guimochi/advent_of_code2023/blob/main/day1/part2.py)

#### Difficulty: ⭐️⭐️⭐☆☆

#### Duration: 60 minutes

This one was a bit more challenging. I had no idea how to proceed at first to get all the digits in words as numbers. I
first thought about using split by numbers. When I don’t know if I can do something in Python, I usually ask Bing Chat.
I asked him if there was a way to split a string by numbers. He told me that I could use the re module. After doing so,
I realized that it didn’t solve my problem. Then I learned about the findall method. I used it to get all the numbers in
the string with the regex `one|two|three|four|five|six|seven|eight|nine|\d`. Then I used a dictionary to get the number
associated with the word. I thought I was done, but then I realized that for more complicated strings
like `nineoneonetwoneightwo`, there were some numbers missing. The last digit `two` was missing for example. It would
find `eight` and I suppose it wouldn’t use the letter t to compose the word `two`. <br> I then decided to use search
instead of findall. It would only return the first match, but then I thought that I could use it in reverse too. I
checked the documentation but didn’t find a way to start by finding the last match. I decided to reverse the string and
then use search to get the last match. I also had to reverse the dictionary to get the matching string.

#### Learned concepts

- library re
- dictionary
- extended slice
- raw string

## [Day 2](https://github.com/guimochi/advent_of_code2023/tree/main/day2)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day2/part1.py)

#### Difficulty: ⭐️⭐️☆☆☆

#### Duration: 48 minutes

It wasn’t challenging. Honestly, the most difficult part was naming all the variables to make them understandable. I had
to perform multiple splits and I wanted to avoid using the same variable name for each one. The logic was quite
straightforward. I created a dictionary with the color name as the key and the highest quantity found at once as the
value. Then, I checked if any of these values were higher than the one given in the puzzle. Voilà!

I was keen on making the code as clean as possible. I provided the type for almost every variable and tried to use as
few hard-coded values as possible. I am quite pleased with the result.

#### Concepts Learned

- Type hinting
- Naming variables can be hard 😅

### [Part 2](https://github.com/guimochi/advent_of_code2023/blob/main/day2/part2.py)

#### Difficulty: ☆☆☆☆☆

#### Duration: 4 minutes

I can’t believe how straightforward it was. I spent more time writing this text than coding the solution. I simply had
to use the previous function, but instead of comparing the maximum allowed quantity, I had to multiply the quantities of
each color. I am really satisfied with what I have accomplished. Thanks to my meticulous approach in the previous part,
I barely had to make any changes to make it work.

#### Concepts Learned

- how important avoiding magic numbers is 😇

## [Day 3](https://github.com/guimochi/advent_of_code2023/tree/main/day3)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day3/part1.py)

#### Difficulty: ⭐️⭐️⭐️⭐️☆

#### Duration: 3 hours 36 minutes

TThis was quite a challenging experience. I initially misunderstood the puzzle not once, but twice. At first, I thought
I was only supposed to check the numbers adjacent to the symbols. Then, I believed I was only supposed to check the top,
left, bottom, and right. It finally dawned on me that I also had to check the diagonals. <br>

I also lost some time due to my unfamiliarity with the Iterator. I wasn't aware that I couldn't iterate over it more
than once. To overcome this, I had to cast it to a list, which allowed me to iterate over it multiple times. <br>

To make the solution as efficient as possible, I utilized a couple of data structures. This might make the solution
appear a bit more complicated.<br>

Despite these challenges, I don't think the problem was particularly hard. The code is quite well-documented, so I'll
provide a quick explanation of the logic here:<br>

1. I created a list of tuples that retain the line of a symbol and its match.
2. I created a set of adjacent coordinates that I would need to check.
3. I created a dictionary with the line as the key and a list of numbers and their respective match.
4. Finally, I summed all the numbers that are in a candidate coordinate.

On a side note, I had a rough start to the day of the challenge. I had only slept for 3 hours and woke up at 6 am when
the challenge started. I had to spot the first misinterpretation right away because I had to go to work.

#### Concepts Learned

- Iterable can't be iterated more than once
- Manipulating set
- Manipulating dictionary
- How important it is to understand the problem before starting to code 🫠

### [Part 2](https://github.com/guimochi/advent_of_code2023/blob/main/day3/part1.py)

#### Difficulty: ⭐️⭐️⭐️☆☆

#### Duration: 1 hour 16 minutes

The logic stays the same but I had to add the match associated with all candidate coordinates to the coordinates. <br>
This caused some keys issues with the dictionary. This solved the issued where a number wouldn't appear multiple times
if
iy was associated with multiple gears and also the fact that I had no way to associate a number with a gear. <br>
It allowed me to link all adjacent numbers to gear. <br>

## [Day 4](https://github.com/guimochi/advent_of_code2023/blob/main/day4)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day4/part1.py)

#### Difficulty: ⭐️☆☆☆☆

#### Duration: 15 minutes

This was easy. Just split split split everywhere. The "hardest" part was managing the times 2, but even that is simple.

### [Part 2](https://github.com/guimochi/advent_of_code2023/blob/main/day4/part2.py)

#### Difficulty: ⭐️⭐️⭐️☆☆

#### Duration: Approximately 2 hours

This was quite belong because I lost myself in what I wanted to do multiple times. The fact that I didn't create any
function in the first exercice didn't help either. As this one was more complicated, i decided to create functions and I
even created a class for the Scratchcard. <br>
I had to think a bit for the recursive function. I initally planned to it
iteratively but it seemed harder. I am quite satisfied with that I managed to it recursively. However, it takes several
seconds to run. I am not sure if it is because of the recursive function or because I created a new Scratchcard for
everytime I call the function `get_rewardd(self)` in Scratchcard. I may decide to optimize it a day in the future. But
it won't be
any time soon.

#### Concepts Learned

- Class
- List comprehension

## [Day 5](https://github.com/guimochi/advent_of_code2023/blob/main/day5)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day5/part1.py)

#### Difficulty: ⭐️⭐️⭐️⭐️⭐️

#### Duration: Approximately 3 hours

I encountered a problem with the `pop` function. Initially, I was under the impression that it removed an element from
the beginning of a list, but it actually removes from the end. <br>
The inputs were quite large and difficult to handle. <br>
In the map input, the destination was placed before the source, which was confusing. <br>
The key value from `a_to_b` was a tuple of strings, but I should have used a single string and obtained the path from a
different source.<br>
I realized that the input values were extremely large. It wasn't feasible to create a complete dictionary, so I had to
keep track of the offset for a specific range.<br>
I made a mistake when I used a `continue` statement instead of `break`. 🥲

#### Concepts Learned

- pop
- list comprehension
- dictionary
- continue vs break
- storing the minimum amount of data is valuable

### [Part 2](https://github.com/guimochi/advent_of_code2023/blob/main/day5/part2.py)

#### Difficulty: 💀

#### Duration: ??

I suspect there might be a nested loop in my code. Despite my efforts to optimize it, I didn't succeed. I spent an
entire day trying to solve and optimize this issue.<br>
When I ran out of ideas, I turned to Bing chat for help. I utilized as many Python functions as possible with
IntervalThree and multi-threading, but to no avail. Eventually, I had to abandon my approach.<br>
In the end, I resorted to a completely different solution that I found online. To be honest, I don't fully understand it
yet.

#### Concepts Learned

- intervaltree
- multi-threading
- python functions
- excalidraw

## [Day 6](https://github.com/guimochi/advent_of_code2023/blob/main/day6)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day6/part1.py)

#### Difficulty: ⭐️☆☆☆☆

#### Duration: 1 hours 10 minutes

I misunderstood the assignment once again. I was under the impression that I had to keep only the fastest races, not all
those that exceeded the previous record. <br>
I spent more time searching for suitable data structures than actually solving the problem. The task was quite
straightforward otherwise.

#### Concepts learned

- heapq

### [Part 2](https://github.com/guimochi/advent_of_code2023/blob/main/day6/part2.py)

#### Difficulty: 🧸

The only modification I made was in the way the lines were read.<br>
However, after resolving this, I looked up an online solution. I think I'll adopt this approach daily from now on. The
solution presented wasn't necessarily more optimal, but it did provide strategies for faster resolution.

#### Concepts learned

- zip

## [Day 7](https://github.com/guimochi/advent_of_code2023/blob/main/day7)

Incoming...
