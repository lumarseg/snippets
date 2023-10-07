# SSH-101

## 1. Configurar tus llaves SSH en local

### Generar las llaves SSH

En tu entorno de computadora, vas a crear una "Llave Pública" y una "Llave Privada".

```bash
ssh-keygen -t rsa -b 4096 -C <correo_electronico>
```

Por defecto, la llaves se guardan en la carpeta "~/.ssh", con el nombre de: "id_rsa" para la llave privada y "id_rsa.pub" para la llave pública.

Para más información ver: [Soporte de Ayuda Github.com](https://help.github.com/es/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), [Soporte git-scm.com](https://git-scm.com/book/it/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key), [Soporte ssh.com](https://www.ssh.com/ssh/keygen).

## 2. Validar tu entorno de trabajo

### Para Windows y Linux

Si usas Windows o Linux, debes seguidamente correr este comando (utilice el Batch de GIT), para verificar que el servidor de llaves SSH está corriendo:

```bash
eval $(ssh-agent -s)
```

Como respuesta tendrá lo siguiente, donde '######' puede ser algun número entero:

```bash
$ eval $(ssh-agent -s)
Agent pid ######
```

El siguiente paso es añadir la llave al servidor de llaves SSH, porque el que exista la llave no es suficiente, es necesario indicar que la llave existe (agregar una identidad al ssh-agent), por tanto ejecute:

```bash
ssh-add <ruta-donde-guardaste-tu-llave-privada>
```

Si necesita tener una lista de llaves (identidades agregadas), utilice el siguiente comando:

```bash
ssh-add -D
```

### Para MAC OS

Si estas usando MAC OS, abra la consola de terminal para verificar que el servidor de llaves SSH está corriendo (observe la diferencia con las ""):

```bash
eval "$(ssh-agent -s)"
```

Seguidamente debes crear un archivo llamado "config", que estará en la carpeta "~/.ssh", con este contenido:

```bash
# Si usas una versión de OSX superior a Mac Sierra (v10.12)
# debes crear o modificar un archivo "config" en la carpeta
# de tu usuario con el siguiente contenido (ten cuidado con
# las mayúsculas):
Host *
        AddKeysToAgent yes
        UseKeychain yes
        IdentityFile ruta-donde-guardaste-tu-llave-privada
```

Reemplace la cadena "ruta-donde-guardaste-tu-llave-privada" por la ruta de la llave privada, obvio !!!.
Posteriormente, debemos agregar la llave privada al servidor de llaves SSH.

```bash
ssh-add -K <ruta-donde-guardaste-tu-llave-privada>
```
