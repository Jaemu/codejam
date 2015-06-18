//Chapter 1, problem 1.1
//Implement an algorithm to determine if a string has all unique characters. 
//What if you can not use additional data structures?

function allUnique(testStr){
	var asciiTable = new Array(255);
	var index = 0;
	var str_index = 0;
	var currentCharCode = 0;
	for(index = 0; index < 256; index++){
		asciiTable[index] = 0;
	}
	for(str_index = 0; str_index < testStr.length; str_index++){
		currentCharCode = testStr.charCodeAt(str_index);
		if(asciiTable[currentCharCode] === 0){
			asciiTable[currentCharCode] = 1;
			continue;
		}
		else{
			return false;
		}
	}
	return true;
}

console.assert(!allUnique('hello'));
console.assert(!allUnique('cBdNee'));
console.assert(!allUnique('abcdefghijklmwnopqrstuvw'));
console.assert(allUnique('helo'));
console.assert(allUnique('abcABC'));
