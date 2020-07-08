function clicked_img(img){
          console.log(img.src);

          var top=document.getElementById('top')

          top.src = img.src;

          top.hidden=false;

          if (img.naturalWidth<screen.width*0.6 && img.naturalHeight<screen.height*0.6) {

            top.width=img.naturalWidth;
            top.height=img.naturalHeight;

          } else {

            top.width=screen.width*0.6;
            top.height=img.naturalHeight/img.naturalWidth*top.width;

          }
 }
