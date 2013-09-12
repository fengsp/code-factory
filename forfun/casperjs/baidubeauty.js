var links = [];
var casper = require('casper').create();

function getLinks() {
    var links = document.getElementsByTagName('img');
    return Array.prototype.map.call(links, function(e) {
        return e.getAttribute('src');
    });
}

function scrollDown() {
    window.scrollTo(0, window.scrollY + 1000);
}

casper.start('http://image.baidu.com/channel#%E7%BE%8E%E5%A5%B3&%E5%85%A8%E9%83%A8&1&0', function() {
    links = this.evaluate(getLinks);
    this.evaluate(scrollDown);
});

for(var i = 0; i < 500; i++) {
    casper.wait(500, function() {
        links = this.evaluate(getLinks);
        this.evaluate(scrollDown);
    });
}

casper.run(function() {
    this.echo(JSON.stringify(links)).exit();
});
