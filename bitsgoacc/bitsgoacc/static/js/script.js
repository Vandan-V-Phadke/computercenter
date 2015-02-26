$(document).ready(function() {
    $("a.new_window").attr("target", "_blank");
    $("#pic").load("static/ajax-contents/cssslider.html");

    $(document).ready(function() {
        $("#cmdComputerLab").click(function() {
            $("#pic").load("static/ajax-contents/ccnow.html");
            var stateObj = {
                'page': 'ccnow.html'
            };
            window.history.pushState(stateObj, "Computer Lab | Computer Centre", "index.html?sub=computer-lab");
            return false;
        });


        $("#cmdComputerCentre").click(function() {
            $("#pic").load("static/ajax-contents/computerCentre.html");
            var stateObj = {
                'page': 'computerCentre.html'
            };
            window.history.pushState(stateObj, "Computer Centre | Computer Centre", "index.html?sub=computer-centre");
            return false;
        });


        $("#cmdAudi").click(function() {
            $("#pic").load("static/ajax-contents/audi.html");
            var stateObj = {
                'page': 'audi.html'
            };
            window.history.pushState(stateObj, "Auditorium | Computer Centre", "index.html?sub=auditorium");
            return false;
        });

        $("#cmdTeleHome").click(function() {
            $("#pic").load("static/ajax-contents/tele_home.html");
            var stateObj = {
                'page': 'tele_home.html'
            };
            window.history.pushState(stateObj, "Tele-presence | Computer Centre", "index.html?sub=tele-presence");
            return false;
        });

        $("#cmdHome").click(function() {
            $("#pic").load("static/ajax-contents/cssslider.html");
            var stateObj = {
                'page': 'cssslider.html'
            };
            window.history.pushState(stateObj, "Computer Centre", "index.html");
            return false;
        });

        //$("#cmdpolLab").click(function(){
        //    $("#pic").load("static/ajax-contents/lab_policy.html");
        //});

        //$("#cmdpolNetwork").click(function(){
        //    $("#pic").load("static/ajax-contents/network_policy.html");
        //});

        $("#cmdRequisitionForms").click(function() {
            $("#pic").load("static/ajax-contents/req_forms.html");
            var stateObj = {
                'page': 'req_forms.html'
            };
            window.history.pushState(stateObj, "Requisition Forms | Computer Centre", "index.html?sub=requisition-forms");
            return false;
        });

        $("#cmdSitemap").click(function() {
            $("#pic").load("static/ajax-contents/sitemap.html");
            var stateObj = {
                'page': 'sitemap.html'
            };
            window.history.pushState(stateObj, "Sitemap | Computer Centre", "index.html?sub=sitemap");
            return false;
        });

        $("#cmdLCDServices").click(function() {
            $("#pic").load("static/ajax-contents/lcd_new.html");
            var stateObj = {
                'page': 'lcd_new.html'
            };
            window.history.pushState(stateObj, "LCD | Computer Centre", "index.html?sub=lcd");
            return false;

        });

        $("#cmdFoodOutlets").click(function() {
            $("#pic").load("static/ajax-contents/food-outlet.html");
            var stateObj = {
                'page': 'food-outlet.html'
            };
            window.history.pushState(stateObj, "LCD | Computer Centre", "index.html?sub=food-outlet");
            return false;

        });


        $("#cmdcontactus").click(function() {
            $("#pic").load("static/ajax-contents/contactUs.html");
            var stateObj = {
                'page': 'contactUs.html'
            };
            window.history.pushState(stateObj, "Contact Us | Computer Centre", "index.html?sub=contactus");
            return false;
        });
    });


    jQuery(".content").hide();
    //toggle the componenet with class msg_body
    jQuery(".CSSTableGenerator").click(function() {
        jQuery(this).next(".content").slideToggle(500);
    });

    var ajax_page_map = {
        'computer-centre': 'computerCentre.html',
        'computer-lab': 'ccnow.html',
        'auditorium': 'audi.html',
        'tele-presence': 'tele_home.html',
        'lcd': 'lcd_new.html',
        'requisition-forms': 'req_forms.html',
        'sitemap': 'sitemap.html',
        'contactus': 'contactUs.html',
        'food-outlet': 'food-outlet.html',
        'audi-booking': 'audi_booking_form.html'
    };

    function getQueryParams(qs) {
        qs = qs.split("+").join(" ");

        var params = {},
            tokens,
            re = /[?&]?([^=]+)=([^&]*)/g;

        while (tokens = re.exec(qs)) {
            params[decodeURIComponent(tokens[1])] = decodeURIComponent(tokens[2]);
        }

        return params;
    }
    var query = getQueryParams(document.location.search);

    if (query.sub in ajax_page_map) {
        $("#pic").load("static/ajax-contents/" + ajax_page_map[query.sub]);
    }

});

window.onpopstate = function(event) {
    if (event.state == null) {
        $("#pic").load("static/ajax-contents/cssslider.html");
        return;
    }
    $("#pic").load("static/ajax-contents/" + event.state.page);
};