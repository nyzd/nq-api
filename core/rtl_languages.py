"""
RTL (Right-to-Left) language codes used by the API.

Keep this list minimal and centralized. Serializers can derive a boolean
by checking if a language code (or its base language) is in this set.
"""

# RTL language codes (lowercase, with region variants)
RTL_LANGUAGE_CODES = {
    # Arabic variants
    'ar', 'ar-ae', 'ar-bh', 'ar-dj', 'ar-dz', 'ar-eg', 'ar-iq', 'ar-jo',
    'ar-kw', 'ar-lb', 'ar-ly', 'ar-ma', 'ar-om', 'ar-qa', 'ar-sa', 'ar-sd',
    'ar-sy', 'ar-tn', 'ar-ye',

    # Persian/Dari variants
    'fa', 'fa-af', 'fa-ir',

    # Hebrew variants
    'he', 'he-il', 'iw',

    # Kurdish (Sorani)
    'ckb', 'ku',

    # Pashto
    'ps',

    # Uighur/Uyghur
    'ug',

    # Urdu variants
    'ur', 'ur-in', 'ur-pk',

    # Punjabi (Shahmukhi script - RTL)
    'pa-pk',

    # Yiddish variants
    'yi', 'yi-us',

    # Additional RTL languages
    'sd',  # Sindhi
    'ks',  # Kashmiri (when written in Arabic script)
    'bal', # Balochi
    'brh', # Brahui
    'haz', # Hazaragi
    'lrc', # Luri
    'mzn', # Mazanderani
    'glk', # Gilaki
    'luz', # Southern Luri
}
