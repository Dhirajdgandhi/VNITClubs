/* Global Variables */
var pass_mismatch = "passwords don't match";
var login_clgid = "College ID number required";
/* End of Global Variables */


function validate_reset_pass()
{
	//alert("ih");
	document.getElementById('passr11').innerHTML = ""
	document.getElementById('passr12').innerHTML = ""
	var retval=true;
	var pass1 = pass_form.pass1.value;
	var pass2 = pass_form.pass2.value;
// Uncomment this later	
/*if(pass1.length < 8)
	{
		document.getElementById('passr11').innerHTML = "minimum 8 characters required";
		retval=false;
	}
	else */if(pass1 != pass2)
	{
		document.getElementById('passr12').innerHTML = "passwords don't match";
		retval=false;
	}
	return retval;
}

function validate_login()
{
	document.getElementById('cidr').innerHTML = "";
	document.getElementById('passr').innerHTML = "";
	var retval=true;
	var clg_id = login_form.usrname.value;
	var pass = login_form.psw.value;
	var ck_cid= /^[0-9]{5}$/;
	if (clg_id=="") {
		document.getElementById('cidr').innerHTML = login_clgid; 
        	retval=false;
    	}
    	else if( !ck_cid.test(clg_id))
    	{
		document.getElementById('cidr').innerHTML = "college id not valid";
		retval=false;
    	}
	
	if(pass=="")
	{
		document.getElementById('passr').innerHTML = "password required";
		retval=false;
	}
//Uncomment this later	
/*else if(pass.length<8)
	{
		document.getElementById('passr').innerHTML = "password of minimum length 8 required";
		retval=false;
	}*/
	return retval;
}

function validate_fp(){
	document.getElementById('cidr').innerHTML = "";
	document.getElementById('emr').innerHTML = "";
	var retval=true;
	var email = fp_form.email.value;
	var ck_email= /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	if (email=="") {
		document.getElementById('emr').innerHTML = "Email field should not be empty"; 
        	retval=false;
    	}
    	else if(!ck_email.test(email))
    	{
		document.getElementById('emr').innerHTML = "Email not vaid";
		retval=false;
    	}
	var clg_id = fp_form.clg_id.value;
	var ck_cid= /^[0-9]{5}$/
	if (clg_id=="") {
		document.getElementById('cidr1').innerHTML = "college id number required"; 
        	retval=false;
    	}
    	else if( !ck_cid.test(clg_id))
    	{
		document.getElementById('cidr1').innerHTML = "college id not valid";
		retval=false;
    	}
	return retval;
}


function validate_register_Form(){
	//alert("hii");
	document.getElementById('fnr').innerHTML = "";
	document.getElementById('lnr').innerHTML = ""; 
	document.getElementById('emr_err').innerHTML = "";
	document.getElementById('mbr1').innerHTML = "";
	document.getElementById('mbr2').innerHTML = "";
	document.getElementById('rnr').innerHTML = "";
	document.getElementById('cidr_err').innerHTML = "";
	document.getElementById('br').innerHTML = "";
	document.getElementById('passr1').innerHTML = "";
	document.getElementById('passr2').innerHTML = "";
	var retval=true;
	var fname = register_form.fname.value;
	var ck_name = /^[A-Za-z]{2,20}$/;
	if (fname=="") {
		document.getElementById('fnr').innerHTML = "Firstname field should not be empty"; 
        	retval=false;
    	}
    	else if(!ck_name.test(fname))
    	{
		document.getElementById('fnr').innerHTML = "Firstname should contain only alphabets";
		retval=false;
    	}	
	var lname = register_form.lname.value;
	if (lname=="") {
		document.getElementById('lnr').innerHTML = "Lastname field should not be empty"; 
        	retval=false;
    	}
    	else if(!ck_name.test(lname))
    	{
		document.getElementById('lnr').innerHTML = "Lastname should contain only alphabets";
		retval=false;
    	}
	var email = register_form.email.value;
	var ck_email= /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	if (email=="") {
		document.getElementById('emr_err').innerHTML = "Email field should not be empty"; 
        	retval=false;
    	}
    	else if(!ck_email.test(email))
    	{
		document.getElementById('emr_err').innerHTML = "Eamil not valid";
		retval=false;
    	}
	var mob1 = register_form.telephone1.value;
	var mob2 = register_form.telephone2.value;
	var ck_mob = /^[0-9]{10,10}$/
	if (mob1=="") {
		document.getElementById('mbr1').innerHTML = "Mobile number required"; 
        	retval=false;
    	}
    	else if(!ck_mob.test(mob1))
    	{
		document.getElementById('mbr1').innerHTML = "10 digit number required";
		retval=false;
    	}
	if(mob2!="" && !ck_mob.test(mob2))
    	{
		document.getElementById('mbr2').innerHTML = "10 digit number required";
		retval=false;
    	}
	var roll_no = register_form.roll_no.value;
	var ck_rn1= /^[B][T][0-9]{2}[A-Z]{3}[0-9]{3}$/
	var ck_rn2= /^[b][t][0-9]{2}[a-z]{3}[0-9]{3}$/
	if (roll_no=="") {
		document.getElementById('rnr').innerHTML = "Roll Number required"; 
        	retval=false;
    	}
    	else if( !(ck_rn1.test(roll_no)) && !(ck_rn2.test(roll_no)))
    	{
		document.getElementById('rnr').innerHTML = "Roll Number not valid";
		retval=false;
    	}
	var clg_id = register_form.clg_id.value;
	var ck_cid= /^[0-9]{5}$/
	if (clg_id=="") {
		document.getElementById('cidr_err').innerHTML = "college id number required"; 
        	retval=false;
    	}
    	else if( !ck_cid.test(clg_id))
    	{
		document.getElementById('cidr_err').innerHTML = "college id not valid";
		retval=false;
    	}
	var branch = register_form.dept.value;
	if (branch=="sb") {
		document.getElementById('br').innerHTML = "select a branch"; 
        	retval=false;
    	}
	var pass1 = register_form.password1.value;
	var pass2 = register_form.password2.value;
	if(pass1.length < 8)
	{
		document.getElementById('passr1').innerHTML = "minimum 8 characters required";
		retval=false;
	}
	if(pass1 != pass2)
	{
		document.getElementById('passr2').innerHTML = "passwords don't match";
		retval=false;
	}
	return retval;	
}


