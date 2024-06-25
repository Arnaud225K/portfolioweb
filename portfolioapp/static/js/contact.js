var temp_button_text;

function CustomFormSubmitPost(e){
    var el = $(e);
    temp_button_text = el.text()
    el.attr('disabled', 'disabled').text("").append('<class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>Chargement...');
};

function CustomFormSubmitResponse(e){
    var el = $(e);
    el.removeAttr('disabled').text(temp_button_text);
};

function resetFormcontact() 
{
	$('#contactForm')[0].reset();
};

"use strict";
var FormControls = function () {

    var contact = function () {

        var form = $('#contactForm')
        form.submit(function(event){
            event.preventDefault();
            CustomFormSubmitPost($('#contactForm button[type=submit]'));
            
            // https://developers.google.com/recaptcha/docs/v3
            
            grecaptcha.ready(function() {
              grecaptcha.execute(recaptcha_site_key, {action: ""}).then(function(token) {

                document.getElementById('id_token').value = token;
                
                var formdata = form.serialize() 
                
                $.ajax({
                    url: form.attr("action"),
                    method: form.attr("method"),
                    data: formdata,
                    success: function(json){
                        CustomFormSubmitResponse($('#contactForm button[type=submit]'));
                        Swal.fire({
                            icon: 'success',
                            title: 'Perfect!',
                            text: json["message"],
                            imageUrl: 'https://i.ibb.co/FV4gxd5/logo-arnok-email.png',
                            imageWidth: 300,
                            imageHeight: 100,
                            imageAlt: 'logo sloc',
                            confirmButtonText: 'OK',
                            confirmButtonColor: '#225f1c',
                            });
                        // Reset form
	                    resetFormcontact();
                    },
                    error: function(xhr){
                        CustomFormSubmitResponse($('#contactForm button[type=submit]'));
                        console.log(xhr.status + ": " + xhr.responseText);
                    }
                }) 
              });
            });
        })    
    };
      

    return {
        init: function() { 
            contact();
        }
    };
}();

jQuery(document).ready(function() {     
    FormControls.init();
});

$(function() {
    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
})