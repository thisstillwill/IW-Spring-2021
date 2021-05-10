# `submission.md`

## Personal Information

- **Name:** REDACTED
- **NetID:** REDACTED
- **Major** COS
- **Class Year:** 2023
- **Operating System:** Linux
- **Python Experience [1-10]:** 8
- **Algorithms Experience [1-10]:** 8

## Write-up Questions

**Question 1:** 

How would you describe the behavior of the depth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

DFS tries to explore a path as far as possible. It stops exploring a particular path only when it reaches a deadend or the goal. When some nodes are blocked off, it will go backstep the path that it's currently on, and take the opening that's the closest to the deadend. 

**Question 2:**

How would you describe the behavior of the breadth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

BFS explores from the start node, where it considers from the nodes that are the same distances from the start before considering any further nodes. When it runs into nodes that are blocked off, it tries to explore from another node that is not blocked from and is the closest from the start node.

**BONUS:**

Depth-first search can also be implemented non-recursively, in a manner very similar to your implementation of breadth-first search. What change would have to be made to implement DFS in this way?

Would use a stack instead of a queue

## Assignment Evaluation

### Quick Feedback

- **Length of Assignment (# Hours):** 1
- **Quality of Instructions [1-10]:** 6
- **Quality of Visualizer [1-10]:** 9
- **Overall Rating [1-10]:** 8

### Written Responses

**Question 1:**

What are your overall thoughts on the assignment? Did it help you learn? If so, in what ways was the assignment helpful? Was the visualizer a useful tool? If so, in what ways was it useful?

It was a pretty interesting way to teach BFS and DFS. I have already learned both in COS classes before, but it was a nice refresher to actually implemented them again after so long. The visualizer was useful, but could be better if there was a adjust the speed in which the grid was filled in, because right now it's slightly difficult to tell what's happening since everything happens in an instant.

**Question 2:**

What would you change about the assignment? Were there any points in particular that seemed confusing? Did you need outside help at any point?

I would add a bit more documentation, especially to the function headers: the data type of the inputs and what data type I should be returning. I did have to look at visualizer.py to see what datatype I was supposed to return at first.

