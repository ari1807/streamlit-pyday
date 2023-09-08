import streamlit as st
import reveal_slides as rs

content_markdown = r"""

# <a target="_blank" href="https://streamlit.io/">Streamlit</a>
<!-- .slide: data-background-video="https://bouzidanas.github.io/videos/pexels-cottonbro-9665235.mp4" data-background-video-loop data-background-video-muted -->

---

## Agenda:
* Introducción
* Instalación
* Aprendizaje
* Componentes
* Despliegue
* Ejemplo

---

## ¿Qué es?

Es un framework de desarrollo de aplicaciones web open-source escrito en Python que te permite crear aplicaciones **interactivas** rápidamente.

--

Fue creado para equipos de *Data Science* y *Machine Learning*. Está orientado a la ciencia de datos

--

## Abstrae al desarrollador de:
* Creación de HTML, CSS, Javascript <!-- .element: class="fragment" data-fragment-index="0" -->
* Creacion de endpoints <!-- .element: class="fragment" data-fragment-index="1" -->
* Integración entre el frontend y el backend <!-- .element: class="fragment" data-fragment-index="2" -->
* etc <!-- .element: class="fragment" data-fragment-index="3" -->

---

## Instalación

A la hora de instalar Streamlit, se recomienda primero configurar un _ambiente virtual_.
Así, las dependencias que instala Streamlit no afectan a otros projectos de Python.
Algunas herramientas:
* <a target="_blank" href="https://python-poetry.org/">poetry</a>
* <a target="_blank" href="https://virtualenv.pypa.io/en/latest/">virtualenv</a>
* <a target="_blank" href="https://www.anaconda.com/">conda</a>

--

Luego se puede instalar en con el manejador de paquetes <a target="_blank" href="https://python-poetry.org/">pip</a>:
```bash
pip install streamlit
```

---

## Aprendizaje

Streamlit tiene una curva de aprendizaje muy leve. Tener una página funcionando es tan
sencillo como importar la librería streamlit en un script de python y ejecutar 
```bash
streamlit run <file>.py
```

--

Tiene una comunidad activa, que se encuentra haciendo mejoras periódicamente.

--

Dejan a disposición mucho material de aprendizaje:
* <a target="_blank" href="https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q">Videotutoriales</a>
* <a target="_blank" href="https://docs.streamlit.io/">Documentación</a>
* <a target="_blank" href="https://streamlit.io/gallery">Galería de aplicaciones</a>
* <a target="_blank" href="https://discuss.streamlit.io/">Foro</a>
* <a target="_blank" href="https://blog.streamlit.io/">Blogs</a>
* Y más...

---

## Componentes

Los *componentes* son 

---

## Despliegue

Streamlit Community Cloud te permite desplegar tu aplicación y disponibilizarla en internet completamente gratis.

--

Streamlit se encarga de:
* La conteneirización de la aplicación.
* El despliegue de la misma.
* Mantener la sincronización con el repositorio.

> Todos los cambios que se realicen en los scripts del repositorio se verán reflejados en la aplicación casi inmediatamente.

--

### Pasos:
- Registrarse en Streamlit Community Cloud con alguna cuenta de email.
- Integrar con una cuenta de Github.
- Crear un repositorio con los scripts.
- Desde Stremlit Community Cloud, indicar el repositorio de despliegue.

--

Luego de unos minutos podrás acceder a tu página web Streamlit desde la URL `nombre-despliegue.streamlit.app`



---
## Fin
"""


theme = st.selectbox("Theme", ["black", "black-contrast", "blood", "dracula", "moon", "white", "white-contrast", "league", "beige", "sky", "night", "serif", "simple", "solarized"], index=10)


presentation = rs.slides(content_markdown, height=500, theme=theme,
        config={"width":900, "height":900, "minScale":0.1, "center":True,
        "maxScale":3.0,
            "margin": 0.1, "plugins": ["highlight", "katex", "zoom", "notes"]},
        initial_state={"indexh": 0, "indexv": 0, "indexf": -1, "paused": False,
            "overview": False}, markdown_props={"data-separator-vertical": "^--$"},
        key="presentation")

if presentation["indexh"] == 0:
    st.markdown("La presentación es...")
