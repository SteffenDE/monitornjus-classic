(function($) {
                $(function() { //on DOM ready
                    $("#scroller").simplyScroll({
                        customClass: 'custom',
                        orientation: 'vertical',
                        auto: true,
                        autoMode: 'loop',
                        frameRate: 60,
                        speed: 1,
                        startOnLoad: true,
                        pauseOnHover: false
                    });
                });
            })(jQuery);