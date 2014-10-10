(function($){

    $.fn.ready(initCountDown);

    function initCountDown() {
        var $countdown = $('.countdown');
        if ($countdown.length) {
            // Take any values from the HTML
            var options = $countdown.data();

            // Convert 'until' value to Date, but support arbitrary other values.
            // Quick way to work around the brokenness of Date.parse() in browsers.
            var until = options['until'];
            if(until && until.indexOf(',') != -1) {
                until = until.split(',');
                options['until'] = new Date(Date.UTC(parseInt(until[0]), parseInt(until[1]) - 1, parseInt(until[2]), parseInt(until[3]), parseInt(until[4]), parseInt(until[5])));
            }

            $countdown.find('.timer').countdown(options);
        }
    }

})(jQuery);
