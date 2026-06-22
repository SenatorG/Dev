@echo off

:: Define log file
set LOGFILE=C:\Users\graym1\Scripts\recyclebin.log

:: Log start time
echo [%DATE% %TIME%] Starting Recycle Bin cleanup... >> %LOGFILE%

:: Run cleanup
cleanmgr.exe /sagerun:1

:: Pause briefly to ensure cleanmgr completes
timeout /t 5 > nul

:: Log completion
echo [%DATE% %TIME%] Recycle Bin cleanup completed. >> %LOGFILE%

:: Show popup
msg * Recycle Bin emptied. See log file for details.
