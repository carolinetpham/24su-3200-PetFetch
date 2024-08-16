########################################################
# Sample agency blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

agencies = Blueprint('agencies', __name__)

# Get all agencies from the DB
@agencies.route('/agencies', methods=['GET'])
def get_agencies():
    current_app.logger.info('agencies_routes.py: GET /agencies')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT agencyID, agencyName, phone, email, street,\
        city, state, zip FROM agencies')

    theData = cursor.fetchall()

    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get total number of adoptions per agency
@agencies.route('/petagencies', methods=['GET'])
def pet_agencies():
    current_app.logger.info('agencies_routes.py: GET /petagencies')

    cursor = db.get_db().cursor()
    theQuery = '''
      SELECT ag.agencyName, COUNT(ad.adoptionID) AS totalAdoptions
      FROM agencies ag
        LEFT JOIN pet_agencies pa on ag.agencyID = pa.agencyID
        LEFT JOIN adoptions ad on pa.petID = ad.petID
      GROUP BY ag.agencyID
      ORDER BY totalAdoptions
    '''
    cursor.execute(theQuery)
    theData = cursor.fetchall()

    theResponse = make_response(theData)
    theResponse.status_code = 200
    theResponse.mimetype = 'application/json'

    return theResponse

# Get the number of most surrendered pets for each breed
@agencies.route('/mostsurrendered', methods=['GET'])
def most_surrendered():
    current_app.logger.info('agencies_routes.py: GET /mostsurrendered')

    cursor = db.get_db().cursor()
    theQuery = '''
     SELECT p.species, p.breed, COUNT(p.petID) AS amount_surrendered
     FROM pets p
         JOIN pet_agencies pa ON p.petID = pa.petID
     GROUP BY p.species, p.breed
     ORDER BY amount_surrendered DESC 
    '''
    cursor.execute(theQuery)
    theData = cursor.fetchall()

    theResponse = make_response(theData)
    theResponse.status_code = 200
    theResponse.mimetype = 'application/json'

    return theResponse

# Get pet detail for a agency with particular petID
@agencies.route('/agencies/<zip>', methods=['GET'])
def get_agency(zip):
    current_app.logger.info('GET /agencies/<zip> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT agencyID, agencyName, phone, email, street,\
        city, state, zip FROM agencies WHERE zip = ' + str(zip))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response