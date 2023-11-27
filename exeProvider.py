import os
import subprocess as sp
import sys

def run_command(command):
    os.system(command)

try:
    # Çalışma dizinini al
    current_path = "current working file path"

    # Python ve pip yollarını belirleme
    python_command = os.path.join(current_path, "env", "bin", "python")
    pip_command = os.path.join(current_path, "env", "bin", "pip")

    # Gerekli paketleri yükleme
    print("Gerekli paketler yükleniyor...")
    run_command(f"{pip_command} install -r {os.path.join(current_path, 'requirement.txt')}")

    # main.py'yi çalıştır
    print("Program çalıştırılıyor...")
    run_command(f"{python_command} {os.path.join(current_path, 'main.py')}")

except Exception as e:
    print(f"Hata oluştu: {e}")
