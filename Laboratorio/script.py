import os 

import shutil

def self_replicate():
    # Obtiene la ruta del script actual
    current_file = __file__

    # Carpeta donde se va a "replicar"
    target_dir = "replicas"
    os.makedirs(target_dir, exist_ok=True)

    # Nombre nuevo para la copia
    copy_name = "copia_del_programa.py"
    target_path = os.path.join(target_dir, copy_name)

    # Copia el archivo actual al destino
    shutil.copy(current_file, target_path)
    print(f"El programa se replicó en: {target_path}")


if __name__ == "__main__":
    self_replicate()
