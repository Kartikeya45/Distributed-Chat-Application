# All TO-DO of Backend

1. Matplotlib hangs when waiting for message
    Soln. : Return empty string instead of blocking
        Inside update(i), return if it is an empty string

2. user_pos = {node: (-1, i) for i, node in enumerate(["U0", "U1", "U2"])}
    server_pos = {node: (1, i) for i, node in enumerate(["S0", "S1"])}
    <br><br>
        These two lines in are specific, make it general
            Problem: The problem is that when we want to show that a server crashed, middle node must not be active.
            Solution: Remove all connections to that server node instead

3. Increase the node size.
    Label not displayed!

4. Due to Ciruclar Imports, not able to import Server to round_robin.py
    So, instead I just copy pasted "class Server" from main_server.py

5. Store all the commands, so that we dont have to rerun the whole thing to see an interactions
    Create a python file to process just these commands all at a time, and if we press left or right arrow, previous or next action takes place accoridnt to command

6. Use different colors to represent differnet interactions between nodes

7. Berkeley, Crisitian create separate run files
    Or put them inside their folders
     -- single line from main_server should be able to run the algorithm

    Or make it menu driven

8. Edge of U4 to NTP not closing
    Commit ID --> 