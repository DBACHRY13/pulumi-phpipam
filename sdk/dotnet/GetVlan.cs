// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Phpipam
{
    public static class GetVlan
    {
        /// <summary>
        /// ## # phpipam.Vlan
        /// 
        /// The `phpipam.Vlan` data source allows one to look up a VLAN in the PHPIPAM
        /// database. This can then be used to assign a VLAN to a subnet in the
        /// `phpipam.Subnet` resource. It can also be used
        /// to gather other information on the VLAN.
        /// 
        /// **Example:**
        /// 
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Phpipam = Pulumi.Phpipam;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var section = Phpipam.GetSection.Invoke(new()
        ///     {
        ///         Name = "Customers",
        ///     });
        /// 
        ///     var vlan = Phpipam.GetVlan.Invoke(new()
        ///     {
        ///         Number = 1000,
        ///     });
        /// 
        ///     var subnet = new Phpipam.Subnet("subnet", new()
        ///     {
        ///         SectionId = section.Apply(getSectionResult =&gt; getSectionResult.SectionId),
        ///         SubnetAddress = "10.10.3.0",
        ///         SubnetMask = 24,
        ///         VlanId = vlan.Apply(getVlanResult =&gt; getVlanResult.VlanId),
        ///     });
        /// 
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Task<GetVlanResult> InvokeAsync(GetVlanArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVlanResult>("phpipam:index/getVlan:getVlan", args ?? new GetVlanArgs(), options.WithDefaults());

        /// <summary>
        /// ## # phpipam.Vlan
        /// 
        /// The `phpipam.Vlan` data source allows one to look up a VLAN in the PHPIPAM
        /// database. This can then be used to assign a VLAN to a subnet in the
        /// `phpipam.Subnet` resource. It can also be used
        /// to gather other information on the VLAN.
        /// 
        /// **Example:**
        /// 
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Phpipam = Pulumi.Phpipam;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var section = Phpipam.GetSection.Invoke(new()
        ///     {
        ///         Name = "Customers",
        ///     });
        /// 
        ///     var vlan = Phpipam.GetVlan.Invoke(new()
        ///     {
        ///         Number = 1000,
        ///     });
        /// 
        ///     var subnet = new Phpipam.Subnet("subnet", new()
        ///     {
        ///         SectionId = section.Apply(getSectionResult =&gt; getSectionResult.SectionId),
        ///         SubnetAddress = "10.10.3.0",
        ///         SubnetMask = 24,
        ///         VlanId = vlan.Apply(getVlanResult =&gt; getVlanResult.VlanId),
        ///     });
        /// 
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Output<GetVlanResult> Invoke(GetVlanInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVlanResult>("phpipam:index/getVlan:getVlan", args ?? new GetVlanInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVlanArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The layer 2 domain ID in the PHPIPAM database.
        /// </summary>
        [Input("l2DomainId")]
        public int? L2DomainId { get; set; }

        /// <summary>
        /// The number of the VLAN to look up.
        /// 
        /// One of `vlan_id` or `number` must be supplied. If both are supplied,
        /// `vlan_id` is used.
        /// </summary>
        [Input("number")]
        public int? Number { get; set; }

        /// <summary>
        /// The ID of the VLAN to look up. **NOTE:** this is the database ID,
        /// not the VLAN number - if you need this, use the `number` parameter.
        /// </summary>
        [Input("vlanId")]
        public int? VlanId { get; set; }

        public GetVlanArgs()
        {
        }
        public static new GetVlanArgs Empty => new GetVlanArgs();
    }

    public sealed class GetVlanInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The layer 2 domain ID in the PHPIPAM database.
        /// </summary>
        [Input("l2DomainId")]
        public Input<int>? L2DomainId { get; set; }

        /// <summary>
        /// The number of the VLAN to look up.
        /// 
        /// One of `vlan_id` or `number` must be supplied. If both are supplied,
        /// `vlan_id` is used.
        /// </summary>
        [Input("number")]
        public Input<int>? Number { get; set; }

        /// <summary>
        /// The ID of the VLAN to look up. **NOTE:** this is the database ID,
        /// not the VLAN number - if you need this, use the `number` parameter.
        /// </summary>
        [Input("vlanId")]
        public Input<int>? VlanId { get; set; }

        public GetVlanInvokeArgs()
        {
        }
        public static new GetVlanInvokeArgs Empty => new GetVlanInvokeArgs();
    }


    [OutputType]
    public sealed class GetVlanResult
    {
        /// <summary>
        /// A key/value map of custom fields for this VLAN.
        /// </summary>
        public readonly ImmutableDictionary<string, object> CustomFields;
        /// <summary>
        /// The description supplied to the VLAN.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The date this resource was last updated.
        /// </summary>
        public readonly string EditDate;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The layer 2 domain ID in the PHPIPAM database.
        /// </summary>
        public readonly int L2DomainId;
        /// <summary>
        /// The name/label of the VLAN.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The number of the VLAN (the actual VLAN ID on your switch).
        /// </summary>
        public readonly int Number;
        /// <summary>
        /// The ID of the VLAN to look up. **NOTE:** this is the database ID,
        /// not the VLAN number - if you need this, use the `number` parameter.
        /// </summary>
        public readonly int VlanId;

        [OutputConstructor]
        private GetVlanResult(
            ImmutableDictionary<string, object> customFields,

            string description,

            string editDate,

            string id,

            int l2DomainId,

            string name,

            int number,

            int vlanId)
        {
            CustomFields = customFields;
            Description = description;
            EditDate = editDate;
            Id = id;
            L2DomainId = l2DomainId;
            Name = name;
            Number = number;
            VlanId = vlanId;
        }
    }
}