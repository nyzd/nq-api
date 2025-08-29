# MushafsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**mushafsCreate**](#mushafscreate) | **POST** /mushafs/ | Create a new Mushaf record|
|[**mushafsDestroy**](#mushafsdestroy) | **DELETE** /mushafs/{uuid}/ | Delete a Mushaf record|
|[**mushafsImportCreate**](#mushafsimportcreate) | **POST** /mushafs/import/ | Import a Mushaf from a JSON file upload|
|[**mushafsList**](#mushafslist) | **GET** /mushafs/ | List all Mushafs (Quranic manuscripts/editions)|
|[**mushafsPartialUpdate**](#mushafspartialupdate) | **PATCH** /mushafs/{uuid}/ | Partially update a Mushaf record|
|[**mushafsRetrieve**](#mushafsretrieve) | **GET** /mushafs/{uuid}/ | Retrieve a specific Mushaf by UUID|
|[**mushafsUpdate**](#mushafsupdate) | **PUT** /mushafs/{uuid}/ | Update an existing Mushaf record|

# **mushafsCreate**
> Mushaf mushafsCreate(mushaf)


### Example

```typescript
import {
    MushafsApi,
    Configuration,
    Mushaf
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new MushafsApi(configuration);

let mushaf: Mushaf; //

const { status, data } = await apiInstance.mushafsCreate(
    mushaf
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mushaf** | **Mushaf**|  | |


### Return type

**Mushaf**

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

# **mushafsDestroy**
> mushafsDestroy()


### Example

```typescript
import {
    MushafsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new MushafsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.mushafsDestroy(
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

# **mushafsImportCreate**
> Mushaf mushafsImportCreate()


### Example

```typescript
import {
    MushafsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new MushafsApi(configuration);

let file: File; //JSON file containing the Mushaf data (default to undefined)

const { status, data } = await apiInstance.mushafsImportCreate(
    file
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **file** | [**File**] | JSON file containing the Mushaf data | defaults to undefined|


### Return type

**Mushaf**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mushafsList**
> Array<Mushaf> mushafsList()


### Example

```typescript
import {
    MushafsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new MushafsApi(configuration);

let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let ordering: 'asc' | 'desc'; //Which field to use when ordering the results. (optional) (default to undefined)
let search: string; //A search term. (optional) (default to undefined)

const { status, data } = await apiInstance.mushafsList(
    limit,
    offset,
    ordering,
    search
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **ordering** | [**&#39;asc&#39; | &#39;desc&#39;**]**Array<&#39;asc&#39; &#124; &#39;desc&#39;>** | Which field to use when ordering the results. | (optional) defaults to undefined|
| **search** | [**string**] | A search term. | (optional) defaults to undefined|


### Return type

**Array<Mushaf>**

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

# **mushafsPartialUpdate**
> Mushaf mushafsPartialUpdate()


### Example

```typescript
import {
    MushafsApi,
    Configuration,
    PatchedMushaf
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new MushafsApi(configuration);

let uuid: string; // (default to undefined)
let patchedMushaf: PatchedMushaf; // (optional)

const { status, data } = await apiInstance.mushafsPartialUpdate(
    uuid,
    patchedMushaf
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedMushaf** | **PatchedMushaf**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Mushaf**

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

# **mushafsRetrieve**
> Mushaf mushafsRetrieve()


### Example

```typescript
import {
    MushafsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new MushafsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.mushafsRetrieve(
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Mushaf**

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

# **mushafsUpdate**
> Mushaf mushafsUpdate(mushaf)


### Example

```typescript
import {
    MushafsApi,
    Configuration,
    Mushaf
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new MushafsApi(configuration);

let uuid: string; // (default to undefined)
let mushaf: Mushaf; //

const { status, data } = await apiInstance.mushafsUpdate(
    uuid,
    mushaf
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mushaf** | **Mushaf**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Mushaf**

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

