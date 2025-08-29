# AyahBreakersResponse

Serializer for the ayahs_breakers endpoint response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **string** | UUID of the ayah | [default to undefined]
**surah** | **number** | Surah number | [default to undefined]
**ayah** | **number** | Ayah number | [default to undefined]
**juz** | **number** | Juz number (null if not a juz breaker) | [default to undefined]
**hizb** | **number** | Hizb number (null if not a hizb breaker) | [default to undefined]
**ruku** | **number** | Ruku number (null if not a ruku breaker) | [default to undefined]
**page** | **number** | Page number (null if not a page breaker) | [default to undefined]
**rub** | **number** | Rub number (null if not a rub breaker) | [default to undefined]
**manzil** | **number** | Manzil number (null if not a manzil breaker) | [default to undefined]

## Example

```typescript
import { AyahBreakersResponse } from '@ntq/sdk';

const instance: AyahBreakersResponse = {
    uuid,
    surah,
    ayah,
    juz,
    hizb,
    ruku,
    page,
    rub,
    manzil,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
