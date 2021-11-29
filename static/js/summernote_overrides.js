odoo.define('web_editor.summernote_override', function (require) {

    'use strict';

    var core = require('web.core');
    var editor = require('web_editor.summernote');
    require('summernote/summernote'); // wait that summernote is loaded

    var _t = core._t;
    var options = $.summernote.options;

    // limit style tags
    options.fontSizes = [_t('Default'), 14, 16, 18, 20, 24, 30, 40, 48];

    return $.summernote;
});
