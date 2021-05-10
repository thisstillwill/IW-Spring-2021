# `submission.md`

## Personal Information

- **Name:** REDACTED
- **NetID:** REDACTED
- **Major** COS
- **Class Year:** 2021
- **Operating System:** Mac
- **Python Experience [1-10]:** 5
- **Algorithms Experience [1-10]:** 7

## Write-up Questions

**Question 1:** 

How would you describe the behavior of the depth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

DFS goes the farthest it can in one direction until it hits a wall. The traversal seems to zigzag up the graph from left to right and then right to left. If nodes are blocked off, it backtracks enough to go in another direction until it is blocked again.

**Question 2:**

How would you describe the behavior of the breadth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

BFS explores all the neighbor nodes until it is blocked. It travels upward and ourtward. If some nodes are blocked, it simply tries to explore around it.

**BONUS:**

Depth-first search can also be implemented non-recursively, in a manner very similar to your implementation of breadth-first search. What change would have to be made to implement DFS in this way?

The implementation of dfs non-recursively is similar to bfs, but instead of a queue, keep a stack of explored nodes.

## Assignment Evaluation

### Quick Feedback

- **Length of Assignment (# Hours):** 1
- **Quality of Instructions [1-10]:** 7
- **Quality of Visualizer [1-10]:** 7
- **Overall Rating [1-10]:** 7

### Written Responses

**Question 1:**

What are your overall thoughts on the assignment? Did it help you learn? If so, in what ways was the assignment helpful? Was the visualizer a useful tool? If so, in what ways was it useful?

I found the assignment enjoyable and the instructions were mostly easy to follow. As a senior COS major and having done many coding interview graph questions, it was a good refresher. The visualizer was helper to see how bfs and dfs traversed. 

**Question 2:**

What would you change about the assignment? Were there any points in particular that seemed confusing? Did you need outside help at any point?

I found the visualizer speed of coloring the grid too fast or too slow sometimes. It would be helpful to be able to control that. I also didn't like that I had to exit the GUI and reissue the visualizer command everytime to retest my code. I found the BFS instructions a bit confusing because it wasn't clear that 'queue of paths' meant list of list and the last bullet of instruction seemed like it referring to 'last node' rather than neighbor 'node' and that the append should actually be outside the for loop.
