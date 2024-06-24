# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetAddressesResult',
    'AwaitableGetAddressesResult',
    'get_addresses',
    'get_addresses_output',
]

@pulumi.output_type
class GetAddressesResult:
    """
    A collection of values returned by getAddresses.
    """
    def __init__(__self__, address_ids=None, custom_field_filter=None, description=None, hostname=None, id=None, subnet_id=None):
        if address_ids and not isinstance(address_ids, list):
            raise TypeError("Expected argument 'address_ids' to be a list")
        pulumi.set(__self__, "address_ids", address_ids)
        if custom_field_filter and not isinstance(custom_field_filter, dict):
            raise TypeError("Expected argument 'custom_field_filter' to be a dict")
        pulumi.set(__self__, "custom_field_filter", custom_field_filter)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if subnet_id and not isinstance(subnet_id, int):
            raise TypeError("Expected argument 'subnet_id' to be a int")
        pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="addressIds")
    def address_ids(self) -> Sequence[int]:
        """
        A list of discovered IP address IDs.
        """
        return pulumi.get(self, "address_ids")

    @property
    @pulumi.getter(name="customFieldFilter")
    def custom_field_filter(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "custom_field_filter")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def hostname(self) -> Optional[str]:
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> int:
        return pulumi.get(self, "subnet_id")


class AwaitableGetAddressesResult(GetAddressesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAddressesResult(
            address_ids=self.address_ids,
            custom_field_filter=self.custom_field_filter,
            description=self.description,
            hostname=self.hostname,
            id=self.id,
            subnet_id=self.subnet_id)


def get_addresses(custom_field_filter: Optional[Mapping[str, Any]] = None,
                  description: Optional[str] = None,
                  hostname: Optional[str] = None,
                  subnet_id: Optional[int] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAddressesResult:
    """
    Use this data source to access information about an existing resource.

    :param Mapping[str, Any] custom_field_filter: A map of custom fields to search for. The filter
           values are regular expressions that follow the RE2 syntax for which you can
           find documentation [here](https://github.com/google/re2/wiki/Syntax). All
           fields need to match for the match to succeed.
           
           ⚠️  **NOTE:** An empty or unspecified `custom_field_filter` value is the
           equivalent to a regular expression that matches everything, and hence will
           return **all** addresses that contain the referenced custom field key!
           Custom fileds must contain mandatory prefix `custom_`.
    :param str description: The description of the IP address. `subnet_id` is required
           when using this field.
    :param str hostname: The host name of the IP address. `subnet_id` is required when
           using this field.
    :param int subnet_id: The ID of the subnet that the address resides in. This is
           required to search on the `description` or `hostname` fields.
           
           One of the following fields is required alongside `subnet_id`:
    """
    __args__ = dict()
    __args__['customFieldFilter'] = custom_field_filter
    __args__['description'] = description
    __args__['hostname'] = hostname
    __args__['subnetId'] = subnet_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('phpipam:index/getAddresses:getAddresses', __args__, opts=opts, typ=GetAddressesResult).value

    return AwaitableGetAddressesResult(
        address_ids=pulumi.get(__ret__, 'address_ids'),
        custom_field_filter=pulumi.get(__ret__, 'custom_field_filter'),
        description=pulumi.get(__ret__, 'description'),
        hostname=pulumi.get(__ret__, 'hostname'),
        id=pulumi.get(__ret__, 'id'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'))


@_utilities.lift_output_func(get_addresses)
def get_addresses_output(custom_field_filter: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                         description: Optional[pulumi.Input[Optional[str]]] = None,
                         hostname: Optional[pulumi.Input[Optional[str]]] = None,
                         subnet_id: Optional[pulumi.Input[int]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAddressesResult]:
    """
    Use this data source to access information about an existing resource.

    :param Mapping[str, Any] custom_field_filter: A map of custom fields to search for. The filter
           values are regular expressions that follow the RE2 syntax for which you can
           find documentation [here](https://github.com/google/re2/wiki/Syntax). All
           fields need to match for the match to succeed.
           
           ⚠️  **NOTE:** An empty or unspecified `custom_field_filter` value is the
           equivalent to a regular expression that matches everything, and hence will
           return **all** addresses that contain the referenced custom field key!
           Custom fileds must contain mandatory prefix `custom_`.
    :param str description: The description of the IP address. `subnet_id` is required
           when using this field.
    :param str hostname: The host name of the IP address. `subnet_id` is required when
           using this field.
    :param int subnet_id: The ID of the subnet that the address resides in. This is
           required to search on the `description` or `hostname` fields.
           
           One of the following fields is required alongside `subnet_id`:
    """
    ...
