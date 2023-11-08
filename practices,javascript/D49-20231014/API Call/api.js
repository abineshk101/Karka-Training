let api_detail={}

function val(info){
    api_detail[info.id]=info.value
    display()
}

function display(){
    document.getElementById("show").innerHTML=JSON.stringify(api_detail,undefined,2)
    }

function save(){
    $.ajax({
        type:"post",
        url:"http://agaram.academy/api/action.php",
        data:{request:"create_candidate",
                name:api_detail.name,
                email:api_detail.email,
                password:api_detail.password,
                aadhar:api_detail.aadhar,
                address:api_detail.address,
                phone:api_detail.phone,
                city:api_detail.city,
                area:api_detail.area,
                pin:api_detail.pin},
        success:function(add){
            console.log(add)
            alert("You have registered your account successfully")
            const inputs = document.querySelectorAll('#name, #email,#password,#aadhar,#address,#phone,#city,#area,#pin');
            inputs.forEach(input => {
                input.value = '';
              });
        },
        error:function(a){
            console.log(a)
        }

    })   
}

function re(){
    window.location="api_list.html"
}

function show_ele(){
    $.ajax({
        type:"get",
        url:"http://agaram.academy/api/action.php",
        data:{
            request:"getAllMembers"
        },
        success:function(give){
            let a=JSON.parse(give)
            let all_data=a.data
            let htmldata=""
            for(i=0;i<all_data.length;i++){
                htmldata=htmldata+`<tr><td>${all_data[i].id}</td>
                                        <td>${all_data[i].name}</td>
                                        <td>${all_data[i].email}</td>
                                        <td>${all_data[i].password}</td>
                                        <td>${all_data[i].aadhar}</td>
                                        <td>${all_data[i].address}</td>
                                        <td>${all_data[i].phone}</td>
                                        <td>${all_data[i].city}</td>
                                        <td>${all_data[i].area}</td>
                                        <td>${all_data[i].pin}</td>`
            }
            document.getElementById("insert").innerHTML=htmldata
        },
        error:function(a){
            console.log(a)

        }
    })
}

function login(){
    $.ajax({
        type:"post",
        url:"http://agaram.academy/api/action.php",
        data:{
            request:"candidate_login",
            email:$('#login_email').val(),
            password:$('#login_password').val()
        },
        success:function(give){
            console.log(give)
        },
        error:function(a){
            console.log(a)

        }
    })
}

