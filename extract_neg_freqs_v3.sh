#

# Program to exctract zero or neg. freqs:

#grep "WITH SHRINKING FACTORS" *.out > neg_freqs_grabbing_more_decimals.txt 
python extract_neg_freqs_v3.py > neg_freqs_grabbing_more_decimals.txt

ex neg_freqs_grabbing_more_decimals.txt <<-EOF
  :g/\[\]/d    
  :g/^$/d     
  :%s/\.\//\r\.\//g 
  :g/MODES         EIGV          FREQUENCIES     IRREP/d
  :g/HARTREE/d
  :g/compilation/d
  :g/crystal/d
  wq " Update changes and quit.
EOF

#echo "" >> neg_freqs_grabbing_more_decimals.txt # Add a new line at the end of the file to allow <extract_neg_freqs_v3_counting.py> to work # This is not necessary
echo "You can now open the 'neg_freqs_grabbing_more_decimals.txt' file, with the summary for all the negative freqs"

echo "Counting the number of negative freqs..."

# In order, these commands are:

# remove lines with "[]"
# remove emtpy lines
# search for "./"
# Add an empty line before "./"
# Update changes and quit.

python extract_neg_freqs_v3_counting.py
