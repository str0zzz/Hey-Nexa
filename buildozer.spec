[app]
title = Nexa Ultimate
package.name = nexaultimate
package.domain = com.nexa.ultimate
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 3.0.0
requirements = python3,kivy,pyjnius,plyer
orientation = portrait
fullscreen = 0
icon.filename = icon.png
presplash.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1

[permissions]
android.permissions = RECORD_AUDIO, CAMERA, INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_CONNECT, BLUETOOTH_SCAN, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, ACCESS_NETWORK_STATE, CHANGE_NETWORK_STATE, READ_SMS, SEND_SMS, RECEIVE_SMS, CALL_PHONE, READ_PHONE_STATE, VIBRATE, FLASHLIGHT, WAKE_LOCK, FOREGROUND_SERVICE, SYSTEM_ALERT_WINDOW, REQUEST_INSTALL_PACKAGES, QUERY_ALL_PACKAGES, POST_NOTIFICATIONS, READ_CONTACTS, WRITE_CONTACTS

[android]
android.api = 33
android.minapi = 21
android.gradle_dependencies = androidx.core:core:1.9.0
android.arch = arm64
android.accept_sdk_license = True
android.allow_download = True
android.icon = icon.png
android.presplash = icon.png
