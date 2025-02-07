import os
import subprocess
import itertools
import re

SETTINGS_FILE = "src/settings.h"

COMPILER_OPTIONS_VALUES = ["-cl-std=CL1.2", "-cl-std=CL2.0"]
KERNEL_VALUES = [5]
TS_VALUES = [8, 16, 32]

BUILD_DIR = "cmake-build-debug"
BUILD_COMMAND = ["cmake", "--build", BUILD_DIR, "--target", "myGEMM", "-j", "14"]
EXECUTABLE_PATH = os.path.join(BUILD_DIR, "bin/myGEMM.exe")

def modify_settings(compiler_option, kernel, ts):
    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        for line in lines:
            if re.match(r"^\s*#define COMPILER_OPTIONS", line):
                f.write(f'#define COMPILER_OPTIONS "{compiler_option}"\n')
            elif re.match(r"^\s*#define KERNEL", line):
                f.write(f"#define KERNEL {kernel}\n")
            elif re.match(r"^\s*#define TS\s+\d+", line):
                f.write(f"#define TS {ts}\n")
            else:
                f.write(line)

def build_and_run():
    result = subprocess.run(BUILD_COMMAND, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)
    result = subprocess.run([EXECUTABLE_PATH], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)


for compiler_option, kernel, ts in itertools.product(COMPILER_OPTIONS_VALUES, KERNEL_VALUES, TS_VALUES):
    modify_settings(compiler_option, kernel, ts)
    if not build_and_run():
        print("Эта комбинация несовместима, переходим к следущей.\n")