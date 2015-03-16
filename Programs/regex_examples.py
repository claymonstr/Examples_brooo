import re

myStr = 'Shake zula, the mic rula, the old schoola, you want a trip, I\'ll bring it to ya.'

# =================TALK ABOUT======================
#               Zero indexing
#               Positive index
#               Negative index
# =================================================

# "being an idiot" string searching = using find
# and substringing for EVERYTHING.
# okay when it's only for one thing on the fly
# but can grow tedious. string.find() is an
# excellent function, but is a major pain
# when you need certain things in a string.

# find(string, [beg, end]) - works on strings and lists. returns
# the position of whatever you're trying to find.
# if it doesn't exist...then it returns -1.
# in a list it only searches for the element in the list
# and not in the individual strings in the list.
pos = myStr.find(',')

# [:] syntax - works on strings and lists.
# just says to use up to this index
Name = myStr[:pos]

# POINT TO EXPLAIN: Why pos + 1 and not just pos?
pos += 1

nextPos = myStr.find(',', pos)
micRula = myStr[pos:nextPos]
nextPos += 1

# Now we'll need to use rfind() because even though
# we're string searching via the

# rfind(string, [beg, end]) - works similarly, but returns
# index from the right side. Still returns -1 if it can't
# find what you're looking for.
# beg and end are optional arguments.
pos = myStr.rfind(',')
print pos

# And so on...as you can see this is a pain
# perhaps an even better example to see why this
# is painful can be shown here. Say we want only
# the part of the string that says "the old schoola"

# IMPORTANT REGULAR EXPRESSION INFO
# regex = regular expression
# used for pattern matching and general
# "not being an idiot" string searching

# Beginning regex example
##HisName = re.search('^(\\w+),', myStr)

##WhatHeDo = re.search(r'')

