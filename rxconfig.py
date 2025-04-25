import os
import reflex as rx

def main():
    # Usa el puerto asignado por el entorno de Render
    port = os.getenv("PORT", 3001)  # Si no encuentra la variable de entorno, usará 3001
    rx.run(port=port)

if __name__ == "__main__":
    main()
