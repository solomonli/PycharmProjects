#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys, re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

"""
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)  ## ['alice@google.com', 'bob@abc.com']
for email in emails:
    # do something with each found email string
    print(email)
"""
# sys.exit(0)


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    names = []
    f = open(filename, 'rU')    # if single quote filename, the file won't be read
    text = f.read()
    f.close()

    year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', text)

    if not year_match:
        sys.stderr.write("Couldn't find the year!")
        sys.exit(1)

    year = year_match.group(1)

    names.append(year)    # year is the first item of the list

    # print(names)

    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)

    rank_dict = {}

    for rank_tuple in tuples:
        (rank, boy, girl) = rank_tuple
        if boy not in rank_dict:
            rank_dict[boy] = rank
        if girl not in rank_dict:
            rank_dict[girl] = rank

    # print(rank_dict)

    sorted_names = sorted(rank_dict.keys())

    for name in sorted_names:
        names.append(name + " " + rank_dict[name])    # append a string to the list name

    return names


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]     # [1:] are those html files

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False

    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    for filename in args:
        names = extract_names(filename)

    # Make text out of the whole list
    text = '\n'.join(names)

    if summary:
        outf = open(filename + '.summary', 'w')
        outf.write(text + '\n')
        outf.close()
    else:
        print(text)

    # For each filename, get the names, then either print the text output
    # or write it to a summary file
  
if __name__ == '__main__':
    main()
