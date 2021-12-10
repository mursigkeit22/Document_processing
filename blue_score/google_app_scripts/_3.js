
function RawMTvsReference() {

  Logger.log("In RawMTvsReference");
  var app = SpreadsheetApp;
  var ss = app.getActiveSpreadsheet();
  var activeSheet = ss.getActiveSheet();


  var columnReference = activeSheet.getRange('D7:D');
  var valuesReference = columnReference.getValues();
  var arrayReference = []
  for (var row in valuesReference) {
    if (valuesReference[row][0]=== ""){
      break;
    }
    arrayReference.push([[valuesReference[row][0].normalize('NFKD')]])
  }
//  Logger.log(arrayReference)


var columnRawMT = activeSheet.getRange('E7:E');
  var valuesRawMT = columnRawMT.getValues();
  var arrayRawMT = []
  for (var row in valuesRawMT) {
    if (valuesRawMT[row][0]=== ""){
      break;
    }
    arrayRawMT.push([valuesRawMT[row][0].normalize('NFKD')])
  }
//  Logger.log(arrayRawMT)

//пусть первый всегда будет референсом, а второй всегда гипотезой - сразу как при подсчете

payload = {"arrayReference": arrayReference,
           "arrayHypothesis":arrayRawMT,
}


  var options = {
  'method' : 'post',
  'payload' : JSON.stringify(payload),
  'contentType': 'application/json'

};

 //const url = 'https://test.coman.app/rest/envelope/get_number';
 const url = 'https://c3yvglef9f.execute-api.us-east-2.amazonaws.com/default/bleu_print'

 const result = UrlFetchApp.fetch(url, options);
Logger.log(result)
 Logger.log(result.getContentText());
var MTCell = activeSheet.getRange("F3")
MTCell.setValue(result.getContentText())
return result.getContentText();

}
