# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

appId: Optional[str]
"""
The application ID required for API requests
"""

endpoint: Optional[str]
"""
The full URL (plus path) to the API endpoint
"""

insecure: Optional[bool]
"""
Whether server should be accessed without verifying the TLS certificate.
"""

nestCustomFields: Optional[bool]
"""
Whether the API client is configured to nest custom values.
"""

password: Optional[str]
"""
The password of the PHPIPAM account
"""

username: Optional[str]
"""
The username of the PHPIPAM account
"""

