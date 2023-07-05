# android-sdk-platform-tools-supporter

```
import sys
sys.path.append("/opt")
import common

https://www.bangseongbeom.com/sys-path-pythonpath.html
```

```
import os
import time
from android_sdk_platform_tools_supporter.android_sdk_platform_tools import AndroidSdkPlatformTools
from python_supporter.check_ip import check_ip #pip install python-supporter

base_directory = os.path.dirname(__file__) + "/platform-tools"
platform_tools = AndroidSdkPlatformTools(base_directory)

devices = platform_tools.check_devices()
    
if not device:
    print(f"USB에 디바이스가 연결되지 않았습니다.")
    exit()

print(f"연결된 디바이스: {device}")

print("모바일 데이터 해제")
platform_tools.data_disable()

print("1초 쉬기")
time.sleep(1)

print("모바일 데이터 연결")
platform_tools.data_enable()

ip = check_ip()
print(f"PC IP: {ip}")
```
