from flask import Flask, Response
import json
import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='666stealthispassWord',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/kenttä/<icao>')

def findMe(icao):
    try:
        icao = str.upper(icao)
        mycursor = connection.cursor()
        mycursor.execute('SELECT NAME, municipality FROM airport WHERE IDENT = "'+ icao +'";')
        find = mycursor.fetchone()
        tilakoodi = 200
        if find != None:
            airport = icao
            nimi = find[0]
            municipality = find[1]
            vastaus = {
                "ICAO": airport,
                "Name": nimi,
                "Municipality": municipality,
            }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Something went very wrong"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "PAGE NOT FOUND, YOU DONE DID IT NOW SON"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)