$(document).ready(function () {
    $(function () {
        $('.nav.nav-tabs li a.tabActive').removeClass('tabActive');
        var current =location.pathname;
        $('ul.nav.nav-tabs li.active a').each(function(){
            var $this =$(this);
            if($this.attr('href').indexOf(current) !== -1){
                $this.addClass('tabActive');
            }
        });
    });
});   
