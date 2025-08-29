# PhrasesApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**phrasesCreate**](#phrasescreate) | **POST** /phrases/ | Create a new phrase|
|[**phrasesDestroy**](#phrasesdestroy) | **DELETE** /phrases/{uuid}/ | Delete a phrase|
|[**phrasesList**](#phraseslist) | **GET** /phrases/ | List all phrases|
|[**phrasesModifyCreate**](#phrasesmodifycreate) | **POST** /phrases/modify/ | Modify phrase translations|
|[**phrasesPartialUpdate**](#phrasespartialupdate) | **PATCH** /phrases/{uuid}/ | Partially update a phrase|
|[**phrasesRetrieve**](#phrasesretrieve) | **GET** /phrases/{uuid}/ | Retrieve a specific phrase by UUID|
|[**phrasesUpdate**](#phrasesupdate) | **PUT** /phrases/{uuid}/ | Update an existing phrase|

# **phrasesCreate**
> Phrase phrasesCreate(phrase)


### Example

```typescript
import {
    PhrasesApi,
    Configuration,
    Phrase
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new PhrasesApi(configuration);

let phrase: Phrase; //

const { status, data } = await apiInstance.phrasesCreate(
    phrase
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phrase** | **Phrase**|  | |


### Return type

**Phrase**

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

# **phrasesDestroy**
> phrasesDestroy()


### Example

```typescript
import {
    PhrasesApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new PhrasesApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.phrasesDestroy(
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

# **phrasesList**
> Array<Phrase> phrasesList()


### Example

```typescript
import {
    PhrasesApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new PhrasesApi(configuration);

const { status, data } = await apiInstance.phrasesList();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<Phrase>**

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

# **phrasesModifyCreate**
> PhraseModify phrasesModifyCreate(phraseModify)

Modify phrase translations for a given language. The \'language\' query parameter is required.

### Example

```typescript
import {
    PhrasesApi,
    Configuration,
    PhraseModify
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new PhrasesApi(configuration);

let language: string; //Language code for the translation (required). (default to undefined)
let phraseModify: PhraseModify; //

const { status, data } = await apiInstance.phrasesModifyCreate(
    language,
    phraseModify
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phraseModify** | **PhraseModify**|  | |
| **language** | [**string**] | Language code for the translation (required). | defaults to undefined|


### Return type

**PhraseModify**

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

# **phrasesPartialUpdate**
> Phrase phrasesPartialUpdate()


### Example

```typescript
import {
    PhrasesApi,
    Configuration,
    PatchedPhrase
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new PhrasesApi(configuration);

let uuid: string; // (default to undefined)
let patchedPhrase: PatchedPhrase; // (optional)

const { status, data } = await apiInstance.phrasesPartialUpdate(
    uuid,
    patchedPhrase
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedPhrase** | **PatchedPhrase**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Phrase**

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

# **phrasesRetrieve**
> Phrase phrasesRetrieve()


### Example

```typescript
import {
    PhrasesApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new PhrasesApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.phrasesRetrieve(
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Phrase**

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

# **phrasesUpdate**
> Phrase phrasesUpdate(phrase)


### Example

```typescript
import {
    PhrasesApi,
    Configuration,
    Phrase
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new PhrasesApi(configuration);

let uuid: string; // (default to undefined)
let phrase: Phrase; //

const { status, data } = await apiInstance.phrasesUpdate(
    uuid,
    phrase
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **phrase** | **Phrase**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Phrase**

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

