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
            if(until && until.indexOf(':') != -1) {
                options['until'] = _parseDate(until);
            }

            $countdown.find('.timer').countdown(options);
        }
    }

    function _parseDate(date)
    {
        // new Date(iso8601) doesn't work in IE8.
        var time_pos = date.indexOf(' ');
        var tz_pos = date.lastIndexOf("+");
        var tz = tz_pos == -1 ? null : date.substring(tz_pos + 1);
        var ymd = date.substring(0, time_pos).split('-');
        var hms = date.substring(time_pos + 1, tz_pos == -1 ? date.length : tz_pos).split(':');
        if(tz == "00:00") {
            return new Date(Date.UTC(ymd[0], ymd[1] - 1, ymd[2], hms[0], hms[1], hms[2]));
        }
        else {
            // NOTE: No other timezone support for now. Add it if you need it.
            return new Date(ymd[0], ymd[1] - 1, ymd[2], hms[0], hms[1], hms[2]);
        }
    }

})(jQuery);
