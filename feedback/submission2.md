# `submission.md`

## Personal Information

- **Name:** REDACTED
- **NetID:** REDACTED
- **Major** ECE
- **Class Year:** 2022
- **Operating System:** Windows
- **Python Experience [1-10]:** 5
- **Algorithms Experience [1-10]:** 6

## Write-up Questions

**Question 1:** 

How would you describe the behavior of the depth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

When I don't block anything it almost seems like it's building up its search horizontally, completing a horizontal row then going up by one until it finishes.
It seems like it's going down individual 'paths' until they terminate before going on to the next individual path, but it runs so fast it's honestly hard to tell.
Also, in BFS I saw there was a red and blue square.  In DFS I only see the red square and not the blue, I assume destination, square.

**Question 2:**

How would you describe the behavior of the breadth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

It seems to traverse all passages at the same time, unlike DFS which would only check a single passage at a time.  Without nodes blocked off it almost goes out like a wave up
to the red square.  It seems that the traversal order is less dependent on however many nodes are around a given node and more dependent on where you are in the entire cycle
of traversal - that didn't make much sense but what I mean is that it seems like where DFS did its own thing and didn's seem to care about where you were at in terms of 
your general search (it would just ping off down some small passage and forget about the rest for a while) BFS seems to pay equal attention to all passages.

**BONUS:**

Depth-first search can also be implemented non-recursively, in a manner very similar to your implementation of breadth-first search. What change would have to be made to implement DFS in this way?

It would be similar to the BFS solution but since DFS searches on the most recently seen node, I would use a stack instead of a queue to load the nodes into the algorithm (haven't tested this, just my basic guess)

## Assignment Evaluation

### Quick Feedback

- **Length of Assignment (# Hours):** 3 (would have been 1 but debug took me longer than it should have)
- **Quality of Instructions [1-10]:** 8 (Very clear, I just would have liked a mention of how to debug with your datatypes)
- **Quality of Visualizer [1-10]:** 6 (It really won't be effective until it gets the QOL fixes mentioned below)
- **Overall Rating [1-10]:** 7 (A very thorough project - just needs a bit of polish on the visualizer itself)

### Written Responses

**Question 1:**

What are your overall thoughts on the assignment? Did it help you learn? If so, in what ways was the assignment helpful? Was the visualizer a useful tool? If so, in what ways was it useful?

This assignment was helpful to visualize the algorithms, but the visualizer just ran so fast that I didn't have time to trace what was happening.  A speed control argument and maybe an argument allowing you to step through each iteration would help.  Also, a mode to visualize the students' algorithms would be amazing for debugging or even testing out different variations on these algorithms.  Most of what I learned was Python syntax stuff - Python doesn't error where I think it would, so debugging just took a bit longer for me because of minor syntactic problems.  I've used python a bit before, but always for graphing or web server coding, never for algorithms.

I'm also a bit confused on why BFS had a destination square and DFS did not.  Could you maybe mention why that is in the instructions?

**Question 2:**

What would you change about the assignment? Were there any points in particular that seemed confusing? Did you need outside help at any point?

I would love if the visualizer also displayed basic controls for itself.  It would also be nice to have it either run slower or give the user control
over its speed.  Also, it would be nice to just have a button to reset it instead of having to back out of it and restart it in the terminal each time.

I'm surprised that the visualizer doesn't show us how our changes effect the algorithm when it runs.  I had a mistake in my dfs algorithm and it kept telling
me I had a mistake, but the visualizer seemed to be working fine so I was confused until I saw that the visualizer would run fine no matter what.  I think
the visualizer should respond to whatever changes people make to their algorithms.

Also, I found myself having an error which just said "returned list type is incorrect" and I actually wasn't sure how to start debugging that.  I looked at the visualizer.py to help myself debug - just make sure that either the source visualizer.py is available, or people are given a guide on what the error messages mean, and a way to do debug prints on your datatypes.