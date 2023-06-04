def lambda_handler(event, context):
    print(event)
    
    if "contact-info" in event:
        print("Processing order...")
        return event
    else:
        print("ERROR: Contact Info not found!")
        raise Exception("ContactIntoNotFound")
