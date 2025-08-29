# OpenAPI Schema Fixes for TypeScript Axios Client Generation

## Summary

The OpenAPI schema has been fixed to ensure proper TypeScript Axios client generation. The following issues have been resolved:

## Issues Fixed

### 1. **Unnecessary multipart/form-data content types**
- **Problem**: Every endpoint was defined with `application/json`, `application/x-www-form-urlencoded`, and `multipart/form-data` content types, even for endpoints that only need JSON
- **Solution**: Removed unnecessary `multipart/form-data` and `form-urlencoded` content types from non-file-upload endpoints
- **Impact**: Reduces client complexity and prevents confusion in TypeScript generation

### 2. **File upload endpoints properly handled**  
- **Preserved multipart/form-data for legitimate file upload endpoints**:
  - `/mushafs/import/` (JSON file upload)
  - `/translations/import/` (JSON file upload) 
  - `/takhtits/{id}/import/` (JSON file upload)
  - `/recitations/{uuid}/upload/{surah_uuid}/` (MP3 file upload)
- **Result**: File upload functions now correctly accept `File` type parameters

### 3. **TypeScript enum conflicts resolved**
- **Problem**: OpenAPI generator was creating duplicate enum declarations causing compilation errors
- **Solution**: Used separate API and model packages with explicit exports to avoid enum conflicts
- **Result**: TypeScript client compiles successfully without errors

### 4. **Improved client structure**
- **Generated separate model and API files** for better organization
- **Clean API class exports** without conflicting enums
- **Proper multipart/form-data handling** for file uploads

## Files Modified

1. `sdk/schema.yaml` - Removed 34 unnecessary multipart/form-data definitions
2. `sdk/typescript/` - Completely regenerated with proper TypeScript structure

## Generated Client Features

✅ **File Upload Support**: `recitationsUploadCreate(surahUuid, uuid, file, wordTimestamps?)` properly handles MP3 uploads  
✅ **Clean TypeScript Types**: All interfaces and enums are properly generated without conflicts  
✅ **Axios Integration**: Full Axios support with proper request/response typing  
✅ **Proper Error Handling**: TypeScript compilation succeeds without errors  

## Verification

The TypeScript client now:
- Compiles successfully with `npm run build`
- Properly handles file uploads with multipart/form-data
- Provides clean API interfaces for all endpoints
- Avoids duplicate enum conflicts

## Usage Example

```typescript
import { RecitationsApi } from '@ntq/sdk';

const api = new RecitationsApi();

// File upload now works properly
const file = new File(['content'], 'surah.mp3', { type: 'audio/mpeg' });
await api.recitationsUploadCreate('surah-uuid', 'recitation-uuid', file);
```