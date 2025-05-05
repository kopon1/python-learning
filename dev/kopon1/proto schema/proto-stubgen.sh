#!/bin/bash
# proto-stubgen.sh
INPUT=${1:-class-type-map.txt}

echo "syntax = \"proto3\";"
echo "package codeium;"
echo "import \"google/protobuf/timestamp.proto\";\n"

awk -F'"' '
BEGIN {
    print "// Auto-generated stubs (verify field types!)"
}
NR%2==1 {
    class = $2
}
NR%2==0 {
    type = $2
    gsub(/.*\./, "", type)
    print "message " type " {\n    // Class: " class "\n}\n"
}
' "$INPUT"