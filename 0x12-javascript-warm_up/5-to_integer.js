#!/usr/bin/node
if(Number.parseInt(process.argv[2]) || process.argv[2] === undefined)
{
    console.log('Not a Number');
}
else
{
    console.log('My number:', parseInt(process.argv[2]));
}
