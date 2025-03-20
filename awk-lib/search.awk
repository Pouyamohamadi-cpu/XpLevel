function searchText(text, file_path) {
    cmd = "awk '/" text "/ {print}' " file_path
    system(cmd)
}

BEGIN {
    searchText(example, file)
}