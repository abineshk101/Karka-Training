let resume_detail={}
let temp={}
function val(get_info,key_name){
  if(key_name){
    if(resume_detail[key_name]){
      resume_detail[key_name]={...resume_detail[key_name]}
    }else{
      resume_detail[key_name]={}
    }resume_detail[key_name][get_info.name]=get_info.value
  }
  else{
    resume_detail[get_info.name]=get_info.value
  }
  display()
}

function add_item(key_name,id,tbl_id,edu_info){
  if(edu_info){
    if(!resume_detail[edu_info]){
      resume_detail[edu_info]=[]
    }
      resume_detail[edu_info].push(temp)
      let keyss=Object.keys(temp)
      for(i=0;i<keyss.length;i++){
        document.getElementById(keyss[i]).value=""
      }
    temp={}
    let ans=""
    for(i=0;i<resume_detail[edu_info].length;i++){
      let a=resume_detail[edu_info][i].institute_name
      let b=resume_detail[edu_info][i].level
      let c=resume_detail[edu_info][i].year
      let d=resume_detail[edu_info][i].percentage
      ans=ans+`<tr id="${edu_info[i]}"><td>${a}</td>
                                      <td>${b}</td>
                                      <td>${c}</td>
                                      <td>${d}</td>
                                      <td><button type="button" class="btn btn-primary" onclick="del(${null},'${edu_info}','${i}')">remove</button></td></tr>`
    }document.getElementById("edu_tbl").innerHTML=ans
    display()
  }else{
  if(key_name){
    if(!resume_detail[key_name]){
      resume_detail[key_name]=[]
    }
  }resume_detail[key_name].push(document.getElementById(id).value)
  document.getElementById(id).value=""
  let htmldata=""
  for(i=0;i<resume_detail[key_name].length;i++){
    htmldata=htmldata+`<div id="${key_name[i]}" class="alert alert-danger"><button type="button" class="btn btn-primary" onclick="del('${resume_detail[key_name][i]}','${key_name}','${i}')">remove</button><ol>${resume_detail[key_name][i]}</ol></div>`
  }document.getElementById(tbl_id).innerHTML=htmldata}
  display()
}

function del(get_item,key_name,idx){
  if(key_name && idx){
    let removed_obj=[]
    for(i=0;i<resume_detail[key_name].length;i++){
      if(i!=idx){
        removed_obj.push(resume_detail[key_name][i])
      }
    }resume_detail[key_name]=removed_obj
  }else
  {
  let skl=[]
  for(i=0;i<resume_detail[key_name].length;i++){
    if(resume_detail[key_name][i]!=get_item){
      skl.push(resume_detail[key_name][i])
    }
  }resume_detail[key_name]=skl
  }
  result=document.getElementById(key_name[idx])
  result.remove()
  display()
}

function add_edu(got){
  temp[got.name]=got.value
}

function display(){
  document.getElementById("show").innerHTML=JSON.stringify(resume_detail)
  }

function sent_ajx(){
  console.log(resume_detail)
  $.ajax({
    type:"post",
    url:"http://agaram.academy/api/action.php",
    data:{
      request :"create_resume",
      user :"abinesh",
      resume:resume_detail
    },
    success:function(show){
      console.log(show)
    },
    error:function(error){
      confirm.log(error)
    }
  })
  // window.location.reload()
}
function redirect(){
  window.location="list.html"
}

function get_ajx(){
  $.ajax({
    type:"get",
    url:"http://agaram.academy/api/action.php",
    data:{
      request :"get_user_resume",
      user :"abinesh"
    },
    success:function(show){
      list1=JSON.parse(show).data
      id_name=""
      for(i=0;i<list1.length;i++){
        id_name=id_name+`<tr>
                            <td>${list1[i].id}</td>
                            <td>${list1[i].user}</td>
                            <td><button type="button" onclick="del_ajx('${list1[i].id}')" class="btn btn-success">remove</button></td>
                            <td><a href="resume.html?id=${list1[i].id}">show my resume</a></td>
                          <tr>`
      }
      document.getElementById("tbl").innerHTML=id_name
      console.log(JSON.parse(show))
    },
    error:function(error){
      console.log("error",error)
    }
  })
  
}

function del_ajx(user_id){
  $.ajax({
    type:"get",
    url:"http://agaram.academy/api/action.php",
    data:{
      request :"delete_user_resume",
      user :"abinesh",
      id:user_id
    },
    success:function(content){
      get_ajx()
    },
    error:function(error){
      console.log(error)
    }
  })
}

function show_resume(){
  const queryString = window.location.search;
  const getparam=new URLSearchParams(queryString);
  let id=getparam.get('id')
  $.ajax({
    type:"get",
    url:"http://agaram.academy/api/action.php",
    data:{
      request :"get_resume_by_id",
      user :"abinesh",
      id:id
    },
    success:function(response){
      let res=JSON.parse(response)
      let taken=JSON.parse(res.data.data)
          let input_name=taken.name
          $('#resume_name').html(input_name)

          let input_objective=taken.objective
          $('#resume_objective').html(input_objective)
          // let input_email=taken.email
          // let input_number=taken.number
          // let input_fthr_name=taken.personal_details.father_name
          // let input_mthr_name=taken.personal_details.mother_name
          // let input_address=taken.personal_details.address
          // let input_district=taken.personal_details.district
          let input_skills=taken.skills
          let skill_data="Programing skills"
          for(i=0;i<input_skills.length;i++){
            skill_data=skill_data+`<ol>&#9658;${input_skills[i]}</ol>`
          }$('#prgrm_skill').html(skill_data)

          let input_lang=taken.languages
          let lang_data=""
          for(i=0;i<input_lang.length;i++){
            lang_data=lang_data+`<ol>&#10146;${input_lang[i]}</ol>`
          }$('#lang_order').html(lang_data)

          let input_edu=taken.education
          let edu_data=""
          for(i=0;i<input_edu.length;i++){
            $('#school_name').html(input_edu[i].institute_name)
            $('#sslc').html(input_edu[i].level)
            input_edu[i].year
            $('#percent').html(input_edu[i].percentage)
          }
        }
      }
    )
}

function download(){
  const page=document.getElementById('whole_resume')
  var opt={
    margin:0,
    filename:'Demo pdf',
    image:{type:'jpeg',quality:0.98},
    html2canvas:{scale:2},
    jsPDF:{unit:'in',format:'letter',orientation:'portrait'}
  }
  html2pdf().set(opt).from(page).save();
}