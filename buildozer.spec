[app]

# (str) Title of your application
title = Angeapp

# (str) Package name
package.name = angeapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let it empty to exclude nothing)
source.exclude_exts = spec

# (list) List of directory to exclude (let it empty to exclude nothing)
source.exclude_dirs = tests, bin, .git

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (list) Supported architectures
android.archs = arm64-v8a

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minAPI = 21

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0
