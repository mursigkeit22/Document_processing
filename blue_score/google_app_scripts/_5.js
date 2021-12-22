function callBleuScript(colReferenceLetter, colHypothesisLetter, cell) {
  Logger.log("In callBlueScript");

  var activeSheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();



  var columnReference = activeSheet.getRange(`${colReferenceLetter}7:${colReferenceLetter}`);
  var valuesReference = columnReference.getValues();

  var columnHypothesis = activeSheet.getRange(`${colHypothesisLetter}7:${colHypothesisLetter}`);
  var valuesHypothesis = columnHypothesis.getValues();


  var arrayReference = []
  var arrayHypothesis = []

  Logger.log("length: " + valuesHypothesis.length);

  for (let i = 0; i < valuesHypothesis.length; i++) {
    if ((valuesReference[i][0] !== "") && (valuesHypothesis[i][0] !== "")) {

      arrayReference.push(valuesReference[i][0].normalize('NFKD'))
      arrayHypothesis.push(valuesHypothesis[i][0].normalize('NFKD'))

    }


  }

  payload = {
    "arrayReference": arrayReference,
    "arrayHypothesis": arrayHypothesis
  }


  var options = {
    'method': 'post',
    'payload': JSON.stringify(payload),
    'contentType': 'application/json'

  }
  //const url = 'https://c3yvglef9f.execute-api.us-east-2.amazonaws.com/default/bleu_print'
  const url = 'https://rr09psiowf.execute-api.us-east-2.amazonaws.com/default/bleu_score'
  const result = UrlFetchApp.fetch(url, options);
  // Logger.log(result.getContentText());

  var MTCell = activeSheet.getRange(cell)
  MTCell.setValue(result.getContentText())

  return result.getContentText();

}
