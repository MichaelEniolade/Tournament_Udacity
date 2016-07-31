#!/usr/bin/env python
#
# Test cases for tournament.py

from tournament import *

def testDeleteMatches():
    deleteMatches()
    print "1. Delete Old matches."


def testDelete():
    deleteMatches()
    deletegamers()
    print "2. Delete gamer records."


def testCount():
    deleteMatches()
    deletegamers()
    k = countgamers()
    if k == '0':
        raise TypeError(
            "countgamers() should return numeric zero, not string '0'.")
    if k != 0:
        raise ValueError("After deleting, countgamers should return zero.")
    print "3. After deleting, countgamers() returns zero."


def testRegister():
    deleteMatches()
    deletegamers()
    registergamer("Michael Eniolade")
    k = countgamers()
    if k != 1:
        raise ValueError(
            "After one gamer registers, countgamers() should be 1.")
    print "4. After registering a gamer, countgamers() returns 1."


def testRegisterCountDelete():
    deleteMatches()
    deletegamers()
    registergamer("Tope Ajayi")
    registergamer("Titi Malove")
    registergamer("Jumoke Moses")
    registergamer("Abigail Violet")
    k = countgamers()
    if k != 4:
        raise ValueError(
            "After registering four gamers, countgamers should be 4.")
    deletegamers()
    k = countgamers()
    if k != 0:
        raise ValueError("After deleting, countgamers should return zero.")
    print "5. gamers can be registered and deleted."


def testslotsBeforeMatches():
    deleteMatches()
    deletegamers()
    registergamer("Albert Abraham")
    registergamer("Ezekiel Malone")
    slots = gamerslots()
    if len(slots) < 2:
        raise ValueError("gamers should appear in gamerslots even before "
                         "they have played any matches.")
    elif len(slots) > 2:
        raise ValueError("Only registered gamers should appear in slots.")
    if len(slots[0]) != 4:
        raise ValueError("Each gamerslots row should have four columns.")
    [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = slots
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        raise ValueError(
            "Newly registered gamers should have no matches or wins.")
    if set([name1, name2]) != set(["Albert Abraham", "Ezekiel Malone"]):
        raise ValueError("Registered gamers' names should appear in slots, "
                         "even if they have no matches played.")
    print "6. Newly registered gamers appear in the slots with no matches."


def testReportMatches():
    deleteMatches()
    deletegamers()
    registergamer("Kiki Lion")
    registergamer("Jennifer Williams")
    registergamer("Gates Lake")
    registergamer("John Lake")
    slots = gamerslots()
    [id1, id2, id3, id4] = [row[0] for row in slots]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    slots = gamerslots()
    for (c, n, i, m) in slots:
        if m != 1:
            raise ValueError("Each gamer should have one match recorded.")
        if c in (id1, id3) and i != 1:
            raise ValueError("Each match winner should have one win recorded.")
        elif c in (id2, id4) and i != 0:
            raise ValueError("Each match loser should have zero wins recorded.")
    print "7. After a match, gamers have updated slots."


def testPairings():
    deleteMatches()
    deletegamers()
    registergamer("Augustus Caezar")
    registergamer("Apple Tom")
    registergamer("Jack Jim")
    registergamer("Khan Ham")
    slots = gamerslots()
    [id1, id2, id3, id4] = [row[0] for row in slots]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    pairings = swissPairings()
    if len(pairings) != 2:
        raise ValueError(
            "For four gamers, swissPairings should return two pairs.")
    [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairings
    correct_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4])])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After one match, gamers with one win should be paired.")
    print "8. After one match, gamers with one win are paired."


if __name__ == '__main__':
    testDeleteMatches()
    testDelete()
    testCount()
    testRegister()
    testRegisterCountDelete()
    testslotsBeforeMatches()
    testReportMatches()
    testPairings()
    print "Success!  All tests pass!"


