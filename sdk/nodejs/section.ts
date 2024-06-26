// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Section extends pulumi.CustomResource {
    /**
     * Get an existing Section resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SectionState, opts?: pulumi.CustomResourceOptions): Section {
        return new Section(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'phpipam:index/section:Section';

    /**
     * Returns true if the given object is an instance of Section.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Section {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Section.__pulumiType;
    }

    /**
     * The section's description.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * The section's display order number.
     */
    public readonly displayOrder!: pulumi.Output<number>;
    /**
     * The ID of the DNS resolver to use in the
     * section.
     */
    public readonly dnsResolverId!: pulumi.Output<number>;
    /**
     * The date this resource was last edited.
     */
    public /*out*/ readonly editDate!: pulumi.Output<string>;
    /**
     * The ID of the parent section in the PHPIPAM
     * database.
     */
    public readonly masterSectionId!: pulumi.Output<number>;
    /**
     * The name of the section.
     */
    public readonly name!: pulumi.Output<string>;
    public /*out*/ readonly permissions!: pulumi.Output<string>;
    /**
     * The ID of the section in the PHPIPAM database.
     */
    public /*out*/ readonly sectionId!: pulumi.Output<number>;
    /**
     * `true` if supernets are only being shown in
     * the subnet listing.
     */
    public readonly showSupernetOnly!: pulumi.Output<boolean>;
    /**
     * `true` if VLANs are being shown in
     * the subnet listing for this section.
     */
    public readonly showVlanInSubnetListing!: pulumi.Output<boolean>;
    /**
     * `true` if VRFs are being shown in
     * the subnet listing for this section.
     */
    public readonly showVrfInSubnetListing!: pulumi.Output<boolean>;
    /**
     * `true` if this subnet is set up to check that IP
     * addresses are valid for the subnets they are in.
     */
    public readonly strictMode!: pulumi.Output<boolean>;
    /**
     * How subnets in this section are ordered.
     */
    public readonly subnetOrdering!: pulumi.Output<string>;

    /**
     * Create a Section resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: SectionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SectionArgs | SectionState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SectionState | undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["displayOrder"] = state ? state.displayOrder : undefined;
            resourceInputs["dnsResolverId"] = state ? state.dnsResolverId : undefined;
            resourceInputs["editDate"] = state ? state.editDate : undefined;
            resourceInputs["masterSectionId"] = state ? state.masterSectionId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["permissions"] = state ? state.permissions : undefined;
            resourceInputs["sectionId"] = state ? state.sectionId : undefined;
            resourceInputs["showSupernetOnly"] = state ? state.showSupernetOnly : undefined;
            resourceInputs["showVlanInSubnetListing"] = state ? state.showVlanInSubnetListing : undefined;
            resourceInputs["showVrfInSubnetListing"] = state ? state.showVrfInSubnetListing : undefined;
            resourceInputs["strictMode"] = state ? state.strictMode : undefined;
            resourceInputs["subnetOrdering"] = state ? state.subnetOrdering : undefined;
        } else {
            const args = argsOrState as SectionArgs | undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["displayOrder"] = args ? args.displayOrder : undefined;
            resourceInputs["dnsResolverId"] = args ? args.dnsResolverId : undefined;
            resourceInputs["masterSectionId"] = args ? args.masterSectionId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["showSupernetOnly"] = args ? args.showSupernetOnly : undefined;
            resourceInputs["showVlanInSubnetListing"] = args ? args.showVlanInSubnetListing : undefined;
            resourceInputs["showVrfInSubnetListing"] = args ? args.showVrfInSubnetListing : undefined;
            resourceInputs["strictMode"] = args ? args.strictMode : undefined;
            resourceInputs["subnetOrdering"] = args ? args.subnetOrdering : undefined;
            resourceInputs["editDate"] = undefined /*out*/;
            resourceInputs["permissions"] = undefined /*out*/;
            resourceInputs["sectionId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Section.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Section resources.
 */
export interface SectionState {
    /**
     * The section's description.
     */
    description?: pulumi.Input<string>;
    /**
     * The section's display order number.
     */
    displayOrder?: pulumi.Input<number>;
    /**
     * The ID of the DNS resolver to use in the
     * section.
     */
    dnsResolverId?: pulumi.Input<number>;
    /**
     * The date this resource was last edited.
     */
    editDate?: pulumi.Input<string>;
    /**
     * The ID of the parent section in the PHPIPAM
     * database.
     */
    masterSectionId?: pulumi.Input<number>;
    /**
     * The name of the section.
     */
    name?: pulumi.Input<string>;
    permissions?: pulumi.Input<string>;
    /**
     * The ID of the section in the PHPIPAM database.
     */
    sectionId?: pulumi.Input<number>;
    /**
     * `true` if supernets are only being shown in
     * the subnet listing.
     */
    showSupernetOnly?: pulumi.Input<boolean>;
    /**
     * `true` if VLANs are being shown in
     * the subnet listing for this section.
     */
    showVlanInSubnetListing?: pulumi.Input<boolean>;
    /**
     * `true` if VRFs are being shown in
     * the subnet listing for this section.
     */
    showVrfInSubnetListing?: pulumi.Input<boolean>;
    /**
     * `true` if this subnet is set up to check that IP
     * addresses are valid for the subnets they are in.
     */
    strictMode?: pulumi.Input<boolean>;
    /**
     * How subnets in this section are ordered.
     */
    subnetOrdering?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Section resource.
 */
export interface SectionArgs {
    /**
     * The section's description.
     */
    description?: pulumi.Input<string>;
    /**
     * The section's display order number.
     */
    displayOrder?: pulumi.Input<number>;
    /**
     * The ID of the DNS resolver to use in the
     * section.
     */
    dnsResolverId?: pulumi.Input<number>;
    /**
     * The ID of the parent section in the PHPIPAM
     * database.
     */
    masterSectionId?: pulumi.Input<number>;
    /**
     * The name of the section.
     */
    name?: pulumi.Input<string>;
    /**
     * `true` if supernets are only being shown in
     * the subnet listing.
     */
    showSupernetOnly?: pulumi.Input<boolean>;
    /**
     * `true` if VLANs are being shown in
     * the subnet listing for this section.
     */
    showVlanInSubnetListing?: pulumi.Input<boolean>;
    /**
     * `true` if VRFs are being shown in
     * the subnet listing for this section.
     */
    showVrfInSubnetListing?: pulumi.Input<boolean>;
    /**
     * `true` if this subnet is set up to check that IP
     * addresses are valid for the subnets they are in.
     */
    strictMode?: pulumi.Input<boolean>;
    /**
     * How subnets in this section are ordered.
     */
    subnetOrdering?: pulumi.Input<string>;
}
