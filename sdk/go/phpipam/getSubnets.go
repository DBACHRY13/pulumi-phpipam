// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package phpipam

import (
	"context"
	"reflect"

	"github.com/DBACHRY13/pulumi-phpipam/sdk/go/phpipam/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetSubnets(ctx *pulumi.Context, args *GetSubnetsArgs, opts ...pulumi.InvokeOption) (*GetSubnetsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetSubnetsResult
	err := ctx.Invoke("phpipam:index/getSubnets:getSubnets", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSubnets.
type GetSubnetsArgs struct {
	// A map of custom fields to search for. The filter
	// values are regular expressions. All fields need to match for the match to
	// succeed.
	//
	// You can find documentation for the regular expression syntax used with the
	// `descriptionMatch` and `customFieldFilter` attributes
	// [here](https://github.com/google/re2/wiki/Syntax).
	//
	// ⚠️  **NOTE:** An empty or unspecified `customFieldFilter` value is the
	// equivalent to a regular expression that matches everything, and hence will
	// return **all** subnets that contain the referenced custom field key!
	// Custom fileds must contain mandatory prefix `custom_`.
	CustomFieldFilter map[string]interface{} `pulumi:"customFieldFilter"`
	// The subnet's description.
	Description *string `pulumi:"description"`
	// A regular expression to match against when searching
	// for a subnet.
	DescriptionMatch *string `pulumi:"descriptionMatch"`
	// The ID of the section of the subnet.
	//
	// One of the following below parameters is required:
	SectionId int `pulumi:"sectionId"`
}

// A collection of values returned by getSubnets.
type GetSubnetsResult struct {
	CustomFieldFilter map[string]interface{} `pulumi:"customFieldFilter"`
	Description       *string                `pulumi:"description"`
	DescriptionMatch  *string                `pulumi:"descriptionMatch"`
	// The provider-assigned unique ID for this managed resource.
	Id        string `pulumi:"id"`
	SectionId int    `pulumi:"sectionId"`
	// A list of subnet IDs that match the given criteria.
	SubnetIds []int `pulumi:"subnetIds"`
}

func GetSubnetsOutput(ctx *pulumi.Context, args GetSubnetsOutputArgs, opts ...pulumi.InvokeOption) GetSubnetsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetSubnetsResult, error) {
			args := v.(GetSubnetsArgs)
			r, err := GetSubnets(ctx, &args, opts...)
			var s GetSubnetsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetSubnetsResultOutput)
}

// A collection of arguments for invoking getSubnets.
type GetSubnetsOutputArgs struct {
	// A map of custom fields to search for. The filter
	// values are regular expressions. All fields need to match for the match to
	// succeed.
	//
	// You can find documentation for the regular expression syntax used with the
	// `descriptionMatch` and `customFieldFilter` attributes
	// [here](https://github.com/google/re2/wiki/Syntax).
	//
	// ⚠️  **NOTE:** An empty or unspecified `customFieldFilter` value is the
	// equivalent to a regular expression that matches everything, and hence will
	// return **all** subnets that contain the referenced custom field key!
	// Custom fileds must contain mandatory prefix `custom_`.
	CustomFieldFilter pulumi.MapInput `pulumi:"customFieldFilter"`
	// The subnet's description.
	Description pulumi.StringPtrInput `pulumi:"description"`
	// A regular expression to match against when searching
	// for a subnet.
	DescriptionMatch pulumi.StringPtrInput `pulumi:"descriptionMatch"`
	// The ID of the section of the subnet.
	//
	// One of the following below parameters is required:
	SectionId pulumi.IntInput `pulumi:"sectionId"`
}

func (GetSubnetsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSubnetsArgs)(nil)).Elem()
}

// A collection of values returned by getSubnets.
type GetSubnetsResultOutput struct{ *pulumi.OutputState }

func (GetSubnetsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSubnetsResult)(nil)).Elem()
}

func (o GetSubnetsResultOutput) ToGetSubnetsResultOutput() GetSubnetsResultOutput {
	return o
}

func (o GetSubnetsResultOutput) ToGetSubnetsResultOutputWithContext(ctx context.Context) GetSubnetsResultOutput {
	return o
}

func (o GetSubnetsResultOutput) CustomFieldFilter() pulumi.MapOutput {
	return o.ApplyT(func(v GetSubnetsResult) map[string]interface{} { return v.CustomFieldFilter }).(pulumi.MapOutput)
}

func (o GetSubnetsResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSubnetsResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o GetSubnetsResultOutput) DescriptionMatch() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSubnetsResult) *string { return v.DescriptionMatch }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetSubnetsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetSubnetsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetSubnetsResultOutput) SectionId() pulumi.IntOutput {
	return o.ApplyT(func(v GetSubnetsResult) int { return v.SectionId }).(pulumi.IntOutput)
}

// A list of subnet IDs that match the given criteria.
func (o GetSubnetsResultOutput) SubnetIds() pulumi.IntArrayOutput {
	return o.ApplyT(func(v GetSubnetsResult) []int { return v.SubnetIds }).(pulumi.IntArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetSubnetsResultOutput{})
}