// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Phpipam
{
    public static class GetSection
    {
        /// <summary>
        /// ## # phpipam.Section
        /// 
        /// The `phpipam.Section` data source allows one to look up a specific section,
        /// either by database ID or name. This data can then be used to manage other parts
        /// of PHPIPAM, such as in the event that the section name is known but not its ID,
        /// which is required for managing subnets.
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
        ///     var subnet = new Phpipam.Subnet("subnet", new()
        ///     {
        ///         SectionId = section.Apply(getSectionResult =&gt; getSectionResult.SectionId),
        ///         SubnetAddress = "10.10.3.0",
        ///         SubnetMask = 24,
        ///     });
        /// 
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Task<GetSectionResult> InvokeAsync(GetSectionArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSectionResult>("phpipam:index/getSection:getSection", args ?? new GetSectionArgs(), options.WithDefaults());

        /// <summary>
        /// ## # phpipam.Section
        /// 
        /// The `phpipam.Section` data source allows one to look up a specific section,
        /// either by database ID or name. This data can then be used to manage other parts
        /// of PHPIPAM, such as in the event that the section name is known but not its ID,
        /// which is required for managing subnets.
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
        ///     var subnet = new Phpipam.Subnet("subnet", new()
        ///     {
        ///         SectionId = section.Apply(getSectionResult =&gt; getSectionResult.SectionId),
        ///         SubnetAddress = "10.10.3.0",
        ///         SubnetMask = 24,
        ///     });
        /// 
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Output<GetSectionResult> Invoke(GetSectionInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSectionResult>("phpipam:index/getSection:getSection", args ?? new GetSectionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSectionArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the section to look up.
        /// 
        /// One of `section_id` or `name` must be supplied. If both are supplied,
        /// `section_id` is used.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// The ID of the section to look up.
        /// </summary>
        [Input("sectionId")]
        public int? SectionId { get; set; }

        public GetSectionArgs()
        {
        }
        public static new GetSectionArgs Empty => new GetSectionArgs();
    }

    public sealed class GetSectionInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the section to look up.
        /// 
        /// One of `section_id` or `name` must be supplied. If both are supplied,
        /// `section_id` is used.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the section to look up.
        /// </summary>
        [Input("sectionId")]
        public Input<int>? SectionId { get; set; }

        public GetSectionInvokeArgs()
        {
        }
        public static new GetSectionInvokeArgs Empty => new GetSectionInvokeArgs();
    }


    [OutputType]
    public sealed class GetSectionResult
    {
        /// <summary>
        /// The section's description.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The section's display order number.
        /// </summary>
        public readonly int DisplayOrder;
        /// <summary>
        /// The ID of the DNS resolver to use in the section.
        /// </summary>
        public readonly int DnsResolverId;
        /// <summary>
        /// The date this resource was last edited.
        /// </summary>
        public readonly string EditDate;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The ID of the parent section in the PHPIPAM database.
        /// </summary>
        public readonly int MasterSectionId;
        /// <summary>
        /// The name of the section.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// A JSON representation of permissions for this section.
        /// </summary>
        public readonly string Permissions;
        /// <summary>
        /// The ID of the section in the PHPIPAM database.
        /// </summary>
        public readonly int SectionId;
        /// <summary>
        /// `true` if supernets are only being shown in the subnet
        /// listing.
        /// </summary>
        public readonly bool ShowSupernetOnly;
        /// <summary>
        /// `true` if VLANs are being shown in the subnet
        /// listing for this section.
        /// </summary>
        public readonly bool ShowVlanInSubnetListing;
        /// <summary>
        /// `true` if VRFs are being shown in the subnet
        /// listing for this section.
        /// </summary>
        public readonly bool ShowVrfInSubnetListing;
        /// <summary>
        /// `true` if this subnet is set up to check that IP addresses
        /// are valid for the subnets they are in.
        /// </summary>
        public readonly bool StrictMode;
        /// <summary>
        /// How subnets in this section are ordered.
        /// </summary>
        public readonly string SubnetOrdering;

        [OutputConstructor]
        private GetSectionResult(
            string description,

            int displayOrder,

            int dnsResolverId,

            string editDate,

            string id,

            int masterSectionId,

            string name,

            string permissions,

            int sectionId,

            bool showSupernetOnly,

            bool showVlanInSubnetListing,

            bool showVrfInSubnetListing,

            bool strictMode,

            string subnetOrdering)
        {
            Description = description;
            DisplayOrder = displayOrder;
            DnsResolverId = dnsResolverId;
            EditDate = editDate;
            Id = id;
            MasterSectionId = masterSectionId;
            Name = name;
            Permissions = permissions;
            SectionId = sectionId;
            ShowSupernetOnly = showSupernetOnly;
            ShowVlanInSubnetListing = showVlanInSubnetListing;
            ShowVrfInSubnetListing = showVrfInSubnetListing;
            StrictMode = strictMode;
            SubnetOrdering = subnetOrdering;
        }
    }
}
