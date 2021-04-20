# IW Spring 2021

> Teaching graph traversal visually

![Visualizer in action](screenshot.png)

This repository is an assignment designed to teach basic graph traversal algorithms. During the assignment, you will analyze the behavior of the breadth-first search and depth-first search algorithms using the provided visualizer. You will also write your own implementation of each algorithm in Python and test them against the reference solutions.

This assignment assumes some basic familiarity with Python and the terminal.

## Getting Started

[Install Python on your computer](https://www.python.org/downloads/), if you do not have it already (Mac users should consider using [Homebrew](https://brew.sh/)). Use the instructions for your operating system to download and test the visualizer:

### Mac

- [Fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) this repository or [use it as a template](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template)

- In the terminal, create and navigate to the folder you want to work in:

```
mkdir mysolutions
cd mysolutions
```

- [Clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repository into your working directory:

```
git clone MY-REPO-URL .
```

*Make sure the “.” character is in the command.*

- [Create a virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) in your working directory:

```
python3 -m venv env
```

- Activate the virtual environment:

```
source env/bin/activate
```

- Install the required packages:

```
python3 -m pip install -r requirements.txt
```

- Test the visualizer by running a demo:

```
python3 visualizer.py bfs
```

You should see a screen pop up with a grid similar to the screenshot.

- Close the visualizer and deactivate the virtual environment:

```
deactivate
```

You will need to reactivate the virtual environment each time you run the visualizer.

### Windows

- [Fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) this repository or [use it as a template](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template)

- At the command prompt, create and navigate to the folder you want to work in:

```
mkdir mysolutions
cd mysolutions
```

- [Clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repository into your working directory:

```
git clone MY-REPO-URL .
```

*Make sure the “.” character is in the command.*

- [Create a virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) in your working directory:

```
py -m venv env
```

- Activate the virtual environment and install the required packages:

```
.\env\Scripts\activate
```

- Install the required packages:

```
py -m pip install -r requirements.txt
```

- Test the visualizer by running a demo:

```
py visualizer.py bfs
```

You should see a screen pop up with a grid similar to the screenshot.

- Close the visualizer and deactivate the virtual environment:

```
deactivate
```

You will need to reactivate the virtual environment each time you run the visualizer.

### Linux

You probably already know what to do.

## Background

A [graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)) describes a set of *nodes* and the relationships between them. [Graph theory](https://en.wikipedia.org/wiki/Graph_theory) is a core focus area of computer science, and many real-world problems can be represented using graphs. Graphs, for example, can be contextualized to represent networks, relationships, navigation, and more.

This assignment explores the use of different algorithms in [graph traversal](https://en.wikipedia.org/wiki/Graph_traversal). The visualizer represents the graph as a grid of nodes. Each node (if not on the edge) is connected to four neigboring nodes. By using the connections between nodes, it is possible to successively visit each reachable node in the graph.

## Part 1: Depth-First Search

[Depth-first search](https://en.wikipedia.org/wiki/Depth-first_search), or DFS, is one of the most common algorithms used for graph traversal. It starts at a root node and explores as far along a given branch as possible (“depth-first”). If the end of a branch is reached, the algorithm backtracks and checks the next possible branch.

In this assignment, depth-first search will be used to return a list of all nodes connected to the root (the red square in the visualizer).

### Step 1: Exploration

Begin by running the visualizer with the `dfs` option:

#### Mac/Linux

```
python3 visualizer.py dfs
```

#### Windows

```
py visualizer.py dfs
```

When the visualizer opens, you can choose to block off certain nodes in the graph. To do so, click the left mouse button over a grid square. Blocked nodes will be colored black in the visualizer. To unblock a node, either:

1. Click the right mouse button
2. Hold <kbd>Ctrl</kbd> and the left mouse button together

When you are ready, run the reference solution by pressing <kbd>Space</kbd>. Experiment with the visualizer. Try blocking off different parts of the graph to see how the algorithm reacts. At this point, you should be able to answer Question 1 in `submission/submission.md`.

### Step 2. Implementation

You will now write your own implementation of depth-first search. Start by opening `solutions.py`. You should see the function `dfs` at the top of the file. The function takes two arguments:

- `node` - the current node being checked
    - The list of neighbors can be accessed through `node.neighbors`
- `explored` - a list of nodes that have already been checked

The visualizer will call your function with `node` initialized to the root (the red square in the visualizer). You should write your function to operate [recursively](https://en.wikipedia.org/wiki/Recursion_(computer_science)). Consider the following pseudocode:

> If the current node hasn't been seen before:
> - Add the node to the list of explored nodes
> - For each of the node's neighbors:
>     - Recursively check each neighbor and update the explored list 
> 
> Return the list of explored nodes

To clarify, the return type is a list of *Nodes* representing all nodes that were reached starting from the root. Write your solution in the `dfs` function. You should **NOT** modify any code outside of `solutions.py`.

### Step 3. Testing

To test your implementation, run the visualizer with the `-t` or `--test` flag: 

#### Mac/Linux

```
python3 visualizer.py dfs -t
```

#### Windows

```
py visualizer.py dfs -t
```

The visualizer will first show the reference solution after pressing <kbd>Space</kbd>. Press <kbd>Space</kbd> again to test your own implementation. One of two things will happen:

1. Your implementation is correct and the message *“All tests passed!”* will show
2. Your implementation is ***incorrect*** and a descriptive error message will show

If your implementation is correct, take a screenshot showing the *“All tests passed!”* message. Name this file `dfs.png` and place it into the `submission/` folder. If your solution has errors, revise your code and test again before moving on.

## Part 2: Breadth-First Search

[Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search), or BFS, takes the opposite approach from DFS. The algorithm explores each neighbor of the current node before moving down the next branch.

In this assignment, breadth-first search will be used to find the shortest path from the root node to the goal node (the red and blue squares in the visualizer).

### Step 1: Exploration

Begin by running the visualizer with the `bfs` option:

#### Mac/Linux

```
python3 visualizer.py bfs
```

#### Windows

```
py visualizer.py bfs
```

As with the DFS demonstration, you can choose to block or unblock particular nodes.

When you are ready, run the reference solution by pressing <kbd>Space</kbd>. Experiment with the visualizer. Try blocking off different parts of the graph to see how the algorithm reacts. At this point, you should be able to answer Question 2 in `submission/submission.md`.

### Step 2. Implementation

You will now write your own implementation of breadth-first search. Start by opening `solutions.py`. You should see the function `bfs`. The function takes two arguments:

- `start` - the root node
- `goal` - the goal node to find a path to

A node's neigbors can still be accessed through `node.neighbors`

Compared to DFS, it is easiest if you write your solution to operate *non-recursively*. Consider the following pseudocode:

> Create a list to track explored nodes
> 
> Create a queue of paths to check, and add the starting node to it
> 
> While the queue isn't empty:
> - Get the first path from the queue
> - Get the last node from the path
> - If the node hasn't been seen yet:
>     - Make a new path with each neighbor and the current path and add it to the queue
>     - If a neighbor is the goal return the path to it
>     - Add the current node to the list of explored nodes

To clarify, the return type is a list of *Nodes* representing the path from the start to the goal. Write your solution in the `bfs` function. It is guaranteed that the start and goal node will never be the same. You should **NOT** modify any code outside of `solutions.py`.

#### Considerations

##### Queues in Python

There are multiple ways to use a [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) in Python. Perhaps the easiest is to simply use Python's built-in list as a queue. Because queues are first-in-first-out (FIFO), you can use `queue.pop(0)` to get the the element at the front of the queue.

##### Creating lists

To create a new list using a sequence from an existing list, you can pass the existing list as an argument to the constructor:

```
new_list = list(old_list)
```

### Step 3. Testing

To test your implementation, run the visualizer with the `-t` or `--test` flag: 

#### Mac/Linux

```
python3 visualizer.py bfs -t
```

#### Windows

```
py visualizer.py bfs -t
```

The visualizer will first show the reference solution after pressing <kbd>Space</kbd>. Press <kbd>Space</kbd> again to test your own implementation. One of two things will happen:

1. Your implementation is correct and the message *“All tests passed!”* will show
2. Your implementation is ***incorrect*** and a descriptive error message will show

If your implementation is correct, take a screenshot showing the *“All tests passed!”* message. Name this file `bfs.png` and place it into the `submission/` folder. If your solution has errors, revise your code and test again before moving on.

## Submission

Your submission will be your fork of this repository. You should have at a minimum the following files:

- `solutions.py`
- `submission/dfs.png`
- `submission/bfs.png`
- `submission/submission.md`
    - Make sure that you have answered *all* questions in `submission.md`.

Submit any local changes to your repository on GitHub:
```
git add .
git commit -m "Submission"
git push -u origin master
```

Share this repository with me (William Svoboda). This can be accomplished in two ways:

1. [Add me as a collaborator](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/inviting-collaborators-to-a-personal-repository) to your repository
    - This is required if your repository is private
2. Send a link to your repository to my email (netid `wsvoboda`)

## Help!

If you are stuck on this assignment, you have two main options:

### Email Me

I can be reached directly via my email (netid `wsvoboda`)

### Office Hours

I will be available for “Office Hours” the week this assignment is released. More details to follow.