function validate_editprof_Form(){

	document.getElementById('fnr_ep').innerHTML = "";
	document.getElementById('lnr_ep').innerHTML = ""; 
	document.getElementById('mbr1_ep').innerHTML = "";
	document.getElementById('mbr2_ep').innerHTML = "";
	document.getElementById('passr1_ep').innerHTML = "";
	document.getElementById('passr2_ep').innerHTML = "";
	var retval=true;
	var fname = editprof_form.fname.value;
	var ck_name = /^[A-Za-z]{2,20}$/;
	if (fname=="") {
		document.getElementById('fnr_ep').innerHTML = "Firstname field should not be empty"; 
        	retval=false;
    	}
    	else if(!ck_name.test(fname))
    	{
		document.getElementById('fnr_ep').innerHTML = "Firstname should contain only alphabets";
		retval=false;
    	}	
	var lname = editprof_form.lname.value;
	if (lname=="") {
		document.getElementById('lnr_ep').innerHTML = "Lastname field should not be empty"; 
        	retval=false;
    	}
    	else if(!ck_name.test(lname))
    	{
		document.getElementById('lnr_ep').innerHTML = "Lastname should contain only alphabets";
		retval=false;
    	}
	var mob1 = editprof_form.telephone1.value;
	var mob2 = editprof_form.telephone2.value;
	var ck_mob = /^[0-9]{10,10}$/
	if (mob1=="") {
		document.getElementById('mbr1_ep').innerHTML = "Mobile number required"; 
        	retval=false;
    	}
    	else if(!ck_mob.test(mob1))
    	{
		document.getElementById('mbr1_ep').innerHTML = "10 digit number required";
		retval=false;
    	}
	if(mob2!="" && !ck_mob.test(mob2))
    	{
		document.getElementById('mbr2_ep').innerHTML = "10 digit number required";
		retval=false;
    	}
	var pass1 = editprof_form.password1.value;
	var pass2 = editprof_form.password2.value;
	if((pass1.length < 8) && !(pass1 == ""))
	{
		document.getElementById('passr1_ep').innerHTML = "minimum 8 characters required";
		retval=false;
	}
	if(pass1 != pass2)
	{
		document.getElementById('passr2_ep').innerHTML = "passwords don't match";
		retval=false;
	}
	return retval;
}





