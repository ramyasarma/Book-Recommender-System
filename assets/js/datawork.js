

//receive data whe submit is pressed
document.getElementById("submit1").addEventListener("click", getData);

//document.getElementById("single").addEventListener("click", chooseOne);

function getData(){
	// var g = document.getElementById("genre").value;
 //    var a = document.getElementById("author").value;
 //    var r = document.getElementById("ratings").value;

 console.log("genre weight: "+ genre_wt);
 console.log("author weight: "+ author_wt);
 console.log("ratings weight: "+ ratings_wt);


// var radios = document.forms["singleform"].elements["feature"];
// for(var i = 0, max = radios.length; i < max; i++) {
//     radios[i].onclick = function() {
//         console.log(this.value);
//     }
// }

// function chooseOne(){
// 	console.log("hello");

// }

var arguments = {'user_id' : 1, 'genre_wt' : genre_wt, 'author_wt' : author_wt, 'ratings_wt' : ratings_wt};
    var data_received;
    var new_books={};


    $.ajax({
      type    : 'POST', // define the type of HTTP verb we want to use (POST for our form)
      url     : 'recompute.php', // the url where we want to POST
      data    : arguments, // our data object
      dataType  : 'json', // what type of data do we expect back from the server
      encode    : true,
      //so that we ca access variables declared outside
      async: false,

      success : function(data){

      	//console.log("hello");
        data_received = JSON.parse(data);
        console.log(data_received);

        for(var i=0;i<5;i++){
          new_books[i] = {"bid":0,"titlex":"",
                              "author":"","image":""};
          new_books[i].bid=data_received[i]['book_id'];
          //console.log(data_received[i]['book_id']);
          new_books[i].titlex=data_received[i]['title'];
          new_books[i].author = data_received[i]['authors'];
          new_books[i].image = data_received[i]['image_url'];
          //console.log(initial_books[i])
        }

      }
    });

        //console.log(new_books);
        //document.getElementById("imageid").src="../template/save.png";

        document.getElementById('a1').getElementsByTagName('h2')[0].innerHTML = new_books[0].titlex;
        document.getElementById('a1').getElementsByTagName('h3')[0].innerHTML = new_books[0].author;
        document.getElementById('a1').getElementsByTagName('img')[0].src = new_books[0].image;

        document.getElementById('a2').getElementsByTagName('h2')[0].innerHTML = new_books[1].titlex;
        document.getElementById('a2').getElementsByTagName('h3')[0].innerHTML = new_books[1].author;
        document.getElementById('a2').getElementsByTagName('img')[0].src = new_books[1].image;

        document.getElementById('a3').getElementsByTagName('h2')[0].innerHTML = new_books[2].titlex;
        document.getElementById('a3').getElementsByTagName('h3')[0].innerHTML = new_books[2].author;
        document.getElementById('a3').getElementsByTagName('img')[0].src = new_books[2].image;

        document.getElementById('a4').getElementsByTagName('h2')[0].innerHTML = new_books[3].titlex;
        document.getElementById('a4').getElementsByTagName('h3')[0].innerHTML = new_books[3].author;
        document.getElementById('a4').getElementsByTagName('img')[0].src = new_books[3].image;

        document.getElementById('a5').getElementsByTagName('h2')[0].innerHTML = new_books[4].titlex;
        document.getElementById('a5').getElementsByTagName('h3')[0].innerHTML = new_books[4].author;
        document.getElementById('a5').getElementsByTagName('img')[0].src = new_books[4].image;



    }
