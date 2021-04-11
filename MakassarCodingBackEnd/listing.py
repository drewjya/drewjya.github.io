from flask import Flask, render_template, request, redirect, jsonify, session

app = Flask(__name__)
app.secret_key = 'kitaorangnyamagerangengs'

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("kunci.json")
firebase_admin.initialize_app(cred)

from firebase_admin import firestore
db = firestore.client()

d=[]

@app.route('/login')
def login():
    if 'login' in session:
        return redirect('/')
    return render_template('login.html')

@app.route('/processlogin', methods=['POST'])
def processlogin():
    name = request.form.get("username")
    word = request.form.get("password")
    data = []
    docs = db.collection('admin').where("username", "==", name).stream()
    for doc in docs:
        data = doc.to_dict()
        print(data)
        if data['password'] == word:
            session['login']= True
            return redirect('/')
    return redirect('/login')
    
@app.route('/')
def index():
    if 'login' not in session:
        return redirect ('/login')
    siswa =[]
    docs = db.collection('users').stream()
    # docs = db.collection('users').where('nilai', '>', 44).stream()
    for doc in docs:
        data = doc.to_dict()
        data["id"]=doc.id
        siswa.append(data)
    return render_template('index.html', s=siswa)

@app.route('/details/<uid>')
def user(uid):
    siswa = db.collection('users').document(uid).get().to_dict()
    return render_template('details.html', mhs=siswa)

@app.route('/awal')
def masukkan():
    data = [
    {
        "nama": "Iggy Fayre",
        "email": "ifayre0@ask.com",
        "nilai": 43,
        "foto": "https://robohash.org/repudiandaenonqui.png?size=100x100&set=set1",
        "alamat": "68 Sunbrook Center",
        "no_hp": "(907) 9485255"
    },
    {
        "nama": "Alexandro Arnowicz",
        "email": "aarnowicz1@desdev.cn",
        "nilai": 45,
        "foto": "https://robohash.org/inciduntsuscipitea.png?size=100x100&set=set1",
        "alamat": "68 6th Parkway",
        "no_hp": "(354) 5539855"
    },
    {
        "nama": "Lainey Kleinhandler",
        "email": "lkleinhandler2@eventbrite.com",
        "nilai": 45,
        "foto": "https://robohash.org/quomolestiaesed.png?size=100x100&set=set1",
        "alamat": "65 Ramsey Drive",
        "no_hp": "(756) 1627755"
    },
    {
        "nama": "Jayson Speak",
        "email": "jspeak3@networksolutions.com",
        "nilai": 58,
        "foto": "https://robohash.org/dolorumasperioresrerum.png?size=100x100&set=set1",
        "alamat": "3502 New Castle Crossing",
        "no_hp": "(648) 1000349"
    },
    {
        "nama": "Doro Allsup",
        "email": "dallsup4@networksolutions.com",
        "nilai": 48,
        "foto": "https://robohash.org/autessevelit.png?size=100x100&set=set1",
        "alamat": "9 Knutson Junction",
        "no_hp": "(437) 3561210"
    },
    {
        "nama": "Etheline Sooper",
        "email": "esooper5@imageshack.us",
        "nilai": 55,
        "foto": "https://robohash.org/etbeataedolores.png?size=100x100&set=set1",
        "alamat": "58 Eagan Center",
        "no_hp": "(681) 6372294"
    },
    {
        "nama": "Cris Reiners",
        "email": "creiners6@fastcompany.com",
        "nilai": 89,
        "foto": "https://robohash.org/praesentiumprovidentquis.png?size=100x100&set=set1",
        "alamat": "84068 Meadow Vale Plaza",
        "no_hp": "(824) 3911823"
    },
    {
        "nama": "Kristofor Spencelayh",
        "email": "kspencelayh7@naver.com",
        "nilai": 73,
        "foto": "https://robohash.org/autquiaut.png?size=100x100&set=set1",
        "alamat": "7 Sunbrook Center",
        "no_hp": "(157) 6082028"
    },
    {
        "nama": "Blakeley d' Elboux",
        "email": "bd8@discuz.net",
        "nilai": 100,
        "foto": "https://robohash.org/cupiditatedistinctiooccaecati.png?size=100x100&set=set1",
        "alamat": "56 Springs Center",
        "no_hp": "(169) 2256442"
    },
    {

        "nama": "Jervis Aspel",
        "email": "jaspel9@google.com",
        "nilai": 46,
        "foto": "https://robohash.org/quiblanditiistempora.png?size=100x100&set=set1",
        "alamat": "61835 Talisman Crossing",
        "no_hp": "(446) 3493755"
    },
    {

        "nama": "Barton Gaither",
        "email": "bgaithera@ftc.gov",
        "nilai": 64,
        "foto": "https://robohash.org/occaecatietipsum.png?size=100x100&set=set1",
        "alamat": "37 Meadow Ridge Road",
        "no_hp": "(476) 8271601"
    },
    {

        "nama": "Kari Bulgen",
        "email": "kbulgenb@ftc.gov",
        "nilai": 87,
        "foto": "https://robohash.org/facilissapientetenetur.png?size=100x100&set=set1",
        "alamat": "76 Golden Leaf Court",
        "no_hp": "(634) 7995320"
    },
    {

        "nama": "Lise Barnson",
        "email": "lbarnsonc@wordpress.com",
        "nilai": 87,
        "foto": "https://robohash.org/officiaconsecteturveritatis.png?size=100x100&set=set1",
        "alamat": "99 3rd Alley",
        "no_hp": "(383) 9948543"
    },
    {

        "nama": "Brunhilde Hubbocks",
        "email": "bhubbocksd@squarespace.com",
        "nilai": 60,
        "foto": "https://robohash.org/magnamrerumdoloremque.png?size=100x100&set=set1",
        "alamat": "37780 Service Pass",
        "no_hp": "(888) 7031858"
    },
    {

        "nama": "Ariel Halewood",
        "email": "ahalewoode@wunderground.com",
        "nilai": 57,
        "foto": "https://robohash.org/eosquiadistinctio.png?size=100x100&set=set1",
        "alamat": "75125 Lakewood Road",
        "no_hp": "(783) 9371576"
    },
    {

        "nama": "Neal Dolder",
        "email": "ndolderf@jiathis.com",
        "nilai": 58,
        "foto": "https://robohash.org/similiqueinvelit.png?size=100x100&set=set1",
        "alamat": "02 Hanover Trail",
        "no_hp": "(814) 2359504"
    },
    {

        "nama": "Kiah Howieson",
        "email": "khowiesong@cbsnews.com",
        "nilai": 59,
        "foto": "https://robohash.org/beataequiafugit.png?size=100x100&set=set1",
        "alamat": "766 La Follette Park",
        "no_hp": "(467) 2937627"
    },
    {

        "nama": "Anne Emburey",
        "email": "aembureyh@dyndns.org",
        "nilai": 44,
        "foto": "https://robohash.org/quiquosipsam.png?size=100x100&set=set1",
        "alamat": "9 Ruskin Drive",
        "no_hp": "(417) 2649418"
    },
    {

        "nama": "Sheilah Spellecy",
        "email": "sspellecyi@ameblo.jp",
        "nilai": 89,
        "foto": "https://robohash.org/eamaioreseum.png?size=100x100&set=set1",
        "alamat": "70 Hoffman Plaza",
        "no_hp": "(940) 4826487"
    },
    {

        "nama": "Jacklin Yoskowitz",
        "email": "jyoskowitzj@wikia.com",
        "nilai": 61,
        "foto": "https://robohash.org/exercitationemquodfuga.png?size=100x100&set=set1",
        "alamat": "344 Cottonwood Trail",
        "no_hp": "(891) 4257330"
    }
    ]
    for isi in data:
        db.collection('users').document().set(isi)
        siswa =[]
        docs = db.collection('users').stream()
        for doc in docs:
            data = doc.to_dict()
            data["id"]=doc.id
            siswa.append(data)
    return render_template('index.html', mhs=siswa)

