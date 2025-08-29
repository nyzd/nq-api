# ProfileApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**profileMeCreate**](#profilemecreate) | **POST** /profile/me/ | Get or update the current user\&#39;s profile|
|[**profileMeRetrieve**](#profilemeretrieve) | **GET** /profile/me/ | Get or update the current user\&#39;s profile|
|[**profileRetrieve**](#profileretrieve) | **GET** /profile/{uuid}/ | Retrieve the user\&#39;s profile by uuid|

# **profileMeCreate**
> Profile profileMeCreate(profile)

GET: Retrieve the current user\'s profile. POST: Update the current user\'s profile information.

### Example

```typescript
import {
    ProfileApi,
    Configuration,
    Profile
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new ProfileApi(configuration);

let profile: Profile; //

const { status, data } = await apiInstance.profileMeCreate(
    profile
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **profile** | **Profile**|  | |


### Return type

**Profile**

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

# **profileMeRetrieve**
> Profile profileMeRetrieve()

GET: Retrieve the current user\'s profile. POST: Update the current user\'s profile information.

### Example

```typescript
import {
    ProfileApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new ProfileApi(configuration);

const { status, data } = await apiInstance.profileMeRetrieve();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Profile**

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

# **profileRetrieve**
> Profile profileRetrieve()


### Example

```typescript
import {
    ProfileApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new ProfileApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.profileRetrieve(
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Profile**

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

