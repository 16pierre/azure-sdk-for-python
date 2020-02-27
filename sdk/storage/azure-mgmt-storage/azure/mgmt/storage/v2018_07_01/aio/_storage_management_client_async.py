# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import StorageManagementClientConfiguration
from .operations_async import Operations
from .operations_async import SkusOperations
from .operations_async import StorageAccountsOperations
from .operations_async import UsagesOperations
from .operations_async import BlobServicesOperations
from .operations_async import BlobContainersOperations
from .operations_async import ManagementPoliciesOperations
from .. import models


class StorageManagementClient(object):
    """The Azure Storage Management API.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.storage.v2018_07_01.aio.operations_async.Operations
    :ivar skus: SkusOperations operations
    :vartype skus: azure.mgmt.storage.v2018_07_01.aio.operations_async.SkusOperations
    :ivar storage_accounts: StorageAccountsOperations operations
    :vartype storage_accounts: azure.mgmt.storage.v2018_07_01.aio.operations_async.StorageAccountsOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.storage.v2018_07_01.aio.operations_async.UsagesOperations
    :ivar blob_services: BlobServicesOperations operations
    :vartype blob_services: azure.mgmt.storage.v2018_07_01.aio.operations_async.BlobServicesOperations
    :ivar blob_containers: BlobContainersOperations operations
    :vartype blob_containers: azure.mgmt.storage.v2018_07_01.aio.operations_async.BlobContainersOperations
    :ivar management_policies: ManagementPoliciesOperations operations
    :vartype management_policies: azure.mgmt.storage.v2018_07_01.aio.operations_async.ManagementPoliciesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = StorageManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.skus = SkusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.storage_accounts = StorageAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.blob_services = BlobServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.blob_containers = BlobContainersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.management_policies = ManagementPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "StorageManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
