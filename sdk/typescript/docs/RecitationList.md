# RecitationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **string** |  | [readonly] [default to undefined]
**status** | **string** | * &#x60;draft&#x60; - Draft * &#x60;pending_review&#x60; - Pending review * &#x60;published&#x60; - Published | [optional] [default to undefined]
**recitation_date** | **string** |  | [default to undefined]
**recitation_location** | **string** |  | [default to undefined]
**duration** | **string** |  | [default to undefined]
**recitation_type** | **string** |  | [default to undefined]
**created_at** | **string** |  | [readonly] [default to undefined]
**updated_at** | **string** |  | [readonly] [default to undefined]
**reciter_account_uuid** | **string** |  | [readonly] [default to undefined]
**mushaf_uuid** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { RecitationList } from '@ntq/sdk';

const instance: RecitationList = {
    uuid,
    status,
    recitation_date,
    recitation_location,
    duration,
    recitation_type,
    created_at,
    updated_at,
    reciter_account_uuid,
    mushaf_uuid,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
