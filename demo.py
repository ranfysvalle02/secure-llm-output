from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LLM Insecure Output Handling Example</title>
    <style>
        /* Basic Reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Courier New', Courier, monospace;
        }

        body {
            background-color: #000;
            color: #0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
            overflow: hidden;
        }

        h1, h2 {
            text-align: center;
            text-shadow: 0 0 5px #00ff00, 0 0 10px #00ff00;
        }

        form {
            background: rgba(0, 255, 0, 0.1);
            padding: 20px;
            border: 2px solid #0f0;
            border-radius: 5px;
            box-shadow: 0 0 15px rgba(0, 255, 0, 0.5);
            width:50%;
        }

        input[type="text"] {
            background-color: black;
            color: #0f0;
            border: 1px solid #0f0;
            padding: 5px;
            width: 100%;
        }

        input[type="submit"] {
            background-color: black;
            color: #0f0;
            border: 1px solid #0f0;
            padding: 5px 10px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #0f0;
            color: black;
        }

        #output {
            margin-top: 15px;
            padding: 10px;
            border: 1px dashed #0f0;
            font-family: 'Courier New', Courier, monospace;
            font-size: 1.2em;
            white-space: pre-wrap;
            text-shadow: 0 0 5px #00ff00, 0 0 10px #00ff00;
        }

        /* Glitch Effect */
        @keyframes glitch {
            0% { transform: translate(2px, 2px); }
            20% { transform: translate(-2px, -2px); }
            40% { transform: translate(2px, -2px); }
            60% { transform: translate(-2px, 2px); }
            80% { transform: translate(2px, 2px); }
            100% { transform: translate(-2px, -2px); }
        }

        h1 {
            animation: glitch 1s infinite;
        }

    </style>
</head>
<body>
    <h1>LLM Output Example</h1>
    <form method="post">
        <label for="user_input">Enter your prompt:</label><br>
        <input type="text" id="user_input" name="user_input"><br><br>
        <input type="submit" value="Submit">
    </form>
    <h2>Output:</h2>
    <div id="output">{{ output|safe }}</div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    if request.method == 'POST':
        user_input = request.form['user_input']
        
        # Insecure handling: directly embedding user input without sanitization
        output = f"You asked: {user_input}. Here is some output: {user_input}"

    return render_template_string(HTML_TEMPLATE, output=output)

if __name__ == '__main__':
    app.run(debug=True)
