import web
from web import form

render = web.template.render('templates/')

urls = ('/','index')
app = web.application(urls, globals())

myform = form.Form(
    form.Checkbox('csv'),
    form.Checkbox('jdf'),
    form.Dropdown('files',['csv','jdf']))

class index:
    def GET(self):
        form = myform()
        return render.formest(form)

    def POST(self):
       form = myform()
       if not form.validates():
           return render.formtest(form)
       else:
           return "Grrreat success! files:%s csv:%s jdf:%s" % (form['files'].value,form['csv'].get_value(),form['jdf'].checked)
            #return "type:form %s,%s" % ( form.get('csv').get_value(),form.get('csv').get_default_id())
if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()
