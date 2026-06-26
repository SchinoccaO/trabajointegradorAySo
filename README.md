# 🖥️ Trabajo Práctico Integrador – Virtualización con VirtualBox y Python

**Materia:** Arquitectura y Sistemas Operativos  
**Carrera:** Tecnicatura Universitaria en Programación  
**Institución:** Universidad Tecnológica Nacional – Facultad Regional San Francisco  
**Ciclo lectivo:** 2026  
**LINK VIDEO**: https://youtu.be/CMBM0LMWM14

**Integrantes:**
- Gonzalez Schinocca, Oriana Nerea
- Moreyra, Lorenzo 

---

## 📋 Descripción del proyecto

Este repositorio contiene el material completo del Trabajo Práctico Integrador sobre **Virtualización**. El trabajo consiste en la instalación y configuración de una máquina virtual con Oracle VirtualBox, la instalación de Ubuntu Desktop como sistema operativo invitado, y el desarrollo y ejecución de un programa en Python para calcular promedios dentro del entorno virtualizado.

---

## 📁 Contenido del repositorio

```
trabajointegradorAySo/
│
├── promedio.py                      # Código fuente del programa Python
├── TP_Informe_GonzalezMoreira.pdf   # Informe técnico completo con capturas
└── README.md                        # Este archivo
```

---

## ⚙️ Requisitos para reproducir el entorno

- Sistema operativo anfitrión: Windows
- [Oracle VirtualBox 7.x](https://www.virtualbox.org/) (hipervisor Tipo 2)
- [Ubuntu Desktop](https://ubuntu.com/desktop) (imagen ISO)
- Python 3 (incluido por defecto en Ubuntu)

---

## 🚀 Cómo ejecutar el programa

Dentro de la máquina virtual (Ubuntu), abrir la terminal y ejecutar:

```bash
python3 promedio.py
```

El programa solicita 5 números. Si se ingresa un valor no numérico, muestra un mensaje de error y vuelve a pedir el dato.

**Ejemplo de ejecución:**
```
ingrese el numero 1: 10
ingrese el numero 2: hola
Error. Ingrese un numero valido
ingrese el numero 2: 20
ingrese el numero 3: 30
ingrese el numero 4: 40
ingrese el numero 5: 50
Lista de numeros ingresados: 
[10.0, 20.0, 30.0, 40.0, 50.0]
Promedio: 30.0
```

---

## 🛠️ Dificultades encontradas durante el desarrollo

### Instalación de pip
Al intentar instalar pip, el paquete no estaba disponible en los repositorios por defecto de Ubuntu. Se resolvió activando el repositorio Universe:

```bash
sudo add-apt-repository universe -y
sudo apt update
sudo apt install python3-pip -y
```

### Error de indentación en promedio.py
Durante la escritura del script en nano se produjo un `TabError` por mezclar tabulaciones y espacios en el mismo bloque de código. Se resolvió reescribiendo las líneas afectadas usando únicamente espacios.

---

## 🔗 Recursos utilizados

- [Documentación oficial de VirtualBox](https://www.virtualbox.org/manual/)
- [Ubuntu Desktop – Canonical](https://ubuntu.com/desktop)

