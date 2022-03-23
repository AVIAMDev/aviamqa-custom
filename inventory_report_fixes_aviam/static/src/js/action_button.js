odoo.define('inventory_report_fixes_aviam.ListController', function (require) {
    "use strict";
    var ListController = require('web.ListController');
    const core = require('web.core');
    const _t = core._t;
    ListController.include({
        
        renderButtons: function($node) {
        this._super.apply(this, arguments);
            if (this.$buttons) {
              this.$buttons.find('.oe_action_change_style').click(this.proxy('action_elements')) ;
            }
        },
        action_elements: function () {
            var self =this
            self.do_action({
                name: _t('Wizard Inventary Report'),
                type: 'ir.actions.act_window',
                res_model: 'inventary.report.wizard',
                views: [[false,'form']],
                view_mode: 'form',
                target: 'new',
            });
        },
    })
});