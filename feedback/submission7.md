# `submission.md`

## Personal Information

-   **Name:** REDACTED
-   **NetID:** REDACTED
-   **Major** COS (BSE)
-   **Class Year:** 2023
-   **Operating System:** macOS Big Sur
-   **Python Experience [1-10]:** 10
-   **Algorithms Experience [1-10]:** 9

## Write-up Questions

**Question 1:**

How would you describe the behavior of the depth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

The algorithm is similar to finding your way through a maze with a ball of yarn. You repeatedly explore available paths starting from a certain point (recursively), all the while laying yarn behind you. If/when you hit a dead-end, you follow your yarn back until reaching the most recent fork and take the next path, if there is one. It traverses the graph by prioritizing depth; it always follows paths until hitting a dead end. When some nodes are blocked off, it "reverses" back to the previous path split.

**Question 2:**

How would you describe the behavior of the breadth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

The algorithm is similar to finding your way to a destination by moving one step at a time from each of the nodes in the order they were visited. It appears to terminate upon reaching the desination node in the upper right, and the path drawn appears to be a shortest path. BFS traverses the graph by prioritizing breadth rather than depth. When some nodes are blocked off, it simply stops searching from that point on (no backtracking).

**BONUS:**

Depth-first search can also be implemented non-recursively, in a manner very similar to your implementation of breadth-first search. What change would have to be made to implement DFS in this way?

Use a stack for `paths` instead of a queue (i.e. both append to and remove from the beginning of the list `paths`). Not sure if this is correct but that's what I would try first.

## Assignment Evaluation

### Quick Feedback

-   **Length of Assignment (# Hours):** 1 hour
-   **Quality of Instructions [1-10]:** 8
-   **Quality of Visualizer [1-10]:** 10
-   **Overall Rating [1-10]:** 9

### Written Responses

**Question 1:**

What are your overall thoughts on the assignment? Did it help you learn? If so, in what ways was the assignment helpful? Was the visualizer a useful tool? If so, in what ways was it useful?

This assignment is very solid and satisfying! I especially like the visualization and the auto-evaluator. Most of my previous knowledge about BFS and DFS came from COS226, so this assignment was a nice refresher on that content (and I appreciated doing it in a language other than Java!). If I were a student with minimal knowledge about graph traversal algorithms, this assignment certainly would have helped me learn the core basics of the two search algorithms. The pseudocode really helps with implementation - I would have spent too long on BFS if not for the guidance you provided. The visualizer was definitely useful and attractive especially to students learning CS. Being able to block off certain nodes and seeing how the algorithms react significantly improves the self-learning experience.

**Question 2:**

What would you change about the assignment? Were there any points in particular that seemed confusing? Did you need outside help at any point?

I would try to clarify the pseudocode description for the "queue of paths" in BFS. It took me some time to realize that it can be done using a 2D list. Additionally, I think that the BFS phrase "if the node hasn't been seen yet" should go underneath a parent bullet point like "iterate through all neighbors of the last node of the path." It took me a while to realize that the already-seen check should go _inside_ of the neighbor loop rather than outside (i.e. `if n in explored` rather than `if last in explored`). Perhaps you did this on purpose though as to not give too much guidance.

I did not need any outside help. Great work on this - you did an amazing job!!
