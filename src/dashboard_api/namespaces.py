from pyinfraboxutils.ibrestplus import api

project = api.namespace('api/dashboard/projects/',
                        description='Project related operations')

settings = api.namespace('api/dashboard/settings/',
                         description='Settings')

account = api.namespace('api/dashboard/account/',
                        description='Account')

github = api.namespace('api/dashboard/github/',
                       description='GitHub')

github_auth = api.namespace('github/',
                            description='GitHub Auth')
