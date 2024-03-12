#!/usr/bin/node
const val = process.argv;
// print process.argv

if (val[2] === undefined) {
  console.log('No argument');
} else {
  console.log(val[2]);
}
