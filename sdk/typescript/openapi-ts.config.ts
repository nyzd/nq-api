import { defineConfig } from '@hey-api/openapi-ts';

export default defineConfig({
  input: '../schema.yaml',
  output: './src/',
  plugins: [{
    name: '@hey-api/client-axios',
    exportFromIndex: true,
  }], 
});
