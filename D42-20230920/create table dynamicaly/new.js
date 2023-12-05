let list=["a","b","c","d"]
function clq(){
    alert("hi")
    let htmldata=""
    for(let i=0;i<list.length;i++){
        htmldata=htmldata+`<tr><td>${list[i]}</td>
                               <td>${list[i]}</td>
                               <td>${list[i]}</td></tr>`
    }
document.getElementById("list_table").innerHTML=htmldata
}
