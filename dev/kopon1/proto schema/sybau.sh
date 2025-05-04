function get_fields() {
    grep -A 30 "class $1 " chat.js | grep 'this\.' | awk -F'[ .=]' '{
        field = $2; 
        gsub(/,/, "", field);
        print "  // UNKNOWN_TYPE " field " = X;"
    }'
}

# Example: Get fields for class "di"
get_fields di