# Counting the number of negative freq's 

import re
import os
import numpy as np
import pdb


# None of the imports are required
# We only need a count
negatives = 0

# Previously I was not closing the file
# This closes it automagically
with open('neg_freqs_grabbing_more_decimals.txt', 'r') as f:
# print f
  for line in f:
         # No need for a regular expression here
         if line.startswith("./"):
           if negatives:
              print 'len(negatives) = ', negatives, '\n'
              negatives = 0
           print line 

         # Used "else if" since both `startswith` can't be true
         elif line.startswith("["):
#          print 'line = ', line

#          print 'type(line) = ', type(line) 
           # `line` is a  <type 'str'>. We need to change if to list,
           #  in order to count. This requires 2 steps:

           # 1st: Remove "[]''" from `line`:
           target2 = line.translate(None, "[]'',")
#          print 'target2 = ', target2
           
           # 2nd: split that line target2
           aux = target2.split()
#          print 'aux = ', aux
#          print 'type(aux) = ', type(aux)
           # `aux` is now a  <type 'list'>.

#          print 'len(aux) = ', len(aux)
#          negatives = negatives + len(aux)
           negatives += len(aux) # more compact

if negatives:
   print 'len(negatives) = ' , negatives


