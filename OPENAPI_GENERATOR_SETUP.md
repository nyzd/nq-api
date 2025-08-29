# OpenAPI Generator TypeScript Axios Client Setup

## Summary

Successfully configured OpenAPI Generator to generate proper TypeScript Axios client code from the Django REST Framework OpenAPI schema. The solution uses OpenAPI Generator's additional properties and configuration options to handle schema complexities correctly.

## OpenAPI Generator Configuration

The correct command to generate the TypeScript Axios client:

```bash
openapi-generator-cli generate \
  -i sdk/schema.yaml \
  -g typescript-axios \
  -o sdk/typescript \
  --additional-properties=npmName="@ntq/sdk",npmVersion="1.1.71",withSeparateModelsAndApi=true,modelPackage=models,apiPackage=api,supportsES6=true,useSingleRequestParameter=false,generateAliasAsModel=false,skipFormModel=true,enumPropertyNaming=PascalCase,ensureUniqueParams=true,sortParamsByRequiredFlag=true
```

## Key Configuration Properties

### **Core Structure**
- `withSeparateModelsAndApi=true` - Separates models and API classes into different packages
- `modelPackage=models` - Models go in the `models/` directory  
- `apiPackage=api` - API classes go in the `api/` directory

### **Form Handling**
- `skipFormModel=true` - Skips generating form models (crucial for multipart/form-data endpoints)
- `useSingleRequestParameter=false` - Uses multiple parameters instead of single request objects

### **Type Generation**
- `generateAliasAsModel=false` - Prevents duplicate model generation for simple aliases
- `ensureUniqueParams=true` - Ensures parameter names are unique to avoid conflicts
- `enumPropertyNaming=PascalCase` - Consistent enum naming convention

### **Code Quality**
- `supportsES6=true` - Generates modern ES6 compatible code
- `sortParamsByRequiredFlag=true` - Required parameters come first
- `sortModelPropertiesByRequiredFlag=true` - Consistent property ordering

## Post-Generation Fix

After generation, the `api.ts` file exports need to be modified to avoid enum conflicts:

**Replace:**
```typescript
export * from './api/auth-api';
export * from './api/ayahs-api';
// ... other exports
```

**With:**
```typescript
// Export API classes directly to avoid enum conflicts
export { AuthApi } from './api/auth-api';
export { AyahsApi } from './api/ayahs-api';
// ... other exports
```

## File Upload Support

The configuration properly handles multipart/form-data endpoints. For example, the `recitationsUploadCreate` method:

```typescript
async recitationsUploadCreate(
  surahUuid: string, 
  uuid: string, 
  file: File, 
  wordTimestamps?: string, 
  options?: RawAxiosRequestConfig
): Promise<AxiosResponse<{ [key: string]: any; }>>
```

**Implementation details:**
- Correctly accepts `File` type parameters
- Generates proper FormData handling
- Sets `multipart/form-data` Content-Type headers
- Handles optional parameters like `word_timestamps`

## Generated Structure

```
sdk/typescript/
├── api/                    # API classes
│   ├── auth-api.ts
│   ├── recitations-api.ts
│   └── ...
├── models/                 # Type definitions
│   ├── ayah.ts
│   ├── recitation.ts
│   └── index.ts
├── api.ts                  # Main API exports (fixed)
├── base.ts                 # Base functionality
├── common.ts               # Common utilities
├── configuration.ts        # Configuration types
└── index.ts                # Main entry point
```

## Usage Example

```typescript
import { RecitationsApi } from '@ntq/sdk';

const api = new RecitationsApi();

// Regular JSON API call
const recitation = await api.recitationsCreate({
  mushaf_uuid: 'uuid',
  recitation_date: '2024-01-01',
  // ... other fields
});

// File upload with multipart/form-data
const file = new File(['audio data'], 'surah.mp3', { type: 'audio/mpeg' });
await api.recitationsUploadCreate(
  'surah-uuid', 
  'recitation-uuid', 
  file, 
  '["optional", "timestamps"]'  // optional word_timestamps as JSON string
);
```

## Key Benefits

✅ **Proper TypeScript Types** - All interfaces generated correctly  
✅ **File Upload Support** - Multipart/form-data handled properly  
✅ **Clean API Structure** - Separated models and APIs prevent conflicts  
✅ **No Compilation Errors** - TypeScript builds successfully  
✅ **Modern Code Generation** - ES6+ compatible output  
✅ **Flexible Configuration** - Easy to regenerate with schema updates  

## Regeneration Process

When the Django API schema changes:

1. Regenerate the schema: `python manage.py spectacular --file sdk/schema.yaml`
2. Regenerate the client: Run the OpenAPI Generator command above
3. Apply the api.ts export fix
4. Build and test: `cd sdk/typescript && npm run build`

This approach ensures the TypeScript client stays in sync with the API while properly handling all content types and file uploads.