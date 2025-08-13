from flask import Flask, request

app = Flask(__name__)

web_sites = [
    {
        "id": 1,
        "name": "Google",
        "site": "https://www.google.com.br"
    },
    {
        "id": 2,
        "name": "GitHub",
        "site": "https://github.com/Savio-S-Morais"
    },
    {
        "id": 3,
        "name": "LinkedIn",
        "site": "https://www.linkedin.com/in/savio-santana-de-morais/"
    }
]

# GET: List informations
@app.route('/web', methods=["GET"])
def list():
    return web_sites

# GET: List all informatiom by ID
@app.route('/web/<int:id>', methods=["GET"])
def show(id):
    info_customer = web_sites[id]
    return info_customer

# GET: List specific information
@app.route('/web/<int:id>/<string:info>', methods=["GET"])
def show_specific(id, info):
    info_customer = web_sites[id][info]
    
    return info_customer

# POST: Add new item in list
@app.route('/web', methods=["POST"])
def add():
    json_infos = request.get_json()
    id = web_sites[-1]["id"] + 1
    name = json_infos["name"]
    site = json_infos["site"]
    
    new_customer = {"id":id, "name":name, "site":site}
    web_sites.append(new_customer)
    
    return web_sites

# PUT: Update item information
@app.route('/web/<int:id>', methods=["PUT"])
def update(id):
    customer_update = web_sites[id]
    new_infos = request.get_json()
    
    customer_update["name"] = new_infos["name"]
    customer_update["site"] = new_infos["site"]
    
    return customer_update

# DELETE: Delete information
@app.route('/web/<int:id>', methods=["DELETE"])
def delete(id):
    del web_sites[id]
    return web_sites

if __name__ == "__main__":
    app.run()