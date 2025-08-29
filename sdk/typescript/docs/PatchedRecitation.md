# PatchedRecitation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **string** |  | [optional] [readonly] [default to undefined]
**mushaf_uuid** | **string** |  | [optional] [default to undefined]
**get_mushaf_uuid** | **string** |  | [optional] [readonly] [default to undefined]
**status** | **string** | * &#x60;draft&#x60; - Draft * &#x60;pending_review&#x60; - Pending review * &#x60;published&#x60; - Published | [optional] [default to undefined]
**reciter_account_uuid** | **string** |  | [optional] [default to undefined]
**recitation_date** | **string** |  | [optional] [default to undefined]
**recitation_location** | **string** |  | [optional] [default to undefined]
**duration** | **string** |  | [optional] [default to undefined]
**recitation_type** | **string** |  | [optional] [default to undefined]
**created_at** | **string** |  | [optional] [readonly] [default to undefined]
**updated_at** | **string** |  | [optional] [readonly] [default to undefined]
**words_timestamps** | **string** |  | [optional] [readonly] [default to undefined]
**ayahs_timestamps** | **string** |  | [optional] [readonly] [default to undefined]

## Example

```typescript
import { PatchedRecitation } from '@ntq/sdk';

const instance: PatchedRecitation = {
    uuid,
    mushaf_uuid,
    get_mushaf_uuid,
    status,
    reciter_account_uuid,
    recitation_date,
    recitation_location,
    duration,
    recitation_type,
    created_at,
    updated_at,
    words_timestamps,
    ayahs_timestamps,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
