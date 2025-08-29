# LoginResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **string** | Authentication token | [default to undefined]
**user** | [**User**](User.md) | User information | [default to undefined]
**expiry** | **string** | Token expiry time | [default to undefined]

## Example

```typescript
import { LoginResponse } from '@ntq/sdk';

const instance: LoginResponse = {
    token,
    user,
    expiry,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
