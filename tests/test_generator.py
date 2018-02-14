import unittest
import bird_on_a_wire


def test_instantiate():
    obj = bird_on_a_wire.Session()
    assert obj


def test_update_quote():
    obj = bird_on_a_wire.Session()
    obj.update_quote()
    assert obj.current_quote

