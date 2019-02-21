function HTTPRequest(doc,urladdress,isHTML){
	$.ajax({
		type: "GET",
		dataType: "html",
		url: urladdress,
		success: function (result) {
			changePage(doc,result,isHTML);
		},
		error: function() {
			alert("Error!");
		}
	});
}

function openPage(laddress){
	var pocTest = $("#pocTest");
	//alert(pocTest)
	HTTPRequest(pocTest,laddress,1);
}

function changePage(doc,htmlContent,isHTML){
	if(isHTML){
		doc.html(htmlContent);
	}else{
		doc.text(htmlContent);
	}
}

function getPoC(par){
	var pocLink = $("#pocLink");
	var input = escape($("#input").val());
	var pocText = $("#pocText");

	if(par == "jsonp"){
		var jsonpUrl = "./poc/php/jsonp.php";
		var cValue = $("#cvalue").val();
		jsonpUrl += "?url=" + input + "&cvalue=" + cValue;
		HTTPRequest(pocText,jsonpUrl,0);
		pocLink.attr("href",jsonpUrl);
	}else if(par == "cors"){
		var corsUrl = null;
		var data = $("#data").val();
		if($('#gMethod:checked').val()){
			corsUrl = "./poc/php/cors_get.php?url=" + input;
		}else if($('#pMethod:checked').val()){
			corsUrl = "./poc/php/cors_post.php?url=" + input + "&data=" + data;
		}

		HTTPRequest(pocText,corsUrl,0);
		pocLink.attr("href",corsUrl);
	}else if(par == "googlehack"){
		googleHack(input,pocText);
	}else if(par == "urlredirect"){
		urlredirectUrl = "./poc/php/urlredirect.php?url=" + input;
		HTTPRequest(pocText,urlredirectUrl,1);
	}else if(par == "jsurl"){
		var jsUrl = "./poc/php/jsurl.php?url=";
		jsUrl += input;
		HTTPRequest(pocText,jsUrl,0);
		pocLink.text(window.location + jsUrl.replace("./",""));
	}else if(par == "302url"){
		var url302 = "./poc/php/302url.php?url=";
		url302 += input;
		pocLink.text(window.location + url302.replace("./",""));
	}
}

function googleHack(url,doc){
	doc.html("");
	var v = url;
	var i = 0;
	var x = "";
	var hack = new Array(
		"https://www.google.com/search?q=site:" + v + "+intitle:index.of",
		"https://www.google.com/search?q=site:" + v + "+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini",
		"https://www.google.com/search?q=site:" + v + "+ext:sql+|+ext:dbf+|+ext:mdb",
		"https://www.google.com/search?q=site:" + v + "+ext:log",
		"https://www.google.com/search?q=site:" + v + "+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup",
		"https://www.google.com/search?q=site:" + v + "+inurl:login",
		"https://www.google.com/search?q=site:" + v + "+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mysql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warning:+pg_connect()%22",
		"https://www.google.com/search?q=site:" + v + "+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv",
		"https://www.google.com/search?q=site:" + v + "+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22"
	)
	var txt = new Array(
		"Directory Traversal",
		"Config File Leak",
		"Data File Leak",
		"Log File Leak",
		"Backup && History",
		"Login Page",
		"SQL Error",
		"Public File",
		"phpinfo()"
	)

	while (i<9)
	{
		doc.append("<br><br><a href='" + hack[i] + "' target='__blank'>" + txt[i] + "</a>");
		i++;
	}
	//alert(doc.html());
}