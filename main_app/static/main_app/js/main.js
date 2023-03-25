(function($) {
"use strict";

/*------------------------------------------------------------------
[Table of contents]

custom function
portfolio gird
banner slider
single item slider
number counter and skill bar animation
skill bar and number counter
mega navigation menu init
countdown timer
back to top
insta feed
video popup
image popup
map window opener add class
Code For Switching Style (FOR DEMO)
Contact From dynamic
XpeedStudio multipile Maps
XpeedStudio Maps



-------------------------------------------------------------------*/

$(window).on('load', function() {

	// custom xs function init

	// setTimeout(() => {
	// 	$('#preloader').fadeOut();
	// }, 500);

	/*==========================================================
			portfolio gird
	======================================================================*/
	if($('.xs-portfolio-grid').length >0) {
		var $portfolioGrid = $('.xs-portfolio-grid'),
		colWidth = function () {
		  var w = $portfolioGrid.width(), 
			columnNum = 1,
			columnWidth = 0;
		  if (w > 1200) {
			columnNum  = 3;
		  } else if (w > 900) {
			columnNum  = 3;
		  } else if (w > 600) {
			columnNum  = 2;
		  } else if (w > 450) {
			columnNum  = 2;
		  } else if (w > 385) {
			columnNum  = 1;
		  }
		  columnWidth = Math.floor(w/columnNum);
		  $portfolioGrid.find('.xs-portfolio-grid-item').each(function() {
			var $item = $(this),
			  multiplier_w = $item.attr('class').match(/xs-portfolio-grid-item-w(\d)/),
			  multiplier_h = $item.attr('class').match(/xs-portfolio-grid-item-h(\d)/),
			  width = multiplier_w ? columnWidth*multiplier_w[1] : columnWidth,
			  height = multiplier_h ? columnWidth*multiplier_h[1]*0.4-12 : columnWidth*0.5;
			$item.css({
			  width: width,
			  //height: height
			});
		  });
		  return columnWidth;
		},
		isotope = function () {
		  $portfolioGrid.isotope({
			resizable: false,
			itemSelector: '.xs-portfolio-grid-item',
			masonry: {
			  columnWidth: colWidth(),
			  gutterWidth: 3
			}
		  });
		};
	  isotope();
	  $(window).resize(isotope);
	  } // End is_exists

}); // END load Function 

$(document).ready(function() {


	/*==========================================================
			banner slider
	======================================================================*/
	if ( $( '.xs-banner-slider' ).length > 0 ) {
		var bannerSlider = $( ".xs-banner-slider" );
		bannerSlider.owlCarousel( {
			items: 1,
			loop: true,
			mouseDrag: true,
			touchDrag: true,
			dots: false,
			nav: true,
			navText: ['<i class="fa fa-angle-left xs-round-nav"></i>','<i class="fa fa-angle-right xs-round-nav"></i>'],
			autoplay: false,
			autoplayTimeout: 5000,
			autoplayHoverPause: true,
			animateOut: 'fadeOut',
			animateIn: 'fadeIn',
			responsive : {
				// breakpoint from 0 up
				0 : {
					nav: false,
				},
				// breakpoint from 480 up
				480 : {
					nav: false,
				},
				// breakpoint from 768 up
				991 : {
					nav: true,
				}
			}
		});
	}

	/*==========================================================
				single item slider
	======================================================================*/
	if ( $( '.xs-single-item-slider' ).length > 0 ) {
		var singleItemSlider = $( ".xs-single-item-slider" );
		singleItemSlider.owlCarousel( {
			items: 1,
			loop: true,
			mouseDrag: true,
			touchDrag: true,
			dots: false,
			nav: true,
			navText: ['<i class="fa fa-arrow-left xs-square-nav"></i>','<i class="fa fa-arrow-right xs-square-nav"></i>'],
			autoplay: true,
			autoplayTimeout: 5000,
			autoplayHoverPause: true,
			animateOut: 'fadeOut',
			animateIn: 'fadeIn',
			responsive : {
				// breakpoint from 0 up
				0 : {
					nav: false,
				},
				// breakpoint from 480 up
				480 : {
					nav: false,
				},
				// breakpoint from 768 up
				768 : {
					nav: true,
				}
			}
		});
	}
	

	/*==========================================================
			number counter and skill bar animation
	=======================================================================*/

	var number_percentage = $(".number-percentage");
	function animateProgressBar(){
		number_percentage.each(function() {
		$(this).animateNumbers($(this).attr("data-value"), true, parseInt($(this).attr("data-animation-duration"), 10));
				var value = $(this).attr("data-value");
				var duration = $(this).attr("data-animation-duration");
		$(this).closest('.xs-skill-bar').find('.xs-skill-track').animate({
			width: value + '%'
			}, 4500);
		});
	}


	if ($('.waypoint-tigger').length > 0) {
		var waypoint = new Waypoint({
			element: document.getElementsByClassName('waypoint-tigger'),
			handler: function(direction) {
				animateProgressBar();
			}
		});
	}

	/*==========================================================
			skill bar and number counter
	=======================================================================*/

	$.fn.animateNumbers = function(stop, commas, duration, ease) {
		return this.each(function() {
			var $this = $(this);
			var start = parseInt($this.text().replace(/,/g, ""), 10);
			commas = (commas === undefined) ? true : commas;
			$({
				value: start
			}).animate({
				value: stop
			}, {
				duration: duration == undefined ? 500 : duration,
				easing: ease == undefined ? "swing" : ease,
				step: function() {
					$this.text(Math.floor(this.value));
					if (commas) {
						$this.text($this.text().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,"));
					}
				},
				complete: function() {
					if (parseInt($this.text(), 10) !== stop) {
						$this.text(stop);
						if (commas) {
							$this.text($this.text().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,"));
						}
					}
				}
			});
		});
	};


	/*==========================================================
			mega navigation menu init
	======================================================================*/
	if ($('.xs-menus').length > 0) {
		$('.xs-menus').xs_nav({
			mobileBreakpoint: 992,
		});
	}
	
	/*==========================================================
			countdown timer
	======================================================================*/
	$('.xs-countdown-timer[data-countdown]').each(function() {
		var $this = $(this), 
			finalDate = $(this).data('countdown');

			$this.countdown(finalDate, function(event) {
			var $this = $(this).html(event.strftime(' ' 
			+ '<span class="timer-count">%-D <span class="timer-title">Days</span></span>  ' 
			+ '<span class="timer-count">%H <span class="timer-title">Hours</span></span> ' 
			+ '<span class="timer-count">%M <span class="timer-title">Minutes</span></span> ' 
			+ '<span class="timer-count">%S <span class="timer-title">Secods</span></span>'));
		});
	});

	/*==========================================================
			back to top
	======================================================================*/ 
	$(document).on('click', '.xs-back-to-top', function(event) {
		event.preventDefault();
		/* Act on the event */

		$('html, body').animate({
			scrollTop: 0,
		}, 1000);
	});

	/*=============================================================
					video popup
	=========================================================================*/
	if ($('.xs-video-popup').length > 0) {
		$('.xs-video-popup').magnificPopup({
			disableOn: 700,
			type: 'iframe',
			mainClass: 'mfp-fade',
			removalDelay: 160,
			preloader: false,
			fixedContentPos: false
		});
	}

	/*=============================================================
					image popup
	=========================================================================*/
	$('.xs-image-popup').magnificPopup({
		type: 'image',
		closeOnContentClick: false,
		closeBtnInside: false,
		mainClass: 'mfp-with-zoom mfp-img-mobile',
		gallery: {
			enabled: true
		},
		zoom: {
			enabled: true,
			duration: 300, // don't foget to change the duration also in CSS
		}
		
	});

	/*==========================================================
			map window opener add class
	======================================================================*/
	$(document).on('click', '.xs-window-opener', function() {
		// body...
		event.preventDefault();

		var main_wraper = $('.xs-widnow-wraper'),
			active_class= 'active';

		if ($(this).parent().parent().hasClass(active_class)) {
			$(this).parent().parent().removeClass(active_class);
		} else {
			$(this).parent().parent().addClass(active_class);
		}
	});

}); // end ready function

$(window).on('scroll', function() {

}); // END Scroll Function 

$(window).on('resize', function() {
	
}); // End Resize

})(jQuery);