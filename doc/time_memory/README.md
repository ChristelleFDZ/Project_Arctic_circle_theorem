# Time and Memory


### Time


Our project allows us to simulate the paving of an Aztec diamond of size 200.
For each iterations, which will correspond to the passage from size n to size n + 1, the animation generates 3 images : 

- Creation of the aztec diamond size n + 1
- Removal of badly positioned dominoes
- Coloring dominoes according to their position.

|        |    Aztec Diamond     |        Dominos |
| :------------ | :-------------: | -------------: |
| Time     |     0.0057 s     |        0.00061 s |

An example is provided in the file above : time_domino.ipynb.

### Memory



The first column represents the line number of the code that has been profiled, the second column (Mem usage) the memory usage of the Python interpreter after that line has been executed. The third column (Increment) represents the difference in memory of the current line with respect to the last one.

So, for example, in the file memory_domino.py 59.2 MiB is the memory usage after the first line has been executed. That includes the memory needed to start up Python, load your script and all of its imports.