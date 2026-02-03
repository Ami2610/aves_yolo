# Detector de Aves con YOLOv11

## Descripción del proyecto

Este proyecto implementa un **detector de objetos personalizado** utilizando **YOLOv11**, entrenado para identificar tres tipos de aves: **Águila, Avestruz y Cóndor**. El modelo fue entrenado en **Google Colab** con un dataset personalizado y posteriormente integrado en una aplicación local desarrollada con **Flask**, **OpenCV** y **Visual Studio Code**, permitiendo la detección en tiempo real mediante cámara web.

---

## Clases detectadas

- Águila
- Avestruz
- Cóndor

---

## Tecnologías utilizadas

- Python 3.10+
- YOLOv11 (Ultralytics)
- PyTorch
- OpenCV
- Flask
- Google Colab (entrenamiento)
- Visual Studio Code (desarrollo local)
- Roboflow (gestión del dataset)

---

## Dataset

El conjunto de datos fue obtenido y gestionado mediante **Roboflow**, y se organizó en formato compatible con YOLO.

**Distribución del dataset:**
- Entrenamiento: 66 imágenes
- Validación: 19 imágenes
- Prueba: 9 imágenes
- **Total:** 94 imágenes

**Clases:** 3 (Águila, Avestruz y Cóndor)

---

## Entrenamiento del modelo (Google Colab)

El entrenamiento del modelo se realizó en **Google Colab**, siguiendo el flujo de trabajo descrito en el siguiente recurso:

🔗 https://omes-va.com/crea-tu-propio-detector-de-objetos-personalizado-con-yolov11/

### Proceso de entrenamiento

1. Preparación del dataset en formato YOLO
2. Configuración del archivo `data.yaml`
3. Entrenamiento del modelo YOLOv11
4. Evaluación mediante métricas estándar de detección de objetos

---

## Resultados del entrenamiento

Las métricas obtenidas evidencian un **desempeño sobresaliente del modelo**, con alta precisión y capacidad de generalización dentro del dominio del problema.

### Métricas globales

- mAP@0.5 ≈ **0.995**
- Alta precisión y recall para todas las clases

### Gráficas del entrenamiento

[Imagen] results.png

[Imagen] confusion_matrix.png

[Imagen] BoxPR_curve.png 

[Imagen] table_metrics.png

[Imagen] example.png
---

## Interpretación de resultados

La curva **Precision–Recall** muestra un comportamiento casi ideal, con valores cercanos a 1 tanto en precisión como en recall, lo que indica que el modelo detecta correctamente los objetos sin generar errores significativos. La matriz de confusión refleja una separación clara entre clases, evidenciando una baja confusión entre Águila, Avestruz y Cóndor.

---

## Ejecución en local (Visual Studio Code)

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Ami2610/aves_yolo.git
cd aves_yolo
```

### 2️⃣ Crear y activar entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Instalar dependencias

```bash
pip install flask opencv-python ultralytics
```

### 4️⃣ Ejecutar la aplicación

```bash
python app.py
```

### 5️⃣ Acceder desde el navegador

```text
http://localhost:5000
```

---

## Aplicación web (detección en tiempo real)

La aplicación integra el modelo entrenado en una interfaz web desarrollada con **Flask**, permitiendo la detección de aves en tiempo real mediante la cámara del dispositivo, mostrando las predicciones directamente en el navegador.
