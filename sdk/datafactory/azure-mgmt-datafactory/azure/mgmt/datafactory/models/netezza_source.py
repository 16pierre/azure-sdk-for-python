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

from .copy_source import CopySource


class NetezzaSource(CopySource):
    """A copy activity Netezza source.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param source_retry_count: Source retry count. Type: integer (or
     Expression with resultType integer).
    :type source_retry_count: object
    :param source_retry_wait: Source retry wait. Type: string (or Expression
     with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type source_retry_wait: object
    :param max_concurrent_connections: The maximum concurrent connection count
     for the source data store. Type: integer (or Expression with resultType
     integer).
    :type max_concurrent_connections: object
    :param type: Required. Constant filled by server.
    :type type: str
    :param query: A query to retrieve data from source. Type: string (or
     Expression with resultType string).
    :type query: object
    :param partition_option: The partition mechanism that will be used for
     Netezza read in parallel. Possible values include: 'None', 'DataSlice',
     'DynamicRange'
    :type partition_option: str or
     ~azure.mgmt.datafactory.models.NetezzaPartitionOption
    :param partition_settings: The settings that will be leveraged for Netezza
     source partitioning.
    :type partition_settings:
     ~azure.mgmt.datafactory.models.NetezzaPartitionSettings
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'source_retry_count': {'key': 'sourceRetryCount', 'type': 'object'},
        'source_retry_wait': {'key': 'sourceRetryWait', 'type': 'object'},
        'max_concurrent_connections': {'key': 'maxConcurrentConnections', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'query': {'key': 'query', 'type': 'object'},
        'partition_option': {'key': 'partitionOption', 'type': 'str'},
        'partition_settings': {'key': 'partitionSettings', 'type': 'NetezzaPartitionSettings'},
    }

    def __init__(self, **kwargs):
        super(NetezzaSource, self).__init__(**kwargs)
        self.query = kwargs.get('query', None)
        self.partition_option = kwargs.get('partition_option', None)
        self.partition_settings = kwargs.get('partition_settings', None)
        self.type = 'NetezzaSource'