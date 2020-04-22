# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class NodeSize(str, Enum):

    none = "None"
    small = "Small"
    medium = "Medium"
    large = "Large"


class NodeSizeFamily(str, Enum):

    none = "None"
    memory_optimized = "MemoryOptimized"


class ProvisioningState(str, Enum):

    provisioning = "Provisioning"
    succeeded = "Succeeded"
    deleting = "Deleting"
    failed = "Failed"
    delete_error = "DeleteError"


class OperationStatus(str, Enum):

    in_progress = "InProgress"
    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"


class GeoBackupPolicyState(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class QueryAggregationFunction(str, Enum):

    min = "min"
    max = "max"
    avg = "avg"
    sum = "sum"


class QueryExecutionType(str, Enum):

    any = "any"
    regular = "regular"
    irregular = "irregular"
    aborted = "aborted"
    exception = "exception"


class QueryObservedMetricType(str, Enum):

    cpu = "cpu"
    io = "io"
    logio = "logio"
    duration = "duration"
    execution_count = "executionCount"


class QueryMetricUnit(str, Enum):

    percentage = "percentage"
    kb = "KB"
    microseconds = "microseconds"


class RestorePointType(str, Enum):

    continuous = "CONTINUOUS"
    discrete = "DISCRETE"


class ReplicationRole(str, Enum):

    primary = "Primary"
    secondary = "Secondary"
    non_readable_secondary = "NonReadableSecondary"
    source = "Source"
    copy = "Copy"


class ReplicationState(str, Enum):

    pending = "PENDING"
    seeding = "SEEDING"
    catch_up = "CATCH_UP"
    suspended = "SUSPENDED"


class TransparentDataEncryptionStatus(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class BlobAuditingPolicyState(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class ManagementOperationState(str, Enum):

    pending = "Pending"
    in_progress = "InProgress"
    succeeded = "Succeeded"
    failed = "Failed"
    cancel_in_progress = "CancelInProgress"
    cancelled = "Cancelled"


class ColumnDataType(str, Enum):

    image = "image"
    text = "text"
    uniqueidentifier = "uniqueidentifier"
    date_enum = "date"
    time = "time"
    datetime2 = "datetime2"
    datetimeoffset = "datetimeoffset"
    tinyint = "tinyint"
    smallint = "smallint"
    int_enum = "int"
    smalldatetime = "smalldatetime"
    real = "real"
    money = "money"
    datetime_enum = "datetime"
    float_enum = "float"
    sql_variant = "sql_variant"
    ntext = "ntext"
    bit = "bit"
    decimal_enum = "decimal"
    numeric = "numeric"
    smallmoney = "smallmoney"
    bigint = "bigint"
    hierarchyid = "hierarchyid"
    geometry = "geometry"
    geography = "geography"
    varbinary = "varbinary"
    varchar = "varchar"
    binary = "binary"
    char = "char"
    timestamp = "timestamp"
    nvarchar = "nvarchar"
    nchar = "nchar"
    xml = "xml"
    sysname = "sysname"


class VulnerabilityAssessmentScanTriggerType(str, Enum):

    on_demand = "OnDemand"
    recurring = "Recurring"


class VulnerabilityAssessmentScanState(str, Enum):

    passed = "Passed"
    failed = "Failed"
    failed_to_run = "FailedToRun"
    in_progress = "InProgress"


class SecurityAlertPolicyState(str, Enum):

    new = "New"
    enabled = "Enabled"
    disabled = "Disabled"


class ResourceIdentityType(str, Enum):

    none = "None"
    system_assigned = "SystemAssigned"


class IntegrationRuntimeType(str, Enum):

    managed = "Managed"
    self_hosted = "SelfHosted"


class IntegrationRuntimeState(str, Enum):

    initial = "Initial"
    stopped = "Stopped"
    started = "Started"
    starting = "Starting"
    stopping = "Stopping"
    need_registration = "NeedRegistration"
    online = "Online"
    limited = "Limited"
    offline = "Offline"
    access_denied = "AccessDenied"


class DataFlowComputeType(str, Enum):

    general = "General"
    memory_optimized = "MemoryOptimized"
    compute_optimized = "ComputeOptimized"


class IntegrationRuntimeSsisCatalogPricingTier(str, Enum):

    basic = "Basic"
    standard = "Standard"
    premium = "Premium"
    premium_rs = "PremiumRS"


class IntegrationRuntimeLicenseType(str, Enum):

    base_price = "BasePrice"
    license_included = "LicenseIncluded"


class IntegrationRuntimeEntityReferenceType(str, Enum):

    integration_runtime_reference = "IntegrationRuntimeReference"
    linked_service_reference = "LinkedServiceReference"


class IntegrationRuntimeEdition(str, Enum):

    standard = "Standard"
    enterprise = "Enterprise"


class ManagedIntegrationRuntimeNodeStatus(str, Enum):

    starting = "Starting"
    available = "Available"
    recycling = "Recycling"
    unavailable = "Unavailable"


class IntegrationRuntimeInternalChannelEncryptionMode(str, Enum):

    not_set = "NotSet"
    ssl_encrypted = "SslEncrypted"
    not_encrypted = "NotEncrypted"


class SelfHostedIntegrationRuntimeNodeStatus(str, Enum):

    need_registration = "NeedRegistration"
    online = "Online"
    limited = "Limited"
    offline = "Offline"
    upgrading = "Upgrading"
    initializing = "Initializing"
    initialize_failed = "InitializeFailed"


class IntegrationRuntimeUpdateResult(str, Enum):

    none = "None"
    succeed = "Succeed"
    fail = "Fail"


class IntegrationRuntimeAutoUpdate(str, Enum):

    on = "On"
    off = "Off"


class IntegrationRuntimeAuthKeyName(str, Enum):

    auth_key1 = "authKey1"
    auth_key2 = "authKey2"


class SsisObjectMetadataType(str, Enum):

    folder = "Folder"
    project = "Project"
    package = "Package"
    environment = "Environment"


class VulnerabilityAssessmentPolicyBaselineName(str, Enum):

    master = "master"
    default = "default"