function validate_exp(){
	document.getElementById('pfr').innerHTML = "";
	document.getElementById('cpr').innerHTML = "";
	document.getElementById('pckgr').innerHTML = "";
	document.getElementById('cgpar').innerHTML = "";
	document.getElementById('nrr').innerHTML = "";
	
	var retval=true;
	var profile = exp_form.profile.value;
	if(profile=="not_selected")
	{
		document.getElementById('pfr').innerHTML = "Select a Profile";
		retval=false;
	}
	var company = exp_form.company.value;
	var new_company = exp_form.new_company.value;
	if(company=="")
	{
		document.getElementById('cpr').innerHTML = "Select a company or select other";
		retval=false;
	}
	if(company =="other" && new_company =="")
	{
		document.getElementById('cpr').innerHTML = "enter the other company name";
		retval=false;
	}
	var pckg = exp_form.package.value;
	var ck_pckg = /^[0-9]{0,}$/
	if(!ck_pckg.test(pckg))
	{
		document.getElementById('pckgr').innerHTML = "package amount not valid";
		retval=false;
	}
	
	var cgpa = exp_form.cgpa.value;
	if((cgpa<0 || cgpa>10) && cgpa!="")
	{
		document.getElementById('cgpar').innerHTML = "cgpa not valid";
		retval=false;
	}
	var rounds = exp_form.rounds.value;
	if(rounds==0)
	{
		document.getElementById('nrr').innerHTML = "Min number of rounds is 1";
		retval=false;
	}
	var j=1;
	while(j <= rounds)
	{
		document.getElementById("round"+j+"timer").innerHTML = "";
		j++;
	}
	var i=1;
	while(i<=rounds)
	{
	      roundno = "round"+i+"time";
	      time=document.getElementById(roundno).value;
	      
	      var ck_time = /^[0-9]{0,}$/
	      round_err= "round"+i+"timer";
	      if(time=="")
	       {
		      document.getElementById("round"+i+"timer").innerHTML = "enter the time";
		      retval=false;
	       }
	       else if(!ck_time.test(time))
		{
			document.getElementById("round"+i+"timer").innerHTML = "time should be numbers showing minutes";
			retval=false;		
		}
		i++;

	}
	return retval;
}



function validate_accept_company_modal(){

formobj=document.forms["accept"+arguments[0]];
//alert( );

	document.getElementById('cnr_acm').innerHTML = ""; 
	document.getElementById('snr_acm').innerHTML = ""; 
document.getElementById('lnr_acm').innerHTML = ""; 
document.getElementById('dnr_acm').innerHTML = ""; 

	var retval=true;
    
    cname=formobj.elements["company_name"].value;
    sname = formobj.elements["short_name"].value;
lname = formobj.elements["long_name"].value;
dname = formobj.elements["display_name"].value;
//startDate = formobj.getElementById('startDate').value;
//recentDate =formobj.getElementById('recentDate').value;

	var ck_name = /^[A-Za-z]{2,20}$/;
	if (cname=="") {
		document.getElementById('cnr_acm').innerHTML = "This field should not be empty"; 
        	retval=false;
    	}
    	else if(!ck_name.test(cname))
    	{
		document.getElementById('cnr_acm').innerHTML = "Name should contain only alphabets";
		retval=false;
    	}	
    if (sname=="") {
		document.getElementById('snr_acm').innerHTML = "This field should not be empty"; 
        	retval=false;
    	}
    	else if(!ck_name.test(sname))
    	{
		document.getElementById('snr_acm').innerHTML = "Name should contain only alphabets";
		retval=false;
    	}	
if (lname=="") {
		document.getElementById('lnr_acm').innerHTML = "This field should not be empty"; 
        	retval=false;
    	}
    	else if(!ck_name.test(lname))
    	{
		document.getElementById('lnr_acm').innerHTML = "Name should contain only alphabets";
		retval=false;
    	}	
if (dname=="") {
		document.getElementById('dnr_acm').innerHTML = "This field should not be empty"; 
        	retval=false;
    	}
    	else if(!ck_name.test(dname))
    	{
		document.getElementById('dnr_acm').innerHTML = "Name should contain only alphabets";
		retval=false;
    	}	
//alert(startDate);
//alert(recentDate);
/*
if ((Date.parse(startDate) <= Date.parse(recentDate))) {
        alert("End date should be greater than Start date");
        //document.getElementById("EndDate").value = "";
retval=false;
    }
*/

    
    return retval;
}
   


function validate_accept_list_modal(){
//alert("hi");
    formobj=document.forms["list"+arguments[0]];
	document.getElementById('cnr_lcm'+arguments[0]).innerHTML = ""; 
document.getElementById('deptr_lcm'+arguments[0]).innerHTML = "";
document.getElementById('typer_lcm'+arguments[0]).innerHTML = "";

	var retval=true;

    var cname_drop=formobj.elements["company_name"];
    var index=cname_drop.selectedIndex;   
    var val=cname_drop.options[index].value;
//alert("hi");

    if(val==0){
        document.getElementById('cnr_lcm'+arguments[0]).innerHTML = "Select a company";
        retval=false;
    }
//alert("hi");
 
    deptobj=formobj.elements["dept"];
    typeobj = formobj.elements["type"];

    //Department
    var flag=0;
    for(i=0;i<8;i++){
        if ( deptobj[i].checked == true )    {flag=1; }
    }
    
    if (flag!=1){
document.getElementById('deptr_lcm'+arguments[0]).innerHTML = "Select a department";
    retval=false;
}
    //Type
    var flag=0;
    for(i=0;i<2;i++){
        if ( typeobj[i].checked == true )    {flag=1; }
    }
    
    if (flag!=1){
document.getElementById('typer_lcm'+arguments[0]).innerHTML = "Select a type";
    retval=false;
}

    return retval;
}