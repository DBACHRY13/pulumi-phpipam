# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 app_id: Optional[pulumi.Input[str]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 nest_custom_fields: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] app_id: The application ID required for API requests
        :param pulumi.Input[str] endpoint: The full URL (plus path) to the API endpoint
        :param pulumi.Input[bool] insecure: Whether server should be accessed without verifying the TLS certificate.
        :param pulumi.Input[bool] nest_custom_fields: Whether the API client is configured to nest custom values.
        :param pulumi.Input[str] password: The password of the PHPIPAM account
        :param pulumi.Input[str] username: The username of the PHPIPAM account
        """
        if app_id is not None:
            pulumi.set(__self__, "app_id", app_id)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if insecure is not None:
            pulumi.set(__self__, "insecure", insecure)
        if nest_custom_fields is not None:
            pulumi.set(__self__, "nest_custom_fields", nest_custom_fields)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[str]]:
        """
        The application ID required for API requests
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The full URL (plus path) to the API endpoint
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter
    def insecure(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether server should be accessed without verifying the TLS certificate.
        """
        return pulumi.get(self, "insecure")

    @insecure.setter
    def insecure(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "insecure", value)

    @property
    @pulumi.getter(name="nestCustomFields")
    def nest_custom_fields(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the API client is configured to nest custom values.
        """
        return pulumi.get(self, "nest_custom_fields")

    @nest_custom_fields.setter
    def nest_custom_fields(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "nest_custom_fields", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the PHPIPAM account
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        The username of the PHPIPAM account
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 nest_custom_fields: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the phpipam package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_id: The application ID required for API requests
        :param pulumi.Input[str] endpoint: The full URL (plus path) to the API endpoint
        :param pulumi.Input[bool] insecure: Whether server should be accessed without verifying the TLS certificate.
        :param pulumi.Input[bool] nest_custom_fields: Whether the API client is configured to nest custom values.
        :param pulumi.Input[str] password: The password of the PHPIPAM account
        :param pulumi.Input[str] username: The username of the PHPIPAM account
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the phpipam package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 nest_custom_fields: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["app_id"] = app_id
            __props__.__dict__["endpoint"] = endpoint
            __props__.__dict__["insecure"] = pulumi.Output.from_input(insecure).apply(pulumi.runtime.to_json) if insecure is not None else None
            __props__.__dict__["nest_custom_fields"] = pulumi.Output.from_input(nest_custom_fields).apply(pulumi.runtime.to_json) if nest_custom_fields is not None else None
            __props__.__dict__["password"] = password
            __props__.__dict__["username"] = username
        super(Provider, __self__).__init__(
            'phpipam',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[Optional[str]]:
        """
        The application ID required for API requests
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[Optional[str]]:
        """
        The full URL (plus path) to the API endpoint
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        The password of the PHPIPAM account
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[Optional[str]]:
        """
        The username of the PHPIPAM account
        """
        return pulumi.get(self, "username")
