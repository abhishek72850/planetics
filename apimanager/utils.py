from rest_framework import status


def BuildResponse(data):
	if(data['success']):
		response = {
			'status' : status.HTTP_200_OK,
			'data' : data['data']
		}
	else:
		response = {
			'status' : data['code'],
			'data' : data['message']
		}

	return response