# Creating the REGEX Patterns for each text format

## Markdown Syntax for the following formats are:

- headings 1 & 2 : `# H1`,`## H2`,
- bold : `**bold text**` ,
- italics : `*italicized text*` ,
- highlight : `==highlighted text==`,
- lists (unordered & ordered)

  - unordered :

  ```
  - First item
  - Second item
  ```

  - ordered :

  ```
  1. First item
  2. Second item
  ```

- hyperlinks : `[title](https://www.example.com)`

For detecting those syntaxes we will use regex (short for regular expression). A regex is a string of text that lets you create patterns that help match, locate, and manage text.

In Javascript, we normally test a regex pattern like this : `/abhik/g.test('my name is abhik')`. Here `/abhik/` is the regex pattern. `.test()` method tests for a match in a string. It returns true or false based on pattern matched or not. We will also use `match()` method which returns an array containing all of the matches, including capturing groups, or null if no match is found.

### Learn more about regex [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions).

## Below are some basics of regex.

- `/`
  : this is basic syntax for regex. It means beginning & ending of regex.Example : `/ /`
- `g`
  : this means global . It retains the index of the last match, allowing subsequent searches to start from the end of the previous match.
- `m`
  : When the multiline flag is enabled, beginning and end anchors (^ and \$) will match the start and end of a line, instead of the start and end of the whole string.
- `$`
  : Matches the end of the string, or the end of a line if the multiline flag (m) is enabled. This matches a position, not a character.
- `.`
  : Matches any character except linebreaks
- `*`
  :Matches 0 or more of the preceding token.
- `+`
  : means 1 or multiple occurences

## Parsing Headings

`/^#[^#].*$/gm` is the regex for Heading 1. Let me break it down for you . So when a user writes

```md
# H1

some lines

## h2

Some more lines
```

The above regex will select the 1st line `# H1` & ignore others. Now let me explain the pattern in details.

- `/^`
  : It matches the begining of the string if multiline (m) flag is enabled.
- `#`
  : this is the character we want to match. It is standardly used for markdown headings.
- `[^#]`
  : `[^]` stands for negated set. It means if the characters in this set is found in the string then the string is **not matched**. Here it means if the # is succeded by another # then it is not heading 1 . Example :`## hi` is not heading 1 but `# hi` is heading 1.
- `.*$/gm`
  : means any character (except linebreaks) is allowed till the string or line ends. `g` & `m` means global & multiline.That means all the matches for the pattern will be captured (globally) & those can be multiple lines.

Similarly for heading 2 I will use `/^##[^#].*$/gm`

## Text Formatting

- `**bold**` = `/\*\*[^\*\n]+\*\*/gm`
  : `\*` means look for star(`*`) however since \* has a different meaning in regex we use `\` escape pattern to say it is the star(\*) character & not regex \*.Here it is written twice `\*\*` which means look for 2 consecutive stars. Then a negated set of `*` so that only 2 stars not more than that. However the set is also required here with `+` because after 2 stars there should be atleast 1 or more characters, every character which is not a star will be selected. Then the ending should also have 2 stars. Also this is multiline & global.
- `_italics_` = `/[^\*]\*[^\*\n]+\*/gm`
  : `[^\*]` means the italic segment should not start with 2 consecutive stars. So the 1st character should not be a star , it can be anything but not a star. The 2nd character should be a star. Then any character except star. Then the ending should also have 1 star. This is also multiline & global.
- `==highlight==` = `/==[^==\n]+==/gm`
  : It begins with double = sign & in between any char except double = then ends with double =.

## Hyperlinks

The regex for links is pretty complex `/\[[\w|\(|\)|\s|\*|\?|\-|\.|\,]*(\]\(){1}[^\)]*\)/gm`.

- `\[`
  : the alternate text for hyperlink starts with [
- `[\w|\(|\)|\s|\*|\?|\-|\.|\,]*`
  : after the [ , there can be any word or symbols like `() * ? - . white space ,` . The occurence can be 0 or more. That means text can be empty too.
- `(\]\()`
  : then the ] will close the text section & open the url section with (.
- `{1}[^\)]*\)`
  : there can be only 1 `(` inside the link section , there can be any character except `)`. \* here means that the link section can be empty or filled.Then \) closes the link section.

## Lists

The regex for entire group of lists is `/^(\s*(\-|\d\.) [^\n]+)+$/gm`. Lets break it down :

- `^(\s*` means either 0 or more space at the start of the line`
- `(\-|\d\.)` means either `-` or `{digit}.`. Example of `{digit}.` is `1. 2.` like that.
- `[^\n]+)+$` means whitespace , then a negated set of any character except newline (\n),`+)+` means the negated set has 1 or more occurences , the entire `((\-|\d\.) [^\n]+)` has 1 or more occurences. `$` means end of the line (because m flag is enabled).

We need the regex for entire list group so that we can have ul tags. We also have seperate regex for each list item for assigning li tags.

The regex for unordered list is `/^\-\s.*$/` it means the line begins with `-` (note the whitespace) , then any character except newline (\n).

The regex for ordered list is `/^\d\.\s.*$/` it means the line begins with `{digit}.` (note the whitespace) , then any character except newline (\n)
