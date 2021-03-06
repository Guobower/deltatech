odoo.define('deltatech_pos.screens', function (require) {
"use strict";

var gui = require('point_of_sale.gui');
var screens = require('point_of_sale.screens');
var core = require('web.core');
var QWeb = core.qweb;
var _t = core._t;


var ReceiptScreenWidget = screens['ReceiptScreenWidget'];

var MyReceiptScreenWidget = ReceiptScreenWidget.extend({

    prepare_bf = function(){

        var order = this.pos.get_order();
        var textfile =  '2;'+ moment().format('L LT') + ' '+ order.name+'\r\n';
            textfile = textfile + '2;\r\n';
            textfile = textfile + '2;'+  this.pos.company.name +'\r\n';

        var orderlines = order.get_orderlines();
        for (var i = 0; i < orderlines.length; i++) {
            var orderline = orderlines[i];
            var prod_name = orderline.product.display_name.substring(0,18)
            textfile = textfile +  '1;'+prod_name+';1;1;'+orderline.price*100+';'+orderline.quantity*100000+'\r\n';
            if ( orderline.product.display_name.length>18){
                prod_name_array = array()
                //for start in range(0,len(prod_name),18):
                //    prod_name_array.append(prod_name[start:start+18])

            }

        }
        var paymentlines = order.get_paymentlines();
        for (var i = 0; i < paymentlines.length; i++) {
            var paymentline = paymentlines[i];
            if ( paymentline.cashregister.journal.type == "cash" ){
                textfile = textfile + '5;'+paymentline.amount *100+';1;1;0\r\n'
            }
            else{
                textfile = textfile + '5;'+paymentline.amount *100+';3;1;0\r\n'
            }

        }

        var name = order.name+'.txt'

        // identific butonul
        var a = this.$('#button_print');
        var file = new Blob([textfile], {type: 'application/octet-stream'});
        a.attr({'href' : URL.createObjectURL(file),  'download' : name});
    }

    download: function(text, name, type) {
          var a = this.$('#button_print')
          var file = new Blob([text], {type: type});
          a.attr({'href' : URL.createObjectURL(file),  'download' : name});
    },

});

gui.define_screen({name:'receipt', widget: MyReceiptScreenWidget});

return {
    ReceiptScreenWidget: MyReceiptScreenWidget
};
}