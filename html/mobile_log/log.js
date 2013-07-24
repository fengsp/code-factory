/**
 * Log For Mobile Debug Usage
 * Specified for touch events test
 * Just add one fixed element to the main document
 * Add the thing you want to log
 * @author fsp
 * date: 20130425
 * version: 0.1
 */
//Log begin
var Log = function() {
    var consolew,             // console window
        objectprintfunc,
        initialized = false;
    return {
        init: function(para) {
            consolew = document.createElement('div');
            consolew.style.textAlign = 'center';
            consolew.style.position = 'fixed';
            consolew.style.right = '10px';
            consolew.style.bottom = '10px';
            consolew.style.background = '#000';
            consolew.style.color = '#00ff00';
            //consolew.style.fontWeight = 'normal';
            consolew.style.fontSize = '15px';
            consolew.style.lineHeight = '18px';
            consolew.style.padding = '5px';
            consolew.innerHTML = 'My Console:';
            document.body.appendChild(consolew);
            
            objectprintfunc = para.objectprintfunc
            initialized = para.initialized
        },

        log: function(info) {
            if(!initialized) {alert('Mobile Log 请于文档加载完成后使用...'); return;}
            if(info instanceof Object) {
                info = objectprint(info);
            }
            consolew.innerText = consolew.innerText + "\n" + info;
        }
    };
}();
//Log end


function type(obj){
	switch(obj){
		case null:
			return "null";
		case undefined:
			return "undefined";
	}
	var s=Object.prototype.toString.call(obj);
	switch(s){
		case "[object String]":
			return "string";
		case "[object Number]":
			return "number";
		case "[object Boolean]":
			return "boolean";
		case "[object Array]":
			return "array";
		case "[object Date]":
			return "date";
		case "[object Function]":
			return "function";
		case "[object RegExp]":
			return "regExp";
		case "[object Object]":
			return "object";
		default:
			return "object";
	}
}
function objectprint(object) {
	var returnobject = '';
	if (object instanceof Array) {
		for(var i=0; i<object.length; i++) {
			returnobject += '[' + objectprint(object[i]) + "]";
		}
	} else if (object instanceof Object) {
		for(var o in object) {
			 returnobject += '{' + o + ' : ' + objectprint(object[o]) + '}';
		}
	} else {
		returnobject += object;
	}
    return returnobject;
}
window.addEventListener('DOMContentLoaded', function() { 
    Log.init({
        objectprint: objectprint,
        initialized:     true
    });
    logTest();
}, false);


function logTest() {
    Log.log('fsptest');
    Log.log('fsptest2');
    Log.log('fsptest3');
    Log.log(['array2', ['array3', 'array4']]);
    Log.log({'dictkey1': 'dictvalue1', 'dictkey2': {'dictkey3': 'dictvalue3'}});
    Log.log({'dictkey4': 'dictvalue4'});
}
