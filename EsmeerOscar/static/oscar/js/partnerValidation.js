$( document ).ready(function() {
    $("#id_name").attr("data-validation", "length");
    $("#id_name").attr("data-validation-length", "min4");
    $("#id_addresses-0-line1").attr("data-validation", "length");
    $("#id_addresses-0-line1").attr("data-validation-length", "min8");
    $("#id_addresses-0-line4").attr("data-validation", "length");
    $("#id_addresses-0-line4").attr("data-validation-length", "min3");
    $("#id_addresses-0-state").attr("data-validation", "length");
    $("#id_addresses-0-state").attr("data-validation-length", "min2");
    $("#id_addresses-0-postcode").attr("data-validation", "length");
    $("#id_addresses-0-postcode").attr("data-validation-length", "min4");
    $.validate();
});
