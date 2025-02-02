@echo OFF

@rem Copyright (c) nexB Inc. and others. All rights reserved.
@rem SPDX-License-Identifier: Apache-2.0
@rem See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
@rem ScanCode is a trademark of nexB Inc.
@rem See https://github.com/nexB/scancode-toolkit for support or download.
@rem See https://aboutcode.org for more information about nexB OSS projects.

@rem  A wrapper to ScanCode command line entry point

set SCANCODE_ROOT_DIR=%~dp0
set SCANCODE_CONFIGURED_PYTHON=%SCANCODE_ROOT_DIR%Scripts\python.exe

if not exist "%SCANCODE_CONFIGURED_PYTHON%" goto configure
goto scancode

:configure
echo * Configuring ScanCode for first use...
echo * WARNING: Native Windows may be deprecated in the future in favor of Windows Subsystem for Linux 2
echo * WARNING: Please visit https://github.com/nexB/scancode-toolkit/issues/2366 for details and to provide feedback
set CONFIGURE_QUIET=-qq
call "%SCANCODE_ROOT_DIR%configure"

@rem Return a proper return code on failure
if %errorlevel% neq 0 (
    exit /b %errorlevel%
)

:scancode
@rem without this things may not always work on Windows 10, but this makes things slower
set PYTHONDONTWRITEBYTECODE=1

set "SCANCODE_CMD_LINE_ARGS= "
set "EXTRACTCODE_CMD_LINE_ARGS= "
set "FILE_ARG= "

for %%i in (%*) do (
    if exist "%SCANCODE_ROOT_DIR%\%%i" (
    set FILE_ARG=%%i
    )
)


:collectarg
    if ""%1""=="""" goto continue
    if ""%1""==""--extractcode"" (
        call "extractcode" %FILE_ARG%
    )
    if not ""%1""==""--extractcode"" (
        call set SCANCODE_CMD_LINE_ARGS=%SCANCODE_CMD_LINE_ARGS% %1
    )
    shift
goto collectarg

:continue

"%SCANCODE_ROOT_DIR%Scripts\scancode" %SCANCODE_CMD_LINE_ARGS%
