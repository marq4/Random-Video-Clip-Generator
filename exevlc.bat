@echo off

set generatedxml=%1
shift

vlc --no-video-title-show --fullscreen --no-qt-fs-controller --play-and-exit %generatedxml%

