@app.route('/result11', methods=['GET', 'POST'])
def result11():
    res = None
    
    if request.method == 'POST':
        start = request.form.get('start', '').strip()
        end = request.form.get('end', '').strip()

        if start and end:
            res = [start, end]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('result11.html', res=res)
