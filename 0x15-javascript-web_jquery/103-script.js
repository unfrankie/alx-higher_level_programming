$('#btn_translate, #language_code').on('click keypress', function(event) {
    if (event.type === 'keypress' && event.which !== 13) {
        return;
    }
    const langCode = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + langCode, function(data) {
        $('#hello').text(data.hello);
    });
});
