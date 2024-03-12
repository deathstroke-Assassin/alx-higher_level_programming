#!/usr/bin/node
const val = Math.floor(Number(process.argv[2]));
if (isNaN(Number(val))) {
  console.log('Not a number');
} else {
  console.log('My number: %s', val);
}
