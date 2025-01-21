from flask import Flask, render_template_string, url_for

app = Flask(__name__)

# Template HTML untuk Homepage
HOMEPAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome Page</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to bottom right, #ff9a9e, #fcc2cf);
            color: #fff;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        .container {
            margin-top: 150px;
        }
        h1 {
            font-size: 60px;
            color: #ffffff;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.4);
        }
        p {
            font-size: 20px;
            color: #ffffff;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            font-size: 18px;
            color: #ffffff;
            text-decoration: none;
            background-color: #ff6f61;
            border-radius: 8px;
            transition: background 0.3s;
        }
        a:hover {
            background-color: #ff3b2f;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Selamat Datang di Project Muhamad Nuno Yang Sangat Spesial!</h1>
        <p>Klik tombol di bawah deh sayang!</p>
        <a href="{{ url_for('slideshow') }}">Lihat Slideshow Foto</a>
        <br><br>
        <a href="{{ url_for('ucapan') }}">Lihat Ucapan</a>
    </div>
</body>
</html>
"""

# Template HTML untuk Halaman Slideshow Foto
SLIDESHOW_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Slideshow Foto</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to bottom right, #ff9a9e, #fad0c4);
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        .slideshow-container {
            position: relative;
            max-width: 80%;
            margin: 50px auto;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        }
        .slides {
            display: none;
        }
        .slides img {
            width: 100%;
        }
        .prev, .next {
            cursor: pointer;
            position: absolute;
            top: 50%;
            width: auto;
            margin-top: -22px;
            padding: 16px;
            color: white;
            font-weight: bold;
            font-size: 18px;
            transition: 0.6s ease;
            user-select: none;
            background-color: rgba(0,0,0,0.5);
            border-radius: 50%;
        }
        .prev {
            left: 10px;
        }
        .next {
            right: 10px;
        }
        .prev:hover, .next:hover {
            background-color: rgba(0,0,0,0.8);
        }
        .dots {
            text-align: center;
            margin: 20px 0;
        }
        .dots span {
            cursor: pointer;
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #bbb;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
        }
        .active, .dots span:hover {
            background-color: #717171;
        }
    </style>
</head>
<body>
    <div class="slideshow-container">
        <div class="slides">
            <img src="{{ url_for('static', filename='foto1.jpg') }}" alt="Foto 1">
        </div>
        <div class="slides">
            <img src="{{ url_for('static', filename='foto2.jpg') }}" alt="Foto 2">
        </div>
        <div class="slides">
            <img src="{{ url_for('static', filename='foto3.jpg') }}" alt="Foto 3">
        </div>
        <div class="slides">
            <img src="{{ url_for('static', filename='foto4.jpg') }}" alt="Foto 4">
        </div>
        <div class="slides">
            <img src="{{ url_for('static', filename='foto5.jpg') }}" alt="Foto 5">
        </div>
        <div class="slides">
            <img src="{{ url_for('static', filename='foto6.jpg') }}" alt="Foto 6">
        </div>
        <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
        <a class="next" onclick="plusSlides(1)">&#10095;</a>
    </div>
    <div class="dots">
        <span class="dot" onclick="currentSlide(1)"></span>
        <span class="dot" onclick="currentSlide(2)"></span>
        <span class="dot" onclick="currentSlide(3)"></span>
        <span class="dot" onclick="currentSlide(4)"></span>
        <span class="dot" onclick="currentSlide(5)"></span>
        <span class="dot" onclick="currentSlide(6)"></span>
    </div>
    <script>
        let slideIndex = 1;
        showSlides(slideIndex);

        function plusSlides(n) {
            showSlides(slideIndex += n);
        }

        function currentSlide(n) {
            showSlides(slideIndex = n);
        }

        function showSlides(n) {
            let i;
            let slides = document.getElementsByClassName("slides");
            let dots = document.getElementsByClassName("dot");
            if (n > slides.length) { slideIndex = 1 }
            if (n < 1) { slideIndex = slides.length }
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }
            for (i = 0; i < dots.length; i++) {
                dots[i].className = dots[i].className.replace(" active", "");
            }
            slides[slideIndex - 1].style.display = "block";
            dots[slideIndex - 1].className += " active";
        }

        setInterval(() => {
            plusSlides(1);
        }, 5000); // Ganti slide setiap 5 detik
    </script>
    <a href="{{ url_for('homepage') }}" style="text-decoration: none; color: white; background: #4CAF50; padding: 10px 20px; border-radius: 10px; display: inline-block; margin: 20px auto;">Kembali ke Homepage</a>
</body>
</html>
"""

@app.route('/')
def homepage():
    return render_template_string(HOMEPAGE_TEMPLATE)

@app.route('/slideshow')
def slideshow():
    return render_template_string(SLIDESHOW_TEMPLATE)

# Template untuk Halaman Ucapan
UCAPAN_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Halaman Ucapan</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to bottom right, #ff9a9e, #fcc2cf);
            color: #fff;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        .container {
            margin-top: 150px;
        }
        h1 {
            font-size: 50px;
            color: #ffffff;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.4);
        }
        p {
            font-size: 20px;
            color: #ffffff;
        }
        a {
            display: inline-block;
            margin-top: 25px;
            padding: 25px 22px;
            font-size: 22px;
            color: #ffffff;
            text-decoration: none;
            background-color: #ff6f61;
            border-radius: 8px;
            transition: background 0.3s;
        }
        a:hover {
            background-color: #ff3b2f;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="heart">❤</div>
        <h1>Selamat Anniversary Yang ke-6 Tahun Anindya Nur Shadrina Hidayat!</h1>
        <h2>Untuk orang yang sangat spesial dan orang yang sangat aku sayang!</h2>
        <p>Terima kasih telah menjadi bagian terindah dalam hidupku.</p>
        <p>Semoga cintaa kita bisa terus tumbuh dan bahagia selalu lagi yaa cintaakuuu!</p>  
        <a href="{{ url_for('homepage') }}">Kembali ke Homepage</a>
    </div>
</body>
</html>
"""

@app.route('/ucapan')
def ucapan():
    return render_template_string(UCAPAN_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True)
