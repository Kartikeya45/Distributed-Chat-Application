Elections in wireless environments

Our servers can be super-peers
    These requirements are easily met using structured Distributed Hash Table (DHT) based systems.

    Another approach is based on positioning nodes in an m-dimensional geometric space. Assume we need to place N super peers evenly throughout the overlay.
    The basic idea is simple: a total of N tokens are spread across N randomly chosen
    nodes. No node can hold more than one token.
    • Each token represents a repelling force by which another token is inclined to move
    away. The net effect is that if all tokens exert the same repulsion force, they will move
    away from each other and spread themselves evenly in the geometric space.
    • This approach requires that nodes holding a token learn about other tokens. To this
    end, we can use a gossiping protocol by which a token’s force is disseminated
    throughout the network.
    • If a node discovers that the total forces that are acting on it exceed a threshold, it will
    move the token in the direction of the combined forces, as shown in Figure 6.23.
    • When a token is held by a node for a given amount of time, that node will promote
    itself to superpeer.

    