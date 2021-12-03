function myFunction() {

  Logger.log("In myFunction");
  var app = SpreadsheetApp;
  var ss = app.getActiveSpreadsheet();
  var activeSheet = ss.getActiveSheet();
  var testColumn = activeSheet.getRange(7, 4,10,1);
  var values = testColumn.getValues();

  let myArray = []
  for (var row in values) {
    for (var col in values[row]) {
      myArray.push(values[row][col])
      // Logger.log(values[row][col]);
  }}

  // Logger.log(myArray)

  var options = {
  'method' : 'post',
  'payload' : JSON.stringify(myArray)
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
