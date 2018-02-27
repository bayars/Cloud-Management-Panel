var lastfile = 'file';
function edit(a,f) {
	lastfile = f;
	console.log(lastfile)
	$.get(a,function(data,status){
		console.log(data);
		if(data == 'ErrorSize'){
			alert('File you requsted exceeded allowed limit of 1MB/Unidentifiable Filename. Try using FTP application for your purpose.');
		}
		else{
			$("#textarea").val(data);
			$("#textarea").show();
			$("#savebutton").show();
			$("#exitbutton").show();
		}
	})
}

function exit() {
	
	$("#textarea").val(null);
	$("#textarea").hide();
	$("#savebutton").hide();
	$("#exitbutton").hide();
}

function saveandsend(a){
	
	a = a + lastfile
	d = document.getElementById("textarea").value;
	$.get(a,{content: d},function(data,status){
		alert (data);
		$("#textarea").hide();
		$("#savebutton").hide();
		$("#exitbutton").hide();
	})
	console.log("data sent");
}
function removefile(fpath,f){
	var r = confirm('Do you want to delete '+f+"?")
	if(r == true){
		window.location.href=fpath;
	}
}