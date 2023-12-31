# android-sdk-supporter

## Android SDK 다운로드
 
명령줄 도구  
https://developer.android.com/studio/command-line?hl=ko#tools-sdk  
Android SDK 명령줄 도구 (android_sdk\cmdline-tools)  
https://developer.android.com/studio#command-tools  
Android SDK 빌드 도구 (android_sdk\build-tools)  
https://androidsdkmanager.azurewebsites.net/Buildtools  
Android SDK 플랫폼 도구 (android_sdk\platform-tools)  
https://developer.android.com/studio/releases/platform-tools?hl=ko#downloads.html  
google drive  
https://drive.google.com/drive/folders/1mfYHbCbwM6HIexV9gQvtPFnIEwo26t0s?usp=drive_link  

```
import os
from android_sdk_supporter.build_tools import BuildTools

android_sdk_directory = os.path.dirname(__file__) + "/android_sdk"
build_tools = BuildTools(android_sdk_directory)
```

```
import os
from android_sdk_supporter.cmdline_tools import CmdlineTools

android_sdk_directory = os.path.dirname(__file__) + "/android_sdk"
cmdline_tools = CmdlineTools(android_sdk_directory)
```

```
import os
import time
from android_sdk_supporter.platform_tools import PlatformTools
from python_supporter.check_ip import check_ip #pip install python-supporter

android_sdk_directory = os.path.dirname(__file__) + "/android_sdk"
platform_tools = PlatformTools(android_sdk_directory)

device = ""
status = ""
try:
    devices = platform_tools.check_devices()

    for d in devices:
        device = d["device"]
        status = d["status"]
        break
    if not devices:
        device = ""
        status = ""
except:
   device = ""
   status = ""

print(f"연결 디바이스 (상태): {device} ({status})")

if not device and not status:
    print(f"USB에 디바이스가 연결되지 않았습니다.")
    exit()

print("모바일 데이터 해제")
platform_tools.data_disable()

print("1초 쉬기")
time.sleep(1)

print("모바일 데이터 연결")
platform_tools.data_enable()

ip = check_ip()
print(f"PC IP: {ip}")
```
