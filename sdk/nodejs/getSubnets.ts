// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getSubnets(args: GetSubnetsArgs, opts?: pulumi.InvokeOptions): Promise<GetSubnetsResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("phpipam:index/getSubnets:getSubnets", {
        "customFieldFilter": args.customFieldFilter,
        "description": args.description,
        "descriptionMatch": args.descriptionMatch,
        "sectionId": args.sectionId,
    }, opts);
}

/**
 * A collection of arguments for invoking getSubnets.
 */
export interface GetSubnetsArgs {
    /**
     * A map of custom fields to search for. The filter
     * values are regular expressions. All fields need to match for the match to
     * succeed.
     *
     * You can find documentation for the regular expression syntax used with the
     * `descriptionMatch` and `customFieldFilter` attributes
     * [here](https://github.com/google/re2/wiki/Syntax).
     *
     * ⚠️  **NOTE:** An empty or unspecified `customFieldFilter` value is the
     * equivalent to a regular expression that matches everything, and hence will
     * return **all** subnets that contain the referenced custom field key!
     * Custom fileds must contain mandatory prefix `custom_`.
     */
    customFieldFilter?: {[key: string]: any};
    /**
     * The subnet's description.
     */
    description?: string;
    /**
     * A regular expression to match against when searching
     * for a subnet.
     */
    descriptionMatch?: string;
    /**
     * The ID of the section of the subnet.
     *
     * One of the following below parameters is required:
     */
    sectionId: number;
}

/**
 * A collection of values returned by getSubnets.
 */
export interface GetSubnetsResult {
    readonly customFieldFilter?: {[key: string]: any};
    readonly description?: string;
    readonly descriptionMatch?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly sectionId: number;
    /**
     * A list of subnet IDs that match the given criteria.
     */
    readonly subnetIds: number[];
}
export function getSubnetsOutput(args: GetSubnetsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSubnetsResult> {
    return pulumi.output(args).apply((a: any) => getSubnets(a, opts))
}

/**
 * A collection of arguments for invoking getSubnets.
 */
export interface GetSubnetsOutputArgs {
    /**
     * A map of custom fields to search for. The filter
     * values are regular expressions. All fields need to match for the match to
     * succeed.
     *
     * You can find documentation for the regular expression syntax used with the
     * `descriptionMatch` and `customFieldFilter` attributes
     * [here](https://github.com/google/re2/wiki/Syntax).
     *
     * ⚠️  **NOTE:** An empty or unspecified `customFieldFilter` value is the
     * equivalent to a regular expression that matches everything, and hence will
     * return **all** subnets that contain the referenced custom field key!
     * Custom fileds must contain mandatory prefix `custom_`.
     */
    customFieldFilter?: pulumi.Input<{[key: string]: any}>;
    /**
     * The subnet's description.
     */
    description?: pulumi.Input<string>;
    /**
     * A regular expression to match against when searching
     * for a subnet.
     */
    descriptionMatch?: pulumi.Input<string>;
    /**
     * The ID of the section of the subnet.
     *
     * One of the following below parameters is required:
     */
    sectionId: pulumi.Input<number>;
}
