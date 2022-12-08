# Advent of code 2022
Using Python with Pandas and Numpy.

www.adventofcode.com



# Notes 
Notes for improvements/optimization later on.

### Day 1
Interesting to solve using Pandas. But it is far more readable to iterate through each line without Pythons built in file reader. 

### Day 2
Current solution is more or less "hardcoded". There is probably a much cleaner solution to be found
by looking at the numeric relationship between `A, B, C`. 

### Day 3
Clean solution utilizing `apply` with Pandas.

Though ``"".join(list(set.intersection(*map(set, list(x)))))`` is verbose and has room for simplification.

### Day 4
Readable and simple with Numpy, but can be vectorized.

### Day 5
Grotesque code, but there is probably no way around it without editing the input beforehand.

### Day 6
Try to remove the range loop.

### Day 7
No usage of Pandas and Numpy expect for file reading. I'm yet to find a way to utilize either of them when
working with Trees and recursion.

### Day 8
Try to remove the range loop. Vectorization.

