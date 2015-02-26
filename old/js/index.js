$( document ).ready(function (){
	
	$("#immersive_slider").immersive_slider({
	  animation: "bounce", // As usual, you can change the animation to these: slide (default), bounce, fade, slideUp, and bounceUp
	  slideSelector: ".slide", // This option will let you assign custom selector for each slides in case .slide is already taken
	  container: ".main", // This option lets you define the container of which the background will appear. Make sure the slider is inside this container as well.
	  cssBlur: false, // Experimental: In case you don't want to keep adding new data-blurred attributes, trigger this to true and it will generate the blur image on the fly (more info below).
	  pagination: false, // Toggle this to false if you don't want a pagination
	  loop: true, // Toggle to false if you don't want the slider to loop. Default is true.
	  autoStart: 4000 // Define the number of milliseconds before it navigates automatically. Change this to 0 or false to disable autoStart. The default value is 5000.
	});
/*
	$(".head").onepage_scroll({
	   sectionContainer: "section", // sectionContainer accepts any kind of selector in case you don't want to use section
	   easing: "ease-in-out", // Easing options accepts the CSS3 easing animation such "ease", "linear", "ease-in", "ease-out", "ease-in-out", or even cubic bezier value such as "cubic-bezier(0.175, 0.885, 0.420, 1.310)"
	   animationTime: 800, // AnimationTime let you define how long each section takes to animate
	   pagination: true, // You can either show or hide the pagination. Toggle true for show, false for hide.
	   updateURL: false, // Toggle this true if you want the URL to be updated automatically when the user scroll to each page.
	   beforeMove: function(index) {}, // This option accepts a callback function. The function will be called before the page moves.
	   afterMove: function(index) {}, // This option accepts a callback function. The function will be called after the page moves.
	   loop: false // You can have the page loop back to the top/bottom when the user navigates at up/down on the first/last page.
	});

*/


	$('#carousel').flexslider({
	    animation: "slide",
	    controlNav: true,
	    animationLoop: true,
	    slideshow: true,
	    itemWidth: 200,
	    itemMargin: 1,
	    asNavFor: '#slider'
	  });

		$('#slider').flexslider({
	    animation: "slide",
	    controlNav: false,
	    animationLoop: true,
	    slideshow: true,
	    sync: "#carousel"
	});
});