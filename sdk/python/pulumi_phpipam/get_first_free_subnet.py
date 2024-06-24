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
    'GetFirstFreeSubnetResult',
    'AwaitableGetFirstFreeSubnetResult',
    'get_first_free_subnet',
    'get_first_free_subnet_output',
]

@pulumi.output_type
class GetFirstFreeSubnetResult:
    """
    A collection of values returned by getFirstFreeSubnet.
    """
    def __init__(__self__, id=None, ip_address=None, subnet_id=None, subnet_mask=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_address and not isinstance(ip_address, str):
            raise TypeError("Expected argument 'ip_address' to be a str")
        pulumi.set(__self__, "ip_address", ip_address)
        if subnet_id and not isinstance(subnet_id, int):
            raise TypeError("Expected argument 'subnet_id' to be a int")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if subnet_mask and not isinstance(subnet_mask, int):
            raise TypeError("Expected argument 'subnet_mask' to be a int")
        pulumi.set(__self__, "subnet_mask", subnet_mask)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        """
        The next available IP address.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> int:
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="subnetMask")
    def subnet_mask(self) -> int:
        return pulumi.get(self, "subnet_mask")


class AwaitableGetFirstFreeSubnetResult(GetFirstFreeSubnetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFirstFreeSubnetResult(
            id=self.id,
            ip_address=self.ip_address,
            subnet_id=self.subnet_id,
            subnet_mask=self.subnet_mask)


def get_first_free_subnet(subnet_id: Optional[int] = None,
                          subnet_mask: Optional[int] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFirstFreeSubnetResult:
    """
    Use this data source to access information about an existing resource.

    :param int subnet_id: The ID of the subnet to look up the subnet in.
    :param int subnet_mask: Mask that will be used to look next available subnet
    """
    __args__ = dict()
    __args__['subnetId'] = subnet_id
    __args__['subnetMask'] = subnet_mask
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('phpipam:index/getFirstFreeSubnet:getFirstFreeSubnet', __args__, opts=opts, typ=GetFirstFreeSubnetResult).value

    return AwaitableGetFirstFreeSubnetResult(
        id=pulumi.get(__ret__, 'id'),
        ip_address=pulumi.get(__ret__, 'ip_address'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        subnet_mask=pulumi.get(__ret__, 'subnet_mask'))


@_utilities.lift_output_func(get_first_free_subnet)
def get_first_free_subnet_output(subnet_id: Optional[pulumi.Input[int]] = None,
                                 subnet_mask: Optional[pulumi.Input[int]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFirstFreeSubnetResult]:
    """
    Use this data source to access information about an existing resource.

    :param int subnet_id: The ID of the subnet to look up the subnet in.
    :param int subnet_mask: Mask that will be used to look next available subnet
    """
    ...