import io
import json
from fdk import response
import requests
import logging

#When OCI Functions invokes your function, it passes a context object ctx to the handler.
#ctx is a context object that provides information about the function and request-specific attributes
#FDK provides data as io.BytesIO type
#data is an object passed by the trigger request containing the payload – the HTTP request body, when calling the function using HTTP

def handler(ctx, data: io.BytesIO=None):
    logging.getLogger().info("jhan function was invoked!!!")
    logging.getLogger().info(ctx.FnID())
    logging.getLogger().info(ctx.AppID())
    logging.getLogger().info(dict(ctx.Config()))
    logging.getLogger().info("Incoming request for URL %s with headers %s", ctx.RequestURL(), ctx.HTTPHeaders())

    url = "https://guk9elytviiyjhz-devadw.adb.uk-london-1.oraclecloudapps.com/ords/covid/demo/test/"

    #resp = get_data(url)
    resp = delete_data(url)

    #return response.Response(ctx, response_data=json.dumps(resp.json()), headers={"Content-Type": "application/json"})
    return response.Response(ctx, response_data=resp, headers={"Content-Type": "application/json"})

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


