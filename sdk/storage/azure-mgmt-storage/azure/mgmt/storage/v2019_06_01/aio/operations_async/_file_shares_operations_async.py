# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMError

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class FileSharesOperations:
    """FileSharesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.storage.v2019_06_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        resource_group_name: str,
        account_name: str,
        maxpagesize: Optional[str] = None,
        filter: Optional[str] = None,
        **kwargs
    ) -> "models.FileShareItems":
        """Lists all shares.

        :param resource_group_name: The name of the resource group within the user's subscription. The
     name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
     Storage account names must be between 3 and 24 characters in length and use numbers and lower-
     case letters only.
        :type account_name: str
        :param maxpagesize: Optional. Specified maximum number of shares that can be included in the
     list.
        :type maxpagesize: str
        :param filter: Optional. When specified, only share names starting with the filter will be
     listed.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileShareItems or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_06_01.models.FileShareItems
        :raises: ~azure.mgmt.core.ARMError
        """
        cls: ClsType["models.FileShareItems"] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-06-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters: Dict[str, Any] = {}
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
            if maxpagesize is not None:
                query_parameters['$maxpagesize'] = self._serialize.query("maxpagesize", maxpagesize, 'str')
            if filter is not None:
                query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

            # Construct headers
            header_parameters: Dict[str, Any] = {}
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('FileShareItems', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares'}

    async def create(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        metadata: Optional[Dict[str, str]] = None,
        share_quota: Optional[int] = None,
        **kwargs
    ) -> "models.FileShare":
        """Creates a new share under the specified account as described by request body. The share resource includes metadata and properties for that share. It does not include a list of the files contained by the share.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and lower-
         case letters only.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number.
        :type share_name: str
        :param metadata: A name-value pair to associate with the share as metadata.
        :type metadata: dict[str, str]
        :param share_quota: The maximum size of the share, in gigabytes. Must be greater than 0, and
         less than or equal to 5TB (5120). For Large File Shares, the maximum size is 102400.
        :type share_quota: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileShare or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_06_01.models.FileShare or ~azure.mgmt.storage.v2019_06_01.models.FileShare
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType["models.FileShare"] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        _file_share = models.FileShare(metadata=metadata, share_quota=share_quota)
        api_version = "2019-06-01"

        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
            'shareName': self._serialize.url("share_name", share_name, 'str', max_length=63, min_length=3),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(_file_share, 'FileShare')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('FileShare', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('FileShare', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}'}

    async def update(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        metadata: Optional[Dict[str, str]] = None,
        share_quota: Optional[int] = None,
        **kwargs
    ) -> "models.FileShare":
        """Updates share properties as specified in request body. Properties not mentioned in the request will not be changed. Update fails if the specified share does not already exist.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and lower-
         case letters only.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number.
        :type share_name: str
        :param metadata: A name-value pair to associate with the share as metadata.
        :type metadata: dict[str, str]
        :param share_quota: The maximum size of the share, in gigabytes. Must be greater than 0, and
         less than or equal to 5TB (5120). For Large File Shares, the maximum size is 102400.
        :type share_quota: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileShare or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_06_01.models.FileShare
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType["models.FileShare"] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        _file_share = models.FileShare(metadata=metadata, share_quota=share_quota)
        api_version = "2019-06-01"

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
            'shareName': self._serialize.url("share_name", share_name, 'str', max_length=63, min_length=3),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(_file_share, 'FileShare')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = self._deserialize('FileShare', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}'}

    async def get(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        **kwargs
    ) -> "models.FileShare":
        """Gets properties of a specified share.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and lower-
         case letters only.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number.
        :type share_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileShare or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_06_01.models.FileShare
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType["models.FileShare"] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-06-01"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
            'shareName': self._serialize.url("share_name", share_name, 'str', max_length=63, min_length=3),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = self._deserialize('FileShare', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}'}

    async def delete(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        **kwargs
    ) -> None:
        """Deletes specified share under its account.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and lower-
         case letters only.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number.
        :type share_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-06-01"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
            'shareName': self._serialize.url("share_name", share_name, 'str', max_length=63, min_length=3),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}'}
