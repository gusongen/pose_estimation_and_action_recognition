set PATH=%PATH%;D:\ffmpeg\bin
ffmpeg -ss 1.0494957 ^
-to  2.7255704 ^
-i ^
 "D:\bishe\data\vedio1.mp4"  ^
 -s 320x240 -f gif  ^
 @REM -r 24  ^
 "D:\bishe\test_1.gif" ^
  -y


