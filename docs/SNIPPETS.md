### Snippets
```markdown
    .       - Any Character Except New Line
    \d      - Digit (0-9)
    \D      - Not a Digit (0-9)
    \w      - Word Character (a-z, A-Z, 0-9, _)
    \W      - Not a Word Character
    \s      - Whitespace (space, tab, newline)
    \S      - Not Whitespace (space, tab, newline)

    \b      - Word Boundary
    \B      - Not a Word Boundary
    ^       - Beginning of a String
    $       - End of a String

    []      - Matches Characters in brackets
    [^ ]    - Matches Characters NOT in brackets
    |       - Either Or
    ( )     - Group

    Quantifiers:
    *       - 0 or More of the preceding pattern
    +       - 1 or More of the preceding pattern
    ?       - 0 or One of the preceding pattern
    {3}     - Exact Number of the preceding pattern
    {3,4}   - Range of Numbers (Minimum, Maximum) of the preceding pattern
```


#### Sample Regexs ####

```markdown
# To match email addresses
[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
```
