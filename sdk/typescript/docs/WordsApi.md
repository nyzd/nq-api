# WordsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**wordsCreate**](#wordscreate) | **POST** /words/ | Create a new Word record|
|[**wordsDestroy**](#wordsdestroy) | **DELETE** /words/{uuid}/ | Delete a Word record|
|[**wordsList**](#wordslist) | **GET** /words/ | List all Words in Ayahs|
|[**wordsPartialUpdate**](#wordspartialupdate) | **PATCH** /words/{uuid}/ | Partially update a Word record|
|[**wordsRetrieve**](#wordsretrieve) | **GET** /words/{uuid}/ | Retrieve a specific Word by UUID|
|[**wordsUpdate**](#wordsupdate) | **PUT** /words/{uuid}/ | Update an existing Word record|

# **wordsCreate**
> Word wordsCreate(word)


### Example

```typescript
import {
    WordsApi,
    Configuration,
    Word
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new WordsApi(configuration);

let word: Word; //
let ayahUuid: string; //UUID of the Ayah to associate the new Word with (if ayah_id is not provided in the body). (optional) (default to undefined)

const { status, data } = await apiInstance.wordsCreate(
    word,
    ayahUuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **word** | **Word**|  | |
| **ayahUuid** | [**string**] | UUID of the Ayah to associate the new Word with (if ayah_id is not provided in the body). | (optional) defaults to undefined|


### Return type

**Word**

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

# **wordsDestroy**
> wordsDestroy()


### Example

```typescript
import {
    WordsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new WordsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.wordsDestroy(
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

# **wordsList**
> Array<Word> wordsList()


### Example

```typescript
import {
    WordsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new WordsApi(configuration);

let ayahUuid: string; //UUID of the Ayah to filter Words by. (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let ordering: 'asc' | 'desc'; //Which field to use when ordering the results. (optional) (default to undefined)
let search: string; //A search term. (optional) (default to undefined)

const { status, data } = await apiInstance.wordsList(
    ayahUuid,
    limit,
    offset,
    ordering,
    search
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **ayahUuid** | [**string**] | UUID of the Ayah to filter Words by. | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **ordering** | [**&#39;asc&#39; | &#39;desc&#39;**]**Array<&#39;asc&#39; &#124; &#39;desc&#39;>** | Which field to use when ordering the results. | (optional) defaults to undefined|
| **search** | [**string**] | A search term. | (optional) defaults to undefined|


### Return type

**Array<Word>**

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

# **wordsPartialUpdate**
> Word wordsPartialUpdate()


### Example

```typescript
import {
    WordsApi,
    Configuration,
    PatchedWord
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new WordsApi(configuration);

let uuid: string; // (default to undefined)
let patchedWord: PatchedWord; // (optional)

const { status, data } = await apiInstance.wordsPartialUpdate(
    uuid,
    patchedWord
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedWord** | **PatchedWord**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Word**

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

# **wordsRetrieve**
> Word wordsRetrieve()


### Example

```typescript
import {
    WordsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new WordsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.wordsRetrieve(
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Word**

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

# **wordsUpdate**
> Word wordsUpdate(word)


### Example

```typescript
import {
    WordsApi,
    Configuration,
    Word
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new WordsApi(configuration);

let uuid: string; // (default to undefined)
let word: Word; //

const { status, data } = await apiInstance.wordsUpdate(
    uuid,
    word
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **word** | **Word**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Word**

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

