#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    query = "DELETE FROM matches"
    c.execute(query)
    DB.commit()
    DB.close()

def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    query = "DELETE FROM players"
    c.execute(query)
    DB.commit()
    DB.close()

def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    query = "SELECT count(*) as num FROM players"
    c.execute(query)
    num = c.fetchone()[0]
    DB.close()
    return num

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    query = "INSERT INTO players values (%s)"
    c.execute(query, (name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    query = """SELECT
                    players.id, players.name,
                    count( CASE WHEN matches.winner = players.id
                                THEN 1
                                ELSE NULL
                            END
                         ) as wins,
                    count( CASE WHEN matches.winner = players.id
                            OR matches.loser = players.id
                                THEN 1
                                ELSE NULL
                            END
                         ) as loss
                FROM
                    players LEFT JOIN matches
                    ON matches.winner = players.id
                        OR matches.loser = players.id
                GROUP BY players.id
            """
    c.execute(query)
    num = c.fetchall()
    DB.close()
    return num


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    # First insert the match data in db
    query = "INSERT INTO matches VAlUES (%i, %i)"
    c.execute(query % (winner, loser))
    DB.commit()
    DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = connect()
    c = DB.cursor()
    query = """ SELECT
                    subq.id, subq.name
                FROM
                  ( SELECT
                        players.id, players.name,
                        count( CASE WHEN matches.winner = players.id
                                THEN 1
                                ELSE NULL
                                END
                             ) as wins
                    FROM
                        players LEFT JOIN matches
                            ON matches.winner = players.id
                    GROUP BY
                        players.id
                    ORDER BY
                        wins
                  ) as subq
            """
    c.execute(query)
    num = c.fetchall()
    # The query returns a list of (name, id) tuples ordered by number
    # of wins. We therefore iterate the list to create swiss pairs
    tl = []
    for i in range(0, len(num)/2):
        i = i*2
        t = (num[i][0], num[i][1], num[i+1][0], num[i+1][1])
        tl.append(t)
    DB.close()
    return tl
