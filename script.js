function back() {
        window.location.href = "index.html";
      }
      
              function setCookie(cname, cvalue, exdays) {
                const d = new Date();
                d.setTime(d.getTime() + (exdays*24*60*60*1000));
                let expires = "expires="+ d.toUTCString();
                document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
              }
              
              function getCookie(cname) {
                let name = cname + "=";
                let decodedCookie = decodeURIComponent(document.cookie);
                let ca = decodedCookie.split(';');
                for(let i = 0; i <ca.length; i++) {
                  let c = ca[i];
                  while (c.charAt(0) == ' ') {
                    c = c.substring(1);
                  }
                  if (c.indexOf(name) == 0) {
                    return c.substring(name.length, c.length);
                  }
                }
                return "";
              }
              
              	var numberIsShowing = false;
              
              	function displayNumber() {
              	    if (numberIsShowing) {
              		numberIsShowing = false;
              		document.getElementById('polaroid').src = "polaroid.png";
              	    } else {
              		numberIsShowing = true;
              		document.getElementById('polaroid').src = "polaroid2.png";
              	    }
              	}
              
              	function swapBG() {
              	  document.body.style.backgroundImage = "url('static.gif')";
              
              	  setTimeout(function swapStatic() {
              		var urlChange = "url('bgG" + (Math.floor(Math.random()*4)) + ".gif')";
              
              		while (document.body.style.backgroundImage == urlChange) {
              		    urlChange = "url('bgG" + (Math.floor(Math.random()*4)) + ".gif')";
              		}
              
              	  	document.body.style.backgroundImage = urlChange;
              	  }, 1000);
              
              	  setTimeout(swapBG, 60000);
              	}
              
              	setTimeout(function changeBG() {
              	  var urlStart = "url('bgG" + (Math.floor(Math.random()*4)) + ".gif')";
              
              	  document.body.style.backgroundImage = urlStart;
              
              	  setTimeout(swapBG, 60000);
              
              	  document.body.style.backgroundSize = "cover";
              	  document.body.style.backgroundRepeat = "no-repeat";
              	  document.body.style.zIndex = -100;
                         	setTimeout(function changeBG() {
              	  	  document.getElementById("slideshow2").style.display = "block";
              		  	setTimeout(function changeBG() {
              	  	  		document.getElementById("applicationWindow").style.display = "block";
              		  		setTimeout(function changeBG() {
              	  	  			document.getElementById("content").style.display = "block";
              		  			setTimeout(function changeBG() {
              						document.getElementById("slideshow").style.display = "block";
              					}, 200)
              				}, 200)
              			}, 200)
              		}, 200)
              	}, 2000)
                  
           