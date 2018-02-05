from eve import Eve

app = Eve()

@app.route('/processor', methods = ['GET'])
def processor():
    with open('/proc/cpuinfo') as f:
        for line in f:
        # Ignore the blank line separating the information between
        # details about two processing units
            if line.strip():
                if line.rstrip('\n').startswith('model name'):
                    model_name = line.rstrip('\n').split(':')[1]
                    return (model_name)

if __name__ == '__main__':
    app.run()
