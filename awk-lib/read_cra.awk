{
   chars += length; words += NF; lines++
} 
END {
   print "Lines:", lines, "Words:", words, "Chars:", chars
}