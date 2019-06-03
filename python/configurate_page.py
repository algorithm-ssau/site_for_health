from yattag import Doc


doc = Doc()
tag = doc.tag
html = doc.tag
head = doc.tag
meta = doc.tag
link = doc.tag
title = doc.tag
script = doc.tag
body = doc.tag
div = doc.tag
a = doc.tag
img = doc.tag
td = doc.tag
br = doc.tag
p = doc.tag
text = doc.text

doc.asis('<DOCTYPE html>')
with tag('html'):
    with tag('head'):
        with tag('meta', charset='UTF-8'):
            with tag('link', href='../../styles/style.css', rel='stylesheet',
                     type='text/css'):
                with tag('title'):
                    text('День 1')
            doc.stag('script', src='../../scripts/script.js')
    with tag('body'):
        with tag('div', klass='top_menu'):
            with tag('div', klass='logo'):
                with tag('a', href='#'):
                    doc.stag('img', src='../../images/logo.png')
            with tag('div', klass='navigation_bar'):
                with tag('div', klass='nav'):
                    with tag('a', href='../all_exercises.html'):
                        text('Упражнения')
                with tag('div', klass='nav'):
                    with tag('a', href='../all_fitness_centers.html'):
                        text('Фитнес-центры')
                with tag('div', klass='nav'):
                    with tag('a', href='../all_treners.html.html'):
                        text('Тренеры')
            with tag('div', klass='share_bar'):
                with tag('div', klass='share'):
                    with tag('a', href='#'):
                        doc.stag('img', src='../../images/vk.png')
                with tag('div', klass='share'):
                    with tag('a', href='#'):
                        doc.stag('img', src='../../images/vk.png')
        with tag('div', klass='central_block'):
            with tag('div', klass='central_block__book'):
                doc.stag('img', src='../images/book.png')
                with tag('div', klass='central_block_exercise'):
                    with tag('br'):
                        with tag('td'):
                            text('Хорошилов Анастас')
                    with tag('br'):
                        with tag('td'):
                            text('Очень хороший тренер')
                    with tag('br'):
                        with tag('td'):
                            text('ЗОЖ - это не всё')
                with tag('div', klass='central_block_exercise'):
                    with tag('br'):
                        with tag('td'):
                            text('Хорошилов Анастас')
                    with tag('br'):
                        with tag('td'):
                            text('Очень хороший тренер')
                    with tag('br'):
                        with tag('td'):
                            text('ЗОЖ - это не всё')
        with tag('div', klass='past_lesson'):
            with tag('a', href='katya.html'):
                text('Предыдущий')
        with tag('div', klass='next_lesson'):
            with tag('a', href='max.html'):
                text('Следующий')
        with tag('div', klass='footer'):
            with tag('p'):
                with tag('a', href='#'):
                    doc.text('Политика конфиденциальности')
                with tag('a', href='#'):
                    doc.text('Связаться с нами')
                with tag('br'):
                    doc.text('All rights reserved')

with open('page_skelet.html', 'w') as f:
    f.write(doc.getvalue())

print(doc.getvalue())





