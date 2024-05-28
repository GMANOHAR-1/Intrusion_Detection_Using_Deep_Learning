from flask import Flask, request, jsonify, render_template
import torch
import torch.nn as nn

app = Flask(__name__)

# Define the neural network architecture
class IntrusionDetectionModel(nn.Module):
    def __init__(self, input_size):
        super(IntrusionDetectionModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.sigmoid(self.fc3(x))
        return x

# Load the model
model_path = "model_2.pth"
model = IntrusionDetectionModel(input_size=28)
model.load_state_dict(torch.load(model_path))
model.eval()

@app.route('/')
def home():
    return render_template('index_ids1.html')

@app.route('/predict', methods=['POST'])
def predict(): 
    try:
        json_data = request.json
        print(json_data)
        input_data = [float(value) for value in json_data.values()]
        input_tensor = torch.tensor(input_data, dtype=torch.float32).view(1, -1)
        print(input_tensor)
        with torch.no_grad():
            prediction = model(input_tensor)
            predicted_class = torch.round(prediction).item()
            print("predicted : ")
            print(predicted_class)
        return jsonify({"prediction": predicted_class})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
