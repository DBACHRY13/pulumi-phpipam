// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The provider type for the phpipam package. By default, resources use package-wide configuration
 * settings, however an explicit `Provider` instance may be created and passed during resource
 * construction to achieve fine-grained programmatic control over provider settings. See the
 * [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
 */
export class Provider extends pulumi.ProviderResource {
    /** @internal */
    public static readonly __pulumiType = 'phpipam';

    /**
     * Returns true if the given object is an instance of Provider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Provider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === "pulumi:providers:" + Provider.__pulumiType;
    }

    /**
     * The application ID required for API requests
     */
    public readonly appId!: pulumi.Output<string | undefined>;
    /**
     * The full URL (plus path) to the API endpoint
     */
    public readonly endpoint!: pulumi.Output<string | undefined>;
    /**
     * The password of the PHPIPAM account
     */
    public readonly password!: pulumi.Output<string | undefined>;
    /**
     * The username of the PHPIPAM account
     */
    public readonly username!: pulumi.Output<string | undefined>;

    /**
     * Create a Provider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ProviderArgs, opts?: pulumi.ResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        {
            resourceInputs["appId"] = args ? args.appId : undefined;
            resourceInputs["endpoint"] = args ? args.endpoint : undefined;
            resourceInputs["insecure"] = pulumi.output(args ? args.insecure : undefined).apply(JSON.stringify);
            resourceInputs["nestCustomFields"] = pulumi.output(args ? args.nestCustomFields : undefined).apply(JSON.stringify);
            resourceInputs["password"] = args ? args.password : undefined;
            resourceInputs["username"] = args ? args.username : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Provider.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Provider resource.
 */
export interface ProviderArgs {
    /**
     * The application ID required for API requests
     */
    appId?: pulumi.Input<string>;
    /**
     * The full URL (plus path) to the API endpoint
     */
    endpoint?: pulumi.Input<string>;
    /**
     * Whether server should be accessed without verifying the TLS certificate.
     */
    insecure?: pulumi.Input<boolean>;
    /**
     * Whether the API client is configured to nest custom values.
     */
    nestCustomFields?: pulumi.Input<boolean>;
    /**
     * The password of the PHPIPAM account
     */
    password?: pulumi.Input<string>;
    /**
     * The username of the PHPIPAM account
     */
    username?: pulumi.Input<string>;
}
