// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Phpipam
{
    /// <summary>
    /// The provider type for the phpipam package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [PhpipamResourceType("pulumi:providers:phpipam")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        /// <summary>
        /// The application ID required for API requests
        /// </summary>
        [Output("appId")]
        public Output<string?> AppId { get; private set; } = null!;

        /// <summary>
        /// The full URL (plus path) to the API endpoint
        /// </summary>
        [Output("endpoint")]
        public Output<string?> Endpoint { get; private set; } = null!;

        /// <summary>
        /// The password of the PHPIPAM account
        /// </summary>
        [Output("password")]
        public Output<string?> Password { get; private set; } = null!;

        /// <summary>
        /// The username of the PHPIPAM account
        /// </summary>
        [Output("username")]
        public Output<string?> Username { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, CustomResourceOptions? options = null)
            : base("phpipam", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The application ID required for API requests
        /// </summary>
        [Input("appId")]
        public Input<string>? AppId { get; set; }

        /// <summary>
        /// The full URL (plus path) to the API endpoint
        /// </summary>
        [Input("endpoint")]
        public Input<string>? Endpoint { get; set; }

        /// <summary>
        /// Whether server should be accessed without verifying the TLS certificate.
        /// </summary>
        [Input("insecure", json: true)]
        public Input<bool>? Insecure { get; set; }

        /// <summary>
        /// Whether the API client is configured to nest custom values.
        /// </summary>
        [Input("nestCustomFields", json: true)]
        public Input<bool>? NestCustomFields { get; set; }

        /// <summary>
        /// The password of the PHPIPAM account
        /// </summary>
        [Input("password")]
        public Input<string>? Password { get; set; }

        /// <summary>
        /// The username of the PHPIPAM account
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public ProviderArgs()
        {
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
