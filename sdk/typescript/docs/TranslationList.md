# TranslationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **string** |  | [readonly] [default to undefined]
**mushaf_uuid** | **string** |  | [readonly] [default to undefined]
**translator_uuid** | **string** |  | [readonly] [default to undefined]
**language** | **string** |  | [default to undefined]
**release_date** | **string** |  | [optional] [default to undefined]
**source** | **string** |  | [optional] [default to undefined]
**status** | **string** | * &#x60;draft&#x60; - Draft * &#x60;pending_review&#x60; - Pending review * &#x60;published&#x60; - Published | [optional] [default to undefined]

## Example

```typescript
import { TranslationList } from '@ntq/sdk';

const instance: TranslationList = {
    uuid,
    mushaf_uuid,
    translator_uuid,
    language,
    release_date,
    source,
    status,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
