#!/usr/bin/env python
"""
md2reveal - convert a basic markdown file to an html file in reveal format.

Usage: when-changed input_file.md [output_file.html]
       when-changed input_file.md [output_file.html] -a AUTHOR -t TITLE -d DESCRIPTION

By Vincent Knight (www.vincent-knight.com)
License: BSD, see LICENSE for more details.
"""
import sys


def print_slide(string, outfile):
    """
    Function to write slides in reveal markdown format.
    """
    outfile = open(outfile, "ab")
    outfile.write("<section align=left data-markdown>")
    outfile.write(string)
    outfile.write("</section>")
    outfile.close()

arguments = sys.argv[1:]  # Read in passed options

if len(arguments) == 0:
    sys.exit("""
Not enough arguments provided.
Please provide at least an input md file and optionally an output html file ('md2reveal_output.html' by default).
             """)

input_file_name = arguments[0]
output_file_name = "md2reveal_output.html"
if len(arguments) >= 2:
    output_file_name = arguments[1]

#Look for title tag
title = "md2reveal.py slides"
if '-t' in arguments:
    tpos = arguments.index('-t')
    title = arguments[tpos+1]

#Look for description tag
description = "Reveal file created using md2reveal.py"
if '-d' in arguments:
    dpos = arguments.index('-d')
    description = arguments[dpos+1]

#Look for author tag
author = "md2reveal"
if '-a' in arguments:
    apos = arguments.index('-a')
    author = arguments[apos+1]

# Write preamble for reveal (things can be tweaked here and things like Mathjax
# added but do so in the output file.

output_file = open(output_file_name, "wb")
output_file.write("""
<!doctype html>
<html lang="en">

	<head>
		<meta charset="utf-8">

		<title>%s</title

		<meta name="description" content=%s>
		<meta name="author" content=%s>

		<meta name="apple-mobile-web-app-capable" content="yes" />
		<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />

		<link rel="stylesheet" href="css/reveal.min.css">
		<link rel="stylesheet" href="css/theme/simple.css" id="theme">

		<!-- For syntax highlighting -->
		<link rel="stylesheet" href="lib/css/zenburn.css">

		<!-- If the query includes 'print-pdf', use the PDF print sheet -->
		<script>
			document.write( '<link rel="stylesheet" href="css/print/' + ( window.location.search.match( /print-pdf/gi ) ? 'pdf' : 'paper' ) + '.css" type="text/css" media="print">' );
		</script>

		<!--[if lt IE 9]>
		<script src="lib/js/html5shiv.js"></script>
		<![endif]-->
	</head>

	<body>

		<div class="reveal">

			<!-- Any section element inside of this container is displayed as a slide -->
			<div class="slides">
""" % (title,description,author))
output_file.close()

# Read in markdown file
input_file = open(input_file_name, "rb")
input_file = input_file.read()
slides = input_file.split("#")[1:]  #Create list with elements corresponding to slides

# Write reveal markdown code
for slide in slides:
    print_slide("###" + slide, output_file_name)

output_file = open(output_file_name, "ab")

# Write end of reveal file
output_file.write("""
			</div>


		</div>

		<script src="lib/js/head.min.js"></script>
		<script src="js/reveal.min.js"></script>

		<script>

			// Full list of configuration options available here:
			// https://github.com/hakimel/reveal.js#configuration
			Reveal.initialize({
				controls: true,
				progress: true,
				history: true,
				center: true,

				theme: Reveal.getQueryHash().theme, // available themes are in /css/theme
				transition: Reveal.getQueryHash().transition || 'linear', // default/cube/page/concave/zoom/linear/none

				// Optional libraries used to extend on reveal.js
				dependencies: [
					{ src: 'lib/js/classList.js', condition: function() { return !document.body.classList; } },
					{ src: 'plugin/markdown/showdown.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
					{ src: 'plugin/markdown/markdown.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
					{ src: 'plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
					{ src: 'plugin/zoom-js/zoom.js', async: true, condition: function() { return !!document.body.classList; } },
					{ src: 'plugin/notes/notes.js', async: true, condition: function() { return !!document.body.classList; } }
					// { src: 'plugin/remotes/remotes.js', async: true, condition: function() { return !!document.body.classList; } }
				]
			});

		</script>

	</body>
</html>
""")
output_file.close()
