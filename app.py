from flask import Flask, render_template, request,jsonify
from LSBSteg import*
import os
import subprocess
from flask import send_file


app = Flask(__name__)

@app.route('/')
def index1():
    result = subprocess.check_output(['python', 'random1.py'])
    return render_template('index1.html')

@app.route('/download_txt', methods=['GET'])
def download_txt_file():
    file_path="C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/textfile/new_textfile.txt"
    # file_path = "C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/download.py"
    return send_file(file_path, as_attachment=True)
@app.route('/download_img', methods=['GET'])
def download_img_file():
    file_path="C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/new_image.png"
    # file_path = "C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/download.py"
    return send_file(file_path, as_attachment=True)

# @app.route('/output')
# def index():
#     result = subprocess.check_output(['python', 'ia2.py'])
#     return render_template('index1.html')

@app.route('/input', methods=['GET', 'POST'])
def index():
    content = request.form.get('content')
    file_path = 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/textfile/new_textfile.txt'  # Specify the file path where you want to save the file

    with open(file_path, 'w') as file:
        file.write(content)
    result=subprocess.check_output(['python', 'hide.py'])
    return render_template('index1.html')

# @app.route('/input')
# def index():
#     # content = request.form.get('content')
#     # file_path = 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/textfile/new_textfile.txt'  # Specify the file path where you want to save the file

#     # with open(file_path, 'w') as file:
#     #     file.write(content)
#     result=subprocess.check_output(['python', 'hide.py'])
#     return render_template('index1.html')

@app.route('/out')
def out():
    try:
        result = subprocess.check_output(['python', 'out.py'], stderr=subprocess.STDOUT)
        result = result.decode('utf-8')
        error = None
    except subprocess.CalledProcessError as e:
        result = "'nothing encrypeted in this image'"
        error = "Error occurred: " + str(e)
    return render_template('index1.html',result=result)





    # # from LSBSteg import*
    # #encoding
    # steg = LSBSteg(cv2.imread("Default.png"))
    # img_encoded = steg.encode_text("my message to ayush")
    # cv2.imwrite("C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/new_image.png", img_encoded)

    # #decoding
    # im = cv2.imread("C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/new_image.png")
    # steg = LSBSteg(im)
    # print("Text value:",steg.decode_text())
    # result =p
    # file_path = 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/textfile/new_textfile.txt'  # Specify the file path where you want to save the file
    # result =result.decode('utf-8')
    # # with open(file_path, 'w', encoding="utf-8") as file:
    # #     file.write(content)
    # # with open(fname, "w", encoding="utf-8") as f:
    # # f.write(html)
    # return render_template('index1.html',result=result)



# @app.route('/')
# def index():
#     # result = subprocess.check_output(['python', 'abcd.py'])
#     result="amit"
#     return render_template('file_upload.html',result=result)


# @app.route('/')
# def index():
#     result = subprocess.check_output(['python', 'abcd.py'])
#     return render_template('file_upload.html',result=result)
    # websites = ['http://www.example1.com', 'http://www.example2.com', 'http://www.example3.com']
    # return jsonify(websites[0])

# @app.route('/')
# def run_a():
#     result = subprocess.check_output(['python', 'abcd.py'])
#     result =result.decode('utf-8')
#     # result =jsonify(result)
#     # return jsonify(result)
#     return result
#     # return render_template('index.html', result=result)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    uploaded_file = request.files['myfile']
    # print(uploaded_file)
    # filename = uploaded_file.filename
    new_filename = 'new_image.png' 
    filepath = os.path.join('static', 'images', new_filename)
    # uploaded_file.save(new_filename)
    uploaded_file.save(filepath)


    # new_filename_1 = 'new_image_1.png' 
    # filepath_1 = os.path.join('static', 'images', new_filename_1)
    # # uploaded_file.save(new_filename)
    # uploaded_file.save(filepath_1)
    return render_template("index1.html")
    # return f'text hide to pic  {filename}'
    # return f'Image saved to {filepath}!'


# @app.route('/upload_textfile', methods=['POST'])
# def upload_textfile():
#     uploaded_file = request.files['mytextfile']
#     filename = uploaded_file.filename
#     new_filename = 'new_textfile.txt' 
#     filepath = os.path.join('static', 'textfile', new_filename)
#     # uploaded_file.save(new_filename)
#     uploaded_file.save(filepath)
#     f = open("static/textfile/new_textfile.txt", "r")
#     # print(f.read(5))
#     return f'text hide to pic  {f.read()}'





# @app.route('/write_file', methods=['POST'])
# def write_file():
#     content = request.form['content']
#     file_path = 'new_textfile.txt'
#     with open("static/textfile/new_textfile.txt", 'w') as file:
#         file.write(content)


@app.route('/save_to_file', methods=['POST'])
def save_to_file():
    content = request.form.get('content')
    file_path = 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/textfile/new_textfile.txt'  # Specify the file path where you want to save the file

    with open(file_path, 'w') as file:
        file.write(content)
    k="text is already saved"
    # result =result.decode('utf-8')
    return render_template('index1.html',k=k)



if __name__ == '__main__':
    app.run(debug=True)
