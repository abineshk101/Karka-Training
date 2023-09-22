// let userdetails=[{email:"abineshk101@gmail.com",
//                   password:"1234abi",
//                   name:"agaram"},
//                 {email:"abinesh123@gmail.com",
//                  password:"abiabiabi",
//                  name:"Abi"}]


// localStorage.setItem("userdetails",JSON.stringify(userdetails));

function login(){
    let login_email=document.getElementById("email").value
    let login_password=document.getElementById("password").value
    let login_username=document.getElementById("username")
    let page=document.getElementById("welcome")
    let out=document.getElementById("loginform")
    userdetails=JSON.parse(localStorage.getItem("userdetails"))
    console.log(userdetails)
    for(var i=0;i<userdetails.length;i++){
        if(login_email==userdetails[i].email && login_password==userdetails[i].password){
                // alert("success")
                localStorage.setItem("loggedIn",true)
                login_username.innerText=`Welcome ${userdetails[i].name}`
                localStorage.setItem("Name",login_username.innerText)
                page.style.display="block"
                out.style.display="none"
            }
        }
    }

function checklogin(){
    let page=document.getElementById("welcome")
    let out=document.getElementById("loginform")
    let login_username=document.getElementById("username")
    login_username.innerText=`${localStorage.getItem("Name")}`
    if(localStorage.getItem("loggedIn")){
        page.style.display="block"
        out.style.display="none"
    }
}

function logout(){
    let page=document.getElementById("welcome")
    let out=document.getElementById("loginform")
    page.style.display="none"
    out.style.display="block"
}

function register(){
    let info1=document.getElementById("registry_input")
    let out=document.getElementById("loginform")
    info1.style.display="block"
    out.style.display="none"
}
function signup(){
    let newid=document.getElementById("new_user").value;
    let newmail=document.getElementById("new_email").value;
    let newpass=document.getElementById("new_password").value;
    if(localStorage.getItem("userdetails")){
        userdetails=JSON.parse(localStorage.getItem("userdetails"))
        userdetails.push({email:newmail,password:newpass,name:newid})
        localStorage.setItem("userdetails",JSON.stringify(userdetails));
    }else{
        let userdetails=[]
        userdetails.push({email:newmail,password:newpass,name:newid})

    }
    
    localStorage.setItem("userdetails",JSON.stringify(userdetails));
    alert("You have registered your account succesfully")
    let out=document.getElementById("loginform")
    let info1=document.getElementById("registry_input")
    out.style.display="block"
    info1.style.display="none"
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
let abs=""
function list(){
    let page=document.getElementById("welcome")
    let info=document.getElementById("userlist")
    let rtrn=document.getElementById("return")
    info.style.display="block"
    page.style.display="none"
    rtrn.style.display="block"
    user_list=JSON.parse(localStorage.getItem("userdetails"))
    let htmldata=""
    for(i=0;i<user_list.length;i++){
        // a=user_list[i].email
        htmldata=htmldata+`<tr><td>${user_list[i].name}</td>
                               <td>${user_list[i].email}</td>
                               <td><button type="button" onclick="update()">edit</button></td>
                               <td><button type="button" onclick="del('${user_list[i].email}')">delete</button></td></tr>`
                               
    }
    document.getElementById("table_body").innerHTML=htmldata
}

function welcomepage(){
    let info=document.getElementById("userlist")
    let rtrn=document.getElementById("return")
    info.style.display="none"
    rtrn.style.display="none"
    checklogin()
}
function change(){
    list()
    //  var1=window.a
    let updt=document.getElementById("update_button")
    let updt_user=document.getElementById("updated_user").value
    let updt_mail=document.getElementById("updated_email").value
    let updt_password=document.getElementById("updated_pass").value
    updt.style.display="none"
    
    let got=JSON.parse(localStorage.getItem("userdetails"))
    for(i=0;i<got.length;i++){
        if(got[i].email==var1){
            got[i].email=updt_mail
            got[i].password=updt_password
            got[i].name=updt_user
        }
    }
    localStorage.setItem("userdetails",JSON.stringify(got))
}

function update(){
    let info=document.getElementById("userlist")
    let rtrn=document.getElementById("return")
    let updt=document.getElementById("update_button")
    updt.style.display="block"
    info.style.display="none"
    rtrn.style.display="none"
}
var1=
function update(i){
    var1=i
}
alert(var1)

    

    // let updt_user=document.getElementById("updated_user").value
    // let updt_mail=document.getElementById("updated_email").value
    // let updt_password=document.getElementById("updated_password").value
    // let got=JSON.parse(localStorage.getItem("userdetails"))
    // for(i=0;i<got.length;i++){
    //     if(got[i].email==mail){
    //         got[i].email=updt_mail
    //         got[i].password=updt_password
    //         got[i].name=updt_user
    //     }
    // }    


