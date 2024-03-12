#!/usr/bin/node
const index = process.argv.length;

// print process.argv
if (index === 2) {
  console.log('No argument');
} else if (index === 3) {
  console.log('argument found');
} else {
  console.log('arguments found');
}
