# 🧶 Amigurumis - Plataforma de Compra y Venta de Patrones

Este proyecto es una plataforma web desarrollada en Django que permite a usuarios registrarse, subir patrones de amigurumis en formato PDF con imagen y descripción, y también comprar patrones subidos por otros usuarios. Es un reto personal enfocado en el desarrollo completo de una aplicación backend con Django y Django REST Framework, utilizando Tailwind CSS para el diseño frontend.

---

## 🚀 Funcionalidades principales

- Registro e inicio de sesión de usuarios (vendedores y compradores).
- Subida de patrones en formato PDF con imagen, descripción y precio.
- Compra de patrones por parte de usuarios registrados.
- Visualización de patrones comprados y subidos.
- Panel de administración personalizado.
- Diseño responsive con Tailwind CSS.

---

## 🧩 Tecnologías utilizadas

- **Python 3**
- **Django 4+**
- **Django REST Framework** (planeado)
- **Tailwind CSS**
- **SQLite** (desarrollo) / PostgreSQL (planeado para producción)

---

## 📁 Estructura del proyecto

amigurumis/
  ├── amigurumis/ # Configuración del proyecto
  ├── usuarios/ # Gestión de usuarios (modelo personalizado)
  ├── patrones/ # Lógica de subida y visualización de patrones
  ├── compras/ # Gestión de compras y relaciones usuario-patrón
  ├── templates/ # Plantillas HTML con Tailwind
  ├── static/ # Archivos estáticos
  ├── media/ # Archivos subidos por los usuarios (imágenes, PDFs)
  └── README.md # Este archivo

## 🛠️ En desarrollo / Pendientes

├── API REST con Django REST Framework.
├── Sistema de valoraciones/comentarios.
├── Filtro y búsqueda por categoría, precio, etc.
├── Interfaz de perfil de usuario.
├── Integración con pasarela de pagos (Stripe, PayPal, etc.).
├── Despliegue en producción (Render / Railway / Vercel).

## 📄 Licencia
Este proyecto es de uso educativo y personal. Si deseas reutilizarlo o contribuir, siéntete libre de abrir un pull request o contactarme.
