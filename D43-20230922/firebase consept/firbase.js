function register(){
    window.location="register.html"
}
function signup(){
    let newid=document.getElementById("new_user").value;
    let newmail=document.getElementById("new_email").value;
    let newpass=document.getElementById("new_password").value;
    let userdetails=[]
    if(localStorage.getItem("userdetails")){
        userdetails=JSON.parse(localStorage.getItem("userdetails"))
    }
        
    userdetails.push({email:newmail,password:newpass,name:newid})
    localStorage.setItem("userdetails",JSON.stringify(userdetails));
    alert("You have registered your account succesfully")
    window.location="login.html"
}
function checklogin(){
    if(localStorage.getItem("loggedIn")){
        let login_username=document.getElementById("username")
        login_username.innerHTML=`Welcome ${localStorage.getItem("Name")}`
    }else{
        window.location="login.html"
    }
}
function login(){
    let login_email=document.getElementById("email").value
    let login_password=document.getElementById("password").value
    userdetails=JSON.parse(localStorage.getItem("userdetails"))
    for(var i=0;i<userdetails.length;i++){
        if(login_email==userdetails[i].email && login_password==userdetails[i].password){
                localStorage.setItem("loggedIn",true)
                localStorage.setItem("Name",`${userdetails[i].name}`)
                window.location="home.html"}
}
}
function logout(){
    localStorage.removeItem("loggedIn")
    localStorage.removeItem("Name")
    window.location="login.html"
}

function list(){
    let info=document.getElementById("userlist")
    info.style.display="block"
    user_list=JSON.parse(localStorage.getItem("userdetails"))
    let htmldata=""
    for(i=0;i<user_list.length;i++){
        htmldata=htmldata+`<tr><td>${user_list[i].name}</td>
                               <td>${user_list[i].email}</td>
                               <td><button type="button" onclick="update('${i}')">edit</button></td>
                               <td><button type="button" onclick="del('${user_list[i].email}')">delete</button></td></tr>`
                               
    }
    document.getElementById("table_body").innerHTML=htmldata
}
function del(mail){
    let newdata=[]
        let rmve=JSON.parse(localStorage.getItem("userdetails"))
        for(i=0;i<rmve.length;i++){
            if(rmve[i].email!=mail){
                newdata.push(rmve[i])
            }
            }
localStorage.setItem("userdetails",JSON.stringify(newdata))
list()
        }



