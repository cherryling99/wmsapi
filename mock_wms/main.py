from fastapi import APIRouter

app = APIRouter()

@app.post("/E2W_Pcom/")
async def e2w_pcom(message: dict):
    result = {
            "Message": {
                "Header": {
                    "UUID": "UUID",
                    "EventID": "E2W_Pcom",
                    "Direction": "Secondary",
                    "SystemID": "WMS"
                },
                "Body": {
                    "ResultInfo": {
                        "Result": "Result",
                        "ResultMessage": "ResultMessage"
                        }
                    }
                }
            }

    return result


@app.post("/E2W_Barcode/")
async def e2w_barcode(message: dict):
    result = {
        "Message": {
            "Header": {
                "UUID": "UUID",
                "EventID": "E2W_Barcode",
                "Direction": "Secondary",
                "SystemID": "WMS"
            },
            "Body": {
                "ResultInfo": {
                    "Result": "Result",
                    "ResultMessage": "ResultMessage"
                }
            }
        }
    }

    return result

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
