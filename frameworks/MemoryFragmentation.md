# Memory Fragmentation

Okay, maybe it is a little ridiculous when create new article just for this definition.
   
Memory Fragmentation is the name of the phenomenon when you cannot store more data into your memory even the available space volume is enough for it.

Example 1:

    The easiest way to think about this is to imagine you have a big empty wall that you need to put pictures of varying sizes on.

    Each picture takes up a certain size and you obviously can't split it into smaller pieces to make it fit. 

    You need an empty spot on the wall, the size of the picture, or else you can't put it up. 

    Now, if you start hanging pictures on the wall and you're not careful about how you arrange them, you will soon end up with 
    a wall that's partially covered with pictures and even though you may have empty spots most new pictures won't fit because 
    they're larger than the available spots. You can still hang really small pictures, but most ones won't fit. 
    
    So you'll have to re-arrange (compact) the ones already on the wall to make room for more..

Example 2: more technical

    Assume that we have 10 bytes of memory:
    |   |   |   |   |   |   |   |   |   |   |
      0   1   2   3   4   5   6   7   8   9
    Then allocate 2 byte blocks, name A and B:
     | A | A | A | B | B | B |   |   |   |   |
       0   1   2   3   4   5   6   7   8   9
    Now remove blocks A:
    |   |   |   | B | B | B |   |   |   |   |
      0   1   2   3   4   5   6   7   8   9
    If we have a block D with size is 5 bytes, we can't put it in even there is 7 bytes left.
    This phenomenon is called memory fragmentation.

Both example was written depend on the answers on [this question on StackoverFlow](https://stackoverflow.com/questions/3770457/what-is-memory-fragmentation#:~:text=Memory%20fragmentation%20is%20when%20most,(i.e.%20malloc%20returns%20null).)