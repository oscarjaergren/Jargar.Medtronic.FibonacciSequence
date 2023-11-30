from flask import Flask, session
from src.generate_fibonacci import FibonacciGenerator

app = Flask(__name__)
app.secret_key = 'fibonacci'

fibonacci_gen = FibonacciGenerator()


@app.route('/')
def fibonacci():
    # Retrieve the current N value from the session or set a default value
    n_value = session.get('n_value', 0)

    # Calculate the Fibonacci value for the current N
    fib_value_return = fibonacci_gen.generate_fibonacci(n_value)

    # Increment the N value for the next request
    n_value += 1

    # Update the N value in the session
    session['n_value'] = n_value

    return str(fib_value_return)


if __name__ == '__main__':
    app.run(port=8080)
