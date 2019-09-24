# -*- coding: utf-8 -*-
"""Test ApiGW"""
from ddd_api_gateway.route_specification import RouteSpecification

_test_route_specification = {
    "apiRef": "Warehouse Inventory",
    "upstreamRef": "Inventory",
    "tls": 'on',
    "policies": {
        "authentication": {
            "type": "Basic"
        }
    }
}


def test_create_route_specification():
    a_route_specification = RouteSpecification(
        api_ref=_test_route_specification["apiRef"],
        upstream_ref=_test_route_specification["upstreamRef"],
        policies=_test_route_specification["policies"],
        tls=_test_route_specification["tls"]
    )

    assert a_route_specification.api_ref is _test_route_specification["apiRef"]
    assert a_route_specification.upstream_ref is _test_route_specification["upstreamRef"]
    assert a_route_specification.policies is _test_route_specification["policies"]
    assert a_route_specification.tls is _test_route_specification["tls"]
    assert a_route_specification.ssl is True


def test_compare_route_specification():
    a_route_specification = RouteSpecification(
        api_ref=_test_route_specification["apiRef"],
        upstream_ref=_test_route_specification["upstreamRef"],
        policies=_test_route_specification["policies"],
        tls=_test_route_specification["tls"]
    )

    b_route_specification = RouteSpecification(
        api_ref=_test_route_specification["apiRef"],
        upstream_ref=_test_route_specification["upstreamRef"],
        policies=_test_route_specification["policies"],
        tls=_test_route_specification["tls"]
    )

    assert a_route_specification.same_as(b_route_specification) is True
