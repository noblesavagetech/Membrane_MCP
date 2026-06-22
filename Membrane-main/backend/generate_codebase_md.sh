#!/bin/bash
OUTPUT="MEMBRANE_CODEBASE.md"

echo "# Membrane Codebase" > $OUTPUT
echo "" >> $OUTPUT

# Exclude list
EXCLUDE=(
    "node_modules"
    "dist"
    ".git"
    "__pycache__"
    "data"
    "MEMBRANE_CODEBASE.md"
    "generate_codebase_md.sh"
    "test_db.py"
    "test_post.py"
    "fix_components4.sh"
    "update_api_base.js"
)

# Build find prune string
PRUNE_STR=""
for EX in "${EXCLUDE[@]}"; do
    PRUNE_STR="$PRUNE_STR -name '$EX' -prune -o"
done

# Find all relevant files and append them to the markdown file
eval "find . $PRUNE_STR -type f \( -name '*.ts' -o -name '*.tsx' -o -name '*.py' -o -name '*.json' -o -name '*.css' -o -name '*.html' \) -print" | sort | while read -r FILE; do
    echo "Processing $FILE"
    echo "## \`$FILE\`" >> "$OUTPUT"
    
    # Determine the extension for markdown syntax highlighting
    EXT="${FILE##*.}"
    if [ "$EXT" = "tsx" ] || [ "$EXT" = "ts" ]; then
        LANG="typescript"
    elif [ "$EXT" = "py" ]; then
        LANG="python"
    elif [ "$EXT" = "json" ]; then
        LANG="json"
    elif [ "$EXT" = "css" ]; then
        LANG="css"
    elif [ "$EXT" = "html" ]; then
        LANG="html"
    else
        LANG=""
    fi

    echo "\`\`\`$LANG" >> "$OUTPUT"
    cat "$FILE" >> "$OUTPUT"
    echo "\`\`\`" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
done

echo "Done generating $OUTPUT"
