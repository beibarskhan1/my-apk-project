[app]
title = My Mobile App
package.name = my_mobile_app
package.domain = org.beibars
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a
# Это пути к твоим картинкам
icon.filename = %(source.dir)s/data/logo/icon.png
presplash.filename = %(source.dir)s/data/logo/presplash.png