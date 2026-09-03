# Documentación del Proyecto: practicaFlask

Aplicación web modular construida con **Flask**, siguiendo el patrón de diseño de fábrica de aplicaciones (Application Factory), Blueprints y una arquitectura limpia y organizada.

---

## 📁 Estructura del Proyecto

```text
practicaFlask/
├── run.py                    # Punto de entrada de la aplicación
├── requirements.txt          # Dependencias de Python
├── .env.example              # Plantilla de variables de entorno
├── .gitignore                # Archivos ignorados por Git
├── config/
│   └── __init__.py           # Configuraciones (Desarrollo, Producción, etc.)
├── app/
│   ├── __init__.py           # Fábrica de la app (create_app) e inicialización de extensiones
│   ├── models.py             # Modelos de base de datos (Ej: User)
│   ├── blueprints/
│   │   ├── __init__.py
│   │   ├── main/             # Blueprint para las páginas públicas/principales
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   └── auth/             # Blueprint para autenticación (login, registro)
│   │       ├── __init__.py
│   │       └── routes.py
│   ├── templates/            # Plantillas HTML (Jinja2)
│   │   ├── base.html         # Plantilla base compartida
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── main/
│   │       └── index.html    # Página de inicio
│   └── static/               # Archivos estáticos
│       ├── css/
│       │   └── style.css     # Estilos globales
│       └── js/
│           └── main.js       # Scripts de JavaScript
└── tests/
    ├── __init__.py
    └── test_basic.py         # Pruebas unitarias básicas
```

---

## 🛠️ Tecnologías y Librerías Principales

- **Python 3.x**
- **Flask**: Microframework web.
- **Flask-SQLAlchemy**: ORM para la gestión de bases de datos relacionales.
- **Flask-Login**: Manejo de sesiones de usuario y autenticación.
- **Flask-Migrate**: Control de migraciones de bases de datos.
- **Python-Dotenv**: Carga de variables de entorno desde archivos `.env`.

---

## 🚀 Guía de Instalación y Ejecución

### 1. Clonar o abrir el proyecto en el Escritorio
Abre una terminal y dirígete a la carpeta del proyecto en el escritorio:
```bash
cd C:\Users\PROGRAMACION\Desktop\practicaFlask
```

### 2. Crear y activar un entorno virtual
```bash
python -m venv venv
# En Windows (CMD/PowerShell):
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno
Crea una copia de `.env.example` renombrándola a `.env` y configura tus variables locales (como la clave secreta y la URI de la base de datos):
```bash
copy .env.example .env
```

### 5. Ejecutar la aplicación
```bash
python run.py
```
La aplicación estará disponible por defecto en: `http://127.0.0.1:5000`

---

## 🧪 Ejecución de Pruebas
Para correr los tests automatizados del proyecto:
```bash
pytest
```
