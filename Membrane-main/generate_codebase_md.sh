#!/bin/bash
OUT_FILE="MEMBRANE_CODEBASE.md"
echo "# Membrane Application Codebase" > $OUT_FILE
echo "*Generated on $(date)*" >> $OUT_FILE
echo "" >> $OUT_FILE
echo "This document contains the complete current state of the Membrane application code (Frontend React/Vite + Backend FastAPI)." >> $OUT_FILE
echo "" >> $OUT_FILE

append_file() {
    if [ -f "$1" ]; then
        echo "## File: \`$1\`" >> $OUT_FILE
        
        # Get extension for syntax highlighting
        ext="${1##*.}"
        case "$ext" in
            py) lang="python" ;;
            ts|tsx) lang="typescript" ;;
            js|jsx) lang="javascript" ;;
            json) lang="json" ;;
            css) lang="css" ;;
            html) lang="html" ;;
            *) lang="" ;;
        esac

        echo '```'$lang >> $OUT_FILE
        cat "$1" >> $OUT_FILE
        # Ensure there's a newline before the closing backticks
        echo "" >> $OUT_FILE 
        echo '```' >> $OUT_FILE
        echo "" >> $OUT_FILE
        echo "---" >> $OUT_FILE
        echo "" >> $OUT_FILE
    fi
}

echo "Gathering Configuration Files..."
append_file "package.json"
append_file "tsconfig.json"
append_file "vite.config.ts"
append_file "backend/requirements.txt"

echo "Gathering Frontend Files (src/)..."
find src -type f \( -name "*.tsx" -o -name "*.ts" -o -name "*.css" \) | sort | while read filepath; do
    append_file "$filepath"
done

echo "Gathering Backend Files (backend/)..."
find backend -type f -name "*.py" | sort | while read filepath; do
    append_file "$filepath"
done

echo "Done generating $OUT_FILE"
