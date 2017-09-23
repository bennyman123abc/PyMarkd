import os
import sys

class Markd:
	def __init__(self):
		self.markdown = []
		
	def add(self, text):
		self.markdown.append(text)
		
	def normal(self, text):
		self.add(text)
		
	def h1(self, text):
		text = "# " + text
		self.add(text)
		
	def h2(self, text):
		text = "## " + text
		self.add(text)
		
	def h3(self, text):
		text = "### " + text
		self.add(text)
	
	def h4(self, text):
		text = "#### " + text
		self.add(text)
		
	def h5(self, text):
		text = "##### " + text
		self.add(text)
		
	def h6(self, text):
		text = "###### " + text
		self.add(text)
		
	def image(self, altText, url):
		text = "![" + altText + "](" + url + ")"
		self.add(text)
		
	def link(self, altText, url):
		text = "[" + altText + "](" + url + ")"
		self.add(text)
		
	def unorderedList(self, items):
		for item in items:
			text = "* " + item
			self.add(text)
			
	def orderedList(self, items):
		i = 1
		for item in items:
			text = str(i) + ". " + item
			self.add(text)
			i+=1
			
	def blockQuote(self, lines):
		for line in lines:
			text = "> " + line
			self.add(text)
			
	def codeBlock(self, lang, text):
		text = "```" + lang + "\n" + text + "\n```"
		self.add(text)
		
	def write(self, filename):
		file = open(filename, "w+")
		for line in self.markdown:
			print line
			line = line + "\n"
			file.write(line)
		file.close()
