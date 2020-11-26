import blueprint.resources.utils.api as Api

class Blueprint:

    @staticmethod
    def run():

        # how to use - example
        api = Api.ApiRequest()
        data = api.get(Api.Endpoints.IT)
        
        print("Hello World...")
