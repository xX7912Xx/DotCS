#! /usr/bin/env node
const child_process=require("child_process");
const fs=require("fs");

let output=child_process.execSync(`nm ${process.argv[2]} -U --extern-only -D`);
let output_lines=output.toString().split("\n");
let output_file="";
let output_map="";
let mapping={};
for(let i of output_lines) {
	let s=i.split(" ");
	let mappart=(i.indexOf("@")==-1)?null:s[2].split("@@")[1];
	if(mappart) {
		s[2]=s[2].split("@@")[0];
	}
	if(s[1]=="T") {
		output_file+=`void ${s[2]}() {}\n`;
	}else if(s[1]=="B") {
		output_file+=`const void *${s[2]};\n`;
	}else if(s[1]=="D") {
		output_file+=`int ${s[2]};\n`;
	}else{
		continue;
	}
	if(mappart) {
		if(!mapping[mappart]) {
			mapping[mappart]=[];
		}
		mapping[mappart].push(s[2]);
	}
}
for(let i in mapping) {
	output_map+=`${i} {\nglobal:\n`;
	for(let s of mapping[i]) {
		output_map+=`${s};\n`;
	}
	output_map+=`};\n\n`;
}
fs.writeFileSync("stub.c", output_file);
if(output_map) {
	fs.writeFileSync("stub.map", output_map);
}