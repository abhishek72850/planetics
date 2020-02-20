var requestAjax=function(options, dataset){

	var object = {
		url:"https://planetics.herokuapp.com/api/search/content",
		data:{},
		type:"GET",
		datatype:'jsonp'
	};

	$.extend(object,options);

	xhr = $.ajax(object).done(function(data){
		console.log(data);

		$.views.settings.allowCode(true);

		if(dataset.type == 'search' || dataset.type == 'pagination'){

			planetics.data = data;

			$(".result_panel").empty();

			var n_tmpl = $.templates("#news_template");
			var s_tmpl = $.templates("#social_template");

			if( data['data']['social'] != null){
				var html_s = s_tmpl.render(data['data']['social']['posts']);	
				$(".result_panel").append(html_s);

				planetics.requestid = data['data']['social']['meta']['requestid'];
			}

			if( data['data']['news'] != null){
		    	var html_n = n_tmpl.render(data['data']['news']['value']);
		    }

		    if(data['data']['news'] != null || data['data']['social'] != null){
				$('#page_counter').text(planetics.page+1);
				planetics.page++;

				$(".result_panel").append(html_n);
			}
			else{
				alert('No Content Available!!!!');
			}

		    $('#loader').hide();

		    $('.result_page_nav').prop(false);
		}
		else if(dataset.type == 'pagination'){

		}
		else if(dataset.type == 'news'){
			news_data = [{
				'source_img':dataset.imgsourcesrc,
				'publish':dataset.publishat,
				'title':dataset.title,
				'type':dataset.type,
				'link':dataset.url,
				'images':dataset.imgarticle,
				'text':data['data']['text'],
				'sentiment':data['data']['sentiment']['data']['sentiment']['document']['label'],
				'keywords':data['data']['keywords']['keywords'],
				'summary':data['data']['summary'],
				'sentences_tones':data['data']['tones']['data']['sentences_tone'],
				'visuals':data['data']['visuals']['data']['images'][0]['classifiers'][0]['classes']
			}];

			var analysis_tmpl = $.templates("#analysis_template");
			var html_analysis = analysis_tmpl.render(news_data);

			$('.analysis_cont').append(html_analysis);
		}
		else if(dataset.type == 'social'){

			social_data = [{
				'source_img':dataset.imgsourcesrc,
				'publish':dataset.publishat,
				'title':dataset.title,
				'type':dataset.type,
				'link':dataset.url,
				'images':dataset.imgarticle,
				'text':dataset.text,
				'sentiment':data['data']['sentiment'] === null ? null:data['data']['sentiment']['data']['sentiment']['document']['label'],
				'keywords':data['data']['keywords'] === null ? null:data['data']['keywords']['keywords'],
				'summary':data['data']['summary'] === null ? null:data['data']['summary'],
				'sentences_tones':data['data']['tones'] === null ? null:data['data']['tones']['data']['sentences_tone'],
				'visuals':data['data']['visuals']
			}];

			var analysis_tmpl = $.templates("#analysis_template");
			var html_analysis = analysis_tmpl.render(social_data);

			$('.analysis_cont').append(html_analysis);
		}

		$('.analysis_loader').hide();

	}).fail(function( jqXHR, textStatus, errorThrown ) {
		console.log(jqXHR);
		alert(jqXHR.statusText);

		$('#loader').hide();
	});
}

var loadContent = function(data){

}
