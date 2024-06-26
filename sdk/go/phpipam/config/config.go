// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/DBACHRY13/pulumi-phpipam/sdk/go/phpipam/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

var _ = internal.GetEnvOrDefault

// The application ID required for API requests
func GetAppId(ctx *pulumi.Context) string {
	return config.Get(ctx, "phpipam:appId")
}

// The full URL (plus path) to the API endpoint
func GetEndpoint(ctx *pulumi.Context) string {
	return config.Get(ctx, "phpipam:endpoint")
}

// Whether server should be accessed without verifying the TLS certificate.
func GetInsecure(ctx *pulumi.Context) bool {
	return config.GetBool(ctx, "phpipam:insecure")
}

// Whether the API client is configured to nest custom values.
func GetNestCustomFields(ctx *pulumi.Context) bool {
	return config.GetBool(ctx, "phpipam:nestCustomFields")
}

// The password of the PHPIPAM account
func GetPassword(ctx *pulumi.Context) string {
	return config.Get(ctx, "phpipam:password")
}

// The username of the PHPIPAM account
func GetUsername(ctx *pulumi.Context) string {
	return config.Get(ctx, "phpipam:username")
}
