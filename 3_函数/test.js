function fn(arr = []){
  arr.push(0)
  console.log(arr)
}
fn()
fn()

/* 匿名函数 */
(function(){

})

let f = function(){

}

fn(function(){

})