class orderlog:
    """
    You run an e-commerce website and want to record the last N order ids in a log.
    Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

    You should be as efficient with time and space as possible.
    """
    def __init__(self, num):
        self.container = [None] * num
        self.current_index = len(self.container)

    def record(self, order_id):
        self.container.append(order_id)
        return f'The Order ID {order_id} has been added to the log.'

    def get_last(self, i):
        if i > self.current_index:
            print(f'The whole log returned since the number {i} outsized the log length {self.current_index}.')
        return self.container[-i:]

"""
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext 
and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 
containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system.
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", 
and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, 
return the length of the longest absolute path to a file in the abstracted file system. 
If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""

