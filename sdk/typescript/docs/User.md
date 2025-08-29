# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **string** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [default to undefined]
**password** | **string** |  | [default to undefined]
**password2** | **string** |  | [default to undefined]
**email** | **string** |  | [default to undefined]
**first_name** | **string** |  | [optional] [default to undefined]
**last_name** | **string** |  | [optional] [default to undefined]

## Example

```typescript
import { User } from '@ntq/sdk';

const instance: User = {
    username,
    password,
    password2,
    email,
    first_name,
    last_name,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
