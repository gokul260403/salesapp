frappe.pages['sales-chart'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Grand Total',
		single_column: true
	});

	let chart_container = $('<div id="realtime-chart" style="height:300px; margin-top:20px;"></div>');
    $(page.main).append(chart_container);
 
    const data = {
        datasets: [
            { name: "Grand Total", values: [] }
        ]
    };
 
    let chart = new frappe.ui.RealtimeChart("#realtime-chart", "sales_update", 10, {
        title: "Live Grand Total",
        data: data,
        type: "line",
        height: 300,
        colors: ["#7cd6fd"]
    });

     
    chart.start_updating();
}