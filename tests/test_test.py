#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""py.test
pip install -U pytest
"""
import pytest

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

def test_file(tmpdir):
    print tmpdir
    assert 0

class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, '__doc__')
