if you move chrome-extension project directory
you need to update Native Messaging Host Location

C:\Projects\Practices\Chrome extensions\Copy URL and Execute\com.moanrisy.gitbash.json

REG ADD "HKCU\Software\Google\Chrome\NativeMessagingHosts\com.my_company.my_application" /ve /t REG_SZ /d "C:\path\to\nmh-manifest.json" /f