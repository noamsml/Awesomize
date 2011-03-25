import web
import buzz
import random

mappings = (
        '/', 'index',
)

app = web.application(mappings, globals())

render = web.template.render("views/")

class index:
    def GET(self):
        result = buzz.awesomize() #(source, high_level_strucure)
        source = result[0]
        quote = result[1]
        img = "bizman" + random.choice(["","2"]) + ".png"
        return render.index(source,quote,img)

if __name__ == "__main__": app.run()
