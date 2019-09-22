import requests
import requests.auth
import json

def get_token(username, password):
    headers = {
        "Content-type": "application/json"
    }
    data = {
        "username": username,
        "password": password
    }
    response = requests.post("https://thehuxley.com/api/login", headers=headers, data=json.dumps(data))
    token_json = response.json()
    return token_json["access_token"]

def getSubmission(access_token, user_id, quiz_id):
	headers = {"Authorization": "Bearer " + access_token}
	query = 'https://www.thehuxley.com/api/v1/quizzes/' + str(quiz_id) + '/users/' + str(user_id) + '/problems'
	response = requests.get(query, headers=headers)
	problems = response.json()
	for problem in problems['problems']:
		if(problem['status'] == 'ACCEPTED'):
			outp = str(problem['id']) + ': ' + problem['name'] + '\t\t| status = ';
			for score in problems['scores']:
				if(problem['id'] == score['problem_id']):
					if(score['submission_count']):
						if(score['user_score'] == score['problem_score']):
							outp += 'ACCEPTED'
						else:
							outp += 'REJECTED'
					else:
						outp += ' - '
					break
			print(outp)

def main(user_id):
	username = input('digite o seu usuario: ')
	password = input('digite a sua senha: ')
	token = get_token(username, password)
	getSubmission(token, user_id, input('digite o id do questionario: '))

main(input('digite seu id: '))