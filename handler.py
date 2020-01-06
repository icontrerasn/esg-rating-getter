import json
import helpers

def get_esg_rating(event, context):
    result = []
    if event['companies']:
        for company in event['companies']:
            result.append(helpers.get_company_rating(company))
    response = {
        "statusCode": 200,
        "companies_data": result
  	}
    return response
