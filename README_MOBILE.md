# 📱 Cómo Compilar tu App para Android

## Opción 1: Compilar ONLINE con GitHub (RECOMENDADO - Gratis)

Esta es la forma más fácil. No necesitas instalar nada en tu computadora.

### Paso 1: Crear una cuenta en GitHub
1. Ve a https://github.com
2. Crea una cuenta gratuita (si no tienes una)
3. Confirma tu email

### Paso 2: Subir tu proyecto a GitHub
1. Ve a https://github.com/new
2. Crea un nuevo repositorio llamado `derivadas-calculator`
3. Inicializa con README
4. Crea el repositorio

### Paso 3: Subir los archivos
En tu computadora, abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/TU_USERNAME/derivadas-calculator.git
git push -u origin main
```

(Reemplaza `TU_USERNAME` con tu nombre de usuario de GitHub)

### Paso 4: Configurar GitHub Actions
1. En tu repositorio de GitHub, ve a "Actions"
2. Busca "Buildozer" y crea el workflow
3. O crea manualmente un archivo `.github/workflows/buildozer.yml` con este contenido:

```yaml
name: Build APK

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Build with Buildozer
      uses: arturadib/Kivy-Buildozer-Action@master
      with:
        command: buildozer android debug
        options: |
          p4a.bootstrap = sdl2
    
    - name: Upload APK
      uses: actions/upload-artifact@v2
      with:
        name: app-debug
        path: bin/*.apk
```

### Paso 5: Descargar el APK compilado
1. Ve a Actions en tu repositorio
2. Espera a que el workflow "Build APK" termine (unos 15-30 minutos)
3. Descarga el archivo `.apk` desde los "artifacts"
4. Transfiere el APK a tu teléfono Android
5. Abre el archivo en tu teléfono para instalar

---

## Opción 2: Compilar con Buildozer Localmente

Si prefieres compilar en tu computadora:

### Requisitos (Una sola vez):
1. **Java Development Kit (JDK)**
   - Descarga desde: https://www.oracle.com/java/technologies/downloads/
   - Instala JDK 11 o superior

2. **Android SDK**
   - Descarga desde: https://developer.android.com/studio
   - Instala Android Studio

3. **Configura variables de entorno (Windows)**
   - Presiona `Win + X` y busca "Variables de entorno"
   - Añade estas rutas:
     ```
     JAVA_HOME = C:\Program Files\Java\jdk-11
     ANDROID_SDK_ROOT = C:\Users\TuUsuario\AppData\Local\Android\Sdk
     ```

### Compilar:
```powershell
cd "c:\ruta\a\tu\proyecto"
buildozer android debug
```

El APK se genera en `bin/derivadascalculator-0.1-debug.apk`

---

## Instalar en tu Teléfono Android

### Opción A: USB (más rápido)
```powershell
adb install -r bin/derivadascalculator-0.1-debug.apk
```

### Opción B: Transferencia manual
1. Conecta tu teléfono por USB
2. Copia el archivo `.apk` a tu teléfono
3. Abre el archivo con el administrador de archivos
4. Toca "Instalar"

### Opción C: Código QR
1. Sube el APK a un servidor web
2. Genera un código QR
3. Escanéa con tu teléfono

---

## Archivos Incluidos

- `main.py` - App compilable para móvil
- `desktop_app.py` - App de escritorio (Windows/Mac/Linux)
- `derivatives_calculator.py` - Motor matemático
- `buildozer.spec` - Configuración para compilar

---

## Troubleshooting

**"Error: No module named sympy"**
- Abre `buildozer.spec` y busca `requirements = `
- Cambia a: `requirements = python3,kivy,sympy,numpy,matplotlib`

**"Build fails"**
- Intenta con GitHub Actions (es más confiable)
- O instala todas las herramientas localmente

**"APK no instala en mi teléfono"**
- Ve a Configuración > Seguridad > Permitir instalación de apps desconocidas
- Habilita la opción para tu administrador de archivos

---

## ¿Necesitas ayuda?

Si algo no funciona, avísame y te ayudaré! 🚀
