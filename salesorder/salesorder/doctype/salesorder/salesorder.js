// Copyright (c) 2025, gokul and contributors
// For license information, please see license.txt
 

frappe.ui.form.on("Items", {
	quantity: function(frm, cdt, cdn){
        Price(frm, cdt, cdn);
    },
    rate: function(frm,cdt,cdn){
        Price(frm,cdt,cdn);     
    },
    items_add: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        row.item = "Bat";
        row.rate = 100;
        row.quantity = 1;
        frm.refresh_field("items");
        frappe.msgprint('A row has been added to the items table');
    },
    items_remove(frm,cdt,cdn){
        frappe.msgprint('A row removed');    
    }, 
    before_items_remove(frm,cdt,cdn){
         frappe.msgprint('A row has to remove from the items table');
    },
    items_move(frm,cdt,cdn){
        frappe.msgprint('A row has moved');
    },
    form_render(frm,cdt,cdn){
         frappe.msgprint('form rendered');
    }
});
function Price(frm,cdt,cdn){
    let row =locals[cdt][cdn];
    row.price=row.rate*row.quantity;
    frm.refresh_field("items");

    let total=0; 
    frm.doc.items.forEach(element => {
        total+=element.price
    });
    frm.set_value("total_amount",total);      

}

frappe.ui.form.on("Salesorder", {
    tax: function(frm){
        Tax(frm)
    },
    total_amount: function(frm){
        Tax(frm)
    },
    // refresh:function(frm){
    //     if(frm.doc.outstanding_amount!=0){
    //         frm.add_custom_button("Make Payment",function(){
    //             frappe.new_doc('Payment',{
    //                 sales_order:frm.doc.name,
    //                 payment_date:frappe.datetime.get_today(),
    //                 outstanding_amount:frm.doc.outstanding_amount,
    //             },
                    
    //             )
    //         })
    //     }

    // }
});

function Tax(frm){
    let tax= frm.doc.tax;
        let tax_amount=(frm.doc.total_amount)*(tax/100);
        frm.set_value("tax_amount",tax_amount)
        frm.refresh_field("tax_amount");

        let net_total=frm.doc.total_amount + tax_amount
        frm.set_value("net_total",net_total)
        frm.set_value("outstanding_amount",net_total)
        frm.refresh_field("net_total");
}

