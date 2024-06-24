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
    'GetAddressResult',
    'AwaitableGetAddressResult',
    'get_address',
    'get_address_output',
]

@pulumi.output_type
class GetAddressResult:
    """
    A collection of values returned by getAddress.
    """
    def __init__(__self__, address_id=None, custom_field_filter=None, custom_fields=None, description=None, device_id=None, edit_date=None, exclude_ping=None, hostname=None, id=None, ip_address=None, is_gateway=None, last_seen=None, mac_address=None, note=None, owner=None, ptr_record_id=None, skip_ptr_record=None, state_tag_id=None, subnet_id=None, switch_port_label=None):
        if address_id and not isinstance(address_id, int):
            raise TypeError("Expected argument 'address_id' to be a int")
        pulumi.set(__self__, "address_id", address_id)
        if custom_field_filter and not isinstance(custom_field_filter, dict):
            raise TypeError("Expected argument 'custom_field_filter' to be a dict")
        pulumi.set(__self__, "custom_field_filter", custom_field_filter)
        if custom_fields and not isinstance(custom_fields, dict):
            raise TypeError("Expected argument 'custom_fields' to be a dict")
        pulumi.set(__self__, "custom_fields", custom_fields)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if device_id and not isinstance(device_id, int):
            raise TypeError("Expected argument 'device_id' to be a int")
        pulumi.set(__self__, "device_id", device_id)
        if edit_date and not isinstance(edit_date, str):
            raise TypeError("Expected argument 'edit_date' to be a str")
        pulumi.set(__self__, "edit_date", edit_date)
        if exclude_ping and not isinstance(exclude_ping, bool):
            raise TypeError("Expected argument 'exclude_ping' to be a bool")
        pulumi.set(__self__, "exclude_ping", exclude_ping)
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_address and not isinstance(ip_address, str):
            raise TypeError("Expected argument 'ip_address' to be a str")
        pulumi.set(__self__, "ip_address", ip_address)
        if is_gateway and not isinstance(is_gateway, bool):
            raise TypeError("Expected argument 'is_gateway' to be a bool")
        pulumi.set(__self__, "is_gateway", is_gateway)
        if last_seen and not isinstance(last_seen, str):
            raise TypeError("Expected argument 'last_seen' to be a str")
        pulumi.set(__self__, "last_seen", last_seen)
        if mac_address and not isinstance(mac_address, str):
            raise TypeError("Expected argument 'mac_address' to be a str")
        pulumi.set(__self__, "mac_address", mac_address)
        if note and not isinstance(note, str):
            raise TypeError("Expected argument 'note' to be a str")
        pulumi.set(__self__, "note", note)
        if owner and not isinstance(owner, str):
            raise TypeError("Expected argument 'owner' to be a str")
        pulumi.set(__self__, "owner", owner)
        if ptr_record_id and not isinstance(ptr_record_id, int):
            raise TypeError("Expected argument 'ptr_record_id' to be a int")
        pulumi.set(__self__, "ptr_record_id", ptr_record_id)
        if skip_ptr_record and not isinstance(skip_ptr_record, bool):
            raise TypeError("Expected argument 'skip_ptr_record' to be a bool")
        pulumi.set(__self__, "skip_ptr_record", skip_ptr_record)
        if state_tag_id and not isinstance(state_tag_id, int):
            raise TypeError("Expected argument 'state_tag_id' to be a int")
        pulumi.set(__self__, "state_tag_id", state_tag_id)
        if subnet_id and not isinstance(subnet_id, int):
            raise TypeError("Expected argument 'subnet_id' to be a int")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if switch_port_label and not isinstance(switch_port_label, str):
            raise TypeError("Expected argument 'switch_port_label' to be a str")
        pulumi.set(__self__, "switch_port_label", switch_port_label)

    @property
    @pulumi.getter(name="addressId")
    def address_id(self) -> int:
        """
        The ID of the IP address in the PHPIPAM database.
        """
        return pulumi.get(self, "address_id")

    @property
    @pulumi.getter(name="customFieldFilter")
    def custom_field_filter(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "custom_field_filter")

    @property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> Mapping[str, Any]:
        """
        A key/value map of custom fields for this address.
        """
        return pulumi.get(self, "custom_fields")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description provided to this IP address.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> int:
        """
        The ID of the associated device in the PHPIPAM database.
        """
        return pulumi.get(self, "device_id")

    @property
    @pulumi.getter(name="editDate")
    def edit_date(self) -> str:
        """
        The last time this resource was modified.
        """
        return pulumi.get(self, "edit_date")

    @property
    @pulumi.getter(name="excludePing")
    def exclude_ping(self) -> bool:
        """
        `true` if this address is excluded from ping probes.
        """
        return pulumi.get(self, "exclude_ping")

    @property
    @pulumi.getter
    def hostname(self) -> str:
        """
        The hostname supplied to this IP address.
        """
        return pulumi.get(self, "hostname")

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
        the IP address.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="isGateway")
    def is_gateway(self) -> bool:
        """
        `true` if this IP address has been designated as a gateway.
        """
        return pulumi.get(self, "is_gateway")

    @property
    @pulumi.getter(name="lastSeen")
    def last_seen(self) -> str:
        """
        The last time this IP address answered ping probes.
        """
        return pulumi.get(self, "last_seen")

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> str:
        """
        The MAC address provided to this IP address.
        """
        return pulumi.get(self, "mac_address")

    @property
    @pulumi.getter
    def note(self) -> str:
        """
        The note supplied to this IP address.
        """
        return pulumi.get(self, "note")

    @property
    @pulumi.getter
    def owner(self) -> str:
        """
        The owner name provided to this IP address.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="ptrRecordId")
    def ptr_record_id(self) -> int:
        """
        The ID of the associated PTR record in the PHPIPAM
        database.
        """
        return pulumi.get(self, "ptr_record_id")

    @property
    @pulumi.getter(name="skipPtrRecord")
    def skip_ptr_record(self) -> bool:
        """
        `true` if PTR records are not being created for this IP
        address.
        """
        return pulumi.get(self, "skip_ptr_record")

    @property
    @pulumi.getter(name="stateTagId")
    def state_tag_id(self) -> int:
        """
        The tag ID in the database for the IP address' specific
        state. **NOTE:** This is currently represented as an integer but may change
        to the specific string representation at a later time.
        """
        return pulumi.get(self, "state_tag_id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> int:
        """
        The database ID of the subnet this IP address belongs to.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="switchPortLabel")
    def switch_port_label(self) -> str:
        """
        A string port label that is associated with this
        address.
        """
        return pulumi.get(self, "switch_port_label")


