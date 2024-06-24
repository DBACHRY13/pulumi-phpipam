// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Phpipam
{
    [PhpipamResourceType("phpipam:index/firstFreeAddress:FirstFreeAddress")]
    public partial class FirstFreeAddress : global::Pulumi.CustomResource
    {
        [Output("addressId")]
        public Output<int> AddressId { get; private set; } = null!;

        [Output("customFields")]
        public Output<ImmutableDictionary<string, object>?> CustomFields { get; private set; } = null!;

        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        [Output("deviceId")]
        public Output<int> DeviceId { get; private set; } = null!;

        [Output("editDate")]
        public Output<string> EditDate { get; private set; } = null!;

        [Output("excludePing")]
        public Output<bool> ExcludePing { get; private set; } = null!;

        [Output("hostname")]
        public Output<string> Hostname { get; private set; } = null!;

        [Output("ipAddress")]
        public Output<string> IpAddress { get; private set; } = null!;

        [Output("isGateway")]
        public Output<bool> IsGateway { get; private set; } = null!;

        [Output("lastSeen")]
        public Output<string> LastSeen { get; private set; } = null!;

        [Output("macAddress")]
        public Output<string> MacAddress { get; private set; } = null!;

        [Output("note")]
        public Output<string> Note { get; private set; } = null!;

        [Output("owner")]
        public Output<string> Owner { get; private set; } = null!;

        [Output("ptrRecordId")]
        public Output<int> PtrRecordId { get; private set; } = null!;

        [Output("skipPtrRecord")]
        public Output<bool> SkipPtrRecord { get; private set; } = null!;

        [Output("stateTagId")]
        public Output<int> StateTagId { get; private set; } = null!;

        [Output("subnetId")]
        public Output<int> SubnetId { get; private set; } = null!;

        [Output("switchPortLabel")]
        public Output<string> SwitchPortLabel { get; private set; } = null!;


        /// <summary>
        /// Create a FirstFreeAddress resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FirstFreeAddress(string name, FirstFreeAddressArgs args, CustomResourceOptions? options = null)
            : base("phpipam:index/firstFreeAddress:FirstFreeAddress", name, args ?? new FirstFreeAddressArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FirstFreeAddress(string name, Input<string> id, FirstFreeAddressState? state = null, CustomResourceOptions? options = null)
            : base("phpipam:index/firstFreeAddress:FirstFreeAddress", name, state, MakeResourceOptions(options, id))
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
        /// <summary>
        /// Get an existing FirstFreeAddress resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FirstFreeAddress Get(string name, Input<string> id, FirstFreeAddressState? state = null, CustomResourceOptions? options = null)
        {
            return new FirstFreeAddress(name, id, state, options);
        }
    }

    public sealed class FirstFreeAddressArgs : global::Pulumi.ResourceArgs
    {
        [Input("customFields")]
        private InputMap<object>? _customFields;
        public InputMap<object> CustomFields
        {
            get => _customFields ?? (_customFields = new InputMap<object>());
            set => _customFields = value;
        }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("deviceId")]
        public Input<int>? DeviceId { get; set; }

        [Input("excludePing")]
        public Input<bool>? ExcludePing { get; set; }

        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        [Input("isGateway")]
        public Input<bool>? IsGateway { get; set; }

        [Input("macAddress")]
        public Input<string>? MacAddress { get; set; }

        [Input("note")]
        public Input<string>? Note { get; set; }

        [Input("owner")]
        public Input<string>? Owner { get; set; }

        [Input("ptrRecordId")]
        public Input<int>? PtrRecordId { get; set; }

        [Input("skipPtrRecord")]
        public Input<bool>? SkipPtrRecord { get; set; }

        [Input("stateTagId")]
        public Input<int>? StateTagId { get; set; }

        [Input("subnetId", required: true)]
        public Input<int> SubnetId { get; set; } = null!;

        [Input("switchPortLabel")]
        public Input<string>? SwitchPortLabel { get; set; }

        public FirstFreeAddressArgs()
        {
        }
        public static new FirstFreeAddressArgs Empty => new FirstFreeAddressArgs();
    }

    public sealed class FirstFreeAddressState : global::Pulumi.ResourceArgs
    {
        [Input("addressId")]
        public Input<int>? AddressId { get; set; }

        [Input("customFields")]
        private InputMap<object>? _customFields;
        public InputMap<object> CustomFields
        {
            get => _customFields ?? (_customFields = new InputMap<object>());
            set => _customFields = value;
        }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("deviceId")]
        public Input<int>? DeviceId { get; set; }

        [Input("editDate")]
        public Input<string>? EditDate { get; set; }

        [Input("excludePing")]
        public Input<bool>? ExcludePing { get; set; }

        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        [Input("ipAddress")]
        public Input<string>? IpAddress { get; set; }

        [Input("isGateway")]
        public Input<bool>? IsGateway { get; set; }

        [Input("lastSeen")]
        public Input<string>? LastSeen { get; set; }

        [Input("macAddress")]
        public Input<string>? MacAddress { get; set; }

        [Input("note")]
        public Input<string>? Note { get; set; }

        [Input("owner")]
        public Input<string>? Owner { get; set; }

        [Input("ptrRecordId")]
        public Input<int>? PtrRecordId { get; set; }

        [Input("skipPtrRecord")]
        public Input<bool>? SkipPtrRecord { get; set; }

        [Input("stateTagId")]
        public Input<int>? StateTagId { get; set; }

        [Input("subnetId")]
        public Input<int>? SubnetId { get; set; }

        [Input("switchPortLabel")]
        public Input<string>? SwitchPortLabel { get; set; }

        public FirstFreeAddressState()
        {
        }
        public static new FirstFreeAddressState Empty => new FirstFreeAddressState();
    }
}