# 1-Million-Games-of-War
Statistics after simulating 1 million games of war

5 Statistics about each game were saved:
1. Turns (length of game)
2. Wars (number of ties)
3. Longest War (longest chain of ties)
4. Winner (which player won)
5. Starting Hand Difference (sum of player1's starting hand - sum of player2's starting hand

Basic Stats:

                    Turns            Wars  Starting Hand Difference
    count  1000000.000000  1000000.000000            1000000.000000
    mean       234.147225       14.652556                  0.017602
    mode        83.000000        5.000000                  0.000000
    std        186.797662       11.360250                 27.252131
    min          3.000000        0.000000               -126.000000
    25%        103.000000        7.000000                -18.000000
    50%        179.000000       11.000000                  0.000000
    75%        308.000000       19.000000                 18.000000
    max       2499.000000      153.000000                122.000000
 ‎ 
                                                
    Longest War: 6

Graphs:

Histogram of the amount of turns each game took
![alt text](https://github.com/jayeml/1-Million-Games-of-War/blob/main/graph%20pictures/Turns.png)

Histogram of the amount of war in each game
![alt text](https://github.com/jayeml/1-Million-Games-of-War/blob/main/graph%20pictures/Wars.png)

Scatter plot that shows how much more likely a player is to win a game with a higher starting hand
![alt text](https://github.com/jayeml/1-Million-Games-of-War/blob/main/graph%20pictures/Unfiltered%20Scattered.png)

Same graph with noise removed
![alt text](https://github.com/jayeml/1-Million-Games-of-War/blob/main/graph%20pictures/Filtered%20Scattered.png)

Line graphs that shows the mean game length for each starting hand difference
![alt text](https://github.com/jayeml/1-Million-Games-of-War/blob/main/graph%20pictures/Unfiltered%20Line.png)

Same graph with noise removed
![alt text](https://github.com/jayeml/1-Million-Games-of-War/blob/main/graph%20pictures/Filtered%20Line.png)

