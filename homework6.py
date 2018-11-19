import json
import subprocess
import sys
import yaml


def py_info():
    version = sys.version[0:5]
    pyenv_vers = subprocess.getoutput("pyenv version-name")
    virt_env = sys.exec_prefix
    exec_loc = sys.executable
    pip_loc = subprocess.getoutput("ls /usr/local/bin/pip*")
    pyth_path = "\n".join(sys.path)
    pack = subprocess.getoutput("pip freeze")
    site_loc = next(p for p in sys.path if 'site-packages' in p)
    return [' 1. Version: ' + version,
            ' 2. Pyenv version-name: ' + pyenv_vers,
            ' 3. Virtual environment: ' + virt_env,
            ' 4. Python executable location: ' + exec_loc,
            ' 5. Pip location & version: \\n' + pip_loc,
            ' 6. PYTHONPATH: \\n' + pyth_path,
            ' 7 Installed packages: name, version:\n' + pack,
            ' 8. Site-packages location: \n' + site_loc]


py = py_info()
print(*py, sep='\n')
json_name = "py_info.json"
with open(json_name, "w") as json_out:
    json_out.write(json.dumps(py, indent=0, sort_keys=False))
yaml_name = "py_info.yaml"
with open(yaml_name, "w") as yml_out:
    yml_out.write(yaml.dump(py, default_flow_style=False))
