#by pouya mohamadi for xplevel
#file manager center
function deleteFile(file_path) {
    cmd = "rm -f " file_path
    system(cmd)  # اجرای دستور برای حذف فایل
}

BEGIN {
    # گرفتن آرگومان از خط فرمان
    if (ARGC > 1) {
        file_path = ARGV[1]
        deleteFile(file_path)
    } else {
        print "Error: No file path provided."
    }
}