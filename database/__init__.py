import os
import importlib
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///database/sqlite/db.db")

Base = declarative_base()


# Caminho absoluto para a pasta "models"
models_package = "database.models"
models_path = os.path.join(os.path.dirname(__file__), "models")

# Importa todos os arquivos .py da pasta models (exceto __init__.py)
for filename in os.listdir(models_path):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]
        importlib.import_module(f"{models_package}.{module_name}")
