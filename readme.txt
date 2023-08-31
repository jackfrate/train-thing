venv setup
`python3.10 -m venv venv`

install requirements
`pip install -r requirements.txt`

get the env file or your own api key and name it `.env`

run the app
`python3 -m uvicorn src.main:app --reload --env-file ./.env`