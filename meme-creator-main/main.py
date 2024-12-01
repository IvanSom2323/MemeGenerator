#Импорт
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

#Результаты формы
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # получаем выбранное изображение
        selected_image = request.form.get('image-selector')

        # Задание №2.Получаем текст
        selected_topText = request.form.get('textTop')
        selected_bottomText = request.form.get('textBottom')
        
        # Задание №3. Получаем расположение текста
        selected_topY = request.form.get('textTop_y')
        selected_bottomY = request.form.get('textBottom_y')

        # Задание №3. Получаем цвет текста
        selected_color = request.form.get('color-selector')

        return render_template('index.html', 
                               selected_image=selected_image, 
                               selected_topText=selected_topText,
                               selected_bottomText=selected_bottomText,
                               selected_color=selected_color,
                               selected_topY=selected_topY,
                               selected_bottomY=selected_bottomY
                               )
    else:
        # отображаем первое изображение по умолчанию
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)