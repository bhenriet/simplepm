# -*- coding: utf-8 -*-        
from pyparsing import *

testString = "[List:   Liste des tAches]"    
listTitle = Suppress("[")+Word(alphas)+Suppress(":")+Group(OneOrMore(Word(alphas+alphas8bit)))+Suppress("]")
# listTitle = Suppress("[")+Word(alphas)+Suppress(":")+Group(OneOrMore(Regex(r"(.+)")))+Suppress("]")





title = listTitle.parseString(testString)

print title
# print alphas

# lineBody = SkipTo(lineEnd).setParseAction(mustBeNonBlank)

# # now define a line with a trailing lineEnd, to be replaced with a space character
# textLine = lineBody + Suppress(lineEnd).setParseAction(replaceWith(" "))

# # define a paragraph, with a separating lineEnd, to be replaced with a double newline
# para = OneOrMore(textLine) + Suppress(lineEnd).setParseAction(replaceWith("\n"))


# print para.parseString(test)v  bd

# greet = Word( alphas ) + "," + Word( alphas ) + "!"

# element = Word( caps, lowers )
# integer = Word( digits )
# elementRef = Group( element + Optional( integer, default="1" ) )
# chemicalFormula = OneOrMore( elementRef )