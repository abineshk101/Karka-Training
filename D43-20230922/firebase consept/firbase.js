const firebaseConfig = {
    apiKey: "AIzaSyAcEw1L4iaWASd1V-dNPo2Co3nYE3yVIwg",
    authDomain: "loginpage-70950.firebaseapp.com",
    databaseURL: "https://loginpage-70950-default-rtdb.firebaseio.com",
    projectId: "loginpage-70950",
    storageBucket: "loginpage-70950.appspot.com",
    messagingSenderId: "191503712726",
    appId: "1:191503712726:web:79bb7f69e3e5c6b4486477"
  };

  firebase.initializeApp(firebaseConfig);
  var db = firebase.database();
  var dataRef = db.ref("registeredUsers");


function register(){
    window.location="register.html"
}
function signup(){
    console.log('register function called');
    let reg_name=document.getElementById("new_user").value
    let reg_email=document.getElementById("new_email").value
    let reg_password=document.getElementById("new_password").value

    let reg_data = {
            name : reg_name,
            email : reg_email,
            password : reg_password,
    }

    dataRef.once('value')
        .then(function(snapshot) {
            let data = snapshot.val();
            console.log(data);
            if(data){
                data.push(reg_data);
                db.ref("registeredUsers").set(data);
            }
            else{
                db.ref(`registeredUsers/${0}`).set(reg_data);
            }
        })
        alert("You have registered your account succesfully")
        window.location="login.html"
}

 

function checklogin(){
    if(localStorage.getItem("loggedin")){
        let login_username=document.getElementById("username")
        login_username.innerHTML=`Welcome ${localStorage.getItem("logname")}`
    }else{
        window.location="login.html"
    }
}
function login(){
    let user_detail=document.getElementById("email").value
    let Password=document.getElementById("password").value
        dataRef.once('value')
        .then(function(snapshot) {
            let data = snapshot.val();
            console.log(data);
            isuser_alive=false
            if(data){
                for(i=0;i<data.length;i++){
                    if ((data[i].email==user_detail) && (data[i].password==Password)){
                        isuser_alive=true
                        alert("login successfully")
                        localStorage.setItem("loggedin",true)
                        localStorage.setItem("logname",data[i].name)
                        window.location="home.html"; 
                        break   
                    }                   
                }
            }if(isuser_alive==false){
                alert("pls register")
            window.location="login.html"}
        })
}                

function logout(){
    localStorage.removeItem("loggedin")
    localStorage.removeItem("logname")
    window.location="login.html"
}

// let alldata=[];
function getitem(){
    let info=document.getElementById("userlist")
    info.style.display="block"
    dataRef.once("value")
    .then(function(ref){
        temp=ref.val()
        htmldata=""
        for(i=0;i<temp.length;i++){
            htmldata=htmldata+`<tr><td>${temp[i].name}</td>
                                   <td>${temp[i].email}</td>
                                   <td><button type="button" onclick="update('${temp[i].email}')">edit</button></td>
                                   <td><button type="button" onclick="del('${temp[i].email}')">delete</button></td></tr>`
                                   
        }
        document.getElementById("table_body").innerHTML=htmldata
        console.log(temp.length)
    })
}

function del(mail){
    newdata=[]
    dataRef.once("value")
    .then(function(ref){
        temp=ref.val()
        for(i=0;i<temp.length;i++){
            if(temp[i].email!=mail){
                newdata.push(temp[i])
            }
        }db.ref("registeredUsers").set(newdata);
        getitem()
    })
}


function update(mail){
    localStorage.setItem("getmail",mail)
    window.location.href="update.html?"+mail;
}
function change(){
    let change_name=document.getElementById("updt_user").value
    let change_email=document.getElementById("updt_email").value
    let change_password=document.getElementById("updt_password").value
    let getmail=localStorage.getItem("getmail")
    alert(getmail)
    dataRef.once("value")
    .then(function(source){
        let details=source.val();
        console.log(details)
        for(i=0;i<details.length;i++){
            if(details[i].email==getmail){
                details[i].email=change_email
                details[i].password=change_password
                details[i].name=change_name
            }
        }
        db.ref("registeredUsers").set(details)
        localStorage.removeItem("getmail")
        getitem()
    })
}



