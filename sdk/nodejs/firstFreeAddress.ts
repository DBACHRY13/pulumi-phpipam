// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class FirstFreeAddress extends pulumi.CustomResource {
    /**
     * Get an existing FirstFreeAddress resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FirstFreeAddressState, opts?: pulumi.CustomResourceOptions): FirstFreeAddress {
        return new FirstFreeAddress(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'phpipam:index/firstFreeAddress:FirstFreeAddress';

    /**
     * Returns true if the given object is an instance of FirstFreeAddress.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FirstFreeAddress {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FirstFreeAddress.__pulumiType;
    }

    public /*out*/ readonly addressId!: pulumi.Output<number>;
    public readonly customFields!: pulumi.Output<{[key: string]: any} | undefined>;
    public readonly description!: pulumi.Output<string>;
    public readonly deviceId!: pulumi.Output<number>;
    public /*out*/ readonly editDate!: pulumi.Output<string>;
    public readonly excludePing!: pulumi.Output<boolean>;
    public readonly hostname!: pulumi.Output<string>;
    public /*out*/ readonly ipAddress!: pulumi.Output<string>;
    public readonly isGateway!: pulumi.Output<boolean>;
    public /*out*/ readonly lastSeen!: pulumi.Output<string>;
    public readonly macAddress!: pulumi.Output<string>;
    public readonly note!: pulumi.Output<string>;
    public readonly owner!: pulumi.Output<string>;
    public readonly ptrRecordId!: pulumi.Output<number>;
    public readonly skipPtrRecord!: pulumi.Output<boolean>;
    public readonly stateTagId!: pulumi.Output<number>;
    public readonly subnetId!: pulumi.Output<number>;
    public readonly switchPortLabel!: pulumi.Output<string>;

    /**
     * Create a FirstFreeAddress resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FirstFreeAddressArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FirstFreeAddressArgs | FirstFreeAddressState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as FirstFreeAddressState | undefined;
            resourceInputs["addressId"] = state ? state.addressId : undefined;
            resourceInputs["customFields"] = state ? state.customFields : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["deviceId"] = state ? state.deviceId : undefined;
            resourceInputs["editDate"] = state ? state.editDate : undefined;
            resourceInputs["excludePing"] = state ? state.excludePing : undefined;
            resourceInputs["hostname"] = state ? state.hostname : undefined;
            resourceInputs["ipAddress"] = state ? state.ipAddress : undefined;
            resourceInputs["isGateway"] = state ? state.isGateway : undefined;
            resourceInputs["lastSeen"] = state ? state.lastSeen : undefined;
            resourceInputs["macAddress"] = state ? state.macAddress : undefined;
            resourceInputs["note"] = state ? state.note : undefined;
            resourceInputs["owner"] = state ? state.owner : undefined;
            resourceInputs["ptrRecordId"] = state ? state.ptrRecordId : undefined;
            resourceInputs["skipPtrRecord"] = state ? state.skipPtrRecord : undefined;
            resourceInputs["stateTagId"] = state ? state.stateTagId : undefined;
            resourceInputs["subnetId"] = state ? state.subnetId : undefined;
            resourceInputs["switchPortLabel"] = state ? state.switchPortLabel : undefined;
        } else {
            const args = argsOrState as FirstFreeAddressArgs | undefined;
            if ((!args || args.subnetId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subnetId'");
            }
            resourceInputs["customFields"] = args ? args.customFields : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["deviceId"] = args ? args.deviceId : undefined;
            resourceInputs["excludePing"] = args ? args.excludePing : undefined;
            resourceInputs["hostname"] = args ? args.hostname : undefined;
            resourceInputs["isGateway"] = args ? args.isGateway : undefined;
            resourceInputs["macAddress"] = args ? args.macAddress : undefined;
            resourceInputs["note"] = args ? args.note : undefined;
            resourceInputs["owner"] = args ? args.owner : undefined;
            resourceInputs["ptrRecordId"] = args ? args.ptrRecordId : undefined;
            resourceInputs["skipPtrRecord"] = args ? args.skipPtrRecord : undefined;
            resourceInputs["stateTagId"] = args ? args.stateTagId : undefined;
            resourceInputs["subnetId"] = args ? args.subnetId : undefined;
            resourceInputs["switchPortLabel"] = args ? args.switchPortLabel : undefined;
            resourceInputs["addressId"] = undefined /*out*/;
            resourceInputs["editDate"] = undefined /*out*/;
            resourceInputs["ipAddress"] = undefined /*out*/;
            resourceInputs["lastSeen"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(FirstFreeAddress.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering FirstFreeAddress resources.
 */
export interface FirstFreeAddressState {
    addressId?: pulumi.Input<number>;
    customFields?: pulumi.Input<{[key: string]: any}>;
    description?: pulumi.Input<string>;
    deviceId?: pulumi.Input<number>;
    editDate?: pulumi.Input<string>;
    excludePing?: pulumi.Input<boolean>;
    hostname?: pulumi.Input<string>;
    ipAddress?: pulumi.Input<string>;
    isGateway?: pulumi.Input<boolean>;
    lastSeen?: pulumi.Input<string>;
    macAddress?: pulumi.Input<string>;
    note?: pulumi.Input<string>;
    owner?: pulumi.Input<string>;
    ptrRecordId?: pulumi.Input<number>;
    skipPtrRecord?: pulumi.Input<boolean>;
    stateTagId?: pulumi.Input<number>;
    subnetId?: pulumi.Input<number>;
    switchPortLabel?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a FirstFreeAddress resource.
 */
export interface FirstFreeAddressArgs {
    customFields?: pulumi.Input<{[key: string]: any}>;
    description?: pulumi.Input<string>;
    deviceId?: pulumi.Input<number>;
    excludePing?: pulumi.Input<boolean>;
    hostname?: pulumi.Input<string>;
    isGateway?: pulumi.Input<boolean>;
    macAddress?: pulumi.Input<string>;
    note?: pulumi.Input<string>;
    owner?: pulumi.Input<string>;
    ptrRecordId?: pulumi.Input<number>;
    skipPtrRecord?: pulumi.Input<boolean>;
    stateTagId?: pulumi.Input<number>;
    subnetId: pulumi.Input<number>;
    switchPortLabel?: pulumi.Input<string>;
}
