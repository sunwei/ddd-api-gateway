# -*- coding: utf-8 -*-
"""Test ApiGW"""
import pytest
from ddd_api_gateway.apigw_factory import create_api_gw
from ddd_api_gateway.api_repository import ApiRepository


@pytest.mark.usefixtures("api_gw_json_data")
def test_find_api_by_id(api_gw_json_data):
    api_gw_instance = create_api_gw("json", data=api_gw_json_data)
    repository = ApiRepository(apis=api_gw_instance.apis)
    first_api = repository.apis[0]
    assert repository.find(first_api.id) is first_api


@pytest.mark.usefixtures("api_gw_json_data")
def test_find_api_by_name(api_gw_json_data):
    api_gw_instance = create_api_gw("json", data=api_gw_json_data)
    repository = ApiRepository(apis=api_gw_instance.apis)
    first_api = repository.apis[0]
    assert repository.find_by_name(first_api.name) is first_api


@pytest.mark.usefixtures("api_gw_json_data")
def test_find_all_apis(api_gw_json_data):
    api_gw_instance = create_api_gw("json", data=api_gw_json_data)
    repository = ApiRepository(apis=api_gw_instance.apis)
    assert repository.find_all() is repository.apis
