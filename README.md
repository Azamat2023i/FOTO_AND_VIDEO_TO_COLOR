<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Преобразование черно-белых фотографий в цветные</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        h1 {
            text-align: center;
        }
        .example {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }
        .example img {
            width: 350px;
            margin: 0 10px;
        }
        .requirements {
            background-color: #eaeaea;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<h1>Преобразование черно-белых фотографий в цветные</h1>

<h2>Установка зависимостей</h2>
<p class="requirements">Для установки необходимых библиотек выполните команду:</p>
<pre class="requirements"><code>pip install -r requirements.txt</code></pre>

<h2>Скрипты для преобразования изображений</h2>
<ul>
    <li><strong>Преобразование одного изображения:</strong> <code>one_file.py</code></li>
    <li><strong>Преобразование всех изображений в папке:</strong> <code>list_of_files.py</code></li>
</ul>

<h2>Примеры преобразования</h2>

<div class="example">
    <div>
        <strong>Пример 1</strong><br>
        <img src="test_input/1.jpg" alt="input1">
        <img src="test_output/1.jpg" alt="output1">
    </div>
    <div>
        <strong>Пример 2</strong><br>
        <img src="test_input/2.jpg" alt="input2">
        <img src="test_output/2.jpg" alt="output2">
    </div>
    <div>
        <strong>Пример 3</strong><br>
        <img src="test_input/3.jpg" alt="input3">
        <img src="test_output/3.jpg" alt="output3">
    </div>
</div>

<h2>Источник обученной модели</h2>
<p>Обученная модель нейросети была взята с сайта <a href="https://www.geeksforgeeks.org/black-and-white-image-colorization-with-opencv-and-deep-learning/" target="_blank">GeeksforGeeks</a>.</p>
</body>
</html>

