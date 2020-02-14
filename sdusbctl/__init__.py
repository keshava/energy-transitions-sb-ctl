#!/usr/bin/python
#
#

# coding=utf-8
from __future__ import absolute_import
from sdusbctl.api.sdusbctl_api_extended import SDUSbCtlApi
from sdusbctl.api_client import ApiClient

api = SDUSbCtlApi(ApiClient())
api.authenticate()
