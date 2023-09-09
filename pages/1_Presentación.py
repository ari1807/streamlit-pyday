import streamlit as st
import reveal_slides as rs
from streamlit_extras.app_logo import add_logo

from PIL import Image
from pathlib import Path

pyday_logo_path = Path(Path(__file__).parent.parent, "public", "images",
    "pyday-logo.png")

st.set_page_config(layout="centered", 
                   menu_items=
                   {
                       'Report a bug': "https://www.github.com/ari1807/streamlit-pyday/issues",
                       'About': "Hecho por Ariadna Aspitia para el PyDay La Plata 2023"
                    },
                    page_icon=Image.open(pyday_logo_path))

logo = add_logo(pyday_logo_path)


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

Fue creado para equipos de *Data Science* y *Machine Learning*. Está orientado a la ciencia de datos.

--

## Abstrae al desarrollador de:
* Escribir HTML, CSS, Javascript <!-- .element: class="fragment" data-fragment-index="0" -->
* Crear los endpoints de la aplicación <!-- .element: class="fragment" data-fragment-index="1" -->
* Integrar el frontend con el backend <!-- .element: class="fragment" data-fragment-index="2" -->

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

Streamlit es muy fácil de aprender. Tener una página funcionando es tan
sencillo como importar la librería de streamlit en un script de Python, escribir alguna línea de código y ejecutar: 
```bash
streamlit run <file>.py
```
o como un módulo de Python:
```bash
python -m streamlit run <file>.py
```

--

Tiene una `comunidad activa`, que se encuentra haciendo mejoras periódicamente. Se puede ver en su <a target="_blank" href="https://roadmap.streamlit.app/">roadmap</a> en qué nuevas funcionalidades se encuentran trabajando.

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

Los <a target="_blank" href="https://streamlit.io/components">*componentes*</a> son módulos de terceros que extienden las posibilidades de Streamlit.
Estos componentes son escritos en JavaScript y HTML y pueden ser renderizados en aplicaciones de Streamlit. Una vez hechos, se envuelven en un paquete Python y se comparten con la comunidad.
--

Para instalar un componente basta con ejecutar:
```bash
pip install <componente>
```

---

## Despliegue

Streamlit provee documentación sobre cómo conteneirizar y desplegar una aplicación Streamlit en <a target="_blank" href="https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker">Docker</a>
y <a target="_blank" href="https://docs.streamlit.io/knowledge-base/tutorials/deploy/kubernetes">Kubernetes</a>. También desde la documentación referencia distintos tutoriales para desplegar Streamlit en distintas nubes.

--

## Streamlit Community Cloud

Streamlit Community Cloud es una opción interesante y sencilla de desplegar tu aplicación y disponibilizarla en internet completamente gratis.

--

Streamlit se encarga de:
* La conteneirización de la aplicación.
* El despliegue de la misma.
* Mantener la sincronización con el repositorio donde tengas tu código.

> Todos los cambios que se realicen en los scripts del repositorio se verán reflejados en la aplicación casi inmediatamente.

--

### Pasos:
- Registrarse en <a target="_blank" href="share.streamlit.io/signup.">Streamlit Community Cloud</a> con alguna cuenta de email.
- Integrar con una cuenta de Github. Una vez hecho esto, se te redirigirá a tu Workspace de Streamlit.
- Crear un repositorio con los scripts.
- Desde Streamlit Community Cloud, hacer clic en `New app` e indicar el repositorio de la aplicación.
--

Luego de unos minutos podrás acceder a tu página web Streamlit desde la URL `<nombre-elegido>.streamlit.app`

---

## Ejemplo

"""


theme = st.selectbox("Theme", ["black", "black-contrast", "blood", "dracula", "moon", "white", "white-contrast", "league", "beige", "sky", "night", "serif", "simple", "solarized"], index=10)


presentation = rs.slides(content_markdown, height=500, theme=theme,
        config={"width":900, "height":900, "minScale":0.1, "center":True,
        "maxScale":3.0,
            "margin": 0.1, "plugins": ["highlight", "katex", "zoom", "notes"]},
        initial_state={"indexh": 0, "indexv": 0, "indexf": -1, "paused": False,
            "overview": False}, markdown_props={"data-separator-vertical": "^--$"},
        key="presentation")
