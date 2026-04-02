from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Go to /factorial?number=5 to calculate factorial"

@app.route('/factorial')
def factorial():
    try:
        num = int(request.args.get('number', 0))
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return f"Factorial of {num} is {fact}"
    except:
        return "Please provide a valid number like /factorial?number=5"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)