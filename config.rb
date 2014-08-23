# Require any additional compass plugins here.

# Paths configuration
css_dir = "tekton/backend/appengine/static/css"
sass_dir = "tekton/backend/appengine/sass"
images_dir = "tekton/backend/appengine/static/img"
fonts_dir = "tekton/backend/appengine/static/fonts"
generated_images_dir = "tekton/backend/appengine/static/img"

# Output style of the compiled CSS
output_style = (environment == :production) ? :compressed : :expanded

# Prefere relative paths in the CSS
relative_assets = true

# Display the original location (SCSS file and line) of the selector
# Useful for debugging
line_comments = true

# SCSS and not SASS
preferred_syntax = :scss
