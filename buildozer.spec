[app]
title = Y-SOCIETY-APP
package.name = ysocietyapp
package.domain = org.ysociety

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,md

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.ndk_api = 21
android.build_tools = 34.0.0

android.permissions = INTERNET,ACCESS_NETWORK_STATE

[buildozer]
log_level = 2
warn_on_root = 1
