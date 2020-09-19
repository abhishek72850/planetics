var requestAjax=function(options, dataset){

	var object = {
		url: window.location.origin + "/api/search/content",
		data:{},
		type:"GET",
		datatype:'jsonp'
	};

	$.extend(object,options);

	planetics.xhr = $.ajax(object).done(function(data){
		console.log(data);

		$.views.settings.allowCode(true);

		if(dataset.type == 'search' || dataset.type == 'pagination'){

			planetics.data = data;

			var n_tmpl = $.templates("#news_template");
			var s_tmpl = $.templates("#social_template");

			var empty = true;

			if(data['data']['news'] === null && data['data']['social'] === null){
				empty = false;
				alert('No Content Available!!!!');
			}
			
			if(empty){
				if(dataset.type == 'pagination'){
					planetics.page++;
					$('#page_counter').text(planetics.page);
				}
				$(".result_panel").empty();
			}

			if( data['data']['news'] !== null){
		    	var html_n = n_tmpl.render(data['data']['news']['value']);
		    	$(".result_panel").append(html_n);
		    }

		    if( data['data']['social'] !== null){
	    		if(data['data']['social']['posts'].length > 0){
	    			var html_s = s_tmpl.render(data['data']['social']['posts']);	
					$(".result_panel").append(html_s);

					planetics.requestid = data['data']['social']['meta']['requestid'];		
	    		}
			}

		    $('#loader').hide();
		    $('.screen_loader').hide();

		    $('.result_page_nav').prop(false);
		}
		else if(dataset.type == 'news'){
			$('.analysis_cont>div:not(:first-child)').empty();
			if(data['data']['visuals'] === null){
				visuals = [];
			}
			else if(!data['data']['visuals']['success']){
				visuals = [];
			}
			else{
				visuals = data['data']['visuals']['data']['images'][0]['classifiers'][0]['classes'];
			}

			news_data = [{
				'analysis_type': 'News Article',
				'source_img':dataset.imgsourcesrc,
				'publish':dataset.publishat,
				'title':dataset.title,
				'type':dataset.type,
				'link':dataset.url,
				'images':dataset.imgarticle,
				'text':data['data']['text'],
				'sentiment':data['data']['sentiment'] === null ? '':data['data']['sentiment']['data']['sentiment']['document']['label'],
                'keywords':data['data']['keywords'] === null ? []:data['data']['keywords']['keywords'],
                'summary':data['data']['summary'] === null ? '':data['data']['summary'],
                'sentences_tones':data['data']['tones'] === null ? []:data['data']['tones']['data']['sentences_tone'],
				'visuals':data['data']['visuals'] === null ? []:data['data']['visuals']['data']['images'][0]['classifiers'][0]['classes']
			}];

			console.log(news_data);

			var analysis_tmpl = $.templates("#analysis_template");
			var html_analysis = analysis_tmpl.render(news_data);

			$('.analysis_cont').append(html_analysis);
		}
		else if(dataset.type == 'social'){
			$('.analysis_cont>div:not(:first-child)').empty();
			social_data = [{
				'analysis_type': 'Social Post',
				'source_img':dataset.imgsourcesrc,
				'publish':dataset.publishat,
				'title':dataset.title,
				'type':dataset.type,
				'link':dataset.url,
				'images':dataset.imgarticle,
				'text':dataset.text,
				'sentiment':data['data']['sentiment'] === null ? '':data['data']['sentiment']['data']['sentiment']['document']['label'],
				'keywords':data['data']['keywords'] === null ? []:data['data']['keywords']['data']['keywords'],
				'summary':data['data']['summary'] === null ? '':data['data']['summary'],
				'sentences_tones':data['data']['tones'] === null ? []:data['data']['tones']['data']['sentences_tone'],
				'visuals':data['data']['visuals'] === null ? []:data['data']['visuals']['data']['images'][0]['classifiers'][0]['classes']
			}];

			console.log(social_data);

			var analysis_tmpl = $.templates("#analysis_template");
			var html_analysis = analysis_tmpl.render(social_data);

			$('.analysis_cont').append(html_analysis);
		}

		$('.analysis_loader').hide();

	}).fail(function( jqXHR, textStatus, errorThrown ) {
		console.log(jqXHR);
		console.log(jqXHR.statusText);

		$('#loader').hide();
		$('.screen_loader').hide();
	});
}

var loadContent = function(data){

}
