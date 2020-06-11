import io
import json
from fdk import response
import requests
import logging

#When OCI Functions invokes your function, it passes a context object ctx to the handler.
#ctx is a context object that provides information about the function and request-specific attributes
#FDK provides data as io.BytesIO type
#data is an object passed by the trigger request containing the payload – the HTTP request body, when calling the function using HTTP
#Using the FDK you don't have to worry about reading input from standard input and writing to standard output to return your response.
#The FDK let's you focus on your function logic and not the mechanics.

def handler(ctx, data: io.BytesIO=None):
    try:
        #no user input
        if len(data.getvalue()) == 0:
            input_data = "No user input data"
        else:
            #log user input
            logging.getLogger().info("Read data : %s",data.getvalue())
            body = json.loads(data.getvalue())
            input_data = body.get("input")

        url = "Your REST API Endpoint"
        # resp = get_data(url)
        resp = delete_data(url)

    except (Exception, ValueError) as ex:
        print(str(ex))

    return response.Response(ctx, response_data=json.dumps(
            {"Input data": input_data,
            "ctx.AppID" : ctx.AppID(),
            "ctx.FnID" : ctx.FnID(),
            "ctx.CallID" : ctx.CallID(),
            "ctx.Config" : dict(ctx.Config()),
            "response code": resp.status_code}), headers={"Content-Type": "application/json"})


#GET data in Covid.test
def get_data(url):
    resp = requests.get(url)
    print("status code: {}".format(resp.status_code))
    return resp

#Delete data in Covid.test
def delete_data(url):
    resp = requests.delete(url)
    print("status code: {}".format(resp.status_code))
    return resp
