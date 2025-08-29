# Surah


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **string** |  | [readonly] [default to undefined]
**mushaf** | [**Mushaf**](Mushaf.md) |  | [readonly] [default to undefined]
**mushaf_uuid** | **string** |  | [default to undefined]
**name** | **string** |  | [default to undefined]
**names** | **string** |  | [readonly] [default to undefined]
**number** | **number** |  | [default to undefined]
**period** | **string** | * &#x60;makki&#x60; - Makki * &#x60;madani&#x60; - Madani | [optional] [default to undefined]
**search_terms** | **string** |  | [optional] [default to undefined]
**number_of_ayahs** | **string** |  | [readonly] [default to undefined]
**bismillah** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { Surah } from '@ntq/sdk';

const instance: Surah = {
    uuid,
    mushaf,
    mushaf_uuid,
    name,
    names,
    number,
    period,
    search_terms,
    number_of_ayahs,
    bismillah,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
