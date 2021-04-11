# Bad Assed Machines State Machine Thing

For more information see the blog post: https://invalidentry.engineer/blog/death-army-robot-firing-squad/

BAMScriptv1 is a regex based state machine language. Each 'tick', each robot is called, with a string of `left_hand_robots_state-right_hand_robots_state` e.g `2-4`. States are strings, but I've used numbers a lot.

Run the program like so:

    python runme.py programs/solution.py 

Graph the programs:

    python drawgraph.py programs/solution.py

