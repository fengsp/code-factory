var PULL = function() {
  var content,
      pullToRefresh,
      message,
      success, 
      start, 
      cancel,
      startY,
      track = false,
	  refresh = false;

  var removeTransition = function() {
    content.style['-webkit-transition-duration'] = 0;
  };
  
  var setHeight = function(height) {
	  content.style.webkitTransform = 'translate3d(0,'+height+'px,0) scale3d(1,1,1)';
	  //content.style.webkitTransform = 'translate(0,'+height+'px)';
	  //content.style.top = height+"px";
  };

  return {
    init: function(o) {
      content = document.getElementById('window');
      pullToRefresh = document.getElementById('pull_refresh_icon');
	  message = document.getElementById('message');
      success = o.success;
      start = o.start;
      cancel = o.cancel;
	  
      document.body.addEventListener('touchstart', function(e) {
        startY = e.touches[0].screenY;
      });

      document.body.addEventListener('touchend', function(e) {
		
        if(refresh) {
          content.style['-webkit-transition-duration'] = '.5s';
          setHeight(0);
		  pullToRefresh.className = 'loading';
		  message.className = 'loading_msg';

          success(function() { // pass down done callback
			setHeight(0);
			pullToRefresh.className = 'arrow_up';
			message.className = 'arrow_up_msg';
            content.addEventListener('transitionEnd', removeTransition);
          });

          refresh = false;
        } else if(track) {
          content.style['-webkit-transition-duration'] = '.25s';
          setHeight(0);
          content.addEventListener('transitionEnd', removeTransition);

          cancel();
        }

        track = false;
		
      });

      document.body.addEventListener('touchmove', function(e) {
		   
		var touchMoved = e.changedTouches[0].screenY - startY;
        var move_to = touchMoved * 0.4; 
		var is_bottom = window.scrollY >= document.body.clientHeight - 
						document.documentElement.clientHeight - 5;
				
        if(is_bottom && touchMoved < 0) 
		{   
			e.preventDefault();
			track = true; // start tracking if near the bottom 
			
        	setHeight(move_to);

        	if(move_to < -50) {
			  pullToRefresh.className = 'arrow_down';
			  message.className = 'arrow_down_msg';
          	  refresh = true;
        	} else {
          	  content.style['-webkit-transition'] = '';
          	  refresh = false;
        	}
		}
      });
    }
  };
}();

