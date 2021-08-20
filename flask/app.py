from flask import Flask, render_template, request
from tensorflow.keras.models import load_model

app = Flask(__name__)
cmd_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','30','41','42','43','44','45','46','47','48','49','50']
#cmd_list = ["tasklist","ver","ipconfig","net_time","cd","systeminfo","netstat","whoami","nbtstat","net_start","set","qprocess","nslookup","fsutil","net_view","type","net_use","echo","net_user","net_group","net_localgroup","dsquery","net_config","csvde","net_share","quser","net_session","query","tracert","nltest","at","move","schtasks","copy","ren","reg","wmic","powershell","md","cscript","runas","sc","netsh","wusa","icacls","del","taskkill","klist","wevtutil","rd"]
commands = []
list_commands = []
dic = ['Not being attacked','Being attacked']

model = load_model('NNLSTM.h5')

model.make_predict_function()
def predict_label(cm):
    list_commands.clear()
    commands.clear()
    for i in range(len(cmd_list)):
        if cmd_list[i] in cm:
            commands.append(1)
        else:
            commands.append(0)
    print(commands)
    list_commands.append(commands)
    list_commands.append(commands)
    p=model.predict(list_commands)
    if p[1:]>0.5: res=1
    else: res=0
    return dic[res]
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': 
        print(request.form.getlist('mycheckbox'))
        return predict_label(request.form.getlist('mycheckbox'))
    return render_template('checkbox.html')
      
