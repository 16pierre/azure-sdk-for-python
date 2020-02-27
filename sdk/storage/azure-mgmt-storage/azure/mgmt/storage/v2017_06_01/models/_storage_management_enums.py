# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class ReasonCode(str, Enum):
    """The reason for the restriction. As of now this can be "QuotaId" or
    "NotAvailableForSubscription". Quota Id is set when the SKU has requiredQuotas parameter as the
    subscription does not belong to that quota. The "NotAvailableForSubscription" is related to
    capacity at DC.
    """

    quota_id = "QuotaId"
    not_available_for_subscription = "NotAvailableForSubscription"

class SkuName(str, Enum):
    """Gets or sets the sku name. Required for account creation; optional for update. Note that in
    older versions, sku name was called accountType.
    """

    standard_lrs = "Standard_LRS"
    standard_grs = "Standard_GRS"
    standard_ragrs = "Standard_RAGRS"
    standard_zrs = "Standard_ZRS"
    premium_lrs = "Premium_LRS"

class SkuTier(str, Enum):
    """Gets the sku tier. This is based on the SKU name.
    """

    standard = "Standard"
    premium = "Premium"

class Kind(str, Enum):
    """Indicates the type of storage account.
    """

    storage = "Storage"
    blob_storage = "BlobStorage"

class State(str, Enum):
    """Gets the state of virtual network rule.
    """

    provisioning = "provisioning"
    deprovisioning = "deprovisioning"
    succeeded = "succeeded"
    failed = "failed"
    network_source_deleted = "networkSourceDeleted"

class ProvisioningState(str, Enum):
    """Gets the status of the storage account at the time the operation was called.
    """

    creating = "Creating"
    resolving_dns = "ResolvingDNS"
    succeeded = "Succeeded"

class AccountStatus(str, Enum):
    """Gets the status indicating whether the primary location of the storage account is available or
    unavailable.
    """

    available = "available"
    unavailable = "unavailable"

class KeySource(str, Enum):
    """The encryption keySource (provider). Possible values (case-insensitive):  Microsoft.Storage,
    Microsoft.Keyvault
    """

    microsoft_storage = "Microsoft.Storage"
    microsoft_keyvault = "Microsoft.Keyvault"

class AccessTier(str, Enum):
    """Required for storage accounts where kind = BlobStorage. The access tier used for billing.
    """

    hot = "Hot"
    cool = "Cool"

class Bypass(str, Enum):
    """Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Possible values are
    any combination of Logging|Metrics|AzureServices (For example, "Logging, Metrics"), or None to
    bypass none of those traffics.
    """

    none = "None"
    logging = "Logging"
    metrics = "Metrics"
    azure_services = "AzureServices"

class DefaultAction(str, Enum):
    """Specifies the default action of allow or deny when no other rules match.
    """

    allow = "Allow"
    deny = "Deny"

class KeyPermission(str, Enum):
    """Permissions for the key -- read-only or full permissions.
    """

    read = "Read"
    full = "Full"

class UsageUnit(str, Enum):
    """Gets the unit of measurement.
    """

    count = "Count"
    bytes = "Bytes"
    seconds = "Seconds"
    percent = "Percent"
    counts_per_second = "CountsPerSecond"
    bytes_per_second = "BytesPerSecond"

class Services(str, Enum):
    """The signed services accessible with the account SAS. Possible values include: Blob (b), Queue
    (q), Table (t), File (f).
    """

    b = "b"
    q = "q"
    t = "t"
    f = "f"

class SignedResourceTypes(str, Enum):
    """The signed resource types that are accessible with the account SAS. Service (s): Access to
    service-level APIs; Container (c): Access to container-level APIs; Object (o): Access to
    object-level APIs for blobs, queue messages, table entities, and files.
    """

    s = "s"
    c = "c"
    o = "o"

class Permissions(str, Enum):
    """The signed permissions for the account SAS. Possible values include: Read (r), Write (w),
    Delete (d), List (l), Add (a), Create (c), Update (u) and Process (p).
    """

    r = "r"
    d = "d"
    w = "w"
    l = "l"
    a = "a"
    c = "c"
    u = "u"
    p = "p"

class SignedResource(str, Enum):
    """The signed services accessible with the service SAS. Possible values include: Blob (b),
    Container (c), File (f), Share (s).
    """

    b = "b"
    c = "c"
    f = "f"
    s = "s"

class Reason(str, Enum):
    """Gets the reason that a storage account name could not be used. The Reason element is only
    returned if NameAvailable is false.
    """

    account_name_invalid = "AccountNameInvalid"
    already_exists = "AlreadyExists"

class HttpProtocol(str, Enum):
    """The protocol permitted for a request made with the account SAS.
    """

    https_http = "https,http"
    https = "https"
