#!/bin/bash

# تعریف توابع
xple_bashonmainfunction_ls() {
    ls "$1"
}

xple_bashonmainfunction_cd() {
    cd "$1" || echo "مسیر موجود نیست."
}

xple_bashonmainfunction_rm() {
    rm -r "$1"
}

xple_bashonmainfunction_cp() {
    cp -r "$1" "$2"
}

xple_bashonmainfunction_cp_f() {
    cp "$1" "$2"
}

xple_bashonmainfunction_killid() {
    kill "$1"
}

xple_bashonmainfunction_killid2() {
    kill -s SIGSTOP "$1"
}

xple_bashonmainfunction_killid3() {
    kill -s SIGCONT "$1"
}

xple_bashonmainfunction_killinfo() {
    kill -l
}

xple_bashonmainfunction_lsl() {
    ls -l
}

xple_bashonmainfunction_makedir() {
    mkdir "$1"
}

xple_bashonmainfunction_tourch() {
    touch "$1"
}

xple_bashonmainfunction_ps_aux() {
    ps aux
}

xple_bashonmainfunction_top() {
    top
}

xple_bashonmainfunction_jobs() {
    jobs
}

xple_bashonmainfunction_fg() {
    fg "$1"
}

xple_bashonmainfunction_read() {
    read -p $1 txt
}

xple_bashonmainfunction_unset() {
    unset "$1"
}

xple_bashonmainfunction_sleep() {
    sleep "$1"
}

xple_bashonmainfunction_own() {
    "$1" "$2"
}

xple_bashonmainfunction_tar() {
    tar -czvf "$1" "$2"
}

xple_bashonmainfunction_du() {
    du -sh "$1"
}

xple_bashonmainfunction_df() {
    df -h
}

xple_bashonmainfunction_ping() {
    ping -c 4 "$1"
}

xple_bashonmainfunction_curl() {
    curl "$1"
}

xple_bashonmainfunction_shotdown() {
    sudo shutdown -h now
}

xple_bashonmainfunction_uptime() {
    uptime
}

xple_bashonmainfunction_shatdownintime() {
    sudo shutdown -h "$1"
}

xple_bashonmainfunction_poweroff() {
    sudo poweroff
}

xple_bashonmainfunction_reboot() {
    sudo reboot
}

xple_bashonmainfunction_freeh() {
    free -h
}

xple_bashonmainfunction_lscpu() {
    lscpu
}

xple_bashonmainfunction_wc_l() {
    wc -l "$1"
}

xple_bashonmainfunction_wc_w() {
    wc -w "$1"
}

xple_bashonmainfunction_stat() {
    stat "$1"
}

xple_bashonmainfunction_vmstat() {
    vmstat
}
xple_bashonmainfunction_freq() {
  lscpu | awk '/CPU max MHz/ {print $NF}'
}
xple_bashonmainfunction_uame() {
  uname -a
}
# مدیریت دستورات با case
case "$1" in
    "xple_bashonmainfunction_uame")
        xple_bashonmainfunction_uame
        ;;
    "xple_bashonmainfunction_freq")
        xple_bashonmainfunction_freq
        ;;
    "xple_bashonmainfunction_ls")
        xple_bashonmainfunction_ls "$2"
        ;;
    "xple_bashonmainfunction_cd")
        xple_bashonmainfunction_cd "$2"
        ;;
    "xple_bashonmainfunction_rm")
        xple_bashonmainfunction_rm "$2"
        ;;
    "xple_bashonmainfunction_cp")
        xple_bashonmainfunction_cp "$2" "$3"
        ;;
    "xple_bashonmainfunction_cp_f")
        xple_bashonmainfunction_cp_f "$2" "$3"
        ;;
    "xple_bashonmainfunction_killid")
        xple_bashonmainfunction_killid "$2"
        ;;
    "xple_bashonmainfunction_killid2")
        xple_bashonmainfunction_killid2 "$2"
        ;;
    "xple_bashonmainfunction_killid3")
        xple_bashonmainfunction_killid3 "$2"
        ;;
    "xple_bashonmainfunction_killinfo")
        xple_bashonmainfunction_killinfo
        ;;
    "xple_bashonmainfunction_lsl")
        xple_bashonmainfunction_lsl
        ;;
    "xple_bashonmainfunction_makedir")
        xple_bashonmainfunction_makedir "$2"
        ;;
    "xple_bashonmainfunction_tourch")
        xple_bashonmainfunction_tourch "$2"
        ;;
    "xple_bashonmainfunction_ps_aux")
        xple_bashonmainfunction_ps_aux
        ;;
    "xple_bashonmainfunction_top")
        xple_bashonmainfunction_top
        ;;
    "xple_bashonmainfunction_jobs")
        xple_bashonmainfunction_jobs
        ;;
    "xple_bashonmainfunction_fg")
        xple_bashonmainfunction_fg "$2"
        ;;
    "xple_bashonmainfunction_read")
        xple_bashonmainfunction_read
        ;;
    "xple_bashonmainfunction_unset")
        xple_bashonmainfunction_unset "$2"
        ;;
    "xple_bashonmainfunction_sleep")
        xple_bashonmainfunction_sleep "$2"
        ;;
    "xple_bashonmainfunction_own")
        xple_bashonmainfunction_own "$2" "$3"
        ;;
    "xple_bashonmainfunction_tar")
        xple_bashonmainfunction_tar "$2" "$3"
        ;;
    "xple_bashonmainfunction_du")
        xple_bashonmainfunction_du "$2"
        ;;
    "xple_bashonmainfunction_df")
        xple_bashonmainfunction_df
        ;;
    "xple_bashonmainfunction_ping")
        xple_bashonmainfunction_ping "$2"
        ;;
    "xple_bashonmainfunction_curl")
        xple_bashonmainfunction_curl "$2"
        ;;
    "xple_bashonmainfunction_shotdown")
        xple_bashonmainfunction_shotdown
        ;;
    "xple_bashonmainfunction_uptime")
        xple_bashonmainfunction_uptime
        ;;
    "xple_bashonmainfunction_shatdownintime")
        xple_bashonmainfunction_shatdownintime "$2"
        ;;
    "xple_bashonmainfunction_poweroff")
        xple_bashonmainfunction_poweroff
        ;;
    "xple_bashonmainfunction_reboot")
        xple_bashonmainfunction_reboot
        ;;
    "xple_bashonmainfunction_freeh")
        xple_bashonmainfunction_freeh
        ;;
    "xple_bashonmainfunction_lscpu")
        xple_bashonmainfunction_lscpu
        ;;
    "xple_bashonmainfunction_wc_l")
        xple_bashonmainfunction_wc_l "$2"
        ;;
    "xple_bashonmainfunction_wc_w")
        xple_bashonmainfunction_wc_w "$2"
        ;;
    "xple_bashonmainfunction_stat")
        xple_bashonmainfunction_stat "$2"
        ;;
    "xple_bashonmainfunction_vmstat")
        xple_bashonmainfunction_vmstat
        ;;
    *)
        echo "دستور نامعتبر است."
        ;;
esac