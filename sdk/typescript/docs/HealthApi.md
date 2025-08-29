# HealthApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**healthRetrieve**](#healthretrieve) | **GET** /health/ | Health check endpoint|

# **healthRetrieve**
> HealthCheckResponse healthRetrieve()

Health check endpoint that verifies the status of PostgreSQL database, S3 storage, RabbitMQ, and Forced Alignment service connections. Returns detailed status information for staff users.

### Example

```typescript
import {
    HealthApi,
    Configuration
} from '@ntq/sdk';

const configuration = new Configuration();
const apiInstance = new HealthApi(configuration);

const { status, data } = await apiInstance.healthRetrieve();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**HealthCheckResponse**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** |  |  -  |
|**503** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

