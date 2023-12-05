function GetData(){
    $.ajax({
        type:"GET",
        url:"https://jsonplaceholder.typicode.com/posts",
        data:"",
        success:function(response){
            let htmldata=""
            for(i=0;i<response.length;i++){
                // console.log(response[i])
                htmldata=htmldata+`<tr>
                                        <td><button onclick="give_id('${response[i].id}')">${response[i].id}</button></td>
                                        <td>${response[i].title}</td>
                                        <td>${response[i].userId}</td>
                                    </tr>`
                                        
            }document.getElementById("tbl").innerHTML=htmldata
        },
        error:function(error){
            console.log(error)
        }
        })
}

function give_id(id){
    $.ajax({
        type:"GET",
        url:`https://jsonplaceholder.typicode.com/posts/${id}/comments`,
        data:"",
        success:function(display){
            console.log(display)
            // for(i=0;i<display.length;i++){
            //     console.log(display[i])
            // }
        }
    })
}

function SendData(){
    $.ajax({
        type:"POST",
        url:"https://jsonplaceholder.typicode.com/posts",
        data:{userId:"Agaram",title:"Welcome Agaram",body:"create"},
        success:function(show){
            console.log(show)
        }
    })
}


