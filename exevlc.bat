@echo off

set generatedxml=%1
shift

"C:\Program Files\VideoLAN\VLC\vlc.exe" --no-video-title-show --fullscreen --no-qt-fs-controller --play-and-exit %generatedxml%

