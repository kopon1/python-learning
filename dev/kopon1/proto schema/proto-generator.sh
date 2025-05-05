#!/bin/bash
# proto-generator.sh - Generates concise reverse-engineered .proto schema from chat.js

INPUT="chat.js"
OUTPUT="codeium_common.proto"

# Initialize proto file with header
echo "syntax = \"proto3\";
package exa.codeium_common_pb;

import \"google/protobuf/timestamp.proto\";

// Auto-generated from $INPUT - Critical messages only
// DO NOT EDIT MANUALLY - Reverse-engineered structure
" > $OUTPUT

# Extract critical message definitions matching Context, File, Repo, Knowledge
awk '
BEGIN { RS = "\nclass "; FS = "\n" }
/typeName = "exa.codeium_common_pb.(Context|File|Repo|Knowledge)/ {
    # Extract proto message name
    match($0, /"exa.codeium_common_pb.([^"]+)"/, arr);
    proto_name = arr[1];

    # Start message definition
    printf "\nmessage %s {\n", proto_name;

    # Extract fields
    in_fields = 0;
    for(i=1; i<=NF; i++) {
        if ($i ~ /fields = /) in_fields = 1;
        if (in_fields && $i ~ /no:/) {
            no = gensub(/.*no: ([0-9]+).*/, "\\1", 1, $i);
            name = gensub(/.*name: \"([^\"]+)\".*/, "\\1", 1, $i);
            kind = "string";
            # Detect type
            if ($i ~ /kind: \"message\"/) {
                match($i, /T: ([A-Za-z]+)/, tarr);
                kind = tarr[1]
            } else if ($i ~ /T: 9/) {
                kind = "string"
            } else if ($i ~ /T: 13/) {
                kind = "int32"
            } else if ($i ~ /T: 8/) {
                kind = "bool"
            }
            # Handle repeated (optional)
            repeated = ($i ~ /repeated: !0/) ? "repeated " : ""
            printf "  %s%s %s = %s;\n", repeated, kind, name, no
        }
        if ($i ~ /\]\)/) break;
    }
    print "}";
}
' "$INPUT" >> "$OUTPUT"

echo -e "\n// Reverse-engineering complete! (~400-600 lines expected)\n// Compile with: protoc --python_out=. $OUTPUT" >> $OUTPUT