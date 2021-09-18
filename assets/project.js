$(document).ready(function(){
 $.getJSON("/displayallcategoryjson",function(data){
   $.each(data,function(index,item){
      $('#cid').append($('<option>').text(item[1]).val(item[0]))

   })

 })


})