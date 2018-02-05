from eve import Eve
app = Eve()

@app.route('/student/john')
def theStudentJohn():
    return "My name is John"

if __name__ == '__main__':
    app.run()
