## @ntq/sdk@1.1.71

This generator creates TypeScript/JavaScript client that utilizes [axios](https://github.com/axios/axios). The generated Node module can be used in the following environments:

Environment
* Node.js
* Webpack
* Browserify

Language level
* ES5 - you must have a Promises/A+ library installed
* ES6

Module system
* CommonJS
* ES6 module system

It can be used in both TypeScript and JavaScript. In TypeScript, the definition will be automatically resolved via `package.json`. ([Reference](https://www.typescriptlang.org/docs/handbook/declaration-files/consumption.html))

### Building

To build and compile the typescript sources to javascript use:
```
npm install
npm run build
```

### Publishing

First build the package then run `npm publish`

### Consuming

navigate to the folder of your consuming project and run one of the following commands.

_published:_

```
npm install @ntq/sdk@1.1.71 --save
```

_unPublished (not recommended):_

```
npm install PATH_TO_GENERATED_PACKAGE --save
```

### Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**authLoginCreate**](docs/AuthApi.md#authlogincreate) | **POST** /auth/login/ | Login with username and password to obtain a Knox token
*AuthApi* | [**authLogoutCreate**](docs/AuthApi.md#authlogoutcreate) | **POST** /auth/logout/ | Logout current user
*AuthApi* | [**authLogoutallCreate**](docs/AuthApi.md#authlogoutallcreate) | **POST** /auth/logoutall/ | Logout from all devices
*AuthApi* | [**authRegisterCreate**](docs/AuthApi.md#authregistercreate) | **POST** /auth/register/ | Register a new user account
*AyahsApi* | [**ayahsCreate**](docs/AyahsApi.md#ayahscreate) | **POST** /ayahs/ | Create a new Ayah record
*AyahsApi* | [**ayahsDestroy**](docs/AyahsApi.md#ayahsdestroy) | **DELETE** /ayahs/{uuid}/ | Delete an Ayah record
*AyahsApi* | [**ayahsList**](docs/AyahsApi.md#ayahslist) | **GET** /ayahs/ | List all Ayahs (Quran verses)
*AyahsApi* | [**ayahsPartialUpdate**](docs/AyahsApi.md#ayahspartialupdate) | **PATCH** /ayahs/{uuid}/ | Partially update an Ayah record
*AyahsApi* | [**ayahsRetrieve**](docs/AyahsApi.md#ayahsretrieve) | **GET** /ayahs/{uuid}/ | Retrieve a specific Ayah by UUID
*AyahsApi* | [**ayahsUpdate**](docs/AyahsApi.md#ayahsupdate) | **PUT** /ayahs/{uuid}/ | Update an existing Ayah record
*GeneralApi* | [**mushafsList**](docs/GeneralApi.md#mushafslist) | **GET** /mushafs/ | List all Mushafs (Quranic manuscripts/editions)
*GeneralApi* | [**mushafsRetrieve**](docs/GeneralApi.md#mushafsretrieve) | **GET** /mushafs/{uuid}/ | Retrieve a specific Mushaf by UUID
*GeneralApi* | [**surahsList**](docs/GeneralApi.md#surahslist) | **GET** /surahs/ | List all Surahs (Quran chapters)
*GeneralApi* | [**surahsRetrieve**](docs/GeneralApi.md#surahsretrieve) | **GET** /surahs/{uuid}/ | Retrieve a specific Surah by UUID
*GeneralApi* | [**takhtitsList**](docs/GeneralApi.md#takhtitslist) | **GET** /takhtits/ | List all Takhtits (text annotations/notes)
*GeneralApi* | [**takhtitsRetrieve**](docs/GeneralApi.md#takhtitsretrieve) | **GET** /takhtits/{uuid}/ | Retrieve a specific Takhtit by UUID
*GeneralApi* | [**translationsList**](docs/GeneralApi.md#translationslist) | **GET** /translations/ | List all Quran Translations
*GeneralApi* | [**translationsRetrieve**](docs/GeneralApi.md#translationsretrieve) | **GET** /translations/{uuid}/ | Retrieve a specific Translation by UUID
*GroupsApi* | [**groupsCreate**](docs/GroupsApi.md#groupscreate) | **POST** /groups/ | Create a new group
*GroupsApi* | [**groupsDestroy**](docs/GroupsApi.md#groupsdestroy) | **DELETE** /groups/{id}/ | Delete a group
*GroupsApi* | [**groupsList**](docs/GroupsApi.md#groupslist) | **GET** /groups/ | List all groups
*GroupsApi* | [**groupsPartialUpdate**](docs/GroupsApi.md#groupspartialupdate) | **PATCH** /groups/{id}/ | Partially update a group
*GroupsApi* | [**groupsRetrieve**](docs/GroupsApi.md#groupsretrieve) | **GET** /groups/{id}/ | Retrieve a specific group by ID
*GroupsApi* | [**groupsUpdate**](docs/GroupsApi.md#groupsupdate) | **PUT** /groups/{id}/ | Update an existing group
*HealthApi* | [**healthRetrieve**](docs/HealthApi.md#healthretrieve) | **GET** /health/ | Health check endpoint
*MushafsApi* | [**mushafsCreate**](docs/MushafsApi.md#mushafscreate) | **POST** /mushafs/ | Create a new Mushaf record
*MushafsApi* | [**mushafsDestroy**](docs/MushafsApi.md#mushafsdestroy) | **DELETE** /mushafs/{uuid}/ | Delete a Mushaf record
*MushafsApi* | [**mushafsImportCreate**](docs/MushafsApi.md#mushafsimportcreate) | **POST** /mushafs/import/ | Import a Mushaf from a JSON file upload
*MushafsApi* | [**mushafsList**](docs/MushafsApi.md#mushafslist) | **GET** /mushafs/ | List all Mushafs (Quranic manuscripts/editions)
*MushafsApi* | [**mushafsPartialUpdate**](docs/MushafsApi.md#mushafspartialupdate) | **PATCH** /mushafs/{uuid}/ | Partially update a Mushaf record
*MushafsApi* | [**mushafsRetrieve**](docs/MushafsApi.md#mushafsretrieve) | **GET** /mushafs/{uuid}/ | Retrieve a specific Mushaf by UUID
*MushafsApi* | [**mushafsUpdate**](docs/MushafsApi.md#mushafsupdate) | **PUT** /mushafs/{uuid}/ | Update an existing Mushaf record
*NotificationsApi* | [**notificationsCreate**](docs/NotificationsApi.md#notificationscreate) | **POST** /notifications/ | Create a new notification
*NotificationsApi* | [**notificationsDestroy**](docs/NotificationsApi.md#notificationsdestroy) | **DELETE** /notifications/{id}/ | Delete a notification
*NotificationsApi* | [**notificationsList**](docs/NotificationsApi.md#notificationslist) | **GET** /notifications/ | List all notifications
*NotificationsApi* | [**notificationsMeList**](docs/NotificationsApi.md#notificationsmelist) | **GET** /notifications/me/ | Get the current user\&#39;s notifications (paginated)
*NotificationsApi* | [**notificationsOpenedRetrieve**](docs/NotificationsApi.md#notificationsopenedretrieve) | **GET** /notifications/opened/ | Mark a notification as opened
*NotificationsApi* | [**notificationsPartialUpdate**](docs/NotificationsApi.md#notificationspartialupdate) | **PATCH** /notifications/{id}/ | Partially update a notification
*NotificationsApi* | [**notificationsRetrieve**](docs/NotificationsApi.md#notificationsretrieve) | **GET** /notifications/{id}/ | Retrieve a specific notification by UUID
*NotificationsApi* | [**notificationsUpdate**](docs/NotificationsApi.md#notificationsupdate) | **PUT** /notifications/{id}/ | Update an existing notification
*NotificationsApi* | [**notificationsViewedRetrieve**](docs/NotificationsApi.md#notificationsviewedretrieve) | **GET** /notifications/viewed/ | Mark notifications as viewed
*PhrasesApi* | [**phrasesCreate**](docs/PhrasesApi.md#phrasescreate) | **POST** /phrases/ | Create a new phrase
*PhrasesApi* | [**phrasesDestroy**](docs/PhrasesApi.md#phrasesdestroy) | **DELETE** /phrases/{uuid}/ | Delete a phrase
*PhrasesApi* | [**phrasesList**](docs/PhrasesApi.md#phraseslist) | **GET** /phrases/ | List all phrases
*PhrasesApi* | [**phrasesModifyCreate**](docs/PhrasesApi.md#phrasesmodifycreate) | **POST** /phrases/modify/ | Modify phrase translations
*PhrasesApi* | [**phrasesPartialUpdate**](docs/PhrasesApi.md#phrasespartialupdate) | **PATCH** /phrases/{uuid}/ | Partially update a phrase
*PhrasesApi* | [**phrasesRetrieve**](docs/PhrasesApi.md#phrasesretrieve) | **GET** /phrases/{uuid}/ | Retrieve a specific phrase by UUID
*PhrasesApi* | [**phrasesUpdate**](docs/PhrasesApi.md#phrasesupdate) | **PUT** /phrases/{uuid}/ | Update an existing phrase
*ProfileApi* | [**profileMeCreate**](docs/ProfileApi.md#profilemecreate) | **POST** /profile/me/ | Get or update the current user\&#39;s profile
*ProfileApi* | [**profileMeRetrieve**](docs/ProfileApi.md#profilemeretrieve) | **GET** /profile/me/ | Get or update the current user\&#39;s profile
*ProfileApi* | [**profileRetrieve**](docs/ProfileApi.md#profileretrieve) | **GET** /profile/{uuid}/ | Retrieve the user\&#39;s profile by uuid
*RecitationsApi* | [**recitationsCreate**](docs/RecitationsApi.md#recitationscreate) | **POST** /recitations/ | Create a new Recitation record
*RecitationsApi* | [**recitationsDestroy**](docs/RecitationsApi.md#recitationsdestroy) | **DELETE** /recitations/{uuid}/ | Delete a Recitation record
*RecitationsApi* | [**recitationsList**](docs/RecitationsApi.md#recitationslist) | **GET** /recitations/ | List all Recitations (audio recordings)
*RecitationsApi* | [**recitationsPartialUpdate**](docs/RecitationsApi.md#recitationspartialupdate) | **PATCH** /recitations/{uuid}/ | Partially update a Recitation record
*RecitationsApi* | [**recitationsRetrieve**](docs/RecitationsApi.md#recitationsretrieve) | **GET** /recitations/{uuid}/ | Retrieve a specific Recitation by UUID
*RecitationsApi* | [**recitationsUpdate**](docs/RecitationsApi.md#recitationsupdate) | **PUT** /recitations/{uuid}/ | Update an existing Recitation record
*RecitationsApi* | [**recitationsUploadCreate**](docs/RecitationsApi.md#recitationsuploadcreate) | **POST** /recitations/{uuid}/upload/{surah_uuid}/ | Upload a surah audio file and optional word-level timestamps for a Recitation
*SurahsApi* | [**surahsCreate**](docs/SurahsApi.md#surahscreate) | **POST** /surahs/ | Create a new Surah record
*SurahsApi* | [**surahsDestroy**](docs/SurahsApi.md#surahsdestroy) | **DELETE** /surahs/{uuid}/ | Delete a Surah record
*SurahsApi* | [**surahsList**](docs/SurahsApi.md#surahslist) | **GET** /surahs/ | List all Surahs (Quran chapters)
*SurahsApi* | [**surahsPartialUpdate**](docs/SurahsApi.md#surahspartialupdate) | **PATCH** /surahs/{uuid}/ | Partially update a Surah record
*SurahsApi* | [**surahsRetrieve**](docs/SurahsApi.md#surahsretrieve) | **GET** /surahs/{uuid}/ | Retrieve a specific Surah by UUID
*SurahsApi* | [**surahsUpdate**](docs/SurahsApi.md#surahsupdate) | **PUT** /surahs/{uuid}/ | Update an existing Surah record
*TakhtitsApi* | [**takhtitsAyahsBreakersCreate**](docs/TakhtitsApi.md#takhtitsayahsbreakerscreate) | **POST** /takhtits/{uuid}/ayahs_breakers/ | Add an ayahs_breaker to this takhtit
*TakhtitsApi* | [**takhtitsAyahsBreakersList**](docs/TakhtitsApi.md#takhtitsayahsbreakerslist) | **GET** /takhtits/{uuid}/ayahs_breakers/ | List all ayahs_breakers for this takhtit (ayahs map style)
*TakhtitsApi* | [**takhtitsAyahsBreakersRetrieve**](docs/TakhtitsApi.md#takhtitsayahsbreakersretrieve) | **GET** /takhtits/{uuid}/ayahs_breakers/{breaker_uuid}/ | Retrieve a specific ayahs_breaker for this takhtit
*TakhtitsApi* | [**takhtitsCreate**](docs/TakhtitsApi.md#takhtitscreate) | **POST** /takhtits/ | Create a new Takhtit record
*TakhtitsApi* | [**takhtitsDestroy**](docs/TakhtitsApi.md#takhtitsdestroy) | **DELETE** /takhtits/{uuid}/ | Delete a Takhtit record
*TakhtitsApi* | [**takhtitsImportCreate**](docs/TakhtitsApi.md#takhtitsimportcreate) | **POST** /takhtits/{uuid}/import/ | Import Ayah Breakers for the specified Takhtit
*TakhtitsApi* | [**takhtitsList**](docs/TakhtitsApi.md#takhtitslist) | **GET** /takhtits/ | List all Takhtits (text annotations/notes)
*TakhtitsApi* | [**takhtitsPartialUpdate**](docs/TakhtitsApi.md#takhtitspartialupdate) | **PATCH** /takhtits/{uuid}/ | Partially update a Takhtit record
*TakhtitsApi* | [**takhtitsRetrieve**](docs/TakhtitsApi.md#takhtitsretrieve) | **GET** /takhtits/{uuid}/ | Retrieve a specific Takhtit by UUID
*TakhtitsApi* | [**takhtitsUpdate**](docs/TakhtitsApi.md#takhtitsupdate) | **PUT** /takhtits/{uuid}/ | Update an existing Takhtit record
*TakhtitsApi* | [**takhtitsWordsBreakersCreate**](docs/TakhtitsApi.md#takhtitswordsbreakerscreate) | **POST** /takhtits/{uuid}/words_breakers/ | Add a words_breaker to this takhtit
*TakhtitsApi* | [**takhtitsWordsBreakersList**](docs/TakhtitsApi.md#takhtitswordsbreakerslist) | **GET** /takhtits/{uuid}/words_breakers/ | List all words_breakers for this takhtit (with line counters)
*TakhtitsApi* | [**takhtitsWordsBreakersRetrieve**](docs/TakhtitsApi.md#takhtitswordsbreakersretrieve) | **GET** /takhtits/{uuid}/words_breakers/{breaker_uuid}/ | Retrieve a specific words_breaker for this takhtit
*TranslationsApi* | [**translationsAyahsCreate**](docs/TranslationsApi.md#translationsayahscreate) | **POST** /translations/{uuid}/ayahs/{ayah_uuid}/ | Create or update (upsert) a specific AyahTranslation
*TranslationsApi* | [**translationsAyahsList**](docs/TranslationsApi.md#translationsayahslist) | **GET** /translations/{uuid}/ayahs/ | List all AyahTranslations for this Translation
*TranslationsApi* | [**translationsAyahsRetrieve**](docs/TranslationsApi.md#translationsayahsretrieve) | **GET** /translations/{uuid}/ayahs/{ayah_uuid}/ | Retrieve a single AyahTranslation for this Translation
*TranslationsApi* | [**translationsAyahsUpdate**](docs/TranslationsApi.md#translationsayahsupdate) | **PUT** /translations/{uuid}/ayahs/{ayah_uuid}/ | Create or update (upsert) a specific AyahTranslation
*TranslationsApi* | [**translationsCreate**](docs/TranslationsApi.md#translationscreate) | **POST** /translations/ | Create a new Translation record
*TranslationsApi* | [**translationsDestroy**](docs/TranslationsApi.md#translationsdestroy) | **DELETE** /translations/{uuid}/ | Delete a Translation record
*TranslationsApi* | [**translationsImportCreate**](docs/TranslationsApi.md#translationsimportcreate) | **POST** /translations/import/ | Import a Translation from a JSON file upload
*TranslationsApi* | [**translationsList**](docs/TranslationsApi.md#translationslist) | **GET** /translations/ | List all Quran Translations
*TranslationsApi* | [**translationsPartialUpdate**](docs/TranslationsApi.md#translationspartialupdate) | **PATCH** /translations/{uuid}/ | Partially update a Translation record
*TranslationsApi* | [**translationsRetrieve**](docs/TranslationsApi.md#translationsretrieve) | **GET** /translations/{uuid}/ | Retrieve a specific Translation by UUID
*TranslationsApi* | [**translationsUpdate**](docs/TranslationsApi.md#translationsupdate) | **PUT** /translations/{uuid}/ | Update an existing Translation record
*UsersApi* | [**usersCreate**](docs/UsersApi.md#userscreate) | **POST** /users/ | Create a new user
*UsersApi* | [**usersDestroy**](docs/UsersApi.md#usersdestroy) | **DELETE** /users/{uuid}/ | Delete a user
*UsersApi* | [**usersList**](docs/UsersApi.md#userslist) | **GET** /users/ | List all users
*UsersApi* | [**usersPartialUpdate**](docs/UsersApi.md#userspartialupdate) | **PATCH** /users/{uuid}/ | Partially update a user
*UsersApi* | [**usersRetrieve**](docs/UsersApi.md#usersretrieve) | **GET** /users/{uuid}/ | Retrieve a specific user by UUID
*UsersApi* | [**usersUpdate**](docs/UsersApi.md#usersupdate) | **PUT** /users/{uuid}/ | Update an existing user
*WordsApi* | [**wordsCreate**](docs/WordsApi.md#wordscreate) | **POST** /words/ | Create a new Word record
*WordsApi* | [**wordsDestroy**](docs/WordsApi.md#wordsdestroy) | **DELETE** /words/{uuid}/ | Delete a Word record
*WordsApi* | [**wordsList**](docs/WordsApi.md#wordslist) | **GET** /words/ | List all Words in Ayahs
*WordsApi* | [**wordsPartialUpdate**](docs/WordsApi.md#wordspartialupdate) | **PATCH** /words/{uuid}/ | Partially update a Word record
*WordsApi* | [**wordsRetrieve**](docs/WordsApi.md#wordsretrieve) | **GET** /words/{uuid}/ | Retrieve a specific Word by UUID
*WordsApi* | [**wordsUpdate**](docs/WordsApi.md#wordsupdate) | **PUT** /words/{uuid}/ | Update an existing Word record


### Documentation For Models

 - [Ayah](docs/Ayah.md)
 - [AyahAdd](docs/AyahAdd.md)
 - [AyahBreaker](docs/AyahBreaker.md)
 - [AyahBreakersResponse](docs/AyahBreakersResponse.md)
 - [AyahInSurah](docs/AyahInSurah.md)
 - [AyahSerializerView](docs/AyahSerializerView.md)
 - [AyahTranslation](docs/AyahTranslation.md)
 - [Group](docs/Group.md)
 - [HealthCheckResponse](docs/HealthCheckResponse.md)
 - [Login](docs/Login.md)
 - [LoginResponse](docs/LoginResponse.md)
 - [LogoutAllResponse](docs/LogoutAllResponse.md)
 - [LogoutResponse](docs/LogoutResponse.md)
 - [Mushaf](docs/Mushaf.md)
 - [Notification](docs/Notification.md)
 - [PatchedAyah](docs/PatchedAyah.md)
 - [PatchedGroup](docs/PatchedGroup.md)
 - [PatchedMushaf](docs/PatchedMushaf.md)
 - [PatchedNotification](docs/PatchedNotification.md)
 - [PatchedPhrase](docs/PatchedPhrase.md)
 - [PatchedRecitation](docs/PatchedRecitation.md)
 - [PatchedSurah](docs/PatchedSurah.md)
 - [PatchedTakhtit](docs/PatchedTakhtit.md)
 - [PatchedTranslationList](docs/PatchedTranslationList.md)
 - [PatchedUser](docs/PatchedUser.md)
 - [PatchedWord](docs/PatchedWord.md)
 - [Phrase](docs/Phrase.md)
 - [PhraseModify](docs/PhraseModify.md)
 - [Profile](docs/Profile.md)
 - [Recitation](docs/Recitation.md)
 - [RecitationList](docs/RecitationList.md)
 - [RegisterResponse](docs/RegisterResponse.md)
 - [Surah](docs/Surah.md)
 - [SurahDetail](docs/SurahDetail.md)
 - [SurahInAyah](docs/SurahInAyah.md)
 - [Takhtit](docs/Takhtit.md)
 - [TakhtitsAyahsBreakersCreateRequest](docs/TakhtitsAyahsBreakersCreateRequest.md)
 - [TakhtitsCreateRequest](docs/TakhtitsCreateRequest.md)
 - [TakhtitsWordsBreakersCreateRequest](docs/TakhtitsWordsBreakersCreateRequest.md)
 - [Translation](docs/Translation.md)
 - [TranslationList](docs/TranslationList.md)
 - [TranslationsAyahsUpdateRequest](docs/TranslationsAyahsUpdateRequest.md)
 - [User](docs/User.md)
 - [Word](docs/Word.md)
 - [WordBreakerDetailResponse](docs/WordBreakerDetailResponse.md)
 - [WordBreakersResponse](docs/WordBreakersResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="knoxApiToken"></a>
### knoxApiToken

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

