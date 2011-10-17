# example local.py

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

WYM_CLASSES = ",\n".join([
    "{'name': 'left-align', 'title': 'Left Align', 'expr': 'p[class!=\"right-align\"][class!=\"center-align\"]'}",
    "{'name': 'right-align', 'title': 'Right Align', 'expr': 'p[class!=\"left-align\"][class!=\"center-align\"]'}",
    "{'name': 'center-align', 'title': 'Center Align', 'expr': 'p[class!=\"right-align\"][class!=\"left-align\"]'}",
])

WYM_STYLES = ",\n".join([
    "{'name': '.left-align', 'css': 'text-align: left;'}",
    "{'name': '.right-align', 'css': 'text-align: right;'}",
    "{'name': '.center-align', 'css': 'text-align: center;'}",
])

JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'
JQUERY_UI_JS = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js'
JQUERY_UI_CSS = 'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/jquery-ui.css'
