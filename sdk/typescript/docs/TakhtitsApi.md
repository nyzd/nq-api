# TakhtitsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**takhtitsAyahsBreakersCreate**](#takhtitsayahsbreakerscreate) | **POST** /takhtits/{uuid}/ayahs_breakers/ | Add an ayahs_breaker to this takhtit|
|[**takhtitsAyahsBreakersList**](#takhtitsayahsbreakerslist) | **GET** /takhtits/{uuid}/ayahs_breakers/ | List all ayahs_breakers for this takhtit (ayahs map style)|
|[**takhtitsAyahsBreakersRetrieve**](#takhtitsayahsbreakersretrieve) | **GET** /takhtits/{uuid}/ayahs_breakers/{breaker_uuid}/ | Retrieve a specific ayahs_breaker for this takhtit|
|[**takhtitsCreate**](#takhtitscreate) | **POST** /takhtits/ | Create a new Takhtit record|
|[**takhtitsDestroy**](#takhtitsdestroy) | **DELETE** /takhtits/{uuid}/ | Delete a Takhtit record|
|[**takhtitsImportCreate**](#takhtitsimportcreate) | **POST** /takhtits/{uuid}/import/ | Import Ayah Breakers for the specified Takhtit|
|[**takhtitsList**](#takhtitslist) | **GET** /takhtits/ | List all Takhtits (text annotations/notes)|
|[**takhtitsPartialUpdate**](#takhtitspartialupdate) | **PATCH** /takhtits/{uuid}/ | Partially update a Takhtit record|
|[**takhtitsRetrieve**](#takhtitsretrieve) | **GET** /takhtits/{uuid}/ | Retrieve a specific Takhtit by UUID|
|[**takhtitsUpdate**](#takhtitsupdate) | **PUT** /takhtits/{uuid}/ | Update an existing Takhtit record|
|[**takhtitsWordsBreakersCreate**](#takhtitswordsbreakerscreate) | **POST** /takhtits/{uuid}/words_breakers/ | Add a words_breaker to this takhtit|
|[**takhtitsWordsBreakersList**](#takhtitswordsbreakerslist) | **GET** /takhtits/{uuid}/words_breakers/ | List all words_breakers for this takhtit (with line counters)|
|[**takhtitsWordsBreakersRetrieve**](#takhtitswordsbreakersretrieve) | **GET** /takhtits/{uuid}/words_breakers/{breaker_uuid}/ | Retrieve a specific words_breaker for this takhtit|

# **takhtitsAyahsBreakersCreate**
> AyahBreaker takhtitsAyahsBreakersCreate()

Add a new ayahs_breaker to this takhtit. Requires ayah_uuid in the request body.

### Example

```typescript
import {
    TakhtitsApi,
    Configuration,
    TakhtitsAyahsBreakersCreateRequest
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TakhtitsApi(configuration);

let uuid: string; // (default to undefined)
let takhtitsAyahsBreakersCreateRequest: TakhtitsAyahsBreakersCreateRequest; // (optional)

const { status, data } = await apiInstance.takhtitsAyahsBreakersCreate(
    uuid,
    takhtitsAyahsBreakersCreateRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **takhtitsAyahsBreakersCreateRequest** | **TakhtitsAyahsBreakersCreateRequest**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**AyahBreaker**

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

# **takhtitsAyahsBreakersList**
> Array<AyahBreakersResponse> takhtitsAyahsBreakersList()

Returns a flat list containing an entry for every ayah in this takhtit, with breaker info similar to the mushaf ayah_map action.

### Example

```typescript
import {
    TakhtitsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TakhtitsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.takhtitsAyahsBreakersList(
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Array<AyahBreakersResponse>**

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

# **takhtitsAyahsBreakersRetrieve**
> AyahBreaker takhtitsAyahsBreakersRetrieve()


### Example

```typescript
import {
    TakhtitsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TakhtitsApi(configuration);

let breakerUuid: string; //UUID of the ayahs_breaker. (default to undefined)
let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.takhtitsAyahsBreakersRetrieve(
    breakerUuid,
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **breakerUuid** | [**string**] | UUID of the ayahs_breaker. | defaults to undefined|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**AyahBreaker**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **takhtitsCreate**
> Takhtit takhtitsCreate()

Create a new Takhtit. Requires mushaf_uuid and account_uuid in the request body.

### Example

```typescript
import {
    TakhtitsApi,
    Configuration,
    TakhtitsCreateRequest
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TakhtitsApi(configuration);

let takhtitsCreateRequest: TakhtitsCreateRequest; // (optional)

const { status, data } = await apiInstance.takhtitsCreate(
    takhtitsCreateRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **takhtitsCreateRequest** | **TakhtitsCreateRequest**|  | |


### Return type

**Takhtit**

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

# **takhtitsDestroy**
> takhtitsDestroy()


### Example

```typescript
import {
    TakhtitsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TakhtitsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.takhtitsDestroy(
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

# **takhtitsImportCreate**
> { [key: string]: any; } takhtitsImportCreate()

Accepts a JSON array of strings with the format \'{surah}:{ayah}\' that denote the ayah at which a new breaker (page by default) begins. Existing breakers whose names start with the provided breaker type (default: \'page\') will be removed before importing the new ones.

### Example

```typescript
import {
    TakhtitsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TakhtitsApi(configuration);

let uuid: string; // (default to undefined)
let file: File; //Text/JSON file containing a list of breakers (e.g. [\\\'2:1\\\', \\\'2:6\\\']). (default to undefined)
let type: string; //Breaker type (e.g., page, juz, hizb, ruku). Defaults to \'page\'. (optional) (default to undefined)

const { status, data } = await apiInstance.takhtitsImportCreate(
    uuid,
    file,
    type
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uuid** | [**string**] |  | defaults to undefined|
| **file** | [**File**] | Text/JSON file containing a list of breakers (e.g. [\\\&#39;2:1\\\&#39;, \\\&#39;2:6\\\&#39;]). | defaults to undefined|
| **type** | [**string**] | Breaker type (e.g., page, juz, hizb, ruku). Defaults to \&#39;page\&#39;. | (optional) defaults to undefined|


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

# **takhtitsList**
> Array<Takhtit> takhtitsList()


### Example

```typescript
import {
    TakhtitsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TakhtitsApi(configuration);

let mushaf: 'hafs'; //Short name of the Mushaf to filter Takhtits by. Common value: \'hafs\'. Any string is accepted. (e.g. \'hafs\', \'warsh\', etc.) (optional) (default to undefined)

const { status, data } = await apiInstance.takhtitsList(
    mushaf
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mushaf** | [**&#39;hafs&#39;**]**Array<&#39;hafs&#39;>** | Short name of the Mushaf to filter Takhtits by. Common value: \&#39;hafs\&#39;. Any string is accepted. (e.g. \&#39;hafs\&#39;, \&#39;warsh\&#39;, etc.) | (optional) defaults to undefined|


### Return type

**Array<Takhtit>**

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

# **takhtitsPartialUpdate**
> Takhtit takhtitsPartialUpdate()


### Example

```typescript
import {
    TakhtitsApi,
    Configuration,
    PatchedTakhtit
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TakhtitsApi(configuration);

let uuid: string; // (default to undefined)
let patchedTakhtit: PatchedTakhtit; // (optional)

const { status, data } = await apiInstance.takhtitsPartialUpdate(
    uuid,
    patchedTakhtit
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedTakhtit** | **PatchedTakhtit**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Takhtit**

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

# **takhtitsRetrieve**
> Takhtit takhtitsRetrieve()


### Example

```typescript
import {
    TakhtitsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TakhtitsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.takhtitsRetrieve(
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Takhtit**

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

# **takhtitsUpdate**
> Takhtit takhtitsUpdate(takhtit)


### Example

```typescript
import {
    TakhtitsApi,
    Configuration,
    Takhtit
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TakhtitsApi(configuration);

let uuid: string; // (default to undefined)
let takhtit: Takhtit; //

const { status, data } = await apiInstance.takhtitsUpdate(
    uuid,
    takhtit
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **takhtit** | **Takhtit**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Takhtit**

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

# **takhtitsWordsBreakersCreate**
> WordBreakerDetailResponse takhtitsWordsBreakersCreate()

Add a new words_breaker to this takhtit. Requires word_uuid in the request body. Only type \'line\' is allowed.

### Example

```typescript
import {
    TakhtitsApi,
    Configuration,
    TakhtitsWordsBreakersCreateRequest
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TakhtitsApi(configuration);

let uuid: string; // (default to undefined)
let takhtitsWordsBreakersCreateRequest: TakhtitsWordsBreakersCreateRequest; // (optional)

const { status, data } = await apiInstance.takhtitsWordsBreakersCreate(
    uuid,
    takhtitsWordsBreakersCreateRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **takhtitsWordsBreakersCreateRequest** | **TakhtitsWordsBreakersCreateRequest**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**WordBreakerDetailResponse**

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

# **takhtitsWordsBreakersList**
> Array<WordBreakersResponse> takhtitsWordsBreakersList()

Returns a flat list containing an entry for every word with a breaker for this takhtit, with a line counter (incremented for each breaker).

### Example

```typescript
import {
    TakhtitsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TakhtitsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.takhtitsWordsBreakersList(
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Array<WordBreakersResponse>**

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

# **takhtitsWordsBreakersRetrieve**
> WordBreakerDetailResponse takhtitsWordsBreakersRetrieve()


### Example

```typescript
import {
    TakhtitsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TakhtitsApi(configuration);

let breakerUuid: string; //UUID of the words_breaker. (default to undefined)
let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.takhtitsWordsBreakersRetrieve(
    breakerUuid,
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **breakerUuid** | [**string**] | UUID of the words_breaker. | defaults to undefined|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**WordBreakerDetailResponse**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

