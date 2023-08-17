#!/usr/bin/node
class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}
}

print () {
	let i = 0;

	while (i < this.width) {
		pattern = '';
		for (let j = 0; j < this.length; j++) {
			pattern += 'X';
		}
		i++;
	}
	console.log(pattern);
}

module.exports = Rectangle;
