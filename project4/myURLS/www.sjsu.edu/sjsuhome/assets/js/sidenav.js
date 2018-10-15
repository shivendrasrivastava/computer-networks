$(document).ready(function() {

  var currUrl = window.location.pathname;
  if(currUrl.indexOf("index.html") < 0){
  	currUrl = currUrl + "index.html";
  }

  var currUrl2 = currUrl.substring(0,currUrl.indexOf('index.html'));  // site/folder/folder/
  var currUrl3 = currUrl.substring(0,currUrl.indexOf('/index.html')); // site/folder/folder

  //Hide the two side navs (the current and parent ones)
  $("#childrenNav").hide();
  $("#siblingNav").hide();

/*

currUrl  = /site/folder/folder/index.html
currUrl2 = /site/folder/folder/
currUrl3 = /site/folder/folder

*/

// Step 2: Build parent <ul>
  $(".secnav").append( 
      "<ul class='sn1' role='navigation'></ul>"
  );

// Step 3: Add siblings

  $("ul#siblingNav li a").each(function(){
      $(".secnav ul[class='sn1']").append($(this).parent()); 
  });

// Step 4: Find the current page
  var foundCurrentPage = false;
  var currentPageTitle = $.trim($("h1.pagetitle").text());

  $("ul.sn1 li a").each(function(){
    if($(this).attr("href") == currUrl || $(this).attr("href") == currUrl2 || $(this).attr("href") == currUrl3){
      $(this).parent().addClass('selected');
      foundCurrentPage = true;
    }
  });

// Step 4b: Add new li.selected to ul.sn1, use <title> value for link text
if(!foundCurrentPage){
      $("<li class='selected'></li>").text(currentPageTitle).appendTo($("ul.sn1"));
}


// Step 5: Add a new ul.navexpand to .selected

$("ul.sn1 li.selected").append(
  "<ul class='sn1 navexpand'></ul>"
  );



// Step 6: Add children to li.selected

  $("ul#childrenNav li a").each(function(){
    $(".navexpand").append(
      "<li>"
      +"<a href='" + $(this).attr('href') + "'>"
      + $(this).text() 
      +"</a></li>")
  });

  //Append the new side nav structure to the nav node, with the current parent nav item
/*
  $(".secnav").append(
  	"<ul class='sn1' role='navigation' title='navSiblings'>"
  	+"<li class='selected'>"+ $("ul#siblingNav li").has("a[href='"+currUrl+"']").text() 
  	+"<li class='selected'>"+ $("ul#siblingNav li").has("a[href='"+currUrl2+"']").text() 
  	+"<li class='selected'>"+ $("ul#siblingNav li").has("a[href='"+currUrl3+"']").text() 
    +"<ul class='sn1 navexpand' style='float:none;' title='navChildren'></ul></li>"
  	+"</ul>"
  );

  //Add the current side nav to the proper spot
  $("ul#childrenNav li a").each(function(){
  	$(".navexpand").append(
  		"<li>"
  		+"<a href='" + $(this).attr('href') + "'>"
  		+ $(this).text() 
  		+"</a></li>")
  });

  //Add the other parent nav items
  $("ul#siblingNav li a").each(function(){
  	if($(this).attr("href") != currUrl && $(this).attr("href") != currUrl2 && $(this).attr("href") != currUrl3){
  		$(".secnav ul[class='sn1']").append($(this).parent()); 
  	}
  });
  */
});
