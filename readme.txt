# 🌟 MLBB Web

Sitio web sobre Mobile Legends: Bang Bang creado con [Reflex](https://reflex.dev), una librería de Python para construir interfaces web modernas.

---

## 🚀 Tecnologías utilizadas

- 🐍 Python 3.11
- ⚛️ Reflex
- ☁️ Netlify (para el despliegue)
- 🧠 Git & GitHub

---

## 🛠️ Cómo correr el proyecto localmente

1. Clona el repositorio:

   ```bash
   git clone https://github.com/dine-lab/web_mlbb.git
   cd web_mlbb
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Corre la app:

   ```bash
   reflex run
   ```

---

## 📁 Estructura del proyecto

```
Mlbb_web/
├── Mlbb_web/            # Componentes de la app Reflex
├── assets/              # Recursos estáticos (imágenes, etc.)
├── .web/                # Archivos generados por Reflex
├── .venv/               # Entorno virtual (excluido del repo)
├── requirements.txt     # Dependencias del proyecto
├── rxconfig.py          # Configuración Reflex
└── README.md            # Este archivo 😎
```

---

## 🌐 Despliegue

La app está desplegada en Netlify. Visítala aquí:  
👉 https://mlbb-bpds.netlify.app (reemplaza esto con tu URL real)

---

## ⚠️ Notas

- `.venv/`, `.web/`, y `__pycache__/` están ignorados en `.gitignore`.
- Este proyecto no necesita Node.js, ya que Reflex genera todo desde Python.

---