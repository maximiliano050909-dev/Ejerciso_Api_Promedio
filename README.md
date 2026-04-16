#  API de Promedio de Calificaciones

##  Descripción

Esta API fue desarrollada con Flask y permite calcular el promedio de un conjunto de calificaciones enviadas mediante una petición HTTP en formato JSON.

Además, incluye un endpoint para convertir temperaturas entre Celsius y Fahrenheit.

---

##  Tecnologías utilizadas

* Python 3
* Flask
* Postman (para pruebas)

---

##  Instalación y ejecución

### 1. Clonar o descargar el proyecto

```bash
git clone <URL_DEL_REPOSITORIO>
cd api_promedio
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno:

* Windows:

```bash
venv\Scripts\activate
```

* Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install flask
```

### 4. Ejecutar la aplicación

```bash
python app.py
```

La API se ejecutará en:

```
http://127.0.0.1:5000
```

---

##  Endpoints

### 🔹 1. Calcular promedio

* **URL:** `/promedio`
* **Método:** POST
* **Descripción:** Calcula el promedio de calificaciones de un estudiante.

####  Entrada (JSON)

```json
{
  "nombre": "Juan",
  "calificaciones": [80, 90, 85, 70]
}
```

####  Respuesta

```json
{
  "nombre": "Juan",
  "promedio": 81.25
}
```

![alt text](image2.png)

---

### 🔹 2. Convertir temperatura

* **URL:** `/convertir-temperatura`
* **Método:** POST
* **Descripción:** Convierte temperaturas entre Celsius y Fahrenheit.

#### 📥 Entrada (JSON)

```json
{
  "valor": 25,
  "escala": "C"
}
```

####  Respuesta

```json
{
  "valor_original": 25,
  "escala_original": "C",
  "resultado": 77.0,
  "escala_convertida": "Fahrenheit"
}
```

---

##  Manejo de errores

La API valida que los datos sean correctos. En caso contrario, devuelve un mensaje de error:

```json
{
  "error": "Datos incompletos o incorrectos"
}
```

---

##  Autor

Proyecto desarrollado como práctica de APIs con Flask.

![alt text](image1.png)