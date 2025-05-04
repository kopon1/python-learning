#!/bin/bash
# proto-generator2.sh - Reverse-engineers .proto from chat.js

INPUT="chat.js"
OUTPUT="codeium_common2.proto"

# Step 1: Initialize proto with header
echo "syntax = \"proto3\";
package exa.codeium_common2_pb;

// Reverse-engineered from JS structure
// NOT from original .proto files
" > $OUTPUT

# Step 2: Extract message definitions
grep -B 100 -A 50 'typeName = "' $INPUT | awk '
BEGIN { RS="class "; OFS=""; }
/typeName = "/ {
  # Extract class name
  split($1,class_info,"{");
  class = class_info[1];
  gsub(/ extends C/, "", class);
  
  # Get protobuf message name
  split($0, type_parts, "\"");
  proto_name = type_parts[2];
  gsub(/.*\./, "", proto_name);
  
  # Start message
  print "\n// JS Class: " class;
  print "message " proto_name " {";

  # Field extraction
  in_fields = 0;
  for(i=1; i<=NF; i++) {
    if ($i ~ /fields = /) in_fields = 1;
    if (in_fields && $i ~ /no:/) {
      # Parse field metadata
      no = gensub(/.*no: ([0-9]+).*/, "\\1", 1, $i);
      name = gensub(/.*name: "([^"]+).*/, "\\1", 1, $i);
      kind = gensub(/.*kind: "([^"]+).*/, "\\1", 1, $i);
      type = "string";
      
      # Type detection
      if ($i ~ /T: [A-Z]/) type = gensub(/.*T: ([A-Za-z]+).*/, "\\1", 1, $i);
      if ($i ~ /T: 9/) type = "string";
      if ($i ~ /T: 13/) type = "int32";
      if (kind == "message") type = gensub(/.*T: ([A-Za-z]+).*/, "\\1", 1, $i);
      
      # Format output
      printf "  %-12s %-18s = %s;\n", type, name, no;
    }
    if ($i ~ /\]\)/) break;
  }
  print "}";
}' >> $OUTPUT

echo "// Generated at: $(date)" >> $OUTPUT