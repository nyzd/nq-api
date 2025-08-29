# Django REST Framework OpenAPI Schema Fixes

## Summary

Fixed the Django REST Framework API configuration to generate proper OpenAPI schema for TypeScript Axios client generation. The issue was resolved by configuring DRF to use JSON-only content types for regular CRUD operations while preserving multipart/form-data for legitimate file upload endpoints.

## Root Cause

The issue was that Django REST Framework was automatically generating multiple content types (`application/json`, `application/x-www-form-urlencoded`, and `multipart/form-data`) for all endpoints by default, even when they don't need file upload capabilities. This caused the OpenAPI generator to create unnecessary and confusing TypeScript interfaces.

## Solution Applied

### 1. **Configure Default Parser Classes** 
Updated `api/settings.py` to limit default parsers to JSON only:

```python
REST_FRAMEWORK = {
    # ... other settings ...
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
}
```

### 2. **Explicit Content Type Specification**
Updated all ViewSets to explicitly specify JSON content types in their `@extend_schema` decorators:

**Files Updated:**
- `account/views.py` - UserViewSet, GroupViewSet, AuthViewSet
- `core/views.py` - ErrorLogViewSet, PhraseViewSet, NotificationViewSet  
- `quran/views/ayahs/views.py` - AyahViewSet
- `quran/views/mushafs/views.py` - MushafViewSet
- `quran/views/recitations/views.py` - RecitationViewSet
- `quran/views/surahs/views.py` - SurahViewSet
- `quran/views/takhtits/views.py` - TakhtitViewSet
- `quran/views/translations/views.py` - TranslationViewSet
- `quran/views/words/views.py` - WordViewSet

**Example Fix:**
```python
@extend_schema_view(
    create=extend_schema(
        summary="Create a new record",
        request={'application/json': MySerializer}  # ✅ Explicit JSON content type
    ),
    update=extend_schema(
        summary="Update an existing record",
        request={'application/json': MySerializer}  # ✅ Explicit JSON content type
    ),
    # ... other methods
)
```

### 3. **Preserved File Upload Endpoints**
File upload actions already had proper configuration:

```python
@action(detail=True, methods=["post"], parser_classes=[MultiPartParser, FormParser])
def upload(self, request, *args, **kwargs):
    # File upload logic with proper multipart/form-data handling
```

## File Upload Endpoints Preserved

The following endpoints correctly maintain multipart/form-data support:
- `/mushafs/import/` - JSON file upload
- `/translations/import/` - JSON file upload  
- `/takhtits/{id}/import/` - JSON file upload
- `/recitations/{uuid}/upload/{surah_uuid}/` - MP3 file upload

## Results

### ✅ **TypeScript Client Generation**
- **Compiles successfully** without TypeScript errors
- **Clean API interfaces** with proper JSON content types only  
- **File uploads work correctly** with `File` type parameters
- **No duplicate enums** or naming conflicts
- **Proper separation** between models and API classes

### ✅ **OpenAPI Schema**
- **JSON-only content types** for regular CRUD operations
- **Multipart/form-data preserved** only for legitimate file uploads
- **Clean schema generation** from Django REST Framework
- **Consistent content type specification** across all endpoints

## Verification

1. **Schema Generation**: OpenAPI schema now generates with clean content types
2. **TypeScript Compilation**: `npm run build` succeeds without errors
3. **File Upload Support**: Upload endpoints properly accept `File` parameters
4. **API Structure**: Clean separation between API classes and models

## Usage Example

```typescript
import { RecitationsApi } from '@ntq/sdk';

const api = new RecitationsApi();

// Regular API calls use JSON
const recitation = await api.recitationsCreate({
    mushaf_uuid: 'uuid',
    recitation_date: '2024-01-01',
    // ... other JSON data
});

// File uploads work with proper File type
const file = new File(['audio data'], 'surah.mp3', { type: 'audio/mpeg' });
await api.recitationsUploadCreate('surah-uuid', 'recitation-uuid', file);
```

## Key Takeaway

The fix was implemented at the **Django REST Framework configuration level** rather than modifying the auto-generated `schema.yaml` file. This ensures:

1. **Maintainable solution** - Schema is auto-generated correctly
2. **Proper separation of concerns** - File uploads vs regular JSON APIs  
3. **TypeScript compatibility** - Clean interfaces for client generation
4. **Future-proof** - New endpoints will follow the same pattern