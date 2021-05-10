# `submission.md`

## Personal Information

- **Name:** REDACTED
- **NetID:** REDACTED
- **Major** COS
- **Class Year:** 2023
- **Operating System:** Mac OS
- **Python Experience [1-10]:** 7
- **Algorithms Experience [1-10]:** 7

## Write-up Questions

**Question 1:**

How would you describe the behavior of the depth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

From the root node, the dfs algo moves to the next node over and recursively continues to do so. When a node is blocked off, the algo returns to the previously explored node and repeats the same process. Essentially, the dfs algo explores as far as it can down a specific "path" and then recursively returns to previous nodes and explores other paths the same way.

**Question 2:**

How would you describe the behavior of the breadth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

At each node, all of it's neighbors are first explored. Then, the path moves to the first neighbor explored, which becomes the new current node.

**BONUS:**

Depth-first search can also be implemented non-recursively, in a manner very similar to your implementation of breadth-first search. What change would have to be made to implement DFS in this way?

Using a stack instead of a queue would effectively implement dfs.

## Assignment Evaluation

### Quick Feedback

- **Length of Assignment (# Hours):** 1
- **Quality of Instructions [1-10]:** 10
- **Quality of Visualizer [1-10]:** 5
- **Overall Rating [1-10]:** 7

### Written Responses

**Question 1:**

What are your overall thoughts on the assignment? Did it help you learn? If so, in what ways was the assignment helpful? Was the visualizer a useful tool? If so, in what ways was it useful?

The readme/website were really clear and easy to follow. The instructions were much better than most COS assignments I've done at Princeton. The only thing I didn't find super helpful was the grid style of the visualizer. As someone who has learned bfs and dfs already, I think that learning these algorithms by visualizing them on a tree is much more intuitive (but I may be bias in this regard because I learned them that way).

**Question 2:**

What would you change about the assignment? Were there any points in particular that seemed confusing? Did you need outside help at any point?

Nothing confusing really. The only thing I would change is what I mentioned above (a tree-shaped visualizer). Really well done! Overall, it's still super useful for learning bfs and dfs.
