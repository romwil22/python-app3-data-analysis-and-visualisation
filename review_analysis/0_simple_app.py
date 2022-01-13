import justpy as jp

# MAKING QUASAR WEB PAGE
def app():
    web_page = jp.QuasarPage()
    h1 = jp.QDiv(a=web_page, text="Analysis of course reviews", classes="text-h2 text-weight-bold text-center q-pa-lg")
    p1 = jp.QDiv(a=web_page, text="These graph represent course review analysis")
    
    return web_page

jp.justpy(app)