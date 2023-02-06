#! /usr/bin/python3

import shapes



# The tests will use this set to detect unexpected aliasing.  Some aliasing is
# expected and required, of course - but spurious aliasing is always an error!

ids = set()



def test_alpha():
    print("Testing shape_alpha()")

    val = shapes.shape_alpha()

    if val[0] != [10,"abc","jkl",40]:
        print("ERROR: Invalid contents")
        return

    if val[1][0] != [1.1,-17]:
        print("ERROR: Invalid contents")
        return

    if val[1][1] != [123,456]:
        print("ERROR: Invalid contents")
        return

    ids = set()
    ids.add(id(val))

    if id(val[0]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[0]))

    if id(val[1]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[1]))

    if id(val[1][1]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[1][1]))

    print("OK")



def test_bravo():
    print("Testing shape_bravo()")

    val = shapes.shape_bravo()

    if val[0][0] != ["whoa","excellent"]:
        print("ERROR: Invalid contents")
        return

    if val[0][1] != ["bogus","righteous"]:
        print("ERROR: Invalid contents")
        return

    if val[1][1] != "rufus":
        print("ERROR: Invalid contents")
        return

    ids = set()
    ids.add(id(val))

    if id(val[0]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[0]))

    if id(val[0][0]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[0][0]))

    if id(val[0][1]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[0][1]))

    if id(val[1]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[1]))

    if val[0][1] is not val[1][0]:
        print("ERROR: Failed aliasing.  retval[0][1] and "+
                                       "retval[1][0] should be aliases.")
        return

    print("OK")



def test_charlie(arg1):
    print("Testing shape_charlie() arg1=<hidden>")

    val = shapes.shape_charlie(arg1)

    if (val         [1] is not arg1 or
        val      [0][1] is not arg1 or
        val   [0][0][1] is not arg1 or
        val[0][0][0][0] is not None or
        val[0][0][0][1] is not arg1):

        print("ERROR: Invalid contents")
        return

    ids = set()
    ids.add(id(val))

    if id(val[0]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[0]))

    if id(val[0][0]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[0][0]))

    if id(val[0][0][0]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[0][0][0]))

    print("OK")



def test_delta(arg1,arg2):
    print("Testing shape_delta() arg1=<hidden> arg2=<hidden>")

    val = shapes.shape_delta(arg1,arg2)

    if (val[0]          is not arg1 or
        val[1]          is not arg2 or
        val[2][0]       is not arg1 or
        val[2][1][0]    is not arg1 or
        val[2][1][1]    is not arg2 or
        val[2][1][2][0] is not arg1 or
        val[2][1][2][1] is not arg2 or
        val[2][1][3]      !=   [30] or
        val[2][2]         !=   [20] or
        val[2][3]       is not arg2 or
        val[3]            !=   [10]):

        print("ERROR: Invalid contents")
        return

    ids = set()
    ids.add(id(val))

    if id(val[2]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[2]))

    if id(val[2][1]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[2][1]))

    if id(val[2][1][2]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[2][1][2]))

    if id(val[2][1][3]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[2][1][3]))

    if id(val[2][2]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[2][2]))

    if id(val[3]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[3]))

    print("OK")



def test_echo(arg1,arg2,arg3):
    print("Testing shape_echo() arg1=<hidden> arg2=<hidden> arg3=<hidden>")

    val = shapes.shape_echo(arg1,arg2,arg3)

    if (val[1]       is not arg1 or
        val[0][1]    is not arg2 or
        val[0][0][1] is not arg3):

        print("ERROR: Invalid contents")
        return

    ids = set()
    ids.add(id(val))

    if id(val[0]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[0]))

    if id(val[0][0]) in ids:
        print("ERROR: Unexpected aliasing")
        return
    ids.add(id(val[0][0]))

    if val[0][0][0] is not val:
        print("ERROR: Failed aliasing.  retval[0][0][0] and "+
                                       "retval should be aliases.")
        return

    print("OK")



test_alpha()
test_bravo()
test_charlie(10)
test_charlie("asdf")
test_charlie([1,2,3])
test_charlie(-1.7)
test_delta("A1", "A2")
test_delta(1,2)
test_delta([1,2],[3,4])
test_delta(shapes.shape_alpha(), shapes.shape_bravo())
test_echo("foo","bar","baz")
test_echo(-1,0,1)
test_echo("first","second","third")

