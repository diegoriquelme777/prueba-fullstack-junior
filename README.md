# Prueba Técnica Full Stack Junior

## Descripción
Proyecto de prueba técnica para desarrollador Full Stack Junior.  
El objetivo es transformar datos de pedidos desde un sistema legacy y mostrarlos en un dashboard simple.  
Incluye:

- **Backend:** FastAPI que transforma el JSON legacy y expone un endpoint REST `/api/pedidos`.
- **Frontend:** React + Vite que consume la API y muestra los pedidos en una tabla, con badges de estado, tarjetas de resumen y filtro.

---

## Tecnologías
- **Backend:** Python 3, FastAPI, Uvicorn  
- **Frontend:** React, Vite, JavaScript/TypeScript  
- **Otros:** CORS habilitado para consumo desde frontend
## Instalación y Ejecución (Windows)

### Backend
1. Entrar a la carpeta `backend`:

```powershell
cd backend


### Crear un entorno virtual
python -m venv venv

###Activar el entorno
venv\Scripts\activate

###Instalar dependencia
pip install fastapi uvicorn python-multipart

###Ejecutar el servidor

uvicorn main:app --reload --port 8000


###Probar que funciona accediendo

http://localhost:8000/api/pedidos


###Entrar a la carpeta frontend

cd ../frontend


###Instalar dependencias

npm install


###Ejecutar el frontend

npm run dev


###Abrir en el navegador

http://localhost:5173