/**
 * Created by Martin on 06.04.2016.
 */
function add_debtor_line() {
    $('#id_debtor_name').material_select('destroy');
    var counter = $('#purchase_form').find('.layout-row').length;
    var elem = $('#purchase_form').find('.layout-row').first().clone();
    var debtor_name = $(elem).find('#id_debtor_name');
    var debt_amount = $(elem).find('#id_debt_amount');

    debtor_name.attr('id', debtor_name.attr('id')+counter);
    debtor_name.attr('name', debtor_name.attr('name')+counter);
    debt_amount.attr('id', debt_amount.attr('id')+counter);
    debt_amount.attr('name', debt_amount.attr('name')+counter);
    debt_amount.val('');
    
    var debt_amount_container = elem.find('#id_debt_amount_container');
    debt_amount_container.find('.active').removeClass('active');
    debt_amount_container.attr('id', debt_amount_container.attr('id')+counter);
    var debt_amount_label = debt_amount_container.find('label');
    debt_amount_label.attr('for', debt_amount_label.attr('for')+counter);

    $('#purchase_form').find('.layout-row').last().after(elem);

    $('#id_debtor_name').material_select();
    $('#id_debtor_name'+counter).material_select();

    $('#id_debt_count').val(counter);
}

function claim_paid(which) {
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        type:"POST",
        url:"kaffeekasse/claim_paid/",
        data: {
            'id': which
        },
        success: function(answer) {
            Materialize.toast(answer.msg, 5000, 'alert-success');
            console.log(answer.success);
            if( answer.success == true ) {
                $('#claim_link_' + answer.id).after('<i class="mdi-navigation-check small green-text"></i>').remove();
            }
        }
    });
}

function show_all_debts() {
    $('.debts').find('.closed').show();
    $('.debt-show-button').hide();
    $('.debt-hide-button').show();
}

function hide_all_debts() {
    $('.debts').find('.closed').hide();
    $('.debt-hide-button').hide();
    $('.debt-show-button').show();
}

function show_all_claims() {
    $('.claims').find('.closed').show();
    $('.claims-show-button').hide();
    $('.claims-hide-button').show();
}

function hide_all_claims() {
    $('.claims').find('.closed').hide();
    $('.claims-hide-button').hide();
    $('.claims-show-button').show();
}

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

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}