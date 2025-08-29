# GroupsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**groupsCreate**](#groupscreate) | **POST** /groups/ | Create a new group|
|[**groupsDestroy**](#groupsdestroy) | **DELETE** /groups/{id}/ | Delete a group|
|[**groupsList**](#groupslist) | **GET** /groups/ | List all groups|
|[**groupsPartialUpdate**](#groupspartialupdate) | **PATCH** /groups/{id}/ | Partially update a group|
|[**groupsRetrieve**](#groupsretrieve) | **GET** /groups/{id}/ | Retrieve a specific group by ID|
|[**groupsUpdate**](#groupsupdate) | **PUT** /groups/{id}/ | Update an existing group|

# **groupsCreate**
> Group groupsCreate(group)


### Example

```typescript
import {
    GroupsApi,
    Configuration,
    Group
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new GroupsApi(configuration);

let group: Group; //

const { status, data } = await apiInstance.groupsCreate(
    group
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group** | **Group**|  | |


### Return type

**Group**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groupsDestroy**
> groupsDestroy()


### Example

```typescript
import {
    GroupsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new GroupsApi(configuration);

let id: number; //A unique integer value identifying this group. (default to undefined)

const { status, data } = await apiInstance.groupsDestroy(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] | A unique integer value identifying this group. | defaults to undefined|


### Return type

void (empty response body)

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groupsList**
> Array<Group> groupsList()


### Example

```typescript
import {
    GroupsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new GroupsApi(configuration);

const { status, data } = await apiInstance.groupsList();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<Group>**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groupsPartialUpdate**
> Group groupsPartialUpdate()


### Example

```typescript
import {
    GroupsApi,
    Configuration,
    PatchedGroup
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new GroupsApi(configuration);

let id: number; //A unique integer value identifying this group. (default to undefined)
let patchedGroup: PatchedGroup; // (optional)

const { status, data } = await apiInstance.groupsPartialUpdate(
    id,
    patchedGroup
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedGroup** | **PatchedGroup**|  | |
| **id** | [**number**] | A unique integer value identifying this group. | defaults to undefined|


### Return type

**Group**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groupsRetrieve**
> Group groupsRetrieve()


### Example

```typescript
import {
    GroupsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new GroupsApi(configuration);

let id: number; //A unique integer value identifying this group. (default to undefined)

const { status, data } = await apiInstance.groupsRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] | A unique integer value identifying this group. | defaults to undefined|


### Return type

**Group**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groupsUpdate**
> Group groupsUpdate(group)


### Example

```typescript
import {
    GroupsApi,
    Configuration,
    Group
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new GroupsApi(configuration);

let id: number; //A unique integer value identifying this group. (default to undefined)
let group: Group; //

const { status, data } = await apiInstance.groupsUpdate(
    id,
    group
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group** | **Group**|  | |
| **id** | [**number**] | A unique integer value identifying this group. | defaults to undefined|


### Return type

**Group**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

