#!/usr/bin/env python
# 
# tournament makes use of a Swiss-system 
#

import psycopg2
import bleach

def connect():
    """to connect to the tournament database"""
    return psycopg2.connect("dbname=tournament_game")


def deleteMatches():
    """this is to remove all match records from the database"""
    connection = connect()
    cursor = connection.cursor()
    sqlquery = "DELETE FROM match"
    cursor.execute(sqlquery)
    connection.commit()
    connection.close()


def deletegamers():
    """this is to remove the gamer records from the database."""
    connection = connect()
    cursor = connection.cursor()
    sqlquery = "DELETE FROM gamer"
    cursor.execute(sqlquery)
    connection.commit()
    connection.close()


def countgamers():
    """this is to display the number of registered gamers."""
    connection = connect()
    cursor = connection.cursor()
    sqlquery = "SELECT COUNT(*) FROM gamer"
    cursor.execute(sqlquery)
    count = cursor.fetchone()[0]
    connection.close()
    return count


def registergamer(name):
    """this adds a new gamer to the tournament database.
    NB : The database assigns a unique serial id number for the gamer. 
    """

    connection = connect()
    cursor = connection.cursor()
    bleached_name = bleach.clean(name, strip=True)
    cursor.execute("insert into gamer (gamer_name) values (%s)", (bleached_name,))
    connection.commit()
    connection.close()


def gamerslots():
    """this returns a list of gamers and their win records in a sorted manner.

    The first entry in the list should be the gamer in first place, or a gamer
    tied for first place if there is currently a tie.

    this will give:
        id: the gamer's unique id (assigned by the database)
        name: the gamer's full name (as registered)
        wins: the number of matches the gamer has won
        matches: the number of matches the gamer has played
    """
    connection = connect()
    cursor = connection.cursor()
    sqlquery = "SELECT * FROM slots;"
    cursor.execute(sqlquery)
    outcome = cursor.fetchall()
    # If the top two outcome have more than 0 wins AND are equal then reorder them
    # by total wins divided by total games played
    if (outcome[0][2] != 0) and (outcome[0][2] == outcome[1][2]):
        sqlquery = "SELECT gamer_id, gamer_name, wonplayer, played " \
                "FROM slots ORDER BY (cast(wonplayer AS DECIMAL)/played)  DESC;"
        cursor.execute(sqlquery)
        outcome = cursor.fetchall()
    connection.close()

    return outcome


def reportMatch(winplayer, loseplayer):
    """Records the outcome of a single match between two gamers.

    method parameters:
      winner: this is the id number of the gamer who won
      loser:  this is the id number of the gamer who lost
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO match (winplayer, loseplayer) VALUES (%s, %s)", (winplayer, loseplayer,))
    connection.commit()
    connection.close()


def swissPairings():
    """ this is to create a list of pairs of gamers for the next round of a match.

    below is what is returned :
        id1: the first gamer's unique id
        name1: the first gamer's name
        id2: the second gamer's unique id
        name2: the second gamer's name
    """

    connection = connect()
    cursor = connection.cursor()
    sqlquery = "SELECT * FROM slots"
    cursor.execute(sqlquery)
    outcome = cursor.fetchall()
    pairings = []
    count = len(outcome)

    for x in range(0, count - 1, 2):
        paired_list = (outcome[x][0], outcome[x][1], outcome[x + 1][0], outcome[x + 1][1])
        pairings.append(paired_list)

    connection.close()
    return pairings

