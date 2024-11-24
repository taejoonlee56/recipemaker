import os
import shutil

def replace_main_py(custom_main_path):
    try:
        import site
        site_packages = site.getsitepackages()[0]
        target_path = os.path.join(site_packages, "open_webui", "apps", "ollama", "main.py")
        
        backup_path = target_path + ".backup"
        if not os.path.exists(backup_path):
            shutil.copyfile(target_path, backup_path)
            print(f"Backed up original main.py to {backup_path}")
        
        shutil.copyfile(custom_main_path, target_path)
        print(f"Replaced main.py with {custom_main_path}")
    
    except Exception as e:
        print(f"Error replacing main.py: {e}")

replace_main_py("./main.py")
