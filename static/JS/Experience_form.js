function display()
{
//alert('funciton');
	var rounds = document.getElementById("rounds").value;
//alert(rounds);
	var s= "";
    	document.getElementById("displayrounds").innerHTML='';
	var i=1;
	while (i<=rounds) {
//alert(i);
//	document.getElementById("roundinfo").visibility = true; 
	
        s+= "<label for='round'"+i+"'>Round " + i + " details :</label> <select name='round"+i+"type'><option value='select'>-select-</option><option value='Technical'>Technical</option><option value='HR'>HR</option><option value='test'>test</option><option value='other'>other</option></select><br><label for='round'"+i+"time'>Time in minutes :</label><input type='text' name='round"+i+"time' value=''></input><br><textarea width='75%' height='20%' name='round"+i+"'></textarea><br><br>"; //Create one textbox as HTML
	i++;
    }
    document.getElementById("displayrounds").innerHTML=s;
	
}
function validate_exp(){
	alert("hii")
	var retval=true;
	var clg_id = exp_form.clg_id.value;
	var ck_cid= /^[0-9]{5}$/
	if (clg_id=="") {
		document.getElementById('cidr').innerHTML = "college id number required"; 
        	retval=false;
    	}
    	else if( !ck_cid.test(clg_id))
    	{
		document.getElementById('cidr').innerHTML = "college id not valid";
		retval=false;
    	}
	var type = exp_form.type.value;
	if(type=="")
	{
		document.getElementById('jir').innerHTML = "Select a type";
		retval=false;
	}
	var dept = exp_form.dept.value;
	if(dept=="default")
	{
		document.getElementById('dpr').innerHTML = "Select a Department";
		retval=false;
	}
	var company = exp_form.company.value;
	var new_company = exp_form.new_company.value;
	if(company=="default" && new_company=="")
	{
		document.getElementById('cpr').innerHTML = "Select a company or enter other company";
		retval=false;
	}
	if(company!="default" && new_company!="")
	{
		document.getElementById('cpr').innerHTML = "either choose from available or enter a name.Both not allowed.";
		retval=false;
	}
	var cgpa = exp_form.cgpa.value;
	if(cgpa=="")
	{
		document.getElementById('cgpar').innerHTML = "Enter your cgpa";
		retval=false;
	}
	else if(cgpa<0 || cgpa>10)
	{
		document.getElementById('cgpar').innerHTML = "cgpa not valid";
		retval=false;
	}
	var rounds = exp_form.rounds.value;
	if(rounds=="default")
	{
		document.getElementById('nrr').innerHTML = "Select number of rounds";
		retval=false;
	}
	return retval;
}


