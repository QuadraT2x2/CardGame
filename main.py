from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/card', methods=['GET', 'POST'])
def card():
    #print(request.form)
    #print(request.args)
    #number = request.form['number']
    if "number" in request.args.keys():
        #print(type(request.args["number"]))
        if request.args['number'] == "1":
            return render_template("index_mage.html")
        
        if request.args['number'] == "2":
            return render_template("index_warrior.html")
        
        if request.args['number'] == "3":
            return render_template("index_knight.html")
        
    return render_template("index.html")


@app.route('/choose',  methods=['GET', 'POST'])
def choose():
    return render_template("choose.html")


@app.route('/fight', methods=["GET", "POST"])
def fight():
    #print(request.form)
    #print(request.args)
    print(request.args['fighter_1'])
    print(request.args['fighter_2'])
    if 'fighter_1' and 'fighter_2' in request.args.keys() and request.args['fighter_1'] != '' and request.args['fighter_2'] != '':
        if request.args['fighter_1'] == 'mage':
            if request.args['fighter_2'] == 'mage':
                return render_template("m_vs_m.html")

            if request.args['fighter_2'] == 'warrior':
                return render_template("m_vs_w.html")

            if request.args['fighter_2'] == 'knight':
                return render_template("m_vs_k.html")


        if request.args['fighter_1'] == 'warrior':
            if request.args['fighter_2'] == 'mage':
                return render_template("w_vs_m.html")

            if request.args['fighter_2'] == 'warrior':
                return render_template("w_vs_w.html")

            if request.args['fighter_2'] == 'knight':
                return render_template("w_vs_k.html")


        if request.args['fighter_1'] == 'knight':
            if request.args['fighter_2'] == 'mage':
                return render_template("k_vs_m.html")

            if request.args['fighter_2'] == 'warrior':
                return render_template("k_vs_w.html")
                
            if request.args['fighter_2'] == 'knight':
                return render_template("k_vs_k.html")
    else:
        return render_template("fight.html")
    


@app.route('/hello')
def hello_world_2():
    return {"Hello": "World 2!"}


@app.route('/boots')
def boots_trap():
    return render_template("hello3.html")


@app.route('/learn')
def learn():
    return render_template("learn.html")
