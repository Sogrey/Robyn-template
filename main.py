
from robyn import Robyn, ALLOW_CORS

from dbHelper.DBHelper import insert1, insert2

app = Robyn(__file__)
# ALLOW_CORS(app, origins=["http://localhost:<PORT>/"])


# get url中带参数
# example: http://127.0.0.1:8081/get/111111/hahahah
@app.get("/get/:userId/:userName")
async def path_params(request):
    userId = request.path_params.get("userId")
    userName = request.path_params.get("userName")
    print(userId, userName)
    return "Hello, world!"

# exampe: http://127.0.0.1:8081/query_params?userId=11111&userName=hahahah

# curl --location 'http://127.0.0.1:8081/query_params?userId=11111&userName=hahahah' \
# --data ''


@app.get("/query_params")
async def query_get(request):
    userId = request.query_params.get('userId')
    userName = request.query_params.get('userName')
    return {userId, userName}


# get body中带参数

# exampe: http://127.0.0.1:8081/insert_body_json
# body:{"userId":"111111","userName":"hahahah"}


@app.post("/insert_body_json")
async def query_get(request):
    query_data = request.body
    return query_data


@app.get("/get/user")
async def getUser(request):
    insert2()
    return "Sogrey!"

if __name__ == "__main__":
    app.start(host="0.0.0.0", port=8081)
