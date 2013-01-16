# Turning markdown in to reveal slides!

The html 5 slides written with [reveal.js](https://github.com/hakimel/reveal.js) look awesome. They also allow for markdown. This script takes advantage of that and writes out the entire html file (preamble etc) needed for a reveal slideshow taking a markdown file as an input.

The markdown file shold seperate slides using the `#` symbol:

    #Title of first slide
    
    Some markdown

    #Title of second slide

    Some more markdown

Note that at the moment no other titles can be indlucded (i.e. don't use '##', '###' etc...).

The idea behind this is that markdown is a great language for writing basic material. Using [pandoc]() you can obtain a bunch of other files from a markdown file:

- LaTeX
- html
- pdf
- docx

Pandoc allows you to create various html 5 slides (not reveal which is my current favorite) as well but I didn't like how it actually did so. This small script takes care of that.

Here's some markdown code:

    #The Plan

    Class schedule:

    - 0900 - 0920: Group presents solution to challenge (R)
    - 0920 - 0940: Class discussion (R)
    - 0940 - 1040: Lab session (R)
    - 1040 - 1100: Break
    - 1100 - 1120: Group presents solution to challenge (SAS)
    - 1120 - 1140: Class discussion (SAS)
    - 1140 - 1040: Lab session (SAS)

Here's the corresponding reveal slide:
![reveal_output](https://github.com/drvinceknight/md2reveal/blob/master/reveal_output.png?raw=true)

# Usage

    when-changed input_file.md [output_file.html]
    when-changed input_file.md [output_file.html] -a AUTHOR -t TITLE -d DESCRIPTION

# License Information
This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0](http://creativecommons.org/licenses/by-sa/3.0/us/) license.  You are free to:

* Share: copy, distribute, and transmit the work,
* Remix: adapt the work

Under the following conditions:

* Attribution: You must attribute the work in the manner specified by the author or licensor (but not in any way that suggests that they endorse you or your use of the work).
* Share Alike: If you alter, transform, or build upon this work, you may distribute the resulting work only under the same or similar license to this one.

When attributing this work, please include me.

