// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { AddressArgs, AddressState } from "./address";
export type Address = import("./address").Address;
export const Address: typeof import("./address").Address = null as any;
utilities.lazyLoad(exports, ["Address"], () => require("./address"));

export { FirstFreeAddressArgs, FirstFreeAddressState } from "./firstFreeAddress";
export type FirstFreeAddress = import("./firstFreeAddress").FirstFreeAddress;
export const FirstFreeAddress: typeof import("./firstFreeAddress").FirstFreeAddress = null as any;
utilities.lazyLoad(exports, ["FirstFreeAddress"], () => require("./firstFreeAddress"));

export { FirstFreeSubnetArgs, FirstFreeSubnetState } from "./firstFreeSubnet";
export type FirstFreeSubnet = import("./firstFreeSubnet").FirstFreeSubnet;
export const FirstFreeSubnet: typeof import("./firstFreeSubnet").FirstFreeSubnet = null as any;
utilities.lazyLoad(exports, ["FirstFreeSubnet"], () => require("./firstFreeSubnet"));

export { GetAddressArgs, GetAddressResult, GetAddressOutputArgs } from "./getAddress";
export const getAddress: typeof import("./getAddress").getAddress = null as any;
export const getAddressOutput: typeof import("./getAddress").getAddressOutput = null as any;
utilities.lazyLoad(exports, ["getAddress","getAddressOutput"], () => require("./getAddress"));

export { GetAddressesArgs, GetAddressesResult, GetAddressesOutputArgs } from "./getAddresses";
export const getAddresses: typeof import("./getAddresses").getAddresses = null as any;
export const getAddressesOutput: typeof import("./getAddresses").getAddressesOutput = null as any;
utilities.lazyLoad(exports, ["getAddresses","getAddressesOutput"], () => require("./getAddresses"));

export { GetFirstFreeAddressArgs, GetFirstFreeAddressResult, GetFirstFreeAddressOutputArgs } from "./getFirstFreeAddress";
export const getFirstFreeAddress: typeof import("./getFirstFreeAddress").getFirstFreeAddress = null as any;
export const getFirstFreeAddressOutput: typeof import("./getFirstFreeAddress").getFirstFreeAddressOutput = null as any;
utilities.lazyLoad(exports, ["getFirstFreeAddress","getFirstFreeAddressOutput"], () => require("./getFirstFreeAddress"));

export { GetFirstFreeSubnetArgs, GetFirstFreeSubnetResult, GetFirstFreeSubnetOutputArgs } from "./getFirstFreeSubnet";
export const getFirstFreeSubnet: typeof import("./getFirstFreeSubnet").getFirstFreeSubnet = null as any;
export const getFirstFreeSubnetOutput: typeof import("./getFirstFreeSubnet").getFirstFreeSubnetOutput = null as any;
utilities.lazyLoad(exports, ["getFirstFreeSubnet","getFirstFreeSubnetOutput"], () => require("./getFirstFreeSubnet"));

export { GetL2domainArgs, GetL2domainResult, GetL2domainOutputArgs } from "./getL2domain";
export const getL2domain: typeof import("./getL2domain").getL2domain = null as any;
export const getL2domainOutput: typeof import("./getL2domain").getL2domainOutput = null as any;
utilities.lazyLoad(exports, ["getL2domain","getL2domainOutput"], () => require("./getL2domain"));

export { GetSectionArgs, GetSectionResult, GetSectionOutputArgs } from "./getSection";
export const getSection: typeof import("./getSection").getSection = null as any;
export const getSectionOutput: typeof import("./getSection").getSectionOutput = null as any;
utilities.lazyLoad(exports, ["getSection","getSectionOutput"], () => require("./getSection"));

export { GetSubnetArgs, GetSubnetResult, GetSubnetOutputArgs } from "./getSubnet";
export const getSubnet: typeof import("./getSubnet").getSubnet = null as any;
export const getSubnetOutput: typeof import("./getSubnet").getSubnetOutput = null as any;
utilities.lazyLoad(exports, ["getSubnet","getSubnetOutput"], () => require("./getSubnet"));

export { GetSubnetsArgs, GetSubnetsResult, GetSubnetsOutputArgs } from "./getSubnets";
export const getSubnets: typeof import("./getSubnets").getSubnets = null as any;
export const getSubnetsOutput: typeof import("./getSubnets").getSubnetsOutput = null as any;
utilities.lazyLoad(exports, ["getSubnets","getSubnetsOutput"], () => require("./getSubnets"));

export { GetVlanArgs, GetVlanResult, GetVlanOutputArgs } from "./getVlan";
export const getVlan: typeof import("./getVlan").getVlan = null as any;
export const getVlanOutput: typeof import("./getVlan").getVlanOutput = null as any;
utilities.lazyLoad(exports, ["getVlan","getVlanOutput"], () => require("./getVlan"));

export { L2domainArgs, L2domainState } from "./l2domain";
export type L2domain = import("./l2domain").L2domain;
export const L2domain: typeof import("./l2domain").L2domain = null as any;
utilities.lazyLoad(exports, ["L2domain"], () => require("./l2domain"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

export { SectionArgs, SectionState } from "./section";
export type Section = import("./section").Section;
export const Section: typeof import("./section").Section = null as any;
utilities.lazyLoad(exports, ["Section"], () => require("./section"));

export { SubnetArgs, SubnetState } from "./subnet";
export type Subnet = import("./subnet").Subnet;
export const Subnet: typeof import("./subnet").Subnet = null as any;
utilities.lazyLoad(exports, ["Subnet"], () => require("./subnet"));

export { VlanArgs, VlanState } from "./vlan";
export type Vlan = import("./vlan").Vlan;
export const Vlan: typeof import("./vlan").Vlan = null as any;
utilities.lazyLoad(exports, ["Vlan"], () => require("./vlan"));


// Export sub-modules:
import * as config from "./config";

export {
    config,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "phpipam:index/address:Address":
                return new Address(name, <any>undefined, { urn })
            case "phpipam:index/firstFreeAddress:FirstFreeAddress":
                return new FirstFreeAddress(name, <any>undefined, { urn })
            case "phpipam:index/firstFreeSubnet:FirstFreeSubnet":
                return new FirstFreeSubnet(name, <any>undefined, { urn })
            case "phpipam:index/l2domain:L2domain":
                return new L2domain(name, <any>undefined, { urn })
            case "phpipam:index/section:Section":
                return new Section(name, <any>undefined, { urn })
            case "phpipam:index/subnet:Subnet":
                return new Subnet(name, <any>undefined, { urn })
            case "phpipam:index/vlan:Vlan":
                return new Vlan(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("phpipam", "index/address", _module)
pulumi.runtime.registerResourceModule("phpipam", "index/firstFreeAddress", _module)
pulumi.runtime.registerResourceModule("phpipam", "index/firstFreeSubnet", _module)
pulumi.runtime.registerResourceModule("phpipam", "index/l2domain", _module)
pulumi.runtime.registerResourceModule("phpipam", "index/section", _module)
pulumi.runtime.registerResourceModule("phpipam", "index/subnet", _module)
pulumi.runtime.registerResourceModule("phpipam", "index/vlan", _module)
pulumi.runtime.registerResourcePackage("phpipam", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:phpipam") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
