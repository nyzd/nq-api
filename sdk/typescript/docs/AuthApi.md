# AuthApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**authLoginCreate**](#authlogincreate) | **POST** /auth/login/ | Login with username and password to obtain a Knox token|
|[**authLogoutCreate**](#authlogoutcreate) | **POST** /auth/logout/ | Logout current user|
|[**authLogoutallCreate**](#authlogoutallcreate) | **POST** /auth/logoutall/ | Logout from all devices|
|[**authRegisterCreate**](#authregistercreate) | **POST** /auth/register/ | Register a new user account|

# **authLoginCreate**
> LoginResponse authLoginCreate(login)

Authenticate user credentials and return an authentication token for API access

### Example

```typescript
import {
    AuthApi,
    Configuration,
    Login
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new AuthApi(configuration);

let login: Login; //

const { status, data } = await apiInstance.authLoginCreate(
    login
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **login** | **Login**|  | |


### Return type

**LoginResponse**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** | Invalid credentials or validation error |  -  |
|**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authLogoutCreate**
> LogoutResponse authLogoutCreate()

Invalidate the current user\'s authentication token. The user will need to login again to access protected endpoints.

### Example

```typescript
import {
    AuthApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new AuthApi(configuration);

const { status, data } = await apiInstance.authLogoutCreate();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**LogoutResponse**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** |  |  -  |
|**401** | Authentication required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authLogoutallCreate**
> LogoutAllResponse authLogoutallCreate()

Invalidate all authentication tokens for the current user across all devices. The user will need to login again on any device to access protected endpoints.

### Example

```typescript
import {
    AuthApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new AuthApi(configuration);

const { status, data } = await apiInstance.authLogoutallCreate();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**LogoutAllResponse**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** |  |  -  |
|**401** | Authentication required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authRegisterCreate**
> RegisterResponse authRegisterCreate(user)

Create a new user account with username, password, email, and optional personal information. Returns user data and authentication token upon successful registration.

### Example

```typescript
import {
    AuthApi,
    Configuration,
    User
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new AuthApi(configuration);

let user: User; //

const { status, data } = await apiInstance.authRegisterCreate(
    user
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user** | **User**|  | |


### Return type

**RegisterResponse**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** |  |  -  |
|**400** | Validation error or user already exists |  -  |
|**422** | Password validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

