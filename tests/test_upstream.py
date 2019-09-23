# -*- coding: utf-8 -*-
"""Test ApiGW"""
from ddd_api_gateway.upstream import Upstream

_endpoints = [
    "api1.com",
    "api2.com",
    "api3.com"
]

_endpoints2 = [
    "http://api1.com",
    "api2.com",
    "api3.com"
]


def test_create_api():
    upstream_test = Upstream("name", _endpoints)

    assert upstream_test.name is "name"
    assert upstream_test.endpoints is _endpoints
    assert upstream_test.id is not None


def test_api_clone():
    upstream_test = Upstream("name", _endpoints)
    clone_api = upstream_test.clone(name="anotherName")

    assert clone_api.name is "anotherName"
    assert upstream_test.endpoints is _endpoints
    assert clone_api.id is not upstream_test.id


def test_hostname():
    upstream_test = Upstream("name", _endpoints)
    upstream_test2 = Upstream("name", _endpoints)
    upstream_test3 = Upstream("name", [])
    assert upstream_test.host == "api1.com"
    assert upstream_test2.host == "api1.com"
    assert upstream_test3.host == ""
