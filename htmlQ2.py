
print("HARI OM")


data= "vs1.txt"
save="omgayatri.html"


import io
import random

open_file=io.open(data,"r",encoding="UTF8")
qas=open_file.readlines()


write_file=io.open(save,"w",encoding="UTF8")
write_file.write(" ")
write_file.close()

write_file=io.open(save,"a",encoding="UTF8")
write_file.write("<!DOCTYPE html><html><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> <title>quiz1</title>  <style>  .hari { position: fixed; right: 20px; top: 0px }    #sample { font-size: 20px; background-color: yellow; color:blue; padding: 3px; }      div { display: none; overflow-y: auto; height: 800px; }        .wrong { border-style: solid; padding:5px; font-size: 18px; }             .right{ border-style: solid; padding: 5px; font-size: 18px; } h1{ margin-top: 50px; color:blue; font-size: 20px; }</style></head><body>")

allHeadings=[]
headingvalue=0

for heading in qas:
  if '#' in heading:
    allHeadings.append(heading[1:])
    
write_file.write(" <p class=\"hari\">  <select id=\"sample\" onchange=\"getvalue()\"> ")

for heading in allHeadings:
  print(heading)
  write_file.write(f"<option value=\"om{str(headingvalue)}\">{heading}</option>")
  headingvalue+=1
  
write_file.write("</select></p>")
  

questions=[]
answers=[]

cou=0
fn=0
quiz_code=[]
headingCounter=0


  
   
qusNumber=0;

for q in qas:
  if '---' in q:
    
    questions.append(q.split("---")[0])
    answers.append(q.split("---")[1])
    
  
    
    ans= "<h2 class='right' onclick=\"this.style.backgroundColor='green' \">"+answers[questions.index(q)]+"</h2>"
    cou+=1
    qusNumber+=1
     
     
     
     
    opt1 = "<h2 class='wrong' onclick=\"this.style.backgroundColor='red' \">"+random.choice(answers)[:-1]+"</h2>"
    opt2 ="<h2 class='wrong'onclick=\"this.style.backgroundColor='red' \">"+ random.choice(answers)[:-1]+"</h2>"
    opt3 ="<h2 class='wrong' onclick=\"this.style.backgroundColor='red' \">"+ random.choice(answers)[:-1]+"</h2>"
    one_str_answer =[ ans,opt1,opt2,opt3]
    two_str_answer = [opt3,ans,opt1,opt2]
    three_str_answer = [opt2,opt3,ans,opt1]
    four_str_answer = [opt1,opt2,opt3,ans]   
    answeres_list = [one_str_answer, two_str_answer, three_str_answer, four_str_answer] 
    random_option = random.choice(answeres_list)
    write_file.write("<h1>"+str(qusNumber)+". "+questions[questions.index(q)]+"</h1>")
    write_file.write("".join(random_option))
  if "#" in q:
    if headingCounter==0:
      write_file.write(f"<div id=\"om{headingCounter}\"> ")
      headingCounter+=1
    elif headingCounter>0:
      write_file.write(f"</div><div id=\"om{str(headingCounter)}\"> ")
      headingCounter+=1
  else:
  
    write_file.write(f"<p>{q}</p>")
      
strScript=" </div> <script>                 var elem = document.querySelectorAll('wrong');                      function getvalue(){ const divs = document.getElementsByTagName('div'); for(div of divs){ div.style.display=\"none\"; }                    document.getElementById(document.getElementById('sample').value).style.display='block';}              </script>   "   
write_file.write(strScript)
write_file.write("</body></html>")
write_file.close()
   
 
   
   
  


      
      
       
       
     
   
   
   
   
   
   
                      
                      
   