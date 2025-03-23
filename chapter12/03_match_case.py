def check_status(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not Found"
        case 104:
            return "Try Again"
        case _:
            return "Unknown Value"
        
print(check_status(204))
    