class AwaitableGetAddressResult(GetAddressResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAddressResult(
            address_id=self.address_id,
            custom_field_filter=self.custom_field_filter,
            custom_fields=self.custom_fields,
            description=self.description,
            device_id=self.device_id,
            edit_date=self.edit_date,
            exclude_ping=self.exclude_ping,
            hostname=self.hostname,
            id=self.id,
            ip_address=self.ip_address,
            is_gateway=self.is_gateway,
            last_seen=self.last_seen,
            mac_address=self.mac_address,
            note=self.note,
            owner=self.owner,
            ptr_record_id=self.ptr_record_id,
            skip_ptr_record=self.skip_ptr_record,
            state_tag_id=self.state_tag_id,
            subnet_id=self.subnet_id,
            switch_port_label=self.switch_port_label)


def get_address(address_id: Optional[int] = None,
                custom_field_filter: Optional[Mapping[str, Any]] = None,
                description: Optional[str] = None,
                hostname: Optional[str] = None,
                ip_address: Optional[str] = None,
                subnet_id: Optional[int] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAddressResult:
    """
    ## # Address

    The `Address` data source allows one to get information about a specific
    IP address within PHPIPAM. Use this address to get general information about a
    specific IP address such as its host name, description and more.

    Lookups for IP addresses can only happen at this time via its entry in the
    database, or the IP address itself. Future versions of this resource, when such
    features become generally available in the PHPIPAM API, will allow lookup based
    on host name, allowing for better ability for this resource to discover IP
    addresses that have been pre-assigned for a specific resource.

    **Example:**

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_phpipam as phpipam

    address = phpipam.get_address(ip_address="10.10.1.1")
    pulumi.export("addressDescription", address.description)
    ```
    <!--End PulumiCodeChooser -->

    **Example With `subnet_id` when multiple subnets share the same ip ranges :**

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_phpipam as phpipam

    address = phpipam.get_address(ip_address="10.10.1.1",
        subnet_id=3)
    pulumi.export("addressDescription", address.description)
    ```
    <!--End PulumiCodeChooser -->

    **Example With `description`:**

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_phpipam as phpipam

    address = phpipam.get_address(subnet_id=3,
        description="Customer 1")
    pulumi.export("addressDescription", address.description)
    ```
    <!--End PulumiCodeChooser -->

    **Example With `custom_field_filter`:**


    :param Mapping[str, Any] custom_field_filter: A map of custom fields to search for. The filter
           values are regular expressions that follow the RE2 syntax for which you can
           find documentation [here](https://github.com/google/re2/wiki/Syntax). All
           fields need to match for the match to succeed.
           
           ⚠️ **NOTE:** `description`, `hostname`, and `custom_field_filter` fields return
           the first match found without any warnings. If you are looking to return
           multiple addresses, combine this data source with the
           `get_addresses` data source.
           
           ⚠️ **NOTE:** An empty or unspecified `custom_field_filter` value is the
           equivalent to a regular expression that matches everything, and hence will
           return the first address it sees in the subnet. Custom fileds must contain mandatory
           prefix `custom_`.
           
           Arguments are processed in the following order of precedence:
    :param str description: The description of the IP address. `subnet_id` is required
           when using this field.
    :param str hostname: The host name of the IP address. `subnet_id` is required when
           using this field.
    :param int subnet_id: , and either one of `description`, `hostname`, or
           `custom_field_filter`
    """
    __args__ = dict()
    __args__['addressId'] = address_id
    __args__['customFieldFilter'] = custom_field_filter
    __args__['description'] = description
    __args__['hostname'] = hostname
    __args__['ipAddress'] = ip_address
    __args__['subnetId'] = subnet_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('phpipam:index/getAddress:getAddress', __args__, opts=opts, typ=GetAddressResult).value

    return AwaitableGetAddressResult(
        address_id=pulumi.get(__ret__, 'address_id'),
        custom_field_filter=pulumi.get(__ret__, 'custom_field_filter'),
        custom_fields=pulumi.get(__ret__, 'custom_fields'),
        description=pulumi.get(__ret__, 'description'),
        device_id=pulumi.get(__ret__, 'device_id'),
        edit_date=pulumi.get(__ret__, 'edit_date'),
        exclude_ping=pulumi.get(__ret__, 'exclude_ping'),
        hostname=pulumi.get(__ret__, 'hostname'),
        id=pulumi.get(__ret__, 'id'),
        ip_address=pulumi.get(__ret__, 'ip_address'),
        is_gateway=pulumi.get(__ret__, 'is_gateway'),
        last_seen=pulumi.get(__ret__, 'last_seen'),
        mac_address=pulumi.get(__ret__, 'mac_address'),
        note=pulumi.get(__ret__, 'note'),
        owner=pulumi.get(__ret__, 'owner'),
        ptr_record_id=pulumi.get(__ret__, 'ptr_record_id'),
        skip_ptr_record=pulumi.get(__ret__, 'skip_ptr_record'),
        state_tag_id=pulumi.get(__ret__, 'state_tag_id'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        switch_port_label=pulumi.get(__ret__, 'switch_port_label'))


@_utilities.lift_output_func(get_address)
def get_address_output(address_id: Optional[pulumi.Input[Optional[int]]] = None,
                       custom_field_filter: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                       description: Optional[pulumi.Input[Optional[str]]] = None,
                       hostname: Optional[pulumi.Input[Optional[str]]] = None,
                       ip_address: Optional[pulumi.Input[Optional[str]]] = None,
                       subnet_id: Optional[pulumi.Input[Optional[int]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAddressResult]:
    """
    ## # Address

    The `Address` data source allows one to get information about a specific
    IP address within PHPIPAM. Use this address to get general information about a
    specific IP address such as its host name, description and more.

    Lookups for IP addresses can only happen at this time via its entry in the
    database, or the IP address itself. Future versions of this resource, when such
    features become generally available in the PHPIPAM API, will allow lookup based
    on host name, allowing for better ability for this resource to discover IP
    addresses that have been pre-assigned for a specific resource.

    **Example:**

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_phpipam as phpipam

    address = phpipam.get_address(ip_address="10.10.1.1")
    pulumi.export("addressDescription", address.description)
    ```
    <!--End PulumiCodeChooser -->

    **Example With `subnet_id` when multiple subnets share the same ip ranges :**

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_phpipam as phpipam

    address = phpipam.get_address(ip_address="10.10.1.1",
        subnet_id=3)
    pulumi.export("addressDescription", address.description)
    ```
    <!--End PulumiCodeChooser -->

    **Example With `description`:**

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_phpipam as phpipam

    address = phpipam.get_address(subnet_id=3,
        description="Customer 1")
    pulumi.export("addressDescription", address.description)
    ```
    <!--End PulumiCodeChooser -->

    **Example With `custom_field_filter`:**


    :param Mapping[str, Any] custom_field_filter: A map of custom fields to search for. The filter
           values are regular expressions that follow the RE2 syntax for which you can
           find documentation [here](https://github.com/google/re2/wiki/Syntax). All
           fields need to match for the match to succeed.
           
           ⚠️ **NOTE:** `description`, `hostname`, and `custom_field_filter` fields return
           the first match found without any warnings. If you are looking to return
           multiple addresses, combine this data source with the
           `get_addresses` data source.
           
           ⚠️ **NOTE:** An empty or unspecified `custom_field_filter` value is the
           equivalent to a regular expression that matches everything, and hence will
           return the first address it sees in the subnet. Custom fileds must contain mandatory
           prefix `custom_`.
           
           Arguments are processed in the following order of precedence:
    :param str description: The description of the IP address. `subnet_id` is required
           when using this field.
    :param str hostname: The host name of the IP address. `subnet_id` is required when
           using this field.
    :param int subnet_id: , and either one of `description`, `hostname`, or
           `custom_field_filter`
    """
    ...
