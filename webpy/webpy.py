import web
import os 
from web import form 

urls = (
	'/upload', 'Upload',
	'/unzip','Unzip',
  '/predict','Predict',
  '/download','Download',
  '/checkbox','Checkbox'
  '/.*','Upload')

myform = form.Form( 
form.Checkbox('Extract CSV'),
form.Checkbox('Extract JDF') 
)     
  
class Upload:  
	def GET(self):  
		web.header("Content-Type","text/html; charset=utf-8")  
		return """<!DOCTYPE html>
<html>
<head>
    <title>Machine learning</title>
    <meta charset="utf-8">
    <meta name="author" content="Federico Cargnelutti">
    <meta name="description" content="mvc.py allows you to use web.py framework in a Model-View-Controller fashion and keep the code separate from each other">
    <meta name="title" content="mvc.py - web.py web application written in MVC style" />
    <meta name="keywords" content="web api, api, apify, rest, restful, web services, framework, library, web development, mobile development, web application, mobile application, web programming, web development london" />
    <meta name="language" content="en" />
    <meta name="robots" content="all,index,follow" />
    <meta name="distribution" content="global" />
    <meta name="rating" content="general" />
    <meta content="all" name="robots" />
    <meta content="global" name="distribution" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    
    <!-- html5 shim, for IE6-8 support of HTML elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- styles -->
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css">
    
    <!-- scripts -->
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js"></script>
</head>

<body>

<!-- Topbar -->
<div class="topbar">
  <div class="fill">
    <div class="container">
      <h3><a href="/">Home</a></h3>
        <ul>
          <li class="">
          <form method="POST" enctype="multipart/form-data" action=""> 
			<input type="file" name="myfile" /> 
			<br/> 
			<input type="submit" /></li>
      <div class="container">
      <div class="content">
        <li class=""><a href="/predict">Predict<span></span></a></li>
      </div>
      </div>
        </ul>
    </div><!-- /container -->
  </div>
</div><!-- /topbar-->

<div class="quickstart">
</div>

<div class="container">
    <div class="content">
    <li class=""><a href="/checkbox">Download<span></span></a></li>
    </div>
</div>
    
<div id="footer">
  <div class="inner">

    <div class="container">
      <p>&nbsp;</p>
      <p>Copyright &copy; 2017 <a href="https://github.com/HaoLIU94" target="_blank">Hao LIU</a>. All Rights Reserved.</p></p>
    </div>
    
  </div>
</div>

</body>
</html>""" 
  

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

		raise myform.render() 

class Unzip:
	def GET(self):
		os.system("python src/unzip.py")
		return web.seeother('/home')
class Checkbox:
	def GET(self):
		#os.system("python src/unzip.py")
		raise render.form(myform)

class Predict:
  def GET(self):
    os.system("python unzip.py")
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