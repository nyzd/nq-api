# AyahSerializerView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **string** |  | [readonly] [default to undefined]
**number** | **number** |  | [default to undefined]
**sajdah** | **string** | * &#x60;none&#x60; - None | [optional] [default to undefined]
**text** | **string** |  | [readonly] [default to undefined]
**breakers** | **string** |  | [readonly] [default to undefined]
**bismillah** | **string** |  | [readonly] [default to undefined]
**surah** | [**SurahInAyah**](SurahInAyah.md) |  | [readonly] [default to undefined]
**mushaf** | **string** |  | [readonly] [default to undefined]
**words** | [**Array&lt;Word&gt;**](Word.md) |  | [readonly] [default to undefined]

## Example

```typescript
import { AyahSerializerView } from '@ntq/sdk';

const instance: AyahSerializerView = {
    uuid,
    number,
    sajdah,
    text,
    breakers,
    bismillah,
    surah,
    mushaf,
    words,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
