from flask import Flask
from flask import render_template,request,redirect
app=Flask(__name__)

item_list=["medicine","tablet"]
@app.route('/todo' ,methods=['GET','POST'])
def todo():
    if request.method=="POST":
        item_list.append(request.form["get_from_user"])
        a=request.form["get_from_user"]
    return render_template("todo.html",items=item_list,a=a)

@app.route('/delete/<item_name>')
def delete(item_name):
    if item_name in item_list:
        item_list.remove(item_name)
    return render_template("todo.html",items=item_list)


@app.route("/updated/<index>",methods=['GET','POST'])
def updated(index):
    if request.method=="POST":
        item_list[int(index)]=request.form["updated_item"]
        return render_template("todo.html",items=item_list)
    else:
        return render_template("update.html",element=item_list[int(index)])


if __name__=='__main__':
    app.run(debug=True)