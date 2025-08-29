# UsersApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**usersCreate**](#userscreate) | **POST** /users/ | Create a new user|
|[**usersDestroy**](#usersdestroy) | **DELETE** /users/{uuid}/ | Delete a user|
|[**usersList**](#userslist) | **GET** /users/ | List all users|
|[**usersPartialUpdate**](#userspartialupdate) | **PATCH** /users/{uuid}/ | Partially update a user|
|[**usersRetrieve**](#usersretrieve) | **GET** /users/{uuid}/ | Retrieve a specific user by UUID|
|[**usersUpdate**](#usersupdate) | **PUT** /users/{uuid}/ | Update an existing user|

# **usersCreate**
> User usersCreate(user)


### Example

```typescript
import {
    UsersApi,
    Configuration,
    User
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new UsersApi(configuration);

let user: User; //

const { status, data } = await apiInstance.usersCreate(
    user
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user** | **User**|  | |


### Return type

**User**

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

# **usersDestroy**
> usersDestroy()


### Example

```typescript
import {
    UsersApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new UsersApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.usersDestroy(
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uuid** | [**string**] |  | defaults to undefined|


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

# **usersList**
> Array<User> usersList()


### Example

```typescript
import {
    UsersApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new UsersApi(configuration);

const { status, data } = await apiInstance.usersList();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<User>**

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

# **usersPartialUpdate**
> User usersPartialUpdate()


### Example

```typescript
import {
    UsersApi,
    Configuration,
    PatchedUser
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new UsersApi(configuration);

let uuid: string; // (default to undefined)
let patchedUser: PatchedUser; // (optional)

const { status, data } = await apiInstance.usersPartialUpdate(
    uuid,
    patchedUser
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedUser** | **PatchedUser**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**User**

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

# **usersRetrieve**
> User usersRetrieve()


### Example

```typescript
import {
    UsersApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new UsersApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.usersRetrieve(
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**User**

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

# **usersUpdate**
> User usersUpdate(user)


### Example

```typescript
import {
    UsersApi,
    Configuration,
    User
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new UsersApi(configuration);

let uuid: string; // (default to undefined)
let user: User; //

const { status, data } = await apiInstance.usersUpdate(
    uuid,
    user
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user** | **User**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**User**

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

