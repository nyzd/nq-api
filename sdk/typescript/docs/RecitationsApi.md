# RecitationsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**recitationsCreate**](#recitationscreate) | **POST** /recitations/ | Create a new Recitation record|
|[**recitationsDestroy**](#recitationsdestroy) | **DELETE** /recitations/{uuid}/ | Delete a Recitation record|
|[**recitationsList**](#recitationslist) | **GET** /recitations/ | List all Recitations (audio recordings)|
|[**recitationsPartialUpdate**](#recitationspartialupdate) | **PATCH** /recitations/{uuid}/ | Partially update a Recitation record|
|[**recitationsRetrieve**](#recitationsretrieve) | **GET** /recitations/{uuid}/ | Retrieve a specific Recitation by UUID|
|[**recitationsUpdate**](#recitationsupdate) | **PUT** /recitations/{uuid}/ | Update an existing Recitation record|
|[**recitationsUploadCreate**](#recitationsuploadcreate) | **POST** /recitations/{uuid}/upload/{surah_uuid}/ | Upload a surah audio file and optional word-level timestamps for a Recitation|

# **recitationsCreate**
> Recitation recitationsCreate(recitation)


### Example

```typescript
import {
    RecitationsApi,
    Configuration,
    Recitation
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new RecitationsApi(configuration);

let recitation: Recitation; //

const { status, data } = await apiInstance.recitationsCreate(
    recitation
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recitation** | **Recitation**|  | |


### Return type

**Recitation**

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

# **recitationsDestroy**
> recitationsDestroy()


### Example

```typescript
import {
    RecitationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new RecitationsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.recitationsDestroy(
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

# **recitationsList**
> Array<RecitationList> recitationsList()


### Example

```typescript
import {
    RecitationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new RecitationsApi(configuration);

let mushaf: 'hafs'; //Short name of the Mushaf to filter Recitations by. Common value: \'hafs\'. Any string is accepted. (e.g. \'hafs\', \'warsh\', etc.) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let ordering: 'asc' | 'desc'; //Which field to use when ordering the results. (optional) (default to undefined)
let reciterUuid: string; //UUID of the Reciter to filter Recitations by. (optional) (default to undefined)
let search: string; //A search term. (optional) (default to undefined)

const { status, data } = await apiInstance.recitationsList(
    mushaf,
    limit,
    offset,
    ordering,
    reciterUuid,
    search
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mushaf** | [**&#39;hafs&#39;**]**Array<&#39;hafs&#39;>** | Short name of the Mushaf to filter Recitations by. Common value: \&#39;hafs\&#39;. Any string is accepted. (e.g. \&#39;hafs\&#39;, \&#39;warsh\&#39;, etc.) | defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **ordering** | [**&#39;asc&#39; | &#39;desc&#39;**]**Array<&#39;asc&#39; &#124; &#39;desc&#39;>** | Which field to use when ordering the results. | (optional) defaults to undefined|
| **reciterUuid** | [**string**] | UUID of the Reciter to filter Recitations by. | (optional) defaults to undefined|
| **search** | [**string**] | A search term. | (optional) defaults to undefined|


### Return type

**Array<RecitationList>**

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

# **recitationsPartialUpdate**
> Recitation recitationsPartialUpdate()


### Example

```typescript
import {
    RecitationsApi,
    Configuration,
    PatchedRecitation
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new RecitationsApi(configuration);

let uuid: string; // (default to undefined)
let patchedRecitation: PatchedRecitation; // (optional)

const { status, data } = await apiInstance.recitationsPartialUpdate(
    uuid,
    patchedRecitation
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedRecitation** | **PatchedRecitation**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Recitation**

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

# **recitationsRetrieve**
> Recitation recitationsRetrieve()


### Example

```typescript
import {
    RecitationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new RecitationsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.recitationsRetrieve(
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Recitation**

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

# **recitationsUpdate**
> Recitation recitationsUpdate(recitation)


### Example

```typescript
import {
    RecitationsApi,
    Configuration,
    Recitation
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new RecitationsApi(configuration);

let uuid: string; // (default to undefined)
let recitation: Recitation; //

const { status, data } = await apiInstance.recitationsUpdate(
    uuid,
    recitation
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recitation** | **Recitation**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Recitation**

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

# **recitationsUploadCreate**
> { [key: string]: any; } recitationsUploadCreate()

Accepts a multipart/form-data request with parts: file (mp3) and optional word_timestamps JSON list.

### Example

```typescript
import {
    RecitationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new RecitationsApi(configuration);

let surahUuid: string; // (default to undefined)
let uuid: string; // (default to undefined)
let file: File; // (default to undefined)
let wordTimestamps: string; //JSON list, optional (optional) (default to undefined)

const { status, data } = await apiInstance.recitationsUploadCreate(
    surahUuid,
    uuid,
    file,
    wordTimestamps
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **surahUuid** | [**string**] |  | defaults to undefined|
| **uuid** | [**string**] |  | defaults to undefined|
| **file** | [**File**] |  | defaults to undefined|
| **wordTimestamps** | [**string**] | JSON list, optional | (optional) defaults to undefined|


### Return type

**{ [key: string]: any; }**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

