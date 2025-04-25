#!/bin/bash

# Instalar Reflex en el entorno local
pip install reflex

# Agregar el binario de pip al PATH para que Netlify lo encuentre
export PATH=$HOME/.local/bin:$PATH

# Ejecutar el export con reflex
reflex export