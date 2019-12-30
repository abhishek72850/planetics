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

		console.log(this.search.value)

		requestAjax({data:{'query':this.search.value}});
	});
});