import os
import shutil
import sys

def self_replicate():
    # Archivo actual que se está ejecutando
    current_file = os.path.abspath(__file__)
    
    # Carpeta donde se almacenarán las copias
    target_dir = "replicas"
    os.makedirs(target_dir, exist_ok=True)
    
    # Contar cuántas copias existen ya
    existing = [f for f in os.listdir(target_dir) if f.startswith("copia_")]
    copy_number = len(existing) + 1
    
    # Nombre nuevo de la copia
    copy_name = f"copia_{copy_number}.py"
    target_path = os.path.join(target_dir, copy_name)
    
    # Copiarse a sí mismo
    shutil.copy(current_file, target_path)
    print(f"[✓] Se creó la copia #{copy_number} en: {target_path}")

if __name__ == "__main__":
    self_replicate()
