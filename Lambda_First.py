import json

def sum(a,b):
    return a+b
    
def lambda_handler(event, context):
    n=event["m"] # here u can configure the values in the event 
    m=event["n"]
    result=sum(m,n)
    print("Addition of {} and {} is {} ".format(m,n,result))
    
