[app]
title = Kivy Basic Accelerometer
package.name = accelbasicexample
package.domain = org.robins
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = plyer,kivy
orientation = portrait
fullscreen = 0
android.permissions = android.hardware.sensor.accelerometer
android.release_artifact = apk
android.arch = arm64-v8a
[buildozer]

log_level = 2

