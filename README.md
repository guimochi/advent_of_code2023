# [Advent of code 2023](https://adventofcode.com/2023)

My solutions to the small programming puzzles

All my solutions will be posted here. I have decided to use this challenge as an opportunity to refine my skills in
Python.
For each puzzle, I will give my personal difficulty, how I proceeded to solve it and what I learned.

## Calendar

| Mon | Tue | Wed | Thu | Fri         | Sat         | Sun         |
|-----|-----|-----|-----|-------------|-------------|-------------|
|     |     |     |     | [1](#day-1) | [2](#day-2) | [3](#day-3) |
| 4   | 5   | 6   | 7   | 8           | 9           | 10          |
| 11  | 12  | 13  | 14  | 15          | 16          | 17          |
| 18  | 19  | 20  | 21  | 22          | 23          | 24          |
| 25  | 26  | 27  | 28  | 29          | 30          | 31          |

## Day 1

### Part 1

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

### Part 2

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

## Day 2

### Part 1

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

### Part 2

#### Difficulty: ☆☆☆☆☆

#### Duration: 4 minutes

I can’t believe how straightforward it was. I spent more time writing this text than coding the solution. I simply had
to use the previous function, but instead of comparing the maximum allowed quantity, I had to multiply the quantities of
each color. I am really satisfied with what I have accomplished. Thanks to my meticulous approach in the previous part,
I barely had to make any changes to make it work.

#### Concepts Learned

- how important avoiding magic numbers is 😇

## Day 3

Incoming ...
