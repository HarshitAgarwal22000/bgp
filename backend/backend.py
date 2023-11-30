from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
import jwt
import subprocess
DATABASE_URL="postgresql://admin:DUBAI@localhost/bgpapi"
engin=create_engine(DATABASE_URL)
print(engin)
app=FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
SECRET_KEY='DUBAI'
def get_token(id,r_id,asn):
    url="homepage.html"
    payload=({
        "id":id,
        "r_id":r_id,
        "asn":asn,
        "url":url
    })
    token=jwt.encode(payload,SECRET_KEY,algorithm='HS256')
    return token
def validate_token(token):
    tok=jwt.decode(token,algorithms='HS256')
    try:
        print(tok)
        return tok
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

@app.get('/')
async def homepag():
    print("dubai")
    return FileResponse('../frontend/login.html')
@app.get('/signup')
async def signup():
    print("dubai")
    return FileResponse('../frontend/login.html')
@app.get('/homepage')
async def homepage():
    print("sign")
    return {"message":"xy"}

@app.post('/login')
async def login(request: Request):
    data= await request.json()
    print(data)
    print("rus")
   
    usern=data
    routerid=data.get("User")
    passw=data.get("Pass")
    asnno=data.get("ASN")
    r=get_token(routerid,passw,asnno)
    
    return jsonable_encoder({"r":r})
@app.get('/file/{username}')
async def get_file(username):
    print("Get")
    command="echo 3 | sudo cat /etc/frr/frr.conf"
    o=subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(o.stdout)
    print(o.stderr)
@app.get('/interfaces/{username}')
async def get_interfaces(username):
    print("Get")
    command="sudo cat /etc/frr/frr.conf"
    o=subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    data=o.stdout
    print(data)
    
    
    ind=data.index("interface")
    stop=data.index("!")
    print(ind)
    print(stop)
    for x in range (ind,stop):
        print(x)
        print(data[x], end="")
        

            
        
@app.get('/neighbors/{username}')
async def get_neighbors(username):
    print("Get n")
@app.get('/adroutes/{username}')
async def get_adroutes(username):
    print("Get ad")
@app.get('/bgpstate/{username}')
async def get_bgpstate(username):
    print("Get bgpstate")
@app.get('/routingtable/{username}')
async def get_routingtable(username):
    print("Get")


    