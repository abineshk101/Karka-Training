let resume_details={};

let temp={};

function val(a,b){
    if(b){
        if(resume_details[b]){
            resume_details[b]={...resume_details[b]}
        }else{
        resume_details[b]={}
        }
        resume_details[b][a.name]=a.value
    }else{
        resume_details[a.name]=a.value
    }display()
}

function add_skill(key,id,tbl_id,edu){
    if(edu){
        if(!resume_details[edu]){
            resume_details[edu]=[]
        }
        resume_details[edu].push(temp)
        let keys=Object.keys(temp)
        for(i=0;i<keys.length;i++){
            document.getElementById(keys[i]).value=""
        }
        temp={}
        display()
    }else{
        if(!resume_details[key]){
            resume_details[key]=[]
        }
        resume_details[key].push(document.getElementById(id).value)
        document.getElementById(id).value=""
        display()
        htmldata=""
        for(i=0;i<resume_details[key].length;i++){
            htmldata=htmldata+`<div id="${key[i]}"><button type="button" onclick="del('${[i]}','${key}')" class="btn btn-primary">
            remove</button><ul>${resume_details[key][i]}</ul></div>`
        }
        document.getElementById(tbl_id).innerHTML=htmldata}
}
function display(){
    document.getElementById("dispaly_items").innerHTML=JSON.stringify(resume_details,undefined,2)
}
function del(indx,key_name){
    resume_details[key_name].splice(indx,1)
    result=document.getElementById(`${key_name[indx]}`)
    result.remove()
    display()
    // let skill_item=[]
    // for(i=0;i<resume_details.skills.length;i++){
    //     if(resume_details.skills[i]!=skl){
    //         skill_item.push(resume_details.skills[i])
    //         resume_details.skills=skill_item
    //     }
    // }console.log(resume_details)
}

function get_info(item){
    temp[item.name]=item.value
}

