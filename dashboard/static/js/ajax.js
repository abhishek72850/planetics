var requestAjax=function(options, dataset){

	var object = {
		url:"https://planetics.herokuapp.com/api/fetch/post",
		data:{},
		type:"GET",
		datatype:'jsonp'
	};

	$.extend(object,options);

	xhr = $.ajax(object).done(function(data){
		console.log(data);

		$.views.settings.allowCode(true);

		if(dataset.type == 'search'){

			planetics.data = data;

			$(".result_panel").empty();

			var n_tmpl = $.templates("#news_template");
			var s_tmpl = $.templates("#social_template");

			if( data['data']['social'] != null){
				var html_s = s_tmpl.render(data['data']['social']['posts']);	
				$(".result_panel").append(html_s);
			}

		    var html_n = n_tmpl.render(data['data']['news']['value']);
		    $(".result_panel").append(html_n);

		    $('#loader').hide();
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
				'sentiment':data['data']['sentiment']['data']['sentiment']['document']['label'],
				'keywords':data['data']['keywords']['keywords'],
				'summary':data['data']['summary'],
				'sentences_tones':data['data']['tones']['data']['sentences_tone'],
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
	});;
}
