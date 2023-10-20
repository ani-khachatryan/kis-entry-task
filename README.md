# 1C Admission Task

## The task
![Снимок экрана от 2023-10-20 23-49-20](https://github.com/ani-khachatryan/kis-entry-task/assets/69533525/e1c110d6-44d7-451d-92e4-d24c5862e3bd)

## My Solution
Given 2 directories, this tool compares the files they contain, counting similarity ratio for each pair. \
My solution uses hashing for identical pairs, and splitting into chunks + lcs for counting the similarity percentage. \
Since every file has up to 10^7 bytes, and we have up to C(10 * 10) file comparisons, using LCS is not really effective,\
because it's O(n*m), that's why I decided to split the data into chunks, and perform the algorithm on every chunk separately.

Use
```
python3 main.py
```
to run the program.

To run the test example, copy the repository, run the program, and write given below as test input:
```
tests/a
tests/b
70
```
