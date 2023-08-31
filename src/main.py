from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello World"};


# TODO: make a new file for the event endpoints

@app.get("/timesAtStop/{stop_id}")
async def get_train_times_at_stop(stop_id: str):
    """
    List of events that should have pagination stuff
    """

    # TODO: SQL HERE 
    return {"message": f"getting stops at {stop_id}"}   
