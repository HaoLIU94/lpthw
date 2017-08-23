import web
import os 
from web import form 

urls = (
	'/upload', 'Upload',
	'/unzip','Unzip',
  '/predict','Predict',
  '/download','Download',
  '/diagrame','Diagrame',
  '/.*','Upload')  

render = web.template.render('templates/')  

myform = form.Form(
    form.Checkbox("Export CSV",value='bar'),
    #form.Checkbox("Export JDF")
  )

class Upload:  
	def GET(self):  
		web.header("Content-Type","text/html; charset=utf-8")  
		return render.main_page()

	def POST(self):  
		x = web.input(myfile={})
		web.form.Button("save").render()
		web.form.Button("action", value="save", html="<b>Save Changes</b>").render()   
		filedir = '/home/hao/server/webpy' # change this to the directory you want to store the file in.  
		if 'myfile' in x: # to check if the file-object is created  
			filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.  
			filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)  
			fout = open(filedir +'/'+ filename,'w') # creates the file where the uploaded file should be stored  
			fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.  
			fout.close() # closes the file, upload complete.
		raise web.seeother('/upload')  

class Unzip:
	def GET(self):
		os.system("python src/unzip.py")
		return web.seeother('/home')

class Predict:
  def GET(self):
    os.system("python src/unzip.py")
    return web.seeother('/home')

class Diagrame:
  def GET(self):
    form = myform()
    return render.formest(form)
    #return render.diagrame()
    #os.system("python src/unzip.py") 
  def POST(self): 
      f = myform()
      c = f["Export CSV"]
      if c.checked():
        #print c.render()
        return web.seeother('/download')
      else:
        return web.seeother('/home')

class Download:
	def GET(self):
		file_name = 'JDF-BUILDASIGN-13-07-2017.tar'
		file_path = '/home/hao/JDF-BUILDASIGN-13-07-2017.tar'
		f = None 
		f = open(file_path, "rb")
		web.header('Content-Type','application/octet-stream')
		web.header('Content-disposition', 'attachment; filename=%s' % file_name)
		return f.read( )

if __name__ == "__main__":  
   app = web.application(urls, globals())   
   app.run()  