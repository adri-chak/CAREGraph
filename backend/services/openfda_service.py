import requests


BASE_URL = "https://api.fda.gov/drug/label.json"


def search_drug(drug_name):

    try:

        response = requests.get(

            BASE_URL,

            params={

                "search": f"openfda.generic_name:{drug_name}",

                "limit": 1

            }

        )

        data = response.json()

        return data

    except Exception as e:

        return {

            "error": str(e)

        }