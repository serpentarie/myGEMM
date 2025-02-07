import subprocess

script_name = "tune_mygemm.py"

for i in range(60):
    try:
        subprocess.run(["python", script_name], check=True)
    except subprocess.CalledProcessError as e:
        break