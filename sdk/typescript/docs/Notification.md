# Notification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **string** |  | [readonly] [default to undefined]
**resource_controller** | **string** |  | [default to undefined]
**resource_action** | **string** |  | [default to undefined]
**resource_uuid** | **string** |  | [optional] [default to undefined]
**status** | **string** | * &#x60;nothing_happened&#x60; - Nothing Happened * &#x60;got_notification&#x60; - User Got Notification * &#x60;viewed_notification&#x60; - User Viewed Notification * &#x60;opened_notification&#x60; - User Opened Notification | [optional] [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**message** | **string** |  | [optional] [default to undefined]
**message_type** | **string** | * &#x60;success&#x60; - Success * &#x60;failed&#x60; - Failed * &#x60;warning&#x60; - Warning * &#x60;pending&#x60; - Pending | [optional] [default to undefined]
**created_at** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { Notification } from '@ntq/sdk';

const instance: Notification = {
    uuid,
    resource_controller,
    resource_action,
    resource_uuid,
    status,
    description,
    message,
    message_type,
    created_at,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
