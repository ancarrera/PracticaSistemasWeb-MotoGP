//<!--
 $(function() {
            $.getJSON("/static/json/circuits.json", {}, function (circuits) {
                $("#id_debut_circuit").autocomplete({
                    source: circuits,
                     minLength: 1,

                });
            });
        });

$(document).ready( function(){ 
$("#id_representative_company").autocomplete({
                source: function( request, response ) {
                    $.ajax({
                        type: 'GET',
                        url: "http://api.climatecounts.org/1/Companies.json?Search="+request.term+"&IncludeBrands=True",
                        dataType: "jsonp",

                        data: {
                            format:'json',
                        },
                        minLength: 2,
                        success: function( data ) {
                                   
                            response( $.map( data.Companies, function( item ) {
                               
                                return {
                                    label: item.Name, 
                                    value: item.Name,
                                }
                            }));
                        } 
                    });
                },
                
                select: function( event, ui ) {
                    if (ui.item) {
                        $("#id_representative_company").val(ui.item.Name);
                    }
                }
            });
    });
//-->
