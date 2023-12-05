var list1=["a","b","c"];
var stringlist=JSON.stringify(list1);
localStorage.setItem("alpha",stringlist)
var variable=localStorage.getItem("alpha");
var clist=JSON.parse(variable)
console.log(clist[2])