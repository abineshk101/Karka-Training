var list1=["a","b","c"];
var stringlist=JSON.stringify(list1);
localStorage.setItem("alpha",stringlist)
console.log(localStorage.getItem("alpha"));

