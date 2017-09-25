function display_rounds(packages,cgpa,num_of_rounds,round1,round2,round3,round4,round5,round6,other_comments,j)
{
//,j)
//alert('function');
	

	var s= "";
    	document.getElementById("displayrounds"+j).innerHTML='';
//alert('rounds' );
	var i=1;

	while (i<= num_of_rounds) {
//alert(i);
//	document.getElementById("roundinfo").visibility = true; 
		
	list=round1.split("<br>***<br>");
//alert(list[0]+list[1]+list[2]);
        s+= "<label for='round'"+i+"'>Round " + i + " details :</label> <select name='round"+i+"type'><option value='"+list[0]+"' default>"+list[0]+"</option><option value='Technical' default>Technical</option><option value='HR'>HR</option></select><br><label for='round'"+i+"time'>Time in minutes :</label><input type='text' name='round"+i+"time' value='"+list[1]+"'></input><br><textarea width='75%' height='20%' name='round"+i+"' value='"+list[2]+"'>"+list[2]+"</textarea><br><br>"; //Create one textbox as HTML
	i++;
    }
    document.getElementById("displayrounds"+j).innerHTML=s;
	
}


function create_div(exp_count,obj)
{
//alert('fun');
	var i=1;
	var s= '';

	//var i=exp_count;
	//document.getElementById("displayrounds").innerHTML=i;
	
	for(i=1;i<=exp_count;i++) { 
		
		var ele = document.createElement("div");
		ele.setAttribute("id","displayrounds"+i);
		ele.innerHTML="";
		displayrounds.appendChild(ele);		
			
		
//alert(i);
	}
}
