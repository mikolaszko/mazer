## MAZER 🐍₪

Maze visualizer and solver

### Created with
Python
Raylib + Pyray
UV


### How does it work
The simplest algorithm for maze solving I could've find, with random neighbour generation and stack to grid mapping.
By assigning directions to the grid positions with offset (stack.top.second + y * maze_width + stack.top.first + x), paths are just "carved out" from the original grid with spaces in-between the cells 
very neat and can be understood within a couple of hours

### What's more to do
- I'd like some sort of UI with user input that would change maze parameters and process controls (start, stop, restart, slower, faster)

### Deep dive
I highly recommend checking out [this video](https://www.youtube.com/watch?v=Y37-gB83HKE&t=1505s).
[javidx9](https://www.youtube.com/@javidx9) does phenomenal work on some very interesting and quite obscure topics, I've reimplemented algorithm in this video using python
