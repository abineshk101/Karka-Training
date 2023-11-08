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
        .then(function(snapshot){
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
            htmldata=htmldata+`<tr><td id="edt_name">${temp[i].name}</td>
                                   <td id="edt_email">${temp[i].email}</td>
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
    dataRef.once("value")
    .then(function(data){
        alldatas=data.val()
    })
    for(var i=0;i<alldatas.length;i++){
        if(alldatas[i].email==mail){
            let e_use=prompt(`"New Username",${alldatas[i].name}`)
            let e_usen=prompt(`"New Mail",${alldatas[i].email}`)
            if(e_use!=alldatas[i].name){
                document.getElementById("edt_name").innerHTML=e_use
            }
            if(e_usen!=alldatas[i].email){
                document.getElementById("edt_email").innerHTML=e_usen
            }
            alldatas[i]=({
                    email:e_usen,
                    name:e_use,
                    password:alldatas[i].password
                })
            }getitem()
    }
    db.ref("registeredUsers").set(alldatas);
    checklogin()
}





