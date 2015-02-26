$( document ).ready(function (){
	var hover = false;
	$('#carousel').flexslider({
	    animation: "slide",
	    controlNav: false,
	    animationLoop: true,
	    slideshow: false,
	    itemWidth: 200,
	    itemMargin: 1,
	    asNavFor: '#slider'
	 });

	$('#slider').flexslider({
	    animation: "fade",
	    controlNav: false,
	    animationLoop: true,
	    slideshow: false,
	    sync: "#carousel",
	});

	$('.next-slide').click(function (event){
		event.preventDefault();
		$('#slider').flexslider("next");
		$('#slider').flexslider("play");
	});

	$('.prev-slide').click(function (){
		$('#slider').flexslider("prev");
		$('#slider').flexslider("play");
	});

	$('#slider').hover(function (){
		$('.next-slide').fadeIn();
		$('.prev-slide').fadeIn();
	});

	$('#slider').mouseleave(function (){
		$('.next-slide').fadeOut();
		$('.prev-slide').fadeOut();
	});

	$('#carousel img').click(function (){
		$('#slider').flexslider("play");
		console.log('Csa');
	});

	setInterval(function(){
		if(!hover){
			$('#slider').flexslider("next");
			console.log('triggered');
		}
	},8000);

	$('#slider').hover(function (){
		hover = true;
	});
	$('#slider').mouseleave(function (){
		hover = false;
	});
	
	/*
	$('#carousel img').hover(function (){
		hover = true;
	});
	$('#carousel img').mouseleave(function (){
		hover = false;
	});
	*/


});