@app.route('/logout')
def logout():
    if 'login' in session:
        session.pop('login') #untuk hapus session tertentu
        #session.clear() untuk hapus semua session
        return redirect('/login')

@app.route('/add', methods=["POST"]) 
def add():
    nama = request.form.get("nama")
    nilai = request.form.get("nilai")
    email = request.form.get("email")
    alamat = request.form.get("alamat")
    no_hp = request.form.get("no_hp")
    users = {
        'alamat' : alamat,
        'email' : email,
        'nama' : nama,
        'nilai' : int(nilai),
        'foto' : 'https://img1.pngdownload.id/20200612/veb/transparent-sound-icon-5ee3bb118dea19.2283328915919828655813.jpg',
        'no_hp' : no_hp
    }
    db.collection('users').document().set(users)
    siswa =[]
    docs = db.collection('users').stream()
    # docs = db.collection('users').where('nilai', '>', 44).stream()
    for doc in docs:
        data = doc.to_dict()
        data["id"]=doc.id
        siswa.append(data)
    return redirect('/')

@app.route('/update/<uid>')
def update(uid):
    user = db.collection('users').document(uid).get()
    users = user.to_dict()
    users['id']=user.id
    return redirect('/')

@app.route('/updatedata/<uid>', methods=["POST"])
def updatedata(uid):
    nama = request.form.get("nama")
    nilai = request.form.get("nilai")
    email = request.form.get("email")
    alamat = request.form.get("alamat")
    no_hp = request.form.get("no_hp")
    db.collection('users').document(uid).update({
        'alamat' : alamat,
        'email' : email,
        'nama' : nama,
        'nilai' : int(nilai),
        'no_hp' : no_hp
    })
    siswa =[]
    docs = db.collection('users').stream()
    # docs = db.collection('users').where('nilai', '>', 44).stream()
    for doc in docs:
        data = doc.to_dict()
        data["id"]=doc.id
        siswa.append(data)
    return redirect('/')

@app.route('/delete/<uid>', methods=["GET"])
def delete(uid):

    db.collection('users').document(uid).delete()
    siswa =[]
    docs = db.collection('users').stream()
    # docs = db.collection('users').where('nilai', '>', 44).stream()
    for doc in docs:
        data = doc.to_dict()
        data["id"]=doc.id
        siswa.append(data)
    return redirect('/')

@app.route('/deleteall')
def delall():
    siswa =[]
    docs = db.collection('users').stream()
    # docs = db.collection('users').where('nilai', '>', 44).stream()
    for doc in docs:
        data = doc.to_dict()
        data["id"]=doc.id
        test = doc.id
        db.collection('users').document(test).delete()
        siswa.append(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)