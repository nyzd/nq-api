# TranslationsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**translationsAyahsCreate**](#translationsayahscreate) | **POST** /translations/{uuid}/ayahs/{ayah_uuid}/ | Create or update (upsert) a specific AyahTranslation|
|[**translationsAyahsList**](#translationsayahslist) | **GET** /translations/{uuid}/ayahs/ | List all AyahTranslations for this Translation|
|[**translationsAyahsRetrieve**](#translationsayahsretrieve) | **GET** /translations/{uuid}/ayahs/{ayah_uuid}/ | Retrieve a single AyahTranslation for this Translation|
|[**translationsAyahsUpdate**](#translationsayahsupdate) | **PUT** /translations/{uuid}/ayahs/{ayah_uuid}/ | Create or update (upsert) a specific AyahTranslation|
|[**translationsCreate**](#translationscreate) | **POST** /translations/ | Create a new Translation record|
|[**translationsDestroy**](#translationsdestroy) | **DELETE** /translations/{uuid}/ | Delete a Translation record|
|[**translationsImportCreate**](#translationsimportcreate) | **POST** /translations/import/ | Import a Translation from a JSON file upload|
|[**translationsList**](#translationslist) | **GET** /translations/ | List all Quran Translations|
|[**translationsPartialUpdate**](#translationspartialupdate) | **PATCH** /translations/{uuid}/ | Partially update a Translation record|
|[**translationsRetrieve**](#translationsretrieve) | **GET** /translations/{uuid}/ | Retrieve a specific Translation by UUID|
|[**translationsUpdate**](#translationsupdate) | **PUT** /translations/{uuid}/ | Update an existing Translation record|

# **translationsAyahsCreate**
> AyahTranslation translationsAyahsCreate()

Provide the ayah\'s UUID in the URL path and the translation\'s UUID as the primary resource path. Body requires only `text` (and optional `bismillah`). If an AyahTranslation already exists it will be updated, otherwise it will be created.

### Example

```typescript
import {
    TranslationsApi,
    Configuration,
    TranslationsAyahsUpdateRequest
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TranslationsApi(configuration);

let ayahUuid: string; // (default to undefined)
let uuid: string; // (default to undefined)
let translationsAyahsUpdateRequest: TranslationsAyahsUpdateRequest; // (optional)

const { status, data } = await apiInstance.translationsAyahsCreate(
    ayahUuid,
    uuid,
    translationsAyahsUpdateRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **translationsAyahsUpdateRequest** | **TranslationsAyahsUpdateRequest**|  | |
| **ayahUuid** | [**string**] |  | defaults to undefined|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**AyahTranslation**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** |  |  -  |
|**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translationsAyahsList**
> Array<AyahTranslation> translationsAyahsList()

Returns a paginated list of all AyahTranslation objects for the given Translation UUID. Optionally filter by surah_uuid (query param).

### Example

```typescript
import {
    TranslationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TranslationsApi(configuration);

let uuid: string; // (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let ordering: 'asc' | 'desc'; //Which field to use when ordering the results. (optional) (default to undefined)
let search: string; //A search term. (optional) (default to undefined)
let surahUuid: string; //UUID of the Surah to filter AyahTranslations by. (optional) (default to undefined)

const { status, data } = await apiInstance.translationsAyahsList(
    uuid,
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
| **uuid** | [**string**] |  | defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **ordering** | [**&#39;asc&#39; | &#39;desc&#39;**]**Array<&#39;asc&#39; &#124; &#39;desc&#39;>** | Which field to use when ordering the results. | (optional) defaults to undefined|
| **search** | [**string**] | A search term. | (optional) defaults to undefined|
| **surahUuid** | [**string**] | UUID of the Surah to filter AyahTranslations by. | (optional) defaults to undefined|


### Return type

**Array<AyahTranslation>**

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

# **translationsAyahsRetrieve**
> AyahTranslation translationsAyahsRetrieve()

Returns a single AyahTranslation object for the given Translation UUID and Ayah UUID. URL: /translations/{translation_uuid}/ayahs/{ayah_uuid}/

### Example

```typescript
import {
    TranslationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TranslationsApi(configuration);

let ayahUuid: string; // (default to undefined)
let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.translationsAyahsRetrieve(
    ayahUuid,
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **ayahUuid** | [**string**] |  | defaults to undefined|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**AyahTranslation**

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

# **translationsAyahsUpdate**
> AyahTranslation translationsAyahsUpdate()

Provide the ayah\'s UUID in the URL path and the translation\'s UUID as the primary resource path. Body requires only `text` (and optional `bismillah`). If an AyahTranslation already exists it will be updated, otherwise it will be created.

### Example

```typescript
import {
    TranslationsApi,
    Configuration,
    TranslationsAyahsUpdateRequest
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TranslationsApi(configuration);

let ayahUuid: string; // (default to undefined)
let uuid: string; // (default to undefined)
let translationsAyahsUpdateRequest: TranslationsAyahsUpdateRequest; // (optional)

const { status, data } = await apiInstance.translationsAyahsUpdate(
    ayahUuid,
    uuid,
    translationsAyahsUpdateRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **translationsAyahsUpdateRequest** | **TranslationsAyahsUpdateRequest**|  | |
| **ayahUuid** | [**string**] |  | defaults to undefined|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**AyahTranslation**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** |  |  -  |
|**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translationsCreate**
> TranslationList translationsCreate(translationList)


### Example

```typescript
import {
    TranslationsApi,
    Configuration,
    TranslationList
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TranslationsApi(configuration);

let translationList: TranslationList; //

const { status, data } = await apiInstance.translationsCreate(
    translationList
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **translationList** | **TranslationList**|  | |


### Return type

**TranslationList**

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

# **translationsDestroy**
> translationsDestroy()


### Example

```typescript
import {
    TranslationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TranslationsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.translationsDestroy(
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

# **translationsImportCreate**
> TranslationList translationsImportCreate()


### Example

```typescript
import {
    TranslationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TranslationsApi(configuration);

let file: File; //JSON file containing the Translation data (default to undefined)

const { status, data } = await apiInstance.translationsImportCreate(
    file
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **file** | [**File**] | JSON file containing the Translation data | defaults to undefined|


### Return type

**TranslationList**

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

# **translationsList**
> Array<TranslationList> translationsList()


### Example

```typescript
import {
    TranslationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TranslationsApi(configuration);

let mushaf: 'hafs'; //Short name of the Mushaf to filter Translations by. Common value: \'hafs\'. Any string is accepted. (e.g. \'hafs\', \'warsh\', etc.) (default to undefined)
let language: 'ber' | 'aa' | 'ab' | 'ae' | 'af' | 'ak' | 'am' | 'an' | 'ar' | 'as' | 'av' | 'ay' | 'az' | 'ba' | 'be' | 'bg' | 'bh' | 'bi' | 'bm' | 'bn' | 'bo' | 'br' | 'bs' | 'ca' | 'ce' | 'ch' | 'co' | 'cr' | 'cs' | 'cu' | 'cv' | 'cy' | 'da' | 'de' | 'dv' | 'dz' | 'ee' | 'el' | 'en' | 'eo' | 'es' | 'et' | 'eu' | 'fa' | 'ff' | 'fi' | 'fj' | 'fo' | 'fr' | 'fy' | 'ga' | 'gd' | 'gl' | 'gn' | 'gu' | 'gv' | 'ha' | 'he' | 'hi' | 'ho' | 'hr' | 'ht' | 'hu' | 'hy' | 'hz' | 'ia' | 'id' | 'ie' | 'ig' | 'ii' | 'ik' | 'io' | 'is' | 'it' | 'iu' | 'ja' | 'jv' | 'ka' | 'kg' | 'ki' | 'kj' | 'kk' | 'kl' | 'km' | 'kn' | 'ko' | 'kr' | 'ks' | 'ku' | 'kv' | 'kw' | 'ky' | 'la' | 'lb' | 'lg' | 'li' | 'ln' | 'lo' | 'lt' | 'lu' | 'lv' | 'mg' | 'mh' | 'mi' | 'mk' | 'ml' | 'mn' | 'mr' | 'ms' | 'mt' | 'my' | 'na' | 'nb' | 'nd' | 'ne' | 'ng' | 'nl' | 'nn' | 'no' | 'nr' | 'nv' | 'ny' | 'oc' | 'oj' | 'om' | 'or' | 'os' | 'pa' | 'pi' | 'pl' | 'ps' | 'pt' | 'qu' | 'rm' | 'rn' | 'ro' | 'ru' | 'rw' | 'sa' | 'sc' | 'sd' | 'se' | 'sg' | 'si' | 'sk' | 'sl' | 'sm' | 'sn' | 'so' | 'sq' | 'sr' | 'ss' | 'st' | 'su' | 'sv' | 'sw' | 'ta' | 'te' | 'tg' | 'th' | 'ti' | 'tk' | 'tl' | 'tn' | 'to' | 'tr' | 'ts' | 'tt' | 'tw' | 'ty' | 'ug' | 'uk' | 'ur' | 'uz' | 've' | 'vi' | 'vo' | 'wa' | 'wo' | 'xh' | 'yi' | 'yo' | 'za' | 'zh' | 'zu'; //Language code to filter Translations by. (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let ordering: 'asc' | 'desc'; //Which field to use when ordering the results. (optional) (default to undefined)
let search: string; //A search term. (optional) (default to undefined)

const { status, data } = await apiInstance.translationsList(
    mushaf,
    language,
    limit,
    offset,
    ordering,
    search
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mushaf** | [**&#39;hafs&#39;**]**Array<&#39;hafs&#39;>** | Short name of the Mushaf to filter Translations by. Common value: \&#39;hafs\&#39;. Any string is accepted. (e.g. \&#39;hafs\&#39;, \&#39;warsh\&#39;, etc.) | defaults to undefined|
| **language** | [**&#39;ber&#39; | &#39;aa&#39; | &#39;ab&#39; | &#39;ae&#39; | &#39;af&#39; | &#39;ak&#39; | &#39;am&#39; | &#39;an&#39; | &#39;ar&#39; | &#39;as&#39; | &#39;av&#39; | &#39;ay&#39; | &#39;az&#39; | &#39;ba&#39; | &#39;be&#39; | &#39;bg&#39; | &#39;bh&#39; | &#39;bi&#39; | &#39;bm&#39; | &#39;bn&#39; | &#39;bo&#39; | &#39;br&#39; | &#39;bs&#39; | &#39;ca&#39; | &#39;ce&#39; | &#39;ch&#39; | &#39;co&#39; | &#39;cr&#39; | &#39;cs&#39; | &#39;cu&#39; | &#39;cv&#39; | &#39;cy&#39; | &#39;da&#39; | &#39;de&#39; | &#39;dv&#39; | &#39;dz&#39; | &#39;ee&#39; | &#39;el&#39; | &#39;en&#39; | &#39;eo&#39; | &#39;es&#39; | &#39;et&#39; | &#39;eu&#39; | &#39;fa&#39; | &#39;ff&#39; | &#39;fi&#39; | &#39;fj&#39; | &#39;fo&#39; | &#39;fr&#39; | &#39;fy&#39; | &#39;ga&#39; | &#39;gd&#39; | &#39;gl&#39; | &#39;gn&#39; | &#39;gu&#39; | &#39;gv&#39; | &#39;ha&#39; | &#39;he&#39; | &#39;hi&#39; | &#39;ho&#39; | &#39;hr&#39; | &#39;ht&#39; | &#39;hu&#39; | &#39;hy&#39; | &#39;hz&#39; | &#39;ia&#39; | &#39;id&#39; | &#39;ie&#39; | &#39;ig&#39; | &#39;ii&#39; | &#39;ik&#39; | &#39;io&#39; | &#39;is&#39; | &#39;it&#39; | &#39;iu&#39; | &#39;ja&#39; | &#39;jv&#39; | &#39;ka&#39; | &#39;kg&#39; | &#39;ki&#39; | &#39;kj&#39; | &#39;kk&#39; | &#39;kl&#39; | &#39;km&#39; | &#39;kn&#39; | &#39;ko&#39; | &#39;kr&#39; | &#39;ks&#39; | &#39;ku&#39; | &#39;kv&#39; | &#39;kw&#39; | &#39;ky&#39; | &#39;la&#39; | &#39;lb&#39; | &#39;lg&#39; | &#39;li&#39; | &#39;ln&#39; | &#39;lo&#39; | &#39;lt&#39; | &#39;lu&#39; | &#39;lv&#39; | &#39;mg&#39; | &#39;mh&#39; | &#39;mi&#39; | &#39;mk&#39; | &#39;ml&#39; | &#39;mn&#39; | &#39;mr&#39; | &#39;ms&#39; | &#39;mt&#39; | &#39;my&#39; | &#39;na&#39; | &#39;nb&#39; | &#39;nd&#39; | &#39;ne&#39; | &#39;ng&#39; | &#39;nl&#39; | &#39;nn&#39; | &#39;no&#39; | &#39;nr&#39; | &#39;nv&#39; | &#39;ny&#39; | &#39;oc&#39; | &#39;oj&#39; | &#39;om&#39; | &#39;or&#39; | &#39;os&#39; | &#39;pa&#39; | &#39;pi&#39; | &#39;pl&#39; | &#39;ps&#39; | &#39;pt&#39; | &#39;qu&#39; | &#39;rm&#39; | &#39;rn&#39; | &#39;ro&#39; | &#39;ru&#39; | &#39;rw&#39; | &#39;sa&#39; | &#39;sc&#39; | &#39;sd&#39; | &#39;se&#39; | &#39;sg&#39; | &#39;si&#39; | &#39;sk&#39; | &#39;sl&#39; | &#39;sm&#39; | &#39;sn&#39; | &#39;so&#39; | &#39;sq&#39; | &#39;sr&#39; | &#39;ss&#39; | &#39;st&#39; | &#39;su&#39; | &#39;sv&#39; | &#39;sw&#39; | &#39;ta&#39; | &#39;te&#39; | &#39;tg&#39; | &#39;th&#39; | &#39;ti&#39; | &#39;tk&#39; | &#39;tl&#39; | &#39;tn&#39; | &#39;to&#39; | &#39;tr&#39; | &#39;ts&#39; | &#39;tt&#39; | &#39;tw&#39; | &#39;ty&#39; | &#39;ug&#39; | &#39;uk&#39; | &#39;ur&#39; | &#39;uz&#39; | &#39;ve&#39; | &#39;vi&#39; | &#39;vo&#39; | &#39;wa&#39; | &#39;wo&#39; | &#39;xh&#39; | &#39;yi&#39; | &#39;yo&#39; | &#39;za&#39; | &#39;zh&#39; | &#39;zu&#39;**]**Array<&#39;ber&#39; &#124; &#39;aa&#39; &#124; &#39;ab&#39; &#124; &#39;ae&#39; &#124; &#39;af&#39; &#124; &#39;ak&#39; &#124; &#39;am&#39; &#124; &#39;an&#39; &#124; &#39;ar&#39; &#124; &#39;as&#39; &#124; &#39;av&#39; &#124; &#39;ay&#39; &#124; &#39;az&#39; &#124; &#39;ba&#39; &#124; &#39;be&#39; &#124; &#39;bg&#39; &#124; &#39;bh&#39; &#124; &#39;bi&#39; &#124; &#39;bm&#39; &#124; &#39;bn&#39; &#124; &#39;bo&#39; &#124; &#39;br&#39; &#124; &#39;bs&#39; &#124; &#39;ca&#39; &#124; &#39;ce&#39; &#124; &#39;ch&#39; &#124; &#39;co&#39; &#124; &#39;cr&#39; &#124; &#39;cs&#39; &#124; &#39;cu&#39; &#124; &#39;cv&#39; &#124; &#39;cy&#39; &#124; &#39;da&#39; &#124; &#39;de&#39; &#124; &#39;dv&#39; &#124; &#39;dz&#39; &#124; &#39;ee&#39; &#124; &#39;el&#39; &#124; &#39;en&#39; &#124; &#39;eo&#39; &#124; &#39;es&#39; &#124; &#39;et&#39; &#124; &#39;eu&#39; &#124; &#39;fa&#39; &#124; &#39;ff&#39; &#124; &#39;fi&#39; &#124; &#39;fj&#39; &#124; &#39;fo&#39; &#124; &#39;fr&#39; &#124; &#39;fy&#39; &#124; &#39;ga&#39; &#124; &#39;gd&#39; &#124; &#39;gl&#39; &#124; &#39;gn&#39; &#124; &#39;gu&#39; &#124; &#39;gv&#39; &#124; &#39;ha&#39; &#124; &#39;he&#39; &#124; &#39;hi&#39; &#124; &#39;ho&#39; &#124; &#39;hr&#39; &#124; &#39;ht&#39; &#124; &#39;hu&#39; &#124; &#39;hy&#39; &#124; &#39;hz&#39; &#124; &#39;ia&#39; &#124; &#39;id&#39; &#124; &#39;ie&#39; &#124; &#39;ig&#39; &#124; &#39;ii&#39; &#124; &#39;ik&#39; &#124; &#39;io&#39; &#124; &#39;is&#39; &#124; &#39;it&#39; &#124; &#39;iu&#39; &#124; &#39;ja&#39; &#124; &#39;jv&#39; &#124; &#39;ka&#39; &#124; &#39;kg&#39; &#124; &#39;ki&#39; &#124; &#39;kj&#39; &#124; &#39;kk&#39; &#124; &#39;kl&#39; &#124; &#39;km&#39; &#124; &#39;kn&#39; &#124; &#39;ko&#39; &#124; &#39;kr&#39; &#124; &#39;ks&#39; &#124; &#39;ku&#39; &#124; &#39;kv&#39; &#124; &#39;kw&#39; &#124; &#39;ky&#39; &#124; &#39;la&#39; &#124; &#39;lb&#39; &#124; &#39;lg&#39; &#124; &#39;li&#39; &#124; &#39;ln&#39; &#124; &#39;lo&#39; &#124; &#39;lt&#39; &#124; &#39;lu&#39; &#124; &#39;lv&#39; &#124; &#39;mg&#39; &#124; &#39;mh&#39; &#124; &#39;mi&#39; &#124; &#39;mk&#39; &#124; &#39;ml&#39; &#124; &#39;mn&#39; &#124; &#39;mr&#39; &#124; &#39;ms&#39; &#124; &#39;mt&#39; &#124; &#39;my&#39; &#124; &#39;na&#39; &#124; &#39;nb&#39; &#124; &#39;nd&#39; &#124; &#39;ne&#39; &#124; &#39;ng&#39; &#124; &#39;nl&#39; &#124; &#39;nn&#39; &#124; &#39;no&#39; &#124; &#39;nr&#39; &#124; &#39;nv&#39; &#124; &#39;ny&#39; &#124; &#39;oc&#39; &#124; &#39;oj&#39; &#124; &#39;om&#39; &#124; &#39;or&#39; &#124; &#39;os&#39; &#124; &#39;pa&#39; &#124; &#39;pi&#39; &#124; &#39;pl&#39; &#124; &#39;ps&#39; &#124; &#39;pt&#39; &#124; &#39;qu&#39; &#124; &#39;rm&#39; &#124; &#39;rn&#39; &#124; &#39;ro&#39; &#124; &#39;ru&#39; &#124; &#39;rw&#39; &#124; &#39;sa&#39; &#124; &#39;sc&#39; &#124; &#39;sd&#39; &#124; &#39;se&#39; &#124; &#39;sg&#39; &#124; &#39;si&#39; &#124; &#39;sk&#39; &#124; &#39;sl&#39; &#124; &#39;sm&#39; &#124; &#39;sn&#39; &#124; &#39;so&#39; &#124; &#39;sq&#39; &#124; &#39;sr&#39; &#124; &#39;ss&#39; &#124; &#39;st&#39; &#124; &#39;su&#39; &#124; &#39;sv&#39; &#124; &#39;sw&#39; &#124; &#39;ta&#39; &#124; &#39;te&#39; &#124; &#39;tg&#39; &#124; &#39;th&#39; &#124; &#39;ti&#39; &#124; &#39;tk&#39; &#124; &#39;tl&#39; &#124; &#39;tn&#39; &#124; &#39;to&#39; &#124; &#39;tr&#39; &#124; &#39;ts&#39; &#124; &#39;tt&#39; &#124; &#39;tw&#39; &#124; &#39;ty&#39; &#124; &#39;ug&#39; &#124; &#39;uk&#39; &#124; &#39;ur&#39; &#124; &#39;uz&#39; &#124; &#39;ve&#39; &#124; &#39;vi&#39; &#124; &#39;vo&#39; &#124; &#39;wa&#39; &#124; &#39;wo&#39; &#124; &#39;xh&#39; &#124; &#39;yi&#39; &#124; &#39;yo&#39; &#124; &#39;za&#39; &#124; &#39;zh&#39; &#124; &#39;zu&#39;>** | Language code to filter Translations by. | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **ordering** | [**&#39;asc&#39; | &#39;desc&#39;**]**Array<&#39;asc&#39; &#124; &#39;desc&#39;>** | Which field to use when ordering the results. | (optional) defaults to undefined|
| **search** | [**string**] | A search term. | (optional) defaults to undefined|


### Return type

**Array<TranslationList>**

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

# **translationsPartialUpdate**
> TranslationList translationsPartialUpdate()


### Example

```typescript
import {
    TranslationsApi,
    Configuration,
    PatchedTranslationList
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TranslationsApi(configuration);

let uuid: string; // (default to undefined)
let patchedTranslationList: PatchedTranslationList; // (optional)

const { status, data } = await apiInstance.translationsPartialUpdate(
    uuid,
    patchedTranslationList
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedTranslationList** | **PatchedTranslationList**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**TranslationList**

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

# **translationsRetrieve**
> Translation translationsRetrieve()


### Example

```typescript
import {
    TranslationsApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TranslationsApi(configuration);

let uuid: string; // (default to undefined)

const { status, data } = await apiInstance.translationsRetrieve(
    uuid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**Translation**

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

# **translationsUpdate**
> TranslationList translationsUpdate(translationList)


### Example

```typescript
import {
    TranslationsApi,
    Configuration,
    TranslationList
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new TranslationsApi(configuration);

let uuid: string; // (default to undefined)
let translationList: TranslationList; //

const { status, data } = await apiInstance.translationsUpdate(
    uuid,
    translationList
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **translationList** | **TranslationList**|  | |
| **uuid** | [**string**] |  | defaults to undefined|


### Return type

**TranslationList**

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

