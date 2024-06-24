// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getL2domain(args?: GetL2domainArgs, opts?: pulumi.InvokeOptions): Promise<GetL2domainResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("phpipam:index/getL2domain:getL2domain", {
        "domainId": args.domainId,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getL2domain.
 */
export interface GetL2domainArgs {
    domainId?: number;
    name?: string;
}

/**
 * A collection of values returned by getL2domain.
 */
export interface GetL2domainResult {
    readonly description: string;
    readonly domainId: number;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly name: string;
    readonly sections: string;
}
export function getL2domainOutput(args?: GetL2domainOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetL2domainResult> {
    return pulumi.output(args).apply((a: any) => getL2domain(a, opts))
}

/**
 * A collection of arguments for invoking getL2domain.
 */
export interface GetL2domainOutputArgs {
    domainId?: pulumi.Input<number>;
    name?: pulumi.Input<string>;
}
