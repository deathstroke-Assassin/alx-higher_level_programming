#!/usr/bin/node
const strng = 'C is fun';
const x = Math.floor(Number(process.argv[2]));
let i;
if (isNaN(Number(x))) {
  console.log('Missing number of occurrences');
}
for (i = 0; i < x; i++) {
  console.log(strng);
}
