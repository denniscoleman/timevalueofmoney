function validateForm() {

	var p_init = document.forms["calculator"]["p_init"].value
	var p_final = document.forms["calculator"]["p_final"].value
	var rate = document.forms["calculator"]["rate"].value
	var duration = document.forms["calculator"]["duration"].value
	var variables = []
	var alert_string = ''

	if ( p_init == null || p_init == "" || isNaN(p_init)) {
		variables.push( "Starting principal");
	}
	if ( rate == null || rate == "" || isNaN(rate)) {
		variables.push( "Interest rate");
	}
	if ( duration == null || duration == "" || isNaN(duration)) {
		variables.push( "Duration");
	}
	if ( p_final == null || p_final == "" || isNaN(p_final)) {
		variables.push( "Ending principal");
	}

	var count = variables.length
	var count_minus_one = count - 1
	if (count == 0) {
		alert ("You need to leave one field empty. That's the value we will calculate.")
		return false;
	} else if (count > 1) {
		alert_string  = "You need to provide a numeric value for " + count_minus_one + " of the following:\n"
		for (i = 0; i < count; i++) {
			alert_string = alert_string.concat(variables[i])
			if (i == count-2) {
				alert_string = alert_string.concat(" or ")
			} else if (i <= count-3) {
				alert_string = alert_string.concat(", ")
			}
		}
		alert (alert_string)
		return false;
	}
}			  

