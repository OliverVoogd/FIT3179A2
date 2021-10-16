var vg_1 = "js/global_disasters_map.vg.json"
var vg_2 = "js/select_countries_disasters.vg.json"
var vg_3 = "js/disasters_deaths.vg.json"
var vg_4 = "js/line_chart.vg.json"

vegaEmbed("#global_map", vg_1, {"actions": false}).then(function(result) {

}).catch(console.error);

vegaEmbed("#select_countries", vg_2, {"actions": false}).then(function(result) {

}).catch(console.error) 

vegaEmbed("#disasters_deaths", vg_3, {"actions": false}).then(function(result) {

}).catch(console.error)

vegaEmbed("#line_chart", vg_4, {"actions": false}).then(function(result) {

}).catch(console.error)