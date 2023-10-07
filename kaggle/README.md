# KAGGLE-COURSE

## Sobre Kaggle

Kaggle es una plataforma en línea para el aprendizaje automático y el ciencia de datos. Ofrece una amplia variedad de herramientas y recursos para la investigación y el desarrollo de modelos de aprendizaje automático, así como una comunidad en línea de científicos de datos y profesionales del aprendizaje automático.

En Kaggle, los usuarios pueden participar en desafíos de ciencia de datos y aprendizaje automático, utilizar herramientas de análisis de datos y visualización, y acceder a una amplia variedad de conjuntos de datos y notebooks de código. También pueden colaborar con otros usuarios en proyectos de ciencia de datos y aprendizaje automático y compartir sus resultados y soluciones en la plataforma.

Kaggle también ofrece una serie de recursos y herramientas educativas para ayudar a los principiantes a aprender sobre el aprendizaje automático y la ciencia de datos. Estos incluyen tutoriales, cursos en línea y documentación técnica.

En resumen, Kaggle es una plataforma útil para los profesionales y aficionados interesados ​​en el aprendizaje automático y la ciencia de datos, ya sea para participar en desafíos, colaborar en proyectos o aprender sobre estas áreas de forma autodirigida.

## Instalar el API de Kaggle

Para instalar la API de Kaggle en Linux, primero necesitarás tener una cuenta de Kaggle y una clave de API. Si no tienes una clave de API, puedes obtenerla siguiendo estos pasos:

Inicia sesión en tu cuenta de Kaggle.
Haz clic en tu nombre de usuario en la esquina superior derecha de la pantalla y selecciona "Mi perfil" del menú desplegable.
Haz clic en el botón "Create New API Token" para crear una nueva clave de API. Kaggle descargará automáticamente un archivo llamado "kaggle.json" que contiene tu clave de API.
Una vez que tengas tu clave de API, puedes instalar la API de Kaggle en Linux siguiendo estos pasos:

1. Abre una terminal y asegúrate de tener instalado pip, el administrador de paquetes de Python. Si no tienes pip instalado, puedes instalarlo ejecutando el comando **"sudo apt-get install python3-pip"**.
2. Ejecuta el comando **"pip3 install kaggle"**. Esto instalará la API de Kaggle en tu máquina. Si usas miniconda, ejecuta el comando **"conda install --channel conda-forge kaggle"**.
3. Una vez que la API de Kaggle se haya instalado, necesitarás configurarla con tu clave de API. Para hacer esto, ejecuta el comando mkdir ~/.kaggle. Esto creará un directorio llamado ".kaggle" en tu directorio home.
4. Mueve el archivo "kaggle.json" que descargaste a tu clave de API a la carpeta ".kaggle" que acabas de crear. Puedes hacer esto ejecutando el comando mv kaggle.json ~/.kaggle.
5. Finalmente, ejecuta el comando chmod 600 ~/.kaggle/kaggle.json para asegurarte de que solo tú tienes acceso a tu clave de API.

Una vez que hayas completado estos pasos, la API de Kaggle estará instalada y configurada en tu máquina Linux. Ya puedes empezar a utilizarla para descargar datasets y participar en competiciones de Kaggle.

## Cargar un dataset

Para cargar un dataset directamente de Kaggle en Pandas, primero necesitarás tener una cuenta de Kaggle y haber instalado la API de Kaggle (Lea el punto anterior). Una vez que hayas hecho esto, puedes seguir los siguientes pasos:

1. Inicia sesión en tu cuenta de Kaggle y ve a la página del dataset que quieres cargar.
2. Haz clic en el botón "Download" y descarga el dataset en formato csv. 
3. En tu terminal, utiliza el comando kaggle datasets download -d <nombre-del-dataset> para descargar el dataset directamente a tu máquina. Reemplaza <nombre-del-dataset> con el nombre del dataset que quieres descargar.
4. Una vez que el dataset se haya descargado, puedes cargarlo en Pandas utilizando el método **pd.read_csv()**. Por ejemplo:

```bash
import pandas as pd

df = pd.read_csv("<ruta-al-archivo>.csv")
```

Reemplaza <ruta-al-archivo> con la ruta completa al archivo csv descargado. Una vez que hayas ejecutado este código, el dataset se cargará en un DataFrame de Pandas y podrás trabajar con él como con cualquier otro DataFrame.
