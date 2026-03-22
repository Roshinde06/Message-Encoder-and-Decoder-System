from flask import Flask, render_template, request

app = Flask(__name__)

# Caesar Cipher Encode
def encode_message(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += char
    return result


# Caesar Cipher Decode
def decode_message(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += char
    return result


@app.route("/", methods=["GET","POST"])
def index():

    output = ""

    if request.method == "POST":

        message = request.form["message"].upper()
        shift = int(request.form["shift"])
        action = request.form["action"]

        if action == "encode":
            output = encode_message(message, shift)

        elif action == "decode":
            output = decode_message(message, shift)

    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(debug=True)