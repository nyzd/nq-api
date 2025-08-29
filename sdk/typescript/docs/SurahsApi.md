# SurahsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**surahsCreate**](#surahscreate) | **POST** /surahs/ | Create a new Surah record|
|[**surahsDestroy**](#surahsdestroy) | **DELETE** /surahs/{uuid}/ | Delete a Surah record|
|[**surahsList**](#surahslist) | **GET** /surahs/ | List all Surahs (Quran chapters)|
|[**surahsPartialUpdate**](#surahspartialupdate) | **PATCH** /surahs/{uuid}/ | Partially update a Surah record|
|[**surahsRetrieve**](#surahsretrieve) | **GET** /surahs/{uuid}/ | Retrieve a specific Surah by UUID|
|[**surahsUpdate**](#surahsupdate) | **PUT** /surahs/{uuid}/ | Update an existing Surah record|

# **surahsCreate**
> Surah surahsCreate(surah)


### Example

```typescript
import {
    SurahsApi,
    Configuration,
    Surah
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new SurahsApi(configuration);

let surah: Surah; //

const { status, data } = await apiInstance.surahsCreate(
    surah
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **surah** | **Surah**|  | |


### Return type

**Surah**

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

# **surahsDestroy**
> surahsDestroy()


### Example

```typescript
import {
    SurahsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new SurahsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.surahsDestroy(
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

# **surahsList**
> Array<Surah> surahsList()


### Example

```typescript
import {
    SurahsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new SurahsApi(configuration);

let mushaf: 'hafs'; //Short name of the Mushaf to filter Surahs by. Common value: \'hafs\'. Any string is accepted. (e.g. \'hafs\', \'warsh\', etc.) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let ordering: 'asc' | 'desc'; //Which field to use when ordering the results. (optional) (default to undefined)
let search: string; //A search term. (optional) (default to undefined)

const { status, data } = await apiInstance.surahsList(
    mushaf,
    limit,
    offset,
    ordering,
    search
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mushaf** | [**&#39;hafs&#39;**]**Array<&#39;hafs&#39;>** | Short name of the Mushaf to filter Surahs by. Common value: \&#39;hafs\&#39;. Any string is accepted. (e.g. \&#39;hafs\&#39;, \&#39;warsh\&#39;, etc.) | defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **ordering** | [**&#39;asc&#39; | &#39;desc&#39;**]**Array<&#39;asc&#39; &#124; &#39;desc&#39;>** | Which field to use when ordering the results. | (optional) defaults to undefined|
| **search** | [**string**] | A search term. | (optional) defaults to undefined|


### Return type

**Array<Surah>**

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

# **surahsPartialUpdate**
> Surah surahsPartialUpdate()


### Example

```typescript
import {
    SurahsApi,
    Configuration,
    PatchedSurah
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new SurahsApi(configuration);

let uuid: string; // (default to undefined)
let patchedSurah: PatchedSurah; // (optional)

const { status, data } = await apiInstance.surahsPartialUpdate(
    uuid,
    patchedSurah
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedSurah** | **PatchedSurah**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Surah**

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

# **surahsRetrieve**
> SurahDetail surahsRetrieve()


### Example

```typescript
import {
    SurahsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new SurahsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.surahsRetrieve(
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**SurahDetail**

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

# **surahsUpdate**
> Surah surahsUpdate(surah)


### Example

```typescript
import {
    SurahsApi,
    Configuration,
    Surah
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new SurahsApi(configuration);

let uuid: string; // (default to undefined)
let surah: Surah; //

const { status, data } = await apiInstance.surahsUpdate(
    uuid,
    surah
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **surah** | **Surah**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Surah**

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

