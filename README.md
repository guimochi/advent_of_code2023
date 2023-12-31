# [Advent of code 2023](https://adventofcode.com/2023)

A daily updated repository of my Python solutions for the Advent of Code challenges. This project reflects my journey of
learning Python and enhancing my problem-solving skills, one puzzle at a time.<br>
For each puzzle, I will give my personal difficulty, how I proceeded to solve it and what I learned from it.

## Calendar

| Mon           | Tue           | Wed           | Thu           | Fri         | Sat         | Sun           |
|---------------|---------------|---------------|---------------|-------------|-------------|---------------|
|               |               |               |               | [1](#day-1) | [2](#day-2) | [3](#day-3)   |
| [4](#day-4)   | [5](#day-5)   | [6](#day-6)   | [7](#day-7)   | [8](#day-8) | [9](#day-9) | [10](#day-10) |
| [11](#day-11) | [12](#day-12) | [13](#day-13) | [14](#day-14) | 15          | 16          | 17            |
| 18            | [19](#day-19) | 20            | 21            | 22          | 23          | 24            |
| 25            | 26            | 27            | 28            | 29          | 30          | 31            |

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
value. Then, I checked if any of these values were higher than the one given in the puzzle. Voilà!<br>

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

This was indeed a challenging task. I misunderstood the puzzle not just once, but twice. Initially, I thought I was only
supposed to check the numbers adjacent to the symbols. Then, I believed I was only supposed to check the top, left,
bottom, and right. It finally dawned on me that I also had to check the diagonals. <br>

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

The logic remains the same, but I had to associate each match with all candidate coordinates. <br>

This led to some key issues with the dictionary. However, it resolved the problem where a number wouldn't appear
multiple times if it was associated with multiple gears, and the fact that I had no way to associate a number with a
gear. <br>

This allowed me to link all adjacent numbers to a gear.

## [Day 4](https://github.com/guimochi/advent_of_code2023/blob/main/day4)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day4/part1.py)

#### Difficulty: ⭐️☆☆☆☆

#### Duration: 15 minutes

This was easy. Just split split split everywhere. The "hardest" part was managing the times 2, but even that is simple.

### [Part 2](https://github.com/guimochi/advent_of_code2023/blob/main/day4/part2.py)

#### Difficulty: ⭐️⭐️⭐️☆☆

#### Duration: Approximately 2 hours

This task was quite lengthy because I lost track of what I wanted to achieve multiple times. The fact that I didn't
create any functions in the first exercise didn't help either. As this one was more complex, I decided to create
functions and even created a class for the Scratchcard. <br>

I had to put some thought into the recursive function. I initially planned to do it iteratively, but that seemed more
challenging. I'm quite satisfied with how I managed to implement it recursively. However, it takes several seconds to
run. I'm not sure if this is due to the recursive function or because I created a new Scratchcard every time I call
the `get_rewardd(self)` function in Scratchcard. I might decide to optimize it someday in the future, but that won't be
anytime soon.

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
- [Excalidraw](https://excalidraw.com/)

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

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day7/part1.py)

#### Difficulty: ⭐️⭐️⭐️☆☆

#### Duration: 1 hours 10 minutes

The underlying logic of the code was fairly straightforward. There was no need to handle straights and flushes. I simply
kept track of the repetition of each card.<br>
The more challenging part was determining which hand was superior to the other. For this, I created a class that would
keep track of the cards converted to an integer and their bid. I had to define the `__lt__` function to allow `heapq` to
sort it.<br>
I manually input each scenario and assigned them arbitrary values. The code has a lot of if-else statements, but I
couldn't think of a different way to handle it.<br>
If two hands had the same combination, I checked the cards one by one and used an `Enum` to assign values to them.
However, this was unnecessary. I could have simply used a dictionary, but I forgot about them at the time. I did
implement this in the second part.<br>
Finally, I used `heapq` to sort all the hands.

#### Concepts learned

- not to use Enum
- all the compare function in a class
- heapq uses lt

### [Part 2](https://github.com/guimochi/advent_of_code2023/blob/main/day7/part2.py)

#### Difficulty: ⭐️⭐️☆☆☆

#### Duration: 30 minutes

The task initially appeared to be more intricate than it truly was.<br>My first step was to substitute the unwieldy enum
with a straightforward function that utilized a map, setting the value of `J` to 0.<br>

In my implementation, I focused on tracking the count of repetitions rather than the cards themselves. This allowed me
to simply augment the highest occurrences by the count of `J`s.<br>

I did face a challenge when `J` emerged as the most frequent value or if `J` was the sole value in the hand. I addressed
this by eliminating its occurrence and incrementing the count of `J`s to the first element of my sorted hand, which
maintains the repetition count for each card.<br>

Upon making this adjustment, I noticed that I could alter the `if-else` conditions since I can now directly access the
first element instead of using `max()`. Moreover, I believe that invoking `max()` every time I performed the check,
rather than sorting from the start, was inefficient. However, I decided not to modify this at the moment due to other
project commitments.<br>

## [Day 8](https://github.com/guimochi/advent_of_code2023/blob/main/day8)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day8/part1.py)

#### Difficulty: ⭐️⭐️⭐️⭐️☆

#### Duration: 2 hours

Once again, I misunderstood the assignment. I’ve reached a point where I know I’ll be giving myself extra work every day
because of this.<br>

Initially, I believed that the input was the path to follow, and from there, the task was to find the shortest route. I
spent about an hour trying to implement a recursive method, but as I’m not yet accustomed to them, I hit a roadblock.
When I finally found a working algorithm, I realized that the assignment requirements were different. So, I had to start
over. <br>

However, the assignment turned out to be much simpler than I had initially thought. I was able to utilize the Noeud
class and method I had previously created and build upon it.

I then simply followed the input until I reached the destination.

#### Concepts learned

- recursive is one of my weak points
- I really need to read the assignment more carefully

### [Part 2](https://github.com/guimochi/advent_of_code2023/blob/main/day8/part2.py)

#### Difficulty: ⭐️⭐️⭐️⭐️☆

#### Duration: 45 minutes

This one was challenging, particularly because there was no issue with the algorithm. However, I thought there might be
a problem since I couldn't find the solution. So, I spent some time verifying that the algorithm wasn't the issue. <br>

Honestly, I considered the smallest common multiple from the beginning, but I was unsure about implementing it from
different starting points. I consulted a professor to confirm if I was on the right track, and he affirmed it. <br>

I was aware that there was a simple algorithm to find the least common multiple (LCM), but I didn't know it by heart.
So, I asked Bing chat to do it for me. <br>

I first looked for the first time each path would reach a `..Z`. Once it reached a `..Z`, I made it loop again to find
the next time it would return to it. That's when I realized that they looped perfectly, which was a significant help.
Honestly, I'm still not sure how I was supposed to make it work from different starting points.<br>

So I had to find the different _cycles_ for each starting point and find the LCM between them.

#### Concepts learned

- LCM algorithm
- GCF algorithm

## [Day 9](https://github.com/guimochi/advent_of_code2023/blob/main/day9)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day9/part1.py)

#### Difficulty: ⭐️⭐️☆☆☆

#### Duration: 1 hour

The puzzle left me more impressed than necessary. I anticipated it to be more challenging given that it's the weekend,
but it turned out to be less daunting than expected. <br>

I approached the exercise by handling each input individually. I aim to continue this approach as much as possible, as I
believe it's more logical. <br>

Initially, I struggled to grasp the input, often forgetting my task. However, I eventually managed to fully wake up and
focus. <br>

For each input, I constructed the entire pyramid. I used the sum of the line to check if it was entirely composed of
zeros, which I thought was a clever idea. However, I later realized that this could pose problems if the line contained
negative numbers and the sum coincidentally equaled zero.<br>

I then appended an extra zero to the last line. I iterated in reverse order, adding the last element of the current line
and the previous one to the preceding line. <br>

Once the pyramid was complete, I added the last element from the first line to a variable.

#### Concepts learned

- I need some time to wake up

### [Part 2](https://github.com/guimochi/advent_of_code2023/blob/main/day9/part2.py)

#### Difficulty: 🧸

#### Duration: 5 minutes

There’s not much to elaborate on here. Simply subtract instead of adding, and insert at the beginning rather than at the
end. That’s essentially all there is to it.

## [Day 10](https://github.com/guimochi/advent_of_code2023/blob/main/day10)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day10/part1.py)

#### Difficulty: ⭐️⭐️⭐️⭐️☆

#### Duration: 1 hour 10 minutes

This task proved to be challenging. Dealing with graphs is not something I'm accustomed to, and it required a
significant amount of thought before I could implement a solution.<br>

I must admit, I'm not entirely pleased with the end result. The code is complex and even upon reviewing it now, I
struggle to comprehend it.<br>

In an attempt to navigate the maze, I chose to keep track of my origin point. This helped me determine the entry and
exit points in a pipe. However, this approach still feels odd.<br>

I also explored a solution that implemented a depth-first search. While it appears to be more elegant and efficient, I
still find it difficult to understand.<br>

#### Concepts learned

- graph
- depth-first search
- enumerate

### [Part 2](https://github.com/guimochi/advent_of_code2023/blob/main/day10/part2.py)

#### Difficulty: 🫠?

#### Duration: 1 hour 40 minutes

I was completely at a loss on how to solve this problem. My professor introduced me to a gif that demonstrated a simple
algorithm for checking the direction of a pipe. Here is the link to the gif: https://imgur.com/a/ukstWKO#ZKurCuH <br>

The workings of this algorithm are still unclear to me. Moreover, the success of my code seems to be input-dependent,
which I find puzzling. If I alter the conditions under which the flag should be raised, the output can vary
drastically - it could be completely incorrect or perfectly accurate, depending on the input. For instance, with one set
of inputs, the code functions as expected, but with another, it fails. Interestingly, when I switch the conditions, the
first set of inputs yields incorrect results, while the second set works fine... <br>

I tested both inputs for the puzzle and found that the second one worked. I decided to stop there, as I have set a
personal limit of three hours per puzzle due to other projects I need to focus on.

#### Concepts learned

- some puzzles are just too hard

## [Day 11](https://github.com/guimochi/advent_of_code2023/blob/main/day11)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day11/part1.py)

#### Difficulty: ⭐️⭐️⭐️☆☆

#### Duration: 1 hour

While the task was not particularly difficult, manipulating the input proved to be a challenge once again. I still don't
have a complete understanding of how to handle it. There was also the subtle detail that inserting a row or column would
offset all subsequent ones.<br>

Apart from that, I don't believe the problem was overly complex. I created a new, expanded galaxy and then calculated
the distance between each galaxy using absolute values.

#### Concepts learned

- \* to unpack
- be careful about offsets
- adding or replacing char in string is no fun

### [Part 2](https://github.com/guimochi/advent_of_code2023/blob/main/day11/part2.py)

#### Difficulty: ⭐️⭐️⭐️☆☆

#### Duration: 30 minutes

This one was intriguing. It was not possible to recreate a new galaxy, so I had to utilize the index of empty lines or
columns.<br>

I verified whether we cross any empty line/row while moving from one galaxy to another. I believe I found an ingenious
method to check this by swapping `ax` with `bx` and `ay` with `by`. Initially, I had two counters, but I later realized
that one was sufficient.<br>

I then multiplied the counter by the expansion size and subtracted the counter's value. This is crucial because when
calculating the distance without expansion, we already traverse the expanded part once.

## [Day 12](https://github.com/guimochi/advent_of_code2023/blob/main/day12)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day12/part1.py)

#### Difficulty: ⭐️⭐️⭐️☆☆

#### Duration: 1 hour 10 minutes

I was aware that my solution would work for part 2, but I still decided to proceed with it because I couldn't
conceive a better one. I was eager to attempt a recursive approach as I believed it was the most effective method,
but unfortunately, I was unsuccessful. <br>

So, I resorted to brute force, generating every possible scenario and verifying their validity. There was nothing
particularly ingenious about this method, but it was effective nonetheless.

### [Part 2](https://github.com/guimochi/advent_of_code2023/blob/main/day12/part2.py)

#### Difficulty: ❌

#### Duration: 2 hours 30 minutes

I was aware that I wouldn’t be able to solve it, or at the very least, it would take me an extended period to devise a
solution. Consequently, I decided to refer to online solutions, and I’m pleased with that decision. <br>

The code is quite complex to elucidate, but I have meticulously commented on every single part for clarity

#### Concepts learned

- pruning
- memorisation
- difficult problems can be easily decomposed
- improved my understanding of recursive functions

## [Day 13](https://github.com/guimochi/advent_of_code2023/blob/main/day13)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day13/part1.py)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day12/part1.py)

#### Difficulty: ⭐️⭐️⭐️☆☆

#### Duration: 1 hour

My approach is straightforward. I iterate through all the blocks, and if I encounter two similar rows adjacent to each
other, I store them in an array. Then, I verify if it’s the center of reflection. <br>

Transposing all the columns into rows seemed like a simple and intuitive idea. However, I ended up providing the input
twice. I could have transposed the block and rechecked it only if necessary. <br>

Although the code lacks proper documentation, I believe I should have created more functions for better clarity. <br>

#### Concepts learned

- transposing lines

### [Part 2](https://github.com/guimochi/advent_of_code2023/blob/main/day13/part2.py)

#### Difficulty: ⭐️⭐️⭐️⭐️☆

#### Duration: 1 hour 20 minutes

This time I documented all functions and explained all checks. This second part is now easier to understand than the
first one, even though it was a bit harder. <br>

I didn’t go through the whole input twice. I used the transpose again. The fact that having a smudge could
transform a line into the center of reflection was hard easy to grasp. Thankfully they gave it in the example,
otherwise I would have probably spent a lot more time. <br>

Furthermore, I misunderstood the assignment (again…). I thought that the smudge would change the line of reflection from
horizontal to vertical and vice-versa, not that it could change it from one place to another. So I lost a bit of time
fixing that. <br>

Overall I am quite satisfied, but there are so many lines of code. There must be ways to do it a lot shorter. <br>

## [Day 14](https://github.com/guimochi/advent_of_code2023/blob/main/day14)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day14/part1.py)

#### Difficulty: ⭐️⭐️☆☆☆

#### Duration: 40 minutes

Here's your revised text:

I am genuinely pleased with this exercise. I'm beginning to grasp the concepts of unpacking, zipping, and enumerating in
Python. Gradually, I'm becoming more adept at utilizing Python's tools. <br>

## [Day 19](https://github.com/guimochi/advent_of_code2023/blob/main/day19)

### [Part 1](https://github.com/guimochi/advent_of_code2023/blob/main/day19/part1.py)

#### Difficulty: ⭐️⭐️☆☆☆

#### Duration: 1 hour 30 minutes

While the task wasn't challenging, it was somewhat monotonous due to the extensive input processing required.<br>

Nonetheless, I gained substantial knowledge from a YouTube video discussing the problem.<br>

Firstly, I was introduced to the `eval` function, which was previously unfamiliar to me. It enables the evaluation of a
string as a Python expression. However, it can potentially interpret malicious code, so it's crucial to use it
judiciously.<br>

Secondly, I discovered that functions can be stored as values in a dictionary. I had contemplated this idea but hadn't
delved deeply into it. It turns out to be quite straightforward to implement.<br>

Lastly, I understood how Python processes function internally. Everything now makes sense. I had been curious about why
Python always requires the `self` argument in a class. It's because Python first casts a method with the `type()`
function before using it. Then, it places the object as the first argument of the function. This explains why we always
have to include `self` as the first argument of a method.<br>

#### Concepts learned

- eval
- storing functions in a dictionary
- how Python processes functions internally
