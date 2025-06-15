from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import importlib
import os
from pathlib import Path

app = FastAPI()

def include_all_routes(app: FastAPI, package: str = "routes"):
    routes_path = Path(__file__).parent / package

    for file in os.listdir(routes_path):
        if file.endswith(".py"):
            module_name = file[:-3]  # Remove .py
            module_path = f"{package}.{module_name}"

            module = importlib.import_module(module_path)

            if hasattr(module, "router"):
                app.include_router(module.router)


include_all_routes(app)
