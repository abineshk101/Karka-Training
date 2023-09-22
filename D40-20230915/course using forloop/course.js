var resume={name:"Abinesh K",
        email:"abineshk101@gmail.com",
        mobile_no:"7904820356",
        hardskills:["undergraduated","hindi_learner"],
        softskills:["leadership","teamworker","sportive_person"],
        educational_qualification:[{course:"SSLC",institute:"Kumari Matriculation Hr sec school",percentage:87.2,passed_out_year:2017},
                                     {course:"HSC",institute:"Kumari Matriculation Hr sec school",percentage:58.8,passed_out_year:2019},
                                     {course:"BE",institute:"DMI Engineering College",percentage:63,passed_out_year:2023}],
        projects:["smartfarmer_app","sensing moisture","Data saving application"],
        experience:[{company:"Wipro",location:"Chennai",years:2,role:"developer"},
                      {company:"Karka academy",location:"Nagercoil",years:1,role:"Teaching Assistant"},
                      {company:"Tech vip",location:"chennai",years:1,role:"Training Assistant"}],
        hobbies:["cricket","listenig music","volleyball"],
        personal_details:{fathers_name:"C.Kumar",
                           fathers_occupation:"cooli",
                           language_known:["Tamil","English"],
                           dob:"11-09-2001",
                           gender:"male",
                           martial_status:"No",
                           address:{door_no:"205/9A",
                                      compound:"Thanunadar Compound",
                                      place:"Vattavilai",
                                      city:"Nagercoil"}}      
        }

// for(i=0;i<3;i++){
//     console.log(i+1,resume.educational_qualification[i].course)
// }
let newone={course:"ME",institute:"DMI Engineering College",percentage:63,passed_out_year:2025}
resume.educational_qualification.push(newone)

// function getcourse(resume){
//     let education=resume.educational_qualification
//     for(i=0;i<education.length;i++){
//         console.log(`${i+1}.${education[i].course}`)
//     }
// }

function getcourse(resume){
    let education=resume.educational_qualification
    for(let 
        i=education.length-1;i>=0;i--){
        console.log(`${i+1}.${education[i].course}`)
    }
}
getcourse(resume)

