# djangoforms

Django Dyanamic Form

Api docs for Dynamic form for fetching forms and adding answers to database


Api Docs
forms are used in this projects as customform model

Important Api links
http://127.0.0.1:8000/form/form/<customform_id>/   #fetch custom form
http://127.0.0.1:8000/form/api-token-auth/                  # Get Auth Token
http://127.0.0.1:8000/form/qanswer/                   # Send or create Answer

Form fetch api is- 
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS

Api = http://127.0.0.1:8000/form/form/<customform_id>/
can use for eg- 
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
http://127.0.0.1:8000/form/form/5/              # where 5 is customform.pk

OUTPUT: (json format) is below --
********************************
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 5,
    "form_title": "form 5",
    "questions": [
        {
            "id": 10,
            "question_text": "what is your name",
            "ftype": 1,
            "options": []
        },
        {
            "id": 11,
            "question_text": "which branch you are?",
            "ftype": 4,
            "options": [
                {
                    "option_text": "mech",
                    "stype": 4
                },
                {
                    "option_text": "cs",
                    "stype": 4
                },
                {
                    "option_text": "it",
                    "stype": 4
                }
            ]
        },
        {
            "id": 12,
            "question_text": "which date",
            "ftype": 7,
            "options": []
        },
        {
            "id": 13,
            "question_text": "gender",
            "ftype": 6,
            "options": [
                {
                    "option_text": "male",
                    "stype": 6
                },
                {
                    "option_text": "female",
                    "stype": 6
                }
            ]
        }
    ]
}
**********************************


Answer Send api-
first we need to get authentication Token 

Get Auth Token link = http://127.0.0.1:8000/form/api-token-auth/
In HTTP Body request use following  -
key = username & value = admin 
password = pass1234

On successful authentication token is obtained
use HTTP header - key = Authorization and value = Token <token recieved>

Answer sent Api -  (Create asnswers) [POST request alowed with Token]
http://127.0.0.1:8000/form/qanswer/

request in json format will save answer to question = 
{
    "question": 1,                                        # Answer linked to this question
    "question_answer": "answer_text",        # Answer text
    "timestamp": <timestamp>,
    "userid": 1                                             # admin User object has pk is 1
}

for example place json request like -

Input = {
        "question": 1,
        "question_answer": "boss 10",
        "timestamp": "2016-06-13T20:32:00Z",
        "userid": 2
    }

Output - HTTP 201 Created status will be shown
