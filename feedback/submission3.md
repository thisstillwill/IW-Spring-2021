# `submission.md`

## Personal Information

- **Name:** REDACTED
- **NetID:** REDACTED
- **Major** Computer Science
- **Class Year:** 2021
- **Operating System:** Mac
- **Python Experience [1-10]:** 7
- **Algorithms Experience [1-10]:** 8

## Write-up Questions

**Question 1:** 

How would you describe the behavior of the depth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

Similar to the game snake, the dfs algorithm would shoot off in one direction and continually travel until it hit a blocked node or a wall. When no blocks are added in, it, for lack of better word, snakes up the expanse of the grid. When some nodes are blocked off, it tries to go around it by visiting the other neighbors that its current block has instead. 

**Question 2:**

How would you describe the behavior of the breadth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

The bfs algorithm investigates nodes based on their distance. It looks at all the nodes that are the closest to the starting point and then it iteratively reaches further and further out. Blocking off a couple of nodes really doesn't change much about the behaviour of the algorithm. 

**BONUS:**

Depth-first search can also be implemented non-recursively, in a manner very similar to your implementation of breadth-first search. What change would have to be made to implement DFS in this way?

I would use a stack instead of a queue.  

## Assignment Evaluation

### Quick Feedback

- **Length of Assignment (# Hours):** <1
- **Quality of Instructions [1-10]:** 9
- **Quality of Visualizer [1-10]:** 8
- **Overall Rating [1-10]:** 9

### Written Responses

**Question 1:**

What are your overall thoughts on the assignment? Did it help you learn? If so, in what ways was the assignment helpful? Was the visualizer a useful tool? If so, in what ways was it useful?

This was really cool! I enjoyed seeing how my code actually percolated throughout the system. For students first learning these 
concepts, I feel like this will definitely be helpful in the debugging process! 

**Question 2:**

What would you change about the assignment? Were there any points in particular that seemed confusing? Did you need outside help at any point?

To improve, I think the following changes would be great:
1) Add time steps and let the students go back and forth in the percolation steps. Especially when decoding, I think it'd be helpful
to examine exactly what went wrong instead of having to rerun the visualizer code. If time steps are too difficult, then even just
letting the student hit spacebar again and again to play it instead of having spacebar close out the window would be great!
2) Some of the error messages are confusing. I mispelled the function push which throws an attribute error which the visualizer
covers up and says "Missing solution!".  
3) Make bfs visualization run slower for the student solution! It was super fast and I didn't actually get to see what was going on. 
4) Make the error messages more specific for the algorithm based errors. I think it just says something like "your path was shorter" for bfs, but it'd be nice to see exactly how much shorter it was (either via text in the error message or even a visualization of my path)