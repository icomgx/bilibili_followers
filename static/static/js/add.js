var looper_time = 0.5 * 1000;
//是否首次执行
var run_once = true;
do_barrager();

function do_barrager() {
    if (run_once) {
        //如果是首次执行,则设置一个定时器,并且把首次执行置为false
        looper = setInterval(do_barrager, looper_time);
        run_once = false;
    }
    //获取
    $.getJSON('MainFunc.ashx?mode=1', function (data) {
        //是否有数据
        if (data.info) {

            $('body').barrager(data);
        }

    });
}               