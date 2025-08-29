# Translation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **string** |  | [readonly] [default to undefined]
**mushaf_uuid** | **string** |  | [readonly] [default to undefined]
**translator_uuid** | **string** |  | [readonly] [default to undefined]
**language** | **string** | * &#x60;ar&#x60; - ar * &#x60;en&#x60; - en * &#x60;fr&#x60; - fr * &#x60;ur&#x60; - ur * &#x60;tr&#x60; - tr * &#x60;id&#x60; - id * &#x60;fa&#x60; - fa * &#x60;ru&#x60; - ru * &#x60;es&#x60; - es * &#x60;de&#x60; - de * &#x60;bn&#x60; - bn * &#x60;zh&#x60; - zh * &#x60;ms&#x60; - ms * &#x60;hi&#x60; - hi * &#x60;sw&#x60; - sw * &#x60;ps&#x60; - ps * &#x60;ku&#x60; - ku * &#x60;az&#x60; - az * &#x60;ha&#x60; - ha * &#x60;so&#x60; - so * &#x60;ta&#x60; - ta * &#x60;te&#x60; - te * &#x60;ml&#x60; - ml * &#x60;pa&#x60; - pa * &#x60;sd&#x60; - sd * &#x60;ug&#x60; - ug * &#x60;uz&#x60; - uz * &#x60;kk&#x60; - kk * &#x60;ky&#x60; - ky * &#x60;tk&#x60; - tk * &#x60;tg&#x60; - tg * &#x60;syr&#x60; - syr * &#x60;ber&#x60; - ber * &#x60;am&#x60; - am * &#x60;om&#x60; - om * &#x60;wo&#x60; - wo * &#x60;yo&#x60; - yo * &#x60;other&#x60; - other | [default to undefined]
**release_date** | **string** |  | [optional] [default to undefined]
**source** | **string** |  | [optional] [default to undefined]
**status** | **string** | * &#x60;draft&#x60; - Draft * &#x60;pending_review&#x60; - Pending review * &#x60;published&#x60; - Published | [optional] [default to undefined]

## Example

```typescript
import { Translation } from '@ntq/sdk';

const instance: Translation = {
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
