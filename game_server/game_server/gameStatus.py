import json

class GameStatus:

    def __init__(self, method, userID, gameID, ballposition, ballvelocity, positionpad1, positionpad2):
        self.method = method
        self.userID = userID
        self.gameID = gameID
        self.ballposition = ballposition
        self.ballvelocity = ballvelocity
        self.positionpad1 = positionpad1
        self.positionpad2 = positionpad2

    def to_dict(self):
        return {
            "method": self.method,
            "userID": self.userID,
            "gameID": self.gameID,
            "ballposition": self.ballposition,
            "ballvelocity": self.ballvelocity,
            "positionpad1": self.positionpad1,
            "positionpad2": self.positionpad2
        }

    def begin_status():
        return GameStatus(method="initialized", userID=0, gameID=0, ballposition={'x': 0, 'z': 0}, ballvelocity={'x': 0, 'z': -2}, positionpad1={'x': 0}, positionpad2={'x': 0})

# def parse_game_input_message(message):
#     try:
#         data = json.loads(message)
#         body_data = json.loads(data['body'])

#         return GameStatus(
#             method=data.get('method'),
#             userID=data.get('userID'),
#             gameID=data.get('GameID'),
#             ballposition=body_data.get('ballposition'),
#             ballvelocity=body_data.get('ballvelocity'),
#             positionpad1=body_data.get('positionpad1'),
#             positionpad2=body_data.get('positionpad2')
#         )
#     except json.JSONDecodeError:
#         print("Error al decodificar el mensaje JSON")
#         return None

def parse_game_input_message(message):
    try:
        data = json.loads(message)
        # Verifica si el JSON proviene del navegador o del servidor
        if 'body' in data:
            body_data = json.loads(data['body'])
            return GameStatus(
                method=data.get('method'),
                userID=data.get('userID'),
                gameID=data.get('GameID'),
                ballposition=body_data.get('ballposition'),
                ballvelocity=body_data.get('ballvelocity'),
                positionpad1=body_data.get('positionpad1'),
                positionpad2=body_data.get('positionpad2')
            )
        else:
            return GameStatus(
                method=data.get('method'),
                userID=data.get('userID'),
                gameID=data.get('GameID'),
                ballposition=data.get('ballposition'),
                ballvelocity=data.get('ballvelocity'),
                positionpad1=data.get('positionpad1'),
                positionpad2=data.get('positionpad2')
            )
    except json.JSONDecodeError:
        print("Error al decodificar el mensaje JSON")
        return None


def print_game_status(game_status):
    if game_status:
        print("Method:", game_status.method)
        print("User ID:", game_status.userID)
        print("Game ID:", game_status.gameID)
        print("Ball Position:", game_status.ballposition)
        print("Ball Velocity:", game_status.ballvelocity)
        print("Position of Pad 1:", game_status.positionpad1)
        print("Position of Pad 2:", game_status.positionpad2)
    else:
        print("No GameStatus object provided.")