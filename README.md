# Tournament_Udacity
The project have a database schema for data storage necessary to run a simple Swiss pairing tournament.

Tournament Results Project
***************************************************************************************************************************************

## Overview

The project have a database schema for data storage necessary to run a simple Swiss pairing tournament.

## python modules

include modules to add players, report games played, rank players and create player match ups.

## Requirements

[PostgreSQL](http://www.postgresql.org/) and [Python](https://www.python.org/) must be installed to use this code.

## Installation

### 1. Data structure/storage set up

When you are done downloading data to your PC, type the following in the terminal for the project to set up the database schema:

*NB: This will overwrite any previous database you have on your PC named, "tournament," so run with care.*

```
psql -f tournament.sql
```

### 2. Run the tests

There is a set of tests in the project to make sure the code is working perfectly. From the project directory type the following command to run the test suite:

```
python tournament_test.py
```

If everything is set up correctly, you should see the following result:

```
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
```

## How to use this project

Run this program from within a python prompt, using the following commands:

```
from tournament import *
```

### Reset tournament data

To delete matches tournament data, run:

```
deleteMatches()
```
To delete players tournament data, run:
```
deletePlayers()
```

### Register new players

To register new players run `registerPlayer(name)`.

**Example:** Registering a player named Tunde Lemo
```
registerPlayer('Tunde Lemo')
```

### Creating match ups

Make use of the `swissPairings()` function to create a list of match ups for a round of the tournament, which will return an list of match ups containing the unique id of each player and name.

If an odd number of players exist, one will be assigned a bye.

### Reporting matches

To report the results of a match, use `reportMatch(winner, loser)`, where winner and loser are the unique ids of the winner and loser of the match, respectively.

**Example:** Rose, whose ID is 17, beats Kennedy, whose ID is 15.
```
reportMatch(17, 15)
```

To report the results of player who had been assigned a bye, use `reportMatch()` with that player listed as the winner and `None` listed as the loser.

**Example:** Reporting a bye to a player whose player ID is 29.
```
reportMatch(29, None)
```

### Get current standings

To return a list of current standings, based on number of wins, use the `playerStandings()` function.
