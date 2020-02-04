$(function(){
	$('#loader').hide();

	$('.nav_toggle').on('click',function(){
		$('.slider_nav').toggleClass('slider_nav_show');
	});

	// create a scene
	new ScrollMagic.Scene({
	    //duration: 100, // the scene should last for a scroll distance of 100px
	    offset: 176 // start this scene after scrolling for 50px
	}).setPin('#search_panel_pin',{pushFollowers: false}).addTo(controller);

	new ScrollMagic.Scene({
	    //duration: 100, // the scene should last for a scroll distance of 100px
	    offset: 0 // start this scene after scrolling for 50px
	}).setPin('#nav',{pushFollowers: false}).addTo(controller);


	$('#search_form').on('submit',function(e){

		e.preventDefault();

		$('#loader').show();

		console.log(this.search.value);

		this.dataset.type = "search";

		console.log(this.dataset);

		requestAjax({data:{'query':this.search.value}},this.dataset);
	});

	$('body').delegate('#analyse','click',function(){

		console.log(this.dataset);

		$('.analysis_details').remove();
		$('.analysis_cont>.operate').remove();
		$('.analysis_loader').show();

		if(this.dataset.type == 'social'){

			$('.analysis_cont').show();

			requestAjax({
				url:'https://planetics.herokuapp.com/api/fetch/analysis/',
				type:'POST',
				data:{
					'type':this.dataset.type,
					'url':this.dataset.url,
					'text':this.dataset.text
				}
			},this.dataset);
		}
		else if(this.dataset.type == 'news'){

			$('.analysis_cont').show();

			requestAjax({
				url:'https://planetics.herokuapp.com/api/fetch/analysis/',
				type:'POST',
				data:{
					'type':this.dataset.type,
					'url':this.dataset.url,
					'img_url':this.dataset.imgarticle,
					'text':this.dataset.text
				}
			},this.dataset);
		}
		else if(this.dataset.type == 'dialog'){
			$('.analysis_cont').hide();
		}
	});
});
