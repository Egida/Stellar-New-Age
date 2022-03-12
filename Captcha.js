const solveCaptcha = require('hcaptcha-solver');
const EventEmitter = require('events');

var target = process.argv[2];

(async () => {
    try {
      const response = await solveCaptcha(target);
      console.log(response);
      // F0_eyJ0eXAiOiJKV1Q...
    } catch (error) {
      console.log('Error :(');
    }
})();