[app]

# (str) Title of your application
title = Calculadora de Derivadas

# (str) Package name
package.name = derivadascalculator

# (str) Package domain (needed for android/ios packaging)
package.domain = com.example

# (source) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,txt

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, dist

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use legacy buildozer.spec (for compatibility)
android.gradle_dependencies = 

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) Android app theme, default is ok for Kivy-based app
# android.theme = "@android:style/Theme.NoTitleBar"

# (bool) Copy presplash backgrounds
android.presplash_iconname = data/icon.png
android.icon_filename = data/icon.png

# (int) Port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
#p4a.port = 

# (str) python-for-android release (default branch will be used)
#p4a.branch = develop

# (str) OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) Android presplash icon background color (new android toolchain)
#android.presplash_iconcolor = #FFFFFF

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
#android.api = 31

# (int) Minimum API your APK will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 30

# (str) Android NDK version to use
#android.ndk = 25b

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warnings about all items which are not ready for production
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. where to put the built APK, IPA or so on)
# bin_dir = ./bin

#################################################################################
# List as sections
#
# You can define all the "list" as [section:key].
# Each line inside a section represents a new item in the list

# The format used internally is equivalent to INI files, so that you can use
# ":" separators in the multi-line values, but that means that the first ":"
# will be used as the "=" separator.
#

# Android features
#android.features = android.hardware.usb.host

# (str) Android logcat filters to use (default is *:S python:D)
# android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (bool) Enable AndroidX support (automatically created if required)
android.enable_androidx = True

# (str) Android logcat filters to use (default is *:S python:D)
# android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (str) python for android (p4a) git repo URL
# p4a.url = https://github.com/kivy/python-for-android

# (str) python for android (p4a) branch to use, defaults to master
p4a.branch = develop

# (str) OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file for custom backup rules (see the documentation)
# android.backup_rules = 

# (bool) Copy presplash backgrounds
#android.presplash_copy = True

# (list) Gradle dependencies (see gradle documentation for format)
# android.gradle_dependencies = com.google.android.material:material:1.1.0

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will be disabled.
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file for custom backup rules (see the documentation)
# android.backup_rules = 

# (bool) Copy presplash backgrounds
#android.presplash_copy = True

# (list) Pattern to match allowed input types, all other types are rejected
android.allowed_orientations = portrait

# (bool) Indicate if the application should be fullscreen or not
#android.fullscreen = True

# (str) Supported orientation (landscape, portrait or all)
android.orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
#android.fullscreen = False

# (str) Supported orientation (landscape, portrait or all)
#android.orientation = landscape

# (bool) Run logcat before each debug session
#android.logcat_before_run = True

# android.release_artifact = aab

# (bool) Copy presplash backgrounds
#android.presplash_copy = True

# (bool) Copy presplash backgrounds
#android.presplash_copy = True
