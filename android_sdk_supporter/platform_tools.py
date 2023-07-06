import os
import platform
import subprocess
import zipfile
import sys

class PlatformTools:
    def __init__(self, base_directory=None):
        super().__init__()
        self.base_directory = base_directory
        self.devices = []

        if self.base_directory:
            if not os.path.exists(f"{self.base_directory}/platform-tools"):
                if platform.system() == 'Darwin': #맥
                    from_zip = f"{self.base_directory}/platform-tools_r34.0.3-darwin.zip"
                elif platform.system() == 'Windows': #윈도우
                    from_zip = f"{self.base_directory}/platform-tools_r34.0.3-windows.zip"
                elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
                    from_zip = f"{self.base_directory}/platform-tools_r34.0.3-linux.zip"
                zip_file = zipfile.ZipFile(from_zip)
                zip_file.extractall(self.base_directory)
                zip_file.close()
        
    def check_devices(self):   
        if self.base_directory:
            cmd = f"{self.base_directory}/platform-tools/adb"
        else:
            cmd = "adb"
        '''
(base) C:\Users\Administrator\Desktop\네이버쇼핑검색클릭업무자동화앱v0.4\platform-tools\platform-tools>adb devices
List of devices attached
R95RB00QRCY     device


(base) C:\Users\Administrator\Desktop\네이버쇼핑검색클릭업무자동화앱v0.4\platform-tools\platform-tools>        
        '''
        '''
(base) C:\Users\Administrator\Desktop\calculator-rpa-app-reflex-appium-android-main\platform-tools\platform-tools>adb devices
List of devices attached
R95RB00QRCY     offline


(base) C:\Users\Administrator\Desktop\calculator-rpa-app-reflex-appium-android-main\platform-tools\platform-tools>        
        '''
        outputs = subprocess.check_output([cmd, "devices"]).decode('utf-8')
        device = None
        for output in outputs.split("\n")[1:]:
            output = output.strip()
            #print(output) #R95RB00QRCY     device
            if output:
                output = output.split("\t")[0]
                device = output
                break
        if device:
            self.devices = [device]
            return [device]
        else:
            self.devices = []
            return []
    
    def data_disable(self):
        if self.base_directory:
            adb = f"{self.base_directory}/platform-tools/adb"
        else:
            adb = "adb"
        cmd = f"{adb} -s {self.devices[0]} shell svc data disable"
        os.system(cmd)

    def data_enable(self):
        if self.base_directory:
            adb = f"{self.base_directory}/platform-tools/adb"
        else:
            adb = "adb"
        cmd = f"{adb} -s {self.devices[0]} shell svc data enable"
        os.system(cmd)