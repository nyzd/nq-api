# HealthCheckResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **string** | Overall health status: healthy, degraded, or unhealthy | [default to undefined]
**services** | **{ [key: string]: { [key: string]: string; }; }** | Detailed status of individual services | [optional] [default to undefined]

## Example

```typescript
import { HealthCheckResponse } from '@ntq/sdk';

const instance: HealthCheckResponse = {
    status,
    services,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
