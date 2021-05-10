# `submission.md`

## Personal Information

- **Name:** REDACTED
- **NetID:** REDACTED
- **Major** physics
- **Class Year:** 2021
- **Operating System:** MAC
- **Python Experience [1-10]:** 3
- **Algorithms Experience [1-10]:** 3

## Write-up Questions

**Question 1:** 

How would you describe the behavior of the depth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

It goes like a tree branching out. The order is depth first such that the algorithm traverses the space until a dead end, at which point it looks back on its path for a way out. It bypasses the nodes that are blocked.

**Question 2:**

How would you describe the behavior of the breadth-first search algorithm? In what order does it traverse the graph? What happens when some nodes are blocked off?

It kinds of expands diagonally, as if push all fronts simultaneously. When some nodes are blocked off, it also bypasses them.

**BONUS:**

Depth-first search can also be implemented non-recursively, in a manner very similar to your implementation of breadth-first search. What change would have to be made to implement DFS in this way?

Instead of taking the first element of the queue as in the BFS, take the last element of the queue at each iteration.

## Assignment Evaluation

### Quick Feedback

- **Length of Assignment (# Hours):** 1
- **Quality of Instructions [1-10]:** 7
- **Quality of Visualizer [1-10]:** 8
- **Overall Rating [1-10]:** 8

### Written Responses

**Question 1:**

What are your overall thoughts on the assignment? Did it help you learn? If so, in what ways was the assignment helpful? Was the visualizer a useful tool? If so, in what ways was it useful?

I think the visualization is quite helpful. Also, the step-by-step guide in the document makes the assignment much easier than expected. The tool is pretty interactive, which makes the experience 
interesting.

**Question 2:**

What would you change about the assignment? Were there any points in particular that seemed confusing? Did you need outside help at any point?

I didn't need outside help, but I think here are a couple of thoughts that I had when I did the assignment:
1. It would be great if the spped of the visualizer is much slower. It was a bit difficult for me to see 
exactly which squares are being filled at each step. It would be cool if there can be like a speed control
where we can speed things up or slow down.
2. The error messages seems a bit confusing, and not exactly pointing out what I did wrong. It kind of 
reminds of the segmentation fault in C programming.
Overall, thanks a lot for this great experience! ;)
