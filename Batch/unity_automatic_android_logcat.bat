set user=juanm
echo %user%
cd "C:\Users\%user%\AppData\Local\Android\Sdk\platform-tools"
adb.exe logcat -s "Unity" > "C:\Users\%user%\Downloads\testX.txt"