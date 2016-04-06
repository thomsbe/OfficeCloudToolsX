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