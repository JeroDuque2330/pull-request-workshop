### *Workshop: Creando Pull Requests en GitHub*

#### *1. Configuración inicial*
   - *Objetivo*: Familiarizarse con el proceso de creación de un pull request en GitHub.
   - *Requisitos previos*: 
     - Tener una cuenta en GitHub.
     - Tener instalado Git en tu máquina.
     - Asegurate de haber agregado tu nombre y tu email en la configuración de git:
      ```bash
        git config user.name "John Doe"
        git config user.email johndoe@example.com
      ```
     - Conocimientos básicos de Git (clonar, agregar, hacer commit, etc.).

#### *2. Realizar un fork del repositorio*
   - *Paso 1*: Entra en el repositorio original en GitHub (Para este ejemplo, puedes omitir este paso).
   - *Paso 2*: Haz clic en el botón "Fork" en la esquina superior derecha.
   - *Paso 3*: Debería redirigirte a una nueva página, no cambies el nombre del repo y simplemente da click en `Create fork`.
   - *Paso 4*: Esto creará una copia del repositorio en tu propia cuenta de GitHub.

#### *3. Descarga el repositorio*
   - *Paso 4*: Descarga (Clona) el repositorio forkeado en tu máquina local.
     ```bash
     git clone https://URL-DEL-REPOSITORIO-FORKEADO
     ```
     
   - *Paso 5*: El comando `git clone`, descargará el repositorio y creará una nueva carpeta con el nombre del mismo. Entra en el directorio del repositorio. Puedes hacerlo con el siguiente comando o simplemente desde Visual Studio _File_ -> _Open Folder_ -> _Selecciona la carpeta descargada_

      ```bash
      cd NOMBRE-DEL-REPOSITORIO
      ```

#### *4. Creación de una nueva rama*
   - *Paso 6*: Crea una nueva rama para trabajar en los cambios.
      ```bash
      git checkout -b mi-nueva-rama
      ```
     

#### *5. Realizar cambios en el código*
   - *Paso 7*: Haz los cambios necesarios en los archivos de tu proyecto.
   - *Paso 8*: Verifica el estado de tus cambios.
      ```bash
      git status
      ```
   - *Paso 9*: Agrega los cambios al área de preparación (staging area).
     ```bash
     git add .
     ```
     
   - *Paso 10*: Haz un commit con un mensaje descriptivo.
     ```bash
     git commit -m "Descripción de los cambios"
     ```

#### *6. Subir los cambios a GitHub*
   - *Paso 11*: Empuja (push) los cambios a la rama que creaste en tu repositorio remoto en GitHub.
     ```bash
     git push origin mi-nueva-rama
     ```

#### *7. Crear un Pull Request*
   - *Paso 12*: Navega a tu repositorio en GitHub.
   - *Paso 13*: Verás un botón que dice “Compare & pull request”. Haz clic en él.
   - *Paso 14*: Añade un título y descripción detallada de los cambios realizados.
   - *Paso 15*: Revisa las diferencias entre las ramas (diffs) para asegurarte de que todo esté en orden.
   - *Paso 16*: Asigna revisores si es necesario.
   - *Paso 17*: Haz clic en “Create Pull Request”.

#### *8. Revisar y fusionar el Pull Request*
   - *Paso 18*: Otro miembro del equipo revisará el pull request y podrá hacer comentarios o solicitar cambios.
   - *Paso 19*: Si todo está bien, se procederá a fusionar (merge) el pull request con la rama principal del repositorio original.
