# Basic Spell Checker



This project was done as a hackerrank basic spell checker challenge as
part of my application for a Data Science Internship @ Jewel Paymentech. 
The position was then offered to me for Summer 2018.

I have done the basic spell checker in hackerrank before modifying the codes
in pycharm to better suit pragmatic cases whereby there are different corpus spanning across multiple txt files. Also, instead of standard input, the inputs
to be corrected will be passed into the program as a command line args. A better
implementation might be to use Google word2vec pre-trained model or the use of word
frequency to measure the probability of the correct spelling of the word given the wrong
spelling.

# Invoking the spell checker
The script is in the project root and the corpus is in <root>/data/*.txt

```shell
# Make sure you are in <root> folder before running the script
$ python spellchecker.py
usage: spellchecker.py word [word ...]

Performs spell checker on the given args.

positional arguments:
word           a word to be corrected

```


With credits from https://norvig.com/spell-correct.html as I believe part of 
the roles and responsibilities of a Data Science Intern involves searching online
resources such as StackOverflow and Google in order to be productive and 
find the correct solution.

Done by **Liu Zhemin**. 

Feel free to contact me @ zliu023@e.ntu.edu.sg