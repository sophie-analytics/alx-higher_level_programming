#!/usr/bin/node
if (isNaN(parseInt(process.argv[2], 10)) || process.argv[2] === undefined)
{
    console.log('Not a Number');
}
else
{
    console.log('My number:', parseInt(process.argv[2], 10));
}
