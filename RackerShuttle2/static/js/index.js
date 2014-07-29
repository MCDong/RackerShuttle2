$(function() {
    $(".datepicker").datepicker();

    $.tablesorter.addParser({
        id: 'severity'
    ,   is: function (s) { return false; }
    ,   format: function (s) {
            return s.toLowerCase().replace(/critical/, 0).replace(/high/, 1).replace(/medium/, 2).replace(/low/, 3).replace(/info/, 4);
        }
    ,   type: 'numeric'
    });

    $("#products").tablesorter({
        theme: "bootstrap"
    });
    $("#findings").tablesorter(
    {   theme: "bootstrap"
    ,   headers: {
            1: { sorter: 'severity'}
        }
    ,   sortList: [[1, 0], [0,0]]
    });
});

