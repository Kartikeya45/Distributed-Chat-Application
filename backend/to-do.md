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

4. 