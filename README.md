# PAPIME_PE103825
Entregables del proyecto PAPIME PE103825

## Contenido

### Simulador

Se desarrolló un simulador para el prototipo Pumas-Rover, construído como parte de este proyecto, utilizando el simulador Webots y la plataforma ROS2. Para correrlo, se deben cumplir los siguientes requerimientos:

* [Ubuntu 24.04](https://ubuntu.com/download/desktop/thank-you?version=24.04.3&architecture=amd64&lts=true)
* [ROS Jazzy](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)
* [Webots 2025a](https://github.com/cyberbotics/webots/releases/download/R2025a/webots_2025a_amd64.deb)

Para instalar, compilar y probar, ejecute:

* cd
* git clone https://github.com/LIRA-UNAM/PAPIME_PE103825
* cd PAPIME_PE103825
* ./Setup.sh
* cd ros2_ws
* colcon build && source install/setup.sh
* ros2 launch webots_simul rover_launch.py

Se debería desplegar un simulador como el siguiente:


### Ejercicios:

1. [Herramientas de Software](https://github.com/LIRA-UNAM/PAPIME_PE103825/blob/main/Ejercicios/Ejercicio01/Ejercicio01.pdf)
2. La plataforma ROS2
