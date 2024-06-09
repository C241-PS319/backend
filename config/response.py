from rest_framework.response import Response

def SuccessResponse(message, data, http_status=200):
    return Response({
        'status': 'success', 
        'message': message, 
        'data': data
    }, status=http_status)

def FailedResponse(message, data, http_status=400):
    return Response({
        'status': 'failed', 
        'message': message, 
        'data': data
    }, status=http_status)