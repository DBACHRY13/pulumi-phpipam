// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package phpipam

import (
	"fmt"

	"github.com/DBACHRY13/pulumi-phpipam/sdk/go/phpipam/internal"
	"github.com/blang/semver"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "phpipam:index/address:Address":
		r = &Address{}
	case "phpipam:index/firstFreeAddress:FirstFreeAddress":
		r = &FirstFreeAddress{}
	case "phpipam:index/firstFreeSubnet:FirstFreeSubnet":
		r = &FirstFreeSubnet{}
	case "phpipam:index/l2domain:L2domain":
		r = &L2domain{}
	case "phpipam:index/section:Section":
		r = &Section{}
	case "phpipam:index/subnet:Subnet":
		r = &Subnet{}
	case "phpipam:index/vlan:Vlan":
		r = &Vlan{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:phpipam" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"phpipam",
		"index/address",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"phpipam",
		"index/firstFreeAddress",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"phpipam",
		"index/firstFreeSubnet",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"phpipam",
		"index/l2domain",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"phpipam",
		"index/section",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"phpipam",
		"index/subnet",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"phpipam",
		"index/vlan",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"phpipam",
		&pkg{version},
	)
}