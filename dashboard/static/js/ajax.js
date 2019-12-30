var requestAjax=function(options){

	var object = {
		url:"http://localhost:8000/api/fetch/post",
		data:{},
		type:"GET",
		datatype:'jsonp'
	};

	$.extend(object,options);

	xhr = $.ajax(object).done(function(data){
		console.log(data);

		$(".result_panel").empty();

		var n_tmpl = $.templates("#news_template");
		var s_tmpl = $.templates("#social_template");

		if( data['data']['social'] != null){
			var html_s = s_tmpl.render(data['data']['social']['posts']);	
			$(".result_panel").append(html_s);
		}

	    var html_n = n_tmpl.render(data['data']['news']['articles']);
	    $(".result_panel").append(html_n);

	    $('#loader').hide();

	}).fail(function( jqXHR, textStatus, errorThrown ) {
		console.log(jqXHR);
		alert(jqXHR.statusText);

		$('#loader').hide();
	});;
}
