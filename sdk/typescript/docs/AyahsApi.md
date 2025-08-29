# AyahsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**ayahsCreate**](#ayahscreate) | **POST** /ayahs/ | Create a new Ayah record|
|[**ayahsDestroy**](#ayahsdestroy) | **DELETE** /ayahs/{uuid}/ | Delete an Ayah record|
|[**ayahsList**](#ayahslist) | **GET** /ayahs/ | List all Ayahs (Quran verses)|
|[**ayahsPartialUpdate**](#ayahspartialupdate) | **PATCH** /ayahs/{uuid}/ | Partially update an Ayah record|
|[**ayahsRetrieve**](#ayahsretrieve) | **GET** /ayahs/{uuid}/ | Retrieve a specific Ayah by UUID|
|[**ayahsUpdate**](#ayahsupdate) | **PUT** /ayahs/{uuid}/ | Update an existing Ayah record|

# **ayahsCreate**
> AyahAdd ayahsCreate(ayahAdd)


### Example

```typescript
import {
    AyahsApi,
    Configuration,
    AyahAdd
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new AyahsApi(configuration);

let ayahAdd: AyahAdd; //

const { status, data } = await apiInstance.ayahsCreate(
    ayahAdd
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **ayahAdd** | **AyahAdd**|  | |


### Return type

**AyahAdd**

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

# **ayahsDestroy**
> ayahsDestroy()


### Example

```typescript
import {
    AyahsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new AyahsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.ayahsDestroy(
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

# **ayahsList**
> Array<Ayah> ayahsList()


### Example

```typescript
import {
    AyahsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new AyahsApi(configuration);

let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let ordering: 'asc' | 'desc'; //Which field to use when ordering the results. (optional) (default to undefined)
let search: string; //A search term. (optional) (default to undefined)
let surahUuid: string; // (optional) (default to undefined)

const { status, data } = await apiInstance.ayahsList(
    limit,
    offset,
    ordering,
    search,
    surahUuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **ordering** | [**&#39;asc&#39; | &#39;desc&#39;**]**Array<&#39;asc&#39; &#124; &#39;desc&#39;>** | Which field to use when ordering the results. | (optional) defaults to undefined|
| **search** | [**string**] | A search term. | (optional) defaults to undefined|
| **surahUuid** | [**string**] |  | (optional) defaults to undefined|


### Return type

**Array<Ayah>**

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

# **ayahsPartialUpdate**
> Ayah ayahsPartialUpdate()


### Example

```typescript
import {
    AyahsApi,
    Configuration,
    PatchedAyah
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new AyahsApi(configuration);

let uuid: string; // (default to undefined)
let patchedAyah: PatchedAyah; // (optional)

const { status, data } = await apiInstance.ayahsPartialUpdate(
    uuid,
    patchedAyah
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedAyah** | **PatchedAyah**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Ayah**

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

# **ayahsRetrieve**
> AyahSerializerView ayahsRetrieve()


### Example

```typescript
import {
    AyahsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new AyahsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.ayahsRetrieve(
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**AyahSerializerView**

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

# **ayahsUpdate**
> Ayah ayahsUpdate(ayah)


### Example

```typescript
import {
    AyahsApi,
    Configuration,
    Ayah
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new AyahsApi(configuration);

let uuid: string; // (default to undefined)
let ayah: Ayah; //

const { status, data } = await apiInstance.ayahsUpdate(
    uuid,
    ayah
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **ayah** | **Ayah**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Ayah**

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

