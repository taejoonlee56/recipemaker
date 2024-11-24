import os
import shutil
import sys
import subprocess

def get_python_version(executable):
    """
    Get the Python version (major.minor) from the given executable path.
    """
    try:
        result = subprocess.run([executable, "--version"], capture_output=True, text=True)
        version = result.stdout.strip().split()[1]
        major_minor = ".".join(version.split(".")[:2])
        return f"python{major_minor}"
    except Exception as e:
        print(f"Error detecting Python version: {e}")
        return None

def get_conda_site_packages():
    """
    Returns the site-packages path for Conda environments.
    """
    conda_prefix = os.environ.get("CONDA_PREFIX")
    if conda_prefix:
        python_executable = os.path.join(conda_prefix, "bin", "python")
        python_version = get_python_version(python_executable)
        if python_version:
            return os.path.join(conda_prefix, "lib", python_version, "site-packages")
    return None

def get_site_packages():
    """
    Returns the correct site-packages path for the current environment (Conda or virtualenv).
    """
    conda_site_packages = get_conda_site_packages()
    if conda_site_packages:
        return conda_site_packages

    # 일반 가상환경 감지
    if sys.prefix != sys.base_prefix:
        python_version = f"python{sys.version_info.major}.{sys.version_info.minor}"
        return os.path.join(sys.prefix, "lib", python_version, "site-packages")
    
    # 전역 환경
    import site
    return site.getsitepackages()[0]

def replace_main_py(custom_main_path):
    try:
        # site-packages 경로 가져오기
        site_packages = get_site_packages()
        target_path = os.path.join(site_packages, "open_webui", "apps", "ollama", "main.py")
        
        # 타겟 경로의 디렉토리가 없는 경우 생성
        target_dir = os.path.dirname(target_path)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            print(f"Created missing directory: {target_dir}")
        
        # 백업 파일 생성
        backup_path = target_path + ".backup"
        if not os.path.exists(backup_path) and os.path.exists(target_path):
            shutil.copyfile(target_path, backup_path)
            print(f"Backed up original main.py to {backup_path}")
        
        # main.py 복사
        shutil.copyfile(custom_main_path, target_path)
        print(f"Replaced main.py with {custom_main_path}")
    
    except Exception as e:
        print(f"Error replacing main.py: {e}")

# 실행
replace_main_py("./main.py")