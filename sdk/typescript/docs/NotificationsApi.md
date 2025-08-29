# NotificationsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**notificationsCreate**](#notificationscreate) | **POST** /notifications/ | Create a new notification|
|[**notificationsDestroy**](#notificationsdestroy) | **DELETE** /notifications/{id}/ | Delete a notification|
|[**notificationsList**](#notificationslist) | **GET** /notifications/ | List all notifications|
|[**notificationsMeList**](#notificationsmelist) | **GET** /notifications/me/ | Get the current user\&#39;s notifications (paginated)|
|[**notificationsOpenedRetrieve**](#notificationsopenedretrieve) | **GET** /notifications/opened/ | Mark a notification as opened|
|[**notificationsPartialUpdate**](#notificationspartialupdate) | **PATCH** /notifications/{id}/ | Partially update a notification|
|[**notificationsRetrieve**](#notificationsretrieve) | **GET** /notifications/{id}/ | Retrieve a specific notification by UUID|
|[**notificationsUpdate**](#notificationsupdate) | **PUT** /notifications/{id}/ | Update an existing notification|
|[**notificationsViewedRetrieve**](#notificationsviewedretrieve) | **GET** /notifications/viewed/ | Mark notifications as viewed|

# **notificationsCreate**
> Notification notificationsCreate(notification)


### Example

```typescript
import {
    NotificationsApi,
    Configuration,
    Notification
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new NotificationsApi(configuration);

let notification: Notification; //

const { status, data } = await apiInstance.notificationsCreate(
    notification
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **notification** | **Notification**|  | |


### Return type

**Notification**

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

# **notificationsDestroy**
> notificationsDestroy()


### Example

```typescript
import {
    NotificationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new NotificationsApi(configuration);

let id: number; //A unique integer value identifying this notification. (default to undefined)

const { status, data } = await apiInstance.notificationsDestroy(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] | A unique integer value identifying this notification. | defaults to undefined|


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

# **notificationsList**
> Array<Notification> notificationsList()


### Example

```typescript
import {
    NotificationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new NotificationsApi(configuration);

let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.notificationsList(
    limit,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**Array<Notification>**

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

# **notificationsMeList**
> Array<Notification> notificationsMeList()

Returns a paginated list of the current user\'s notifications. Marks notifications in the current page as \'got_notification\' if not already marked.

### Example

```typescript
import {
    NotificationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new NotificationsApi(configuration);

let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.notificationsMeList(
    limit,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**Array<Notification>**

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

# **notificationsOpenedRetrieve**
> { [key: string]: any; } notificationsOpenedRetrieve()

Marks a specific notification as \'opened_notification\' using its uuid (provided as a query parameter).

### Example

```typescript
import {
    NotificationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new NotificationsApi(configuration);

let uuid: string; //UUID of the notification to mark as opened. (default to undefined)

const { status, data } = await apiInstance.notificationsOpenedRetrieve(
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uuid** | [**string**] | UUID of the notification to mark as opened. | defaults to undefined|


### Return type

**{ [key: string]: any; }**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**400** |  |  -  |
|**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notificationsPartialUpdate**
> Notification notificationsPartialUpdate()


### Example

```typescript
import {
    NotificationsApi,
    Configuration,
    PatchedNotification
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new NotificationsApi(configuration);

let id: number; //A unique integer value identifying this notification. (default to undefined)
let patchedNotification: PatchedNotification; // (optional)

const { status, data } = await apiInstance.notificationsPartialUpdate(
    id,
    patchedNotification
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedNotification** | **PatchedNotification**|  | |
| **id** | [**number**] | A unique integer value identifying this notification. | defaults to undefined|


### Return type

**Notification**

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

# **notificationsRetrieve**
> Notification notificationsRetrieve()


### Example

```typescript
import {
    NotificationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new NotificationsApi(configuration);

let id: number; //A unique integer value identifying this notification. (default to undefined)

const { status, data } = await apiInstance.notificationsRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] | A unique integer value identifying this notification. | defaults to undefined|


### Return type

**Notification**

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

# **notificationsUpdate**
> Notification notificationsUpdate(notification)


### Example

```typescript
import {
    NotificationsApi,
    Configuration,
    Notification
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new NotificationsApi(configuration);

let id: number; //A unique integer value identifying this notification. (default to undefined)
let notification: Notification; //

const { status, data } = await apiInstance.notificationsUpdate(
    id,
    notification
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **notification** | **Notification**|  | |
| **id** | [**number**] | A unique integer value identifying this notification. | defaults to undefined|


### Return type

**Notification**

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

# **notificationsViewedRetrieve**
> { [key: string]: any; } notificationsViewedRetrieve()

Marks all notifications with status \'got_notification\' as \'viewed_notification\' for the current user.

### Example

```typescript
import {
    NotificationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new NotificationsApi(configuration);

const { status, data } = await apiInstance.notificationsViewedRetrieve();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**{ [key: string]: any; }**

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

