(a) The algorithm compares two lists against each other and returns true if there are duplicate items in the lists.

(b) Because the second for loop is nested inside the first one
So if *n* is 5 both lists are 5 long the first loop will start compare the first item with all of the second lists items,in this case five.
So in the worst case scenario It will run through the first loop 5 times and the second loop 5x5 times or 5 squared.

(c) Because now *j* list is *i* long on each *i* loop the *j* list will be as long as the current *i* loop is. 
So in the first iteration of the loop *i* will be 1 and the *j* list will be 1 long.

(d) Because you are cutting the second for loop in almost half, the only instance where both lists are the same lenght is the last iteration of the *i* loop.
Thus if *n* is 10 on the first loop *j* will go through 1 loop, on the second 2 loops, on the third 3 loops and so on. So at the end of 10n loop
*j* will have gone trough 1+2+3+4+5+6+7+8+9+10=56 loops when in the first scenario it would have been 100 loops.

(e) No, because the second loop is much smaller. Instead the loop now is linear O(n). So instead of if n is 5 looping 25 times it now loops 1+2+3+4+5=15 times
