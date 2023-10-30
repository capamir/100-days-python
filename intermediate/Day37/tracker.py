
class Pixela:
    pixela_endpoint = "https://pixe.la/v1/users"

    def __init__(self):
        self.username = ''
        self.token = ""
        self.graphs = []

    def create_user(self):
        user_params = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }

    def create_habit(self):
        pass

    def create_pixel(self, id):
        GRAPH_ID = id
        pixel_creation_endpoint = f"{self.pixela_endpoint}/{self.username}/graphs/{GRAPH_ID}"

    @property
    def headers(self):
        return {
            "X-USER-TOKEN": self.token
        }

