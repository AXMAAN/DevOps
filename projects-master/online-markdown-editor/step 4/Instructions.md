# Converting the Markdown to HTML

So when we type the input is stored in content. Then this content is tested with `.test()` method for various regex patterns & then the text is wrapped with html tags based on that pattern. We get an array of potential matches of a particular pattern using `match()` method of string & then we extract text from each of the match & wrap it with correct html tags & replace the original match.

For example : When we match a heading 1 & capture `# hi` we then extract `hi` from the capture & this is the extracted text. Now we replace `# hi` with `<h1> hi</h1>`. Similarly we do for other patterns.

> `.test()` method tests for a match in a string. It returns true or false based on pattern matched or not. We will also use `match()` method which returns an array containing all of the matches, including capturing groups, or null if no match is found.

First things first , we will be doing all our markdown to html conversions inside the input event listener. Read the comments inside code to understand it better.

```js
textinput.addEventListener('input', (e) => {
  let content = e.target.value
  // here we will do the conversion
  markdown_preview.innerHTML = content
})
```

> Note : The `slice()` method is used to extract a section of a string and return it as a new string, without modifying the original string.

## The conversion for h1 is something like this below :

```javascript
if (h1.test(content)) {
  const matches = content.match(h1) // returns array [] of all heading 1

  matches.forEach((element) => {
    const extractedText = element.slice(1)
    // each element is sliced from index 1
    // Example string : # Hi , then string will be ' Hi' because at index 1 is whitespace.
    content = content.replace(element, `<h1>${extractedText}</h1>`)
    // then replace the matched string with formatted HTML whose text content is extracted text.
    // finally reassign this replaced string.
  })
}
```

## The conversion for h2 is something like this below :

```javascript
if (h2.test(content)) {
  const matches = content.match(h2) // returns array [] of all heading 2
  matches.forEach((element) => {
    const extractedText = element.slice(2) // each element is sliced from index 2
    // Example string : ## Hi , then string will be ' Hi' because at index 2 is whitespace.
    content = content.replace(element, `<h2>${extractedText}</h2>`)
    // then replace the matched string with formatted HTML whose text content is extracted text.
    // finally reassign this replaced string.
  })
}
```

## The conversion for bold is something like this below :

```javascript
if (bold.test(content)) {
  const matches = content.match(bold)
  matches.forEach((element) => {
    const extractedText = element.slice(2, -2) //sliced from index 2 till the (total length - 2)
    // Example : **abhik** , index 2 is a, so the new string is started from a
    // total length of string is 9  therefore 9 - 2 is 7. So the new string is from index 2 to 7 which is abhik
    content = content.replace(element, `<strong>${extractedText}</strong>`)
  })
}
```

## The conversion for highlight is same as bold :

```javascript
if (highlight.test(content)) {
  const matches = content.match(highlight)
  matches.forEach((element) => {
    const extractedText = element.slice(2, -2) //sliced from index 2 till the (total length - 2)
    // Example : ==abhik== , index 2 is a, so the new string is started from a
    // total length is 9  therefore 9 - 2 is 7. So the new string is from index 2 to 7 which is abhik
    content = content.replace(
      element,
      `<span class="highlight">${extractedText}</span>`,
      // we will add custom styles for highlight class in style.css
    )
  })
}
```

## The conversion for italics is something like this below :

```javascript
if (italics.test(content)) {
  const matches = content.match(italics)
  matches.forEach((element) => {
    const extractedText = element.slice(2, -1)
    //sliced from index 2 till the (total length - 1)
    // Example : *abhik* , index 2 is a because the regex for italics says there should be 1 more character before star, so the new string is started from a
    // total length is 8  therefore 8 - 1  is 7. So the new string is from index 2 to 7 which is abhik
    content = content.replace(element, `<em>${extractedText}</em>`)
  })
}
```

## The conversion of hyperlinks :

```js
if (link.test(content)) {
  const links = content.match(link)
  // ['[abhikb](https://www.youtube.com/c/abhikb)']
  links.forEach((element) => {
    const text = element.match(/^\[.*\]/)[0].slice(1, -1) // abhikb will be extracted
    const url = element.match(/\]\(.*\)/)[0].slice(2, -1)
    // https://www.youtube.com/c/abhikb will be extracted
    content = content.replace(element, `<a href="${url}">${text}</a>`)
  })
}
```

## The conversion of lists is :

Example string

```md
- hi
- bye

1. hdhd
2. jdjdj
```

Code for converting that md to html :

```javascript
if (lists.test(content)) {
  const matches = content.match(lists)

  matches.forEach((list) => {
    const listArray = list.split('\n')
    // ['- hi', '- bye', '', '1. hdhd', '2. jdjdj']
    const formattedList = listArray
      .map((currentValue, index, array) => {
        if (unorderedList.test(currentValue)) {
          currentValue = `<li>${currentValue.slice(2)}</li>`

          if (!unorderedList.test(array[index - 1])) {
            //array[index-1] will be false if it is null,undefined or < 0
            // unorderedList.test(array[index - 1]) will return true only if the the array element at index - 1 is ul element
            // !unorderedList.test(array[index - 1]) will return true if the unorderedList.test(array[index - 1]) returns false
            currentValue = '<ul>' + currentValue
            // this means if the previous element of the list element in the array  is not a list element or this list element is the 1st element of the array  then add a starting ul tag
          }
          if (!unorderedList.test(array[index + 1])) {
            //array[index+1] will be false if it is null,undefined or > length of the array
            // unorderedList.test(array[index + 1]) will return true only if the the array element at index+1 is ul element
            // !unorderedList.test(array[index + 1]) will return true if the unorderedList.test(array[index + 1]) returns false
            currentValue = currentValue + '</ul>'
            // this means if the next element of the list element in the array  is not a list element or this list element is the last element of the array  then append a closing ul tag
          }
        }
        //Similarly create ol
        if (orderedList.test(currentValue)) {
          currentValue = `<li>${currentValue.slice(2)}</li>`

          if (!orderedList.test(array[index - 1])) {
            currentValue = '<ol>' + currentValue
          }

          if (!orderedList.test(array[index + 1])) {
            currentValue = currentValue + '</ol>'
          }
        }

        return currentValue
      })
      .join('')

    content = content.replace(list, formattedList)
  })
}
```

## Other lines

Finally we add all the normal text lines (not headings or lists) inside p tags

```javascript
content = content
  .split('\n')
  .map((line) => {
    if (!line.startsWith('<') && line !== '') {
      // if line is not empty & does not start with html tag
      return line.replace(line, `<p>${line}</p>`)
    } else {
      return line
    }
  })
  .join('\n')
```

By Now Preview side should have HTML preview of whatever markdown you write on text editor.
