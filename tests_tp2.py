from tp2 import *
import yaml
import io

def test_box_create():
    b = Box()

def test_box_add():
    b = Box()
    b.add("truc1")
    b.add("truc2")

def test_box_in():
    b = Box()
    b.add("truc1")
    b.add("truc2")

    assert "truc1" in b
    assert "truc2" in b

def test_box_remove():
    b = Box()
    b.add("truc1")
    b.remove("truc1")

    assert "truc1" not in b

def test_box_is_open():
    b = Box()

    b.open()
    assert b.is_open()

    b.close()
    assert not b.is_open()

def test_action_look():
    b = Box()

    b.add("ceci")
    b.add("cela")

    b.open()
    assert b.action_look() == "la boite contient : ceci, cela"

    b.close()
    assert b.action_look() == "la boite est fermee"

def test_thing_create():
    t = Thing(3)
    assert t.volume() == 3

def test_box_capacity():
    b = Box()

    assert b.capacity() is None

    b.set_capacity(5)

    assert b.capacity() == 5


def test_has_room_for():
    b = Box()
    t = Thing(3)

    assert b.has_room_for(t)

    b.set_capacity(3)
    assert b.has_room_for(t)

    b.set_capacity(2)
    assert not b.has_room_for(t)

def test_action_add():
    b = Box()
    t = Thing(3)
    b.close()
    assert not b.action_add(t)

    b.open()
    assert b.action_add(t)

    b.set_capacity(3)

    assert b.action_add(t)
    assert b.capacity() == 0

    assert not b.action_add(t)

def test_repr_thing():
    t = Thing(3)
    t.set_name("bidule")

    assert t.__repr__() == "bidule"

def test_has_name():
    t = Thing(3)
    t.set_name("bidule")

    assert t.has_name("bidule")
    assert not t.has_name("bidule1")

def test_find():
    b = Box()
    t = Thing(3)
    t.set_name("bidule")

    b.open()
    b.action_add(t)

    assert b.find("bidule") == t
    assert b.find("bidule1") is None

    b.close()
    assert b.find("bidule") is None
 
def test_box_from_yaml():
    text="""
    - is_open: true
      capacity: 3
    - is_open: false
      capacity: 5
    """

    stream = io.StringIO(text)
    l = yaml.load(stream)

    b1 = Box.from_yaml(l[0])
    b2 = Box.from_yaml(l[1])

    assert b1.is_open()
    assert b1.capacity() == 3
    assert not b2.is_open()
    assert b2.capacity() == 5
