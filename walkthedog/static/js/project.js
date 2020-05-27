/* Project specific Javascript goes here. */

$(document).ready(function () {

    $("#phone").mask("+38(099)999-99-99");
    $("#date").mask("99.99.9999", {placeholder: "дд.мм.гггг" });

    $("#time").mask('99:99:99');

    $(".datetimepicker").datetimepicker({
        autoclose: true,
        componentIcon: '.mdi.mdi-calendar',
        navIcons: {
            rightIcon: 'mdi mdi-chevron-right',
            leftIcon: 'mdi mdi-chevron-left'
        },
        startView: 'decade',
        format: 'dd.mm.yyyy',
        //   minDate: (new Date()).getDate(),
        //  maxDate: new Date(new Date().setDate((new Date().getDate()) + 30))
    });
});
