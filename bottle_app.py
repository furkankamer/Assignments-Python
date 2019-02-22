
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################
import bottle

from bottle import route, run, default_app, debug, get, request, post, request, static_file
from bottle import *



from csv import reader 
contents = [] 
input_file = open("a2_input.csv","r") 
for row in reader(input_file):     
    contents = contents + [row] 
    

    
    
    
    
def htmlify(title,head,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8"  />
                <meta name="viewport" content="width=device-width, initial-scale=1.0"  />
                <style>
                table {
                font-family: serif;
}
                td {
                border: 3px;
                text-align: center;
                padding: 10px;
}
                ul{
                text-shadow: 0.5px 0.5px #ff0000
                }
                h1 {
                color: gray;
                text-shadow: 2px 2px #ffffff;
                }
                form {
                text-align: center;
                align: center;
                
                }
                input {
                
                }
                input[type=text] {
                width: 300px;
                
                }
                
                th{
                text-shadow: 0.5px 0.5px #0000ff;
                
                }
                td{
                text-shadow: 0.5px 0.5px #00ffff;
                }
                tr {
                background-color: rgba(80, 0, 0, 0.9); 
                color: gray;
                
                transition: background-color 1s ease-in-out;
}
</style>
                <title>%s</title>
            </head>
            <body style="color: blue; background-image: url(./image.jpg); background-repeat: no-repeat; background-size:cover ;">
            <div style="border-color: black; border-style: solid; border-width:5px; background-color: rgba(80, 0, 0, 0.9); color: gray; background-size: cover; font-size:18px; font-style: italic; font-weight: bold; font-family: serif;">
            <h1>%s</h1>
            
            %s
            
            </body>
        </html>

    """ % (title,head,text)
    return page







@get('/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root='./', mimetype='image/jpg')



@route('/results', 'GET')
def resultingss():
    statistics = """ <table>"""
    
    for z in range (0,7):
        statistics += """<tr>"""
        for m in range (0,6):
            statistics += """<td>""" + str(contents[z][m]) + """</td>"""
    statistics += """</table>"""                                       

    return htmlify("statistics","General Statistics", str(statistics)+"""</div>""")



@route ('/trilogy', 'POST')
def resultingsss():
    trilogy_statistics = """<table> <tr><th>Release Year</th>
<th>Film</th>
<th>Production Budget(Million $)</th>
<th>Domestic Opening Weekend(Million $)</th>
<th>Domestic Box Office(Million $)</th>
<th>Worldwide Box Office(Million $)</th></tr>"""
    trilogy_type = request.POST.get('trilogy')
    trilogy_type2 = request.POST.get('trilogy2')
    trilogy_type3 = request.POST.get('trilogy3')
    if str(trilogy_type) == "lordoftherings":
        
        if str(trilogy_type2) == "leastbudget":
                for u in range (2,4):
                    trilogy_statistics += """<tr>"""
                    for w in range (0,6):
                        trilogy_statistics += """<td>""" + str(contents[u][w]) + """</td>"""
        elif str(trilogy_type2) == "mostbudget":
                for u in range (1,2):
                    trilogy_statistics += """<tr>"""
                    for w in range (0,6):
                        trilogy_statistics += """<td>""" + str(contents[u][w]) + """</td>"""
        elif str(trilogy_type3) == "mostboxoffice":
               for z in range (3,4):
                    trilogy_statistics += """<tr>"""
                    for m in range (0,6):
                        trilogy_statistics += """<td>""" + str(contents[z][m]) + """</td>"""
                    
        elif str(trilogy_type3) == "leastboxoffice":
               for z in range (1,2):
                    trilogy_statistics += """<tr>"""
                    for m in range (0,6):
                        trilogy_statistics += """<td>""" + str(contents[z][m]) + """</td>"""
                        
        else:   
            for z in range (1,4):
                    trilogy_statistics += """<tr>"""
                    for m in range (0,6):
                        trilogy_statistics += """<td>""" + str(contents[z][m]) + """</td>"""                
                        
                        
        
    elif str(trilogy_type) == "hobbit":
            if str(trilogy_type3) == "mostboxoffice":
                for z in range (4,5):
                    trilogy_statistics += """<tr>"""
                    for m in range (0,6):
                        trilogy_statistics += """<td>""" + str(contents[z][m]) + """</td>"""
                    
            elif str(trilogy_type3) == "leastboxoffice":
                   for z in range (6,7):
                        trilogy_statistics += """<tr>"""
                        for m in range (0,6):
                            trilogy_statistics += """<td>""" + str(contents[z][m]) + """</td>"""
            
            else:
                   for z in range (4,7):
                        trilogy_statistics += """<tr>"""
                        for m in range (0,6):
                            trilogy_statistics += """<td>""" + str(contents[z][m]) + """</td>"""
    
    
    
    
    elif str(trilogy_type2) == "leastbudget":
         
            for z in range (2,4):
                trilogy_statistics += """<tr>"""
                for m in range (0,6):
                    trilogy_statistics += """<td>""" + str(contents[z][m]) + """</td>"""
    elif str(trilogy_type2) == "mostbudget":
         
            for z in range (4,7):
                trilogy_statistics += """<tr>"""
                for m in range (0,6):
                    trilogy_statistics += """<td>""" + str(contents[z][m]) + """</td>"""                
    
    elif str(trilogy_type2) == "mostbudget":
         
            for z in range (4,7):
                trilogy_statistics += """<tr>"""
                for m in range (0,6):
                    trilogy_statistics += """<td>""" + str(contents[z][m]) + """</td>"""
    
    elif str(trilogy_type3) == "mostboxoffice":
           for z in range (3,4):
                trilogy_statistics += """<tr>"""
                for m in range (0,6):
                    trilogy_statistics += """<td>""" + str(contents[z][m]) + """</td>"""
                    
    elif str(trilogy_type3) == "leastboxoffice":
           for z in range (1,2):
                trilogy_statistics += """<tr>"""
                for m in range (0,6):
                    trilogy_statistics += """<td>""" + str(contents[z][m]) + """</td>"""                
    
    else:
        for z in range (1,7):
            trilogy_statistics += """<tr>"""
            for m in range (0,6):
                 trilogy_statistics += """<td>""" + str(contents[z][m]) + """</td>"""
    trilogy_statistics += """</table>"""                                       
    
  
    return htmlify("statistics","Trilogy Statistics", str(trilogy_statistics) + """</div>""")

@route('/optional', 'POST')

def optional_search():
    entered_information = request.POST.get('information_entered')
    statistics = request.POST.get('statistics')
    optional_statistics = """<table> <tr><th>Release Year</th>
<th>Film</th>
<th>Production Budget(Million $)</th>
<th>Domestic Opening Weekend(Million $)</th>
<th>Domestic Box Office(Million $)</th>
<th>Worldwide Box Office(Million $)</th></tr>"""
    
    if str(statistics) == "date":
        for z in range (0,7):
            if str(contents[z][0]).casefold() == str(entered_information).casefold():
                
                optional_statistics += """<tr>"""
                for t in range (0,6):
                    optional_statistics += """<td>""" + str(contents[z][t]) + """</td>"""
                optional_statistics += """</tr>"""
                break
                
              
            
    if str(statistics) == "filmname":
        for s in range (0,7):
            
            if str(contents[s][1]).casefold() == str(entered_information).casefold():
                optional_statistics += """<tr>"""
                for q in range (0,6):
                    optional_statistics += """<td>""" + str(contents[s][q]) + """</td>"""
                optional_statistics += """</tr>"""
                break
    
        
    optional_statistics += """</table>"""
    
    return htmlify("optional", "Optional Statistics", str(optional_statistics) + """</div>""" )

                               
    


def resulting():
    resultings = """
    <form class="searching" action="/optional" method="POST" target="_blank">
          <fieldset>
          Search:<br><br>
          <input type="text" name="information_entered" value="2001"><br> 
          <br>
          By Date:<br>
          <input type="radio" name="statistics" value="date" checked><br>
          By Film Name:<br>
          <input type="radio" name="statistics" value="filmname"> 
          <br>
          <input type="submit" value="Find">
          <br><br>
          </fieldset>
    </form>
    <p style="font-size:18px; font-weight:bold; text-align:center; text-shadow: 0.5px 0.5px #ff0000 "> For Reveal Trilogy Statistics</p>
    <form action ="/trilogy" method="POST" target="_blank">
    
    <input type="checkbox" name="trilogy" value="lordoftherings" checked>The Lord Of the Rings Trilogy:<br>
    <input type="checkbox" name="trilogy" value="hobbit">The Hobbit Trilogy:<br>
    <input type="radio" name="trilogy2" value="leastbudget"> The Film(s) that have Least Budget <br>
    <input type="radio" name="trilogy2" value="mostbudget"> The Film(s) that have Most Budget <br>
    <input type="radio" name="trilogy3" value="mostboxoffice"> The Film(s) that have Most Box Office<br>
    <input type="radio" name="trilogy3" value="leastboxoffice"> The Film(s) that have Least Box Office <br>
    <br>
    <input type="submit" value="Click">
    </form>
    <br><br><br>
    <form action="/results" method="GET" target="_blank">
    For All Statistics<br>
    <input type="submit" value="show">
    </form>
    
    """
    return resultings




@route ('/')
def index():
    return htmlify("Statistics About Two Film Trilogies", "Some Statistics About Lord Of the Rings and Hobbit Film Trilogy", """<h2>Names and Release Year of the films</h2><ul>
<li> <strong>Release Year</strong>:2001 <strong>Film Name</strong>:The Lord of the Rings The Fellowship of the Ring </li>
<li> <strong>Release Year</strong>:2002 <strong>Film Name</strong>:The Lord of the Rings The Two Towers</li>
<li> <strong>Release Year</strong>:2003 <strong>Film Name</strong>:The Lord of the Rings The Return of the King</li>
<li> <strong>Release Year</strong>:2012 <strong>Film Name</strong>:The Hobbit An Unexpected Journey</li>
<li> <strong>Release Year</strong>:2013 <strong>Film Name</strong>:The Hobbit The Desolation of Smaug</li>
<li> <strong>Release Year</strong>:2014 <strong>Film Name</strong>:The Hobbit The Battle of the Five Armies</li>
</ul>""" +str(resulting()) + """</div>"""    )


#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

