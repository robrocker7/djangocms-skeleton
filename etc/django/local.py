# example local.py
DEBUG = False
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '', # Or path to database file if using sqlite3.
            'USER': '',
            'PASSWORD': '',     # Not used with sqlite3.
            'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}
CMS_TEMPLATES = (
    ('newproject.html', 'New Project'),
)

LANGUAGES = [
    ('en', 'English'),
]

CMS_SEO_FIELDS = True

# Folder Options
# Add more folder options for custom folder gallery
CMSPLUGIN_FILER_FOLDER_VIEW_OPTIONS = (
    ('list', "List"),
    ('slideshow', 'Slideshow'),
)

JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'
JQUERY_UI_JS = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js'
JQUERY_UI_CSS = 'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/jquery-ui.css'

# TINYMCE settings
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': '800',
    'height': '400',
}
