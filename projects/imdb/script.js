
$(document).ready(function(){
	var prev;
	$(".film-url").hover(function(){
		var contents;
		var imdbid=  $(this).parent().attr('id');
		if(prev!=imdbid)
		{
			prev=imdbid;
			$('#mov-info').html();
			var imdburl='http://imdbapi.com/?i='+imdbid;
			$.getJSON('http://whateverorigin.org/get?url=' + encodeURIComponent(imdburl) + '&callback=?', function(data){
			contents=data.contents;
			var ijson = eval("(" + contents + ")");
			icode='<div class="fleft"><img src="';
			if(ijson.Response!="False")
			{
				if(ijson.Poster!="N/A")
					icode+=ijson.Poster;
				else
					icode+="images/noimage.png";
				icode+='" class="posterimg" /></div><div class="rinfo fright"><div class="mov-title">'+ijson.Title+'</div><div class="">Director: '+ijson.Director+'</div>';
				icode+='<div class="">Writer: '+ijson.Writer+'</div>';
				icode+='<div class="">Stars: '+ijson.Actors+'</div>';
				icode+='</div><div class="clear"></div>';
				icode+='Plot: '+ijson.Plot;
			}
			else
				icode+='images/noimage.png" class="posterimg" /></div><div class="mov-title fleft">Not Available</div><div class="clear">'
			$('#mov-info').html(icode);
		   });
		}
		$('#mov-info').removeClass("nodisplay");
		$(this).parent().parent().addClass("film-hov");
	
    },function(){
		$('#mov-info').addClass("nodisplay");
		$(this).parent().parent().removeClass("film-hov");
	});
});