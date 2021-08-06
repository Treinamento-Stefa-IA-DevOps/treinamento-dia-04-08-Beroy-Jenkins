import pickle
from fastapi import FastAPI, Query


app = FastAPI()
@app.post('/model')
## Coloque seu codigo na função abaixo

#definindo os parametros e os limites
def titanic(Lifeboat:int, Sex:int= Query(..., ge=0, le=1), Age:float= Query(..., ge=1),  Pclass:int= Query(..., ge=1, le=3)):
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)
        #titanic recebe 'DecisionTreeClassifier(random_state=1)'

#tenta retornar respostas
    try:
        return {
            'survived': bool(titanic.predict([[Sex,Age,Lifeboat,Pclass]])),
            'status': 200,
            'message': 'OK',
        }
    except Exception:
        return {
            'status': 500,
            'message': "Internal Server Error"
        }


@app.get('/model')
def get():
    return {'hello':'test'}
    