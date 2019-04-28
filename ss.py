def word_break(text, dictionary):
    """
    Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
    If there is more than one possible reconstruction, return any of them.
    If there is no possible reconstruction, then return null.

    For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
    you should return ['the', 'quick', 'brown', 'fox'].

    Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
    return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
    :param text: a string of letters, without space
    :param dictionary: a list of strings
    :return: a list of strings
    """
    if len(text) == 1 or 0:
        return None

    for i in range(1, len(text)):
        if text[:i] in dictionary:
           # res.append(text[:i])
           print(text[:i])
           text = text[i+1:]
        else:
            break

    return word_break(text, dictionary)


print(word_break("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']))


"""
public class Solution {
    public boolean wordBreak(String s, Set<String> dict) {
        boolean[] t = new boolean[s.length()+1];
        t[0] = true; //set first to be true, why?
        //Because we need initial state
 
        for(int i=0; i<s.length(); i++){
            //should continue from match position
            if(!t[i]) 
                continue;
 
            for(String a: dict){
                int len = a.length();
                int end = i + len;
                if(end > s.length())
                    continue;
 
                if(t[end]) continue;
 
                if(s.substring(i, end).equals(a)){
                    t[end] = true;
                }
            }
        }
 
        return t[s.length()];
    }
}
"""

"""
public boolean wordBreak(String s, Set<String> wordDict) {
    int[] pos = new int[s.length()+1];
 
    Arrays.fill(pos, -1);
 
    pos[0]=0;
 
    for(int i=0; i<s.length(); i++){
        if(pos[i]!=-1){
            for(int j=i+1; j<=s.length(); j++){
                String sub = s.substring(i, j);
                if(wordDict.contains(sub)){
                    pos[j]=i;
                }
            } 
        }
    }
 
    return pos[s.length()]!=-1;
}
"""




def tiles(matrix):
    """
    You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
    Each False boolean represents a tile you can walk on.

    Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required
    to reach the end coordinate from the start. If there is no possible path, then return null.
    You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

    For example, given the following board:
    [[f, f, f, f],
    [t, t, f, t],
    [f, f, f, f],
    [f, f, f, f]]

    and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required
    to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
    :param matrix: a list of lists containing booleans
    :return: an integer
    """