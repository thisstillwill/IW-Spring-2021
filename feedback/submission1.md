# `submission.md`

## Personal Information

- **Name:** REDACTED
- **NetID:** REDACTED
- **Major** COS
- **Class Year:** 2022
- **Operating System:** Mac OSX
- **Python Experience [1-10]:** 9
- **Algorithms Experience [1-10]:** 8

## Write-up Questions

**Question 1:**

How would you describe the behavior of the depth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

YOUR ANSWER HERE
The algorithm always visits nodes in the same direction until it can't anymore, either because a node is blocked off or because it has hit a wall, at which point it changes directions. If there is nowhere to go in all directions, it goes to the "most recent" location where it can make a move.

**Question 2:**

How would you describe the behavior of the breadth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

The BFS algorithm moves in a "wave," which is to say that instead of one branch exploring far off into the grid, the entire "surface" of the explored space moves together. As this surface increases in size, points further from the source are accessed more slowly, but more points closer to the source are accessed than would be by DFS (for the same time period). When a wall or blocked-off node is encountered, BFS simply skips exploring that region and goes onto the next node to be explored.

**BONUS:**

Depth-first search can also be implemented non-recursively, in a manner very similar to your implementation of breadth-first search. What change would have to be made to implement DFS in this way?

You can use a explicit stack data structure instead of depending on Python's built-in function stack. In Python, this could be accomplished by just using a list, where you add to the list when discovering possible neighbors and popping from the list when you're ready to explore those neighbors.

## Assignment Evaluation

### Quick Feedback

- **Length of Assignment (# Hours):** 0.5
- **Quality of Instructions [1-10]:** 9
- **Quality of Visualizer [1-10]:** 10
- **Overall Rating [1-10]:** 10

### Written Responses

**Question 1:**

What are your overall thoughts on the assignment? Did it help you learn? If so, in what ways was the assignment helpful? Was the visualizer a useful tool? If so, in what ways was it useful?

I enjoyed the assignment. It felt sort of like one of those interview-style questions, where the dfs implementation was the warm-up and the bfs (w/ returning the full path specification) was the main question. I think the visualizer was a great component of the assignment and one that I would've appreciated having in a class like COS 226. It may be simple enough to understand an algorithm through powerpoint animations but visualizing the end-result of your work can help you to distinguish nuances between pretty similar graph traversal algorithms.

**Question 2:**

What would you change about the assignment? Were there any points in particular that seemed confusing? Did you need outside elp at any point?

I thought instructions were overall very clear but was a little confused by the fact that in the dfs implementation, we were supposed to both add to the explored list and return it. Although this was laid out clearly in the instructions, it might have just been a personal thing. From the perspective of a course assignment, I liked the way the instructions were laid out, from running the visualizer to the hint to write about DFS after visualizing (instead of waiting until we were done coding).
