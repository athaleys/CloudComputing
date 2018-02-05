MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'student_db'
RESOURCE_METHODS = ['GET', 'POST']

DOMAIN = {
    'student': {
        'schema' : {
            'firstname' : {
                'type':'string'
            },
            'lastname' : {
                'type':'string'
            },
            'school' : {
                'type':'string'
            },
            'university' : {
                'type':'string'
            },
            'email' : {
                'type':'string',
                'unique': True
            },
        }
    }
}

