//Write code to reverse a C-Style String. 
//(C-String means that “abcd” is represented as five characters, including the null character.)

//Note - there isn't really a C-style string in javascript.  In chrome, ''.charCodeAt(0) is NaN but '\0'.charCodeAt(0) is 0
//For super noodly weirdness, see what happens with:
//'\r\n\t' == false
//true
//'\r\n\t' === false
//false
//
//
//Moving on...
//Method 1:
function reverseString1(testStr){
	var index = testStr.length;
	var result = [];
	for(index; index>-1; index--){
		result.push(testStr[index]);
	}
	return result;
}

console.assert(reverseString('hello').length === 6);
console.assert(reverseString('hello').join('') === 'olleh');

//Method 2:
function reverseString2(testStr){
	return testStr.split('')
	.reverse()
	.join();
}