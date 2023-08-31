from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello World"};


# TODO: make a new file for the event endpoints

@app.get("/events/")
async def get_events():
    """
    List of events that should have pagination stuff
    """

    # TODO: SQL HERE 
    return {"message": "Hello World"}   

@app.get("/events/{event_id}")
async def get_event(event_id: str):
    """
    Get a single event
    """
    return {"message": f"got event {event_id}"}   
