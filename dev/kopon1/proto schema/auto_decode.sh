#!/bin/bash

# --------------------------------------------------
# >>>>>>>> ONLY MODIFY THIS CONFIG SECTION <<<<<<<<
# --------------------------------------------------
ROOT_MESSAGE_NAME="CodeContextItem"  # Change if different
CHAT_JS="C:\Users\ladla\Desktop\Chat Decoder 2\chat.js"                    # Path to your chat.js
PB_FILE="C:\Users\ladla\Desktop\Chat Decoder 2\chat.pb"                    # Path to your .pb file
MAX_ITERATIONS=10                    # Usually needs 5-10 cycles
# --------------------------------------------------

# Derived configuration (don't modify)
PROTO_FILE="auto_generated.proto"
GENERATED_DIR="generated"
LOG_FILE="proto_gen.log"

# Initialize
mkdir -p "$GENERATED_DIR"
rm -f "$PROTO_FILE" "$GENERATED_DIR"/*_pb2* "$LOG_FILE"

# Find root message class
ROOT_CLASS=$(grep -B1 "typeName = \".*\.$ROOT_MESSAGE_NAME\"" "$CHAT_JS" | grep -oP 'class \K\w+')
[ -z "$ROOT_CLASS" ] && { echo "❌ Root message $ROOT_MESSAGE_NAME not found"; exit 1; }

# Create initial proto file
echo "// Auto-generated Proto File
syntax = \"proto3\";
package codeium;

import \"google/protobuf/timestamp.proto\";

message $ROOT_MESSAGE_NAME {
  // Trigger initial errors
  oneof scope_item {
    File file = 1;
    Directory directory = 2;
  }
  google.protobuf.Timestamp timestamp = 3;
}" > "$PROTO_FILE"

# Processing loop
for ((i=1; i<=MAX_ITERATIONS; i++)); do
  echo -e "\n=== ITERATION $i ===" | tee -a "$LOG_FILE"
  
  # Generate Python code
  protoc --proto_path=. --python_out="$GENERATED_DIR" "$PROTO_FILE" 2> errors.log
  
  # Check completion
  if [ ! -s errors.log ]; then
    echo -e "\n✅ All dependencies resolved!" | tee -a "$LOG_FILE"
    break
  fi

  # Get missing types
  MISSING_TYPES=$(grep -oP '"\\K[^"]+' errors.log | sort | uniq)
  echo "Missing types:" $MISSING_TYPES | tee -a "$LOG_FILE"
  
  # Process each missing type
  while read -r type; do
    echo "Processing $type..." | tee -a "$LOG_FILE"
    
    # Find class for type
    CLASS=$(grep -B1 "typeName = \".*\.$type\"" "$CHAT_JS" | grep -oP 'class \K\w+')
    [ -z "$CLASS" ] && continue
    
    # Add message stub
    echo -e "\nmessage $type {}" >> "$PROTO_FILE"
    
    # Find and add fields (modify field detection as needed)
    grep -A 50 "class $CLASS " "$CHAT_JS" | grep 'this\.' | awk -F'[.=]' '{
      field = $2; 
      gsub(/[ ,]/,"",field);
      type = "string";
      if (field ~ /Count$/) type = "int32";
      if (field ~ /^is_/) type = "bool";
      printf "  %-15s %-20s = %d;\n", type, field, NR;
    }' | sed -i "/message $type {/r /dev/stdin" "$PROTO_FILE"
    
  done <<< "$MISSING_TYPES"
done

# Final test
echo -e "\n=== DECODING TEST ==="
python3 -c "
from generated import auto_generated_pb2
with open('$PB_FILE', 'rb') as f:
    try:
        msg = auto_generated_pb2.$ROOT_MESSAGE_NAME()
        msg.ParseFromString(f.read())
        print('✅ Decoding successful! Message structure:')
        print(msg)
    except Exception as e:
        print('❌ Final error:', str(e))
"

echo -e "\nProcess complete! Review $PROTO_FILE for any remaining 'string' placeholders."