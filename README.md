# kis-entry-task

Given 2 directories, this tool compares the files they contain, counting similarity ratio for each pair. 
My solution uses hashing for identical pairs, and splitting into chunks + lcs for counting the similarity percentage.

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
