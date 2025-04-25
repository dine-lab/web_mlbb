import reflex as rx

def index():
    return rx.vstack(
        rx.heading("Mobile Legends: Bang Bang", size="9", color="#11317a"),
        rx.image(src="https://cdn-bgp.bluestacks.com/BGP/us/gametiles_com.mobile.legends.jpg", width="300px"),
        rx.text("¡Bienvenido a la arena de batalla más épica para móviles!"),
        rx.heading("¿Qué es Mobile Legends?", size="7", mt="6"),
        rx.text("Mobile Legends: Bang Bang es un juego multijugador en línea (MOBA) desarrollado y publicado por Moonton, una filial de ByteDance. Lanzado en 2016, el juego se ha vuelto popular en el sureste de Asia y fue uno de los juegos seleccionados para el primer evento con Esports en los Juegos del Sudeste Asiático 2019 desarrollado en Filipinas."),
        rx.heading("Jugabilidad", size="7", mt="6"),
        rx.text("Mobile Legends: Bang Bang es un MOBA diseñado para celulares. Los dos equipos enemigos se enfrentan para alcanzar y destruir la base enemiga, al mismo tiempo que defienden la propia por medio del control de líneas, las tres 'líneas' conocidas como 'superior', 'media', e 'inferior', las cuales conectan ambas bases. Personajes más débiles controlados por computadora, llamados 'minions', aparecen en las bases de cada equipo y siguen las tres líneas hacía la base del equipo enemigo, luchando contra enemigos y torres."),
        rx.heading("Modos de juego", size="7", mt="6"),
        rx.text("- Clásico"),
        rx.text("- Clasificatoria"),
        rx.text("- Arcade"),
        rx.text("- Coliseo"),
        rx.heading("Héroes populares", size="7", mt="6"),
        rx.text("• Alucard • Gusion • Layla • Nana • Tigreal"),
        rx.button("Visitar sitio oficial", on_click=rx.redirect("https://m.mobilelegends.com/")),
        padding="4em",
        spacing="2"
    )

app = rx.App()
app.add_page(index, title="Mobile Legends App")