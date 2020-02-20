$(function(){
	
	$('.form_cont>form').on('submit',function(e){

		e.preventDefault();
		$('.analysis_loader').show();

		var object = {
			url:"https://planetics.herokuapp.com/api/fetch/summary/",
			data:{
				'content' : this.content.value
			},
			type:"POST",
			datatype:'jsonp'
		};

		xhr = $.ajax(object).done(function(data){
			$('.analysis_loader').hide();			
			console.log(data);

			$('.summary_para').text(data['data']);

		}).fail(function( jqXHR, textStatus, errorThrown ) {
			console.log(jqXHR);
			alert(jqXHR.statusText);

			$('.analysis_loader').hide();
		});	
	});

});