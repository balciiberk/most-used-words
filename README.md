# Most Used Words

This program finds the most used words in the given .pdf files.

It can be used for finding the most used words in a language by adding .pdf e-books. However if only one book is given, the most used words would be the name of the characters in the book or it would depend on the writing style of the author. So this program is written for reading multiple .pdf files.

It reads the .pdf files, cleans the words from punctuation, converts to lowercase and splits the words. Then it saves the list of the words in json format. Lastly it reads the json file counts the words and shows most used words or plots it in a bar plot.

An example bar plot:
[most-used-10-words](/images/plot_en.png)
