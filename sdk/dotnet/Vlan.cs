// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Phpipam
{
    [PhpipamResourceType("phpipam:index/vlan:Vlan")]
    public partial class Vlan : global::Pulumi.CustomResource
    {
        /// <summary>
        /// A key/value map of custom fields for this
        /// VLAN.
        /// 
        /// ⚠️ **NOTE on custom fields:** PHPIPAM installations with custom fields must have
        /// all fields set to optional when using this plugin. For more info see
        /// [here](https://github.com/phpipam/phpipam/issues/1073). Further to this, either
        /// ensure that your fields also do not have default values, or ensure the default
        /// is set in your TF configuration. Diff loops may happen otherwise!
        /// </summary>
        [Output("customFields")]
        public Output<ImmutableDictionary<string, object>?> CustomFields { get; private set; } = null!;

        /// <summary>
        /// The description supplied to the VLAN.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The date this resource was last updated.
        /// </summary>
        [Output("editDate")]
        public Output<string> EditDate { get; private set; } = null!;

        /// <summary>
        /// The layer 2 domain ID in the PHPIPAM database.
        /// </summary>
        [Output("l2DomainId")]
        public Output<int> L2DomainId { get; private set; } = null!;

        /// <summary>
        /// The name/label of the VLAN.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The number of the VLAN (the actual VLAN ID on your switch).
        /// </summary>
        [Output("number")]
        public Output<int> Number { get; private set; } = null!;

        /// <summary>
        /// The ID of the VLAN to look up. **NOTE:** this is the database ID,
        /// not the VLAN number - if you need this, use the `number` parameter.
        /// </summary>
        [Output("vlanId")]
        public Output<int> VlanId { get; private set; } = null!;


        /// <summary>
        /// Create a Vlan resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Vlan(string name, VlanArgs args, CustomResourceOptions? options = null)
            : base("phpipam:index/vlan:Vlan", name, args ?? new VlanArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Vlan(string name, Input<string> id, VlanState? state = null, CustomResourceOptions? options = null)
            : base("phpipam:index/vlan:Vlan", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Vlan resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Vlan Get(string name, Input<string> id, VlanState? state = null, CustomResourceOptions? options = null)
        {
            return new Vlan(name, id, state, options);
        }
    }

    public sealed class VlanArgs : global::Pulumi.ResourceArgs
    {
        [Input("customFields")]
        private InputMap<object>? _customFields;

        /// <summary>
        /// A key/value map of custom fields for this
        /// VLAN.
        /// 
        /// ⚠️ **NOTE on custom fields:** PHPIPAM installations with custom fields must have
        /// all fields set to optional when using this plugin. For more info see
        /// [here](https://github.com/phpipam/phpipam/issues/1073). Further to this, either
        /// ensure that your fields also do not have default values, or ensure the default
        /// is set in your TF configuration. Diff loops may happen otherwise!
        /// </summary>
        public InputMap<object> CustomFields
        {
            get => _customFields ?? (_customFields = new InputMap<object>());
            set => _customFields = value;
        }

        /// <summary>
        /// The description supplied to the VLAN.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The layer 2 domain ID in the PHPIPAM database.
        /// </summary>
        [Input("l2DomainId")]
        public Input<int>? L2DomainId { get; set; }

        /// <summary>
        /// The name/label of the VLAN.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The number of the VLAN (the actual VLAN ID on your switch).
        /// </summary>
        [Input("number", required: true)]
        public Input<int> Number { get; set; } = null!;

        public VlanArgs()
        {
        }
        public static new VlanArgs Empty => new VlanArgs();
    }

    public sealed class VlanState : global::Pulumi.ResourceArgs
    {
        [Input("customFields")]
        private InputMap<object>? _customFields;

        /// <summary>
        /// A key/value map of custom fields for this
        /// VLAN.
        /// 
        /// ⚠️ **NOTE on custom fields:** PHPIPAM installations with custom fields must have
        /// all fields set to optional when using this plugin. For more info see
        /// [here](https://github.com/phpipam/phpipam/issues/1073). Further to this, either
        /// ensure that your fields also do not have default values, or ensure the default
        /// is set in your TF configuration. Diff loops may happen otherwise!
        /// </summary>
        public InputMap<object> CustomFields
        {
            get => _customFields ?? (_customFields = new InputMap<object>());
            set => _customFields = value;
        }

        /// <summary>
        /// The description supplied to the VLAN.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The date this resource was last updated.
        /// </summary>
        [Input("editDate")]
        public Input<string>? EditDate { get; set; }

        /// <summary>
        /// The layer 2 domain ID in the PHPIPAM database.
        /// </summary>
        [Input("l2DomainId")]
        public Input<int>? L2DomainId { get; set; }

        /// <summary>
        /// The name/label of the VLAN.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The number of the VLAN (the actual VLAN ID on your switch).
        /// </summary>
        [Input("number")]
        public Input<int>? Number { get; set; }

        /// <summary>
        /// The ID of the VLAN to look up. **NOTE:** this is the database ID,
        /// not the VLAN number - if you need this, use the `number` parameter.
        /// </summary>
        [Input("vlanId")]
        public Input<int>? VlanId { get; set; }

        public VlanState()
        {
        }
        public static new VlanState Empty => new VlanState();
    }
}
