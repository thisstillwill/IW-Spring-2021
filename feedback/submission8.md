# `submission.md`

## Personal Information

-   **Name:** REDACTED
-   **NetID:** REDACTED
-   **Major** COS
-   **Class Year:** 2023
-   **Operating System:** macOS Catalina
-   **Python Experience [1-10]:** 6
-   **Algorithms Experience [1-10]:** 5

## Write-up Questions

**Question 1:**

How would you describe the behavior of the depth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

The depth-first search algorithm, as the name entails, traverses the graph depth-first. From the starting node, it traverses down a path of connected nodes as far as it can until it no longer has adjacent nodes to visit. Then, it backtracks to the most previously visited node and traverses down any other paths that extend from that node, making sure not to re-visit any nodes that it has already visited. When the path hits a node that is blocked off, it simply backtracks to the most recently visited nodes and tries to visit the next neighboring node.

**Question 2:**

How would you describe the behavior of the breadth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

Breadth-first search traverses the graph by first visiting each neighbor of the current node. It visits nodes in increasing distance from the starting node. If a node is blocked off, I believe that it simply does not add that node to the queue and continues visiting neighbors of the current node.

**BONUS:**

Depth-first search can also be implemented non-recursively, in a manner very similar to your implementation of breadth-first search. What change would have to be made to implement DFS in this way?

N/A

## Assignment Evaluation

### Quick Feedback

-   **Length of Assignment (# Hours):** 2/3 hours
-   **Quality of Instructions [1-10]:** 7
-   **Quality of Visualizer [1-10]:** 7
-   **Overall Rating [1-10]:** 7

### Written Responses

**Question 1:**

What are your overall thoughts on the assignment? Did it help you learn? If so, in what ways was the assignment helpful? Was the visualizer a useful tool? If so, in what ways was it useful?

Assignment was a great review of BFS/DFS algorithms, which I had learned in COS226 but had never implemented. So, this assignment was very helpful in teaching me how to implement the BFS/DFS algorithms. The visualizer was not particularly useful for me because I had previously seen BFS/DFS traces, but I think the interactive element is great for first-time learners. Personally, since I learned about graph theory with graphs visualized as circles for nodes and lines for edges, that visualization makes more intuitive sense for me than a grid with implied edges. But for someone who has no previous exposure to graphs, visualizing graphs as grids, which everyone is already familiar with, seems reasonable to me. One main issue with the visualizer is that it's somewhat slow -- not the fault of the programmer, since the visualizer program is probably huge and will inevitably be slow. But user experience wise, I sometimes got frustrated having to click a single box multiple times for it to be blacked out and often had trouble dragging my mouse to block entire swaths of the page. Maybe you can make the grid size somewhat smaller to speed up the program and make it easier to select relatively more blocks on the graph?

**Question 2:**

What would you change about the assignment? Were there any points in particular that seemed confusing? Did you need outside help at any point?

I would make the pseudocode more clear. Since I have seen code for DFS/BFS implementations before, the pseudocode was pretty clear to me, but for someone who is learning DFS/BFS for the first time, this assignment would be really challenging. It would be helpful to explain why the pseudocode works in implementing DFS/BFS, rather than simply giving it to a student to translate into code. In particular, some points in the BFS pseudocode were unclear. For example, you use the verb "Get" to say "get the first path" and "get the last node", but in code, the actions are completely different, since you want to "pop" the first path but simply "retrieve" the last node (without removing it). The use of the same verb misled me to pop both elements, rather than simply retrieving without removing the last node. Also, it is unclear that the conditional check for whether a neighbor is the goal should be inside the loop; indent the bullet point further to clarify this.
