"use strict";
$(document).ready(function() {
    // =========================================================
    // =========    Menu Customizer [ HTML ] code   ============
    // =========================================================
    $('body').append('' +
        '<div id="styleSelector" class="menu-styler">' +
            '<div class="style-toggler">' +
                '<a href="#!"></a>' +
            '</div>' +
            '<div class="style-block">' +
                '<h6 class="mb-2">Dasho Live Menu Customizer</h6>' +
                '<hr class="my-0">' +
                '<h6>Layouts</h6>' +
                '<div class="theme-color layout-type">' +
                    '<a href="#!" class=" active" data-value="menu-dark" title="Default Layout"><span></span><span></span></a>' +
                    '<a href="#!" class="" data-value="menu-light" title="Light"><span></span><span></span></a>' +
                    '<a href="#!" class="" data-value="dark" title="Dark"><span></span><span></span></a>' +
                    '<a href="#!" class="" data-value="reset" title="Reset">Reset to Default</a>' +
                '</div>' +
                '<p class="f-12 mb-1"><span class="text-c-red">*</span> in Prebuild Layout you redirect to new page</p>' +
                '<div class="form-group mb-3">' +
                    '<div class="switch switch-primary d-inline m-r-10">' +
                        '<input type="checkbox" id="icon-colored">' +
                        '<label for="icon-colored" class="cr"></label>' +
                    '</div>' +
                    '<label>Icon Color</label>' +
                '</div>' +
                '<ul class="nav nav-pills mb-2" id="pills-cust-tab" role="tablist">' +
                    '<li class="nav-item">' +
                        '<a class="nav-link active" id="pills-color-tab" data-bs-toggle="pill" href="#pills-color" role="tab" aria-controls="pills-color" aria-selected="true">Color</a>' +
                    '</li>' +
                    '<li class="nav-item">' +
                        '<a class="nav-link" id="pills-pages-tab" data-bs-toggle="pill" href="#pills-pages" role="tab" aria-controls="pills-pages" aria-selected="false">Layout</a>' +
                    '</li>' +
                    '<li class="nav-item">' +
                        '<a class="nav-link" id="pills-extra-tab" data-bs-toggle="pill" href="#pills-extra" role="tab" aria-controls="pills-extra" aria-selected="false">Extra</a>' +
                    '</li>' +
                '</ul>' +
                '<div class="tab-content" id="pills-cust-tabContent">' +
                    '<div class="tab-pane fade show active" id="pills-color" role="tabpanel" aria-labelledby="pills-color-tab">' +
                        '<h6>header background</h6>' +
                        '<div class="theme-color header-color">' +
                            '<a href="#!" class=" active" data-value="header-default"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="header-blue"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="header-red"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="header-purple"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="header-info"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="header-dark"><span></span><span></span></a>' +
                        '</div>' +
                        '<h6>Menu Brand Color</h6>' +
                        '<div class="theme-color brand-color">' +
                            '<a href="#!" class=" active" data-value="brand-default"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="brand-blue"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="brand-red"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="brand-purple"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="brand-info"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="brand-dark"><span></span><span></span></a>' +
                        '</div>' +
                        '<h6>Menu background</h6>' +
                        '<div class="theme-color navbar-color">' +
                            '<a href="#!" class=" active" data-value="navbar-default"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="navbar-blue"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="navbar-red"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="navbar-purple"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="navbar-info"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="navbar-dark"><span></span><span></span></a>' +
                        '</div>' +
                        '<h6>Menu background [ Gradient ]</h6>' +
                        '<div class="theme-color navbar-gradient-color">' +
                            '<a href="#!" class=" active" data-value="navbar-default"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="navbar-gradient-blue"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="navbar-gradient-red"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="navbar-gradient-purple"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="navbar-gradient-info"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="navbar-gradient-dark"><span></span><span></span></a>' +
                        '</div>' +
                        '<h6>Menu background [ Pattern ]</h6>' +
                        '<div class="theme-color navbar-pattern">' +
                            '<a href="#!" class="" data-value="navbar-pattern-1"></a>' +
                            '<a href="#!" class="" data-value="navbar-pattern-2"></a>' +
                            '<a href="#!" class="" data-value="navbar-pattern-3"></a>' +
                            '<a href="#!" class="" data-value="navbar-pattern-4"></a>' +
                            '<a href="#!" class="" data-value="navbar-pattern-5"></a>' +
                            '<a href="#!" class="" data-value="navbar-pattern-6"></a>' +
                        '</div>' +
                        '<h6>Navbar Image</h6>' +
                        '<div class="theme-color navbar-images">' +
                            '<a href="#!" class="" data-value="navbar-image-1"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="navbar-image-2"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="navbar-image-3"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="navbar-image-4"><span></span><span></span></a>' +
                            '<a href="#!" class="" data-value="navbar-image-5"><span></span><span></span></a>' +
                        '</div>' +
                    '</div>' +
                    '<div class="tab-pane fade" id="pills-pages" role="tabpanel" aria-labelledby="pills-pages-tab">' +
                        '<div class="form-group mb-0">' +
                            '<div class="switch switch-primary d-inline m-r-10">' +
                                '<input type="checkbox" id="theme-rtl">' +
                                '<label for="theme-rtl" class="cr"></label>' +
                            '</div>' +
                            '<label>RTL</label>' +
                        '</div>' +
                        '<div class="form-group mb-0">' +
                            '<div class="switch switch-primary d-inline m-r-10">' +
                                '<input type="checkbox" id="menu-fixed" checked>' +
                                '<label for="menu-fixed" class="cr"></label>' +
                            '</div>' +
                            '<label>Menu Fixed</label>' +
                        '</div>' +
                        '<div class="form-group mb-0">' +
                            '<div class="switch switch-primary d-inline m-r-10">' +
                                '<input type="checkbox" id="header-fixed" checked>' +
                                '<label for="header-fixed" class="cr"></label>' +
                            '</div>' +
                            '<label>Header Fixed</label>' +
                        '</div>' +
                        '<div class="form-group mb-0">' +
                            '<div class="switch switch-primary d-inline m-r-10">' +
                                '<input type="checkbox" id="box-layouts">' +
                                '<label for="box-layouts" class="cr"></label>' +
                            '</div>' +
                            '<label>Box Layouts</label>' +
                        '</div>' +

                    '</div>' +
                    '<div class="tab-pane fade" id="pills-extra" role="tabpanel" aria-labelledby="pills-extra-tab">' +
                        '<h6>Menu Dropdown Icon</h6>' +
                        '<div class="theme-color">' +
                            '<div class="form-group d-inline">' +
                                '<div class="radio radio-primary d-inline">' +
                                    '<input type="radio" name="radio-in-1" id="drpicon-1" checked onchange="drpicon(\'style1\')">' +
                                    '<label for="drpicon-1" class="cr"><i class="feather icon-chevron-right"></i></label>' +
                                '</div>' +
                            '</div>' +
                            '<div class="form-group d-inline">' +
                                '<div class="radio radio-primary d-inline">' +
                                    '<input type="radio" name="radio-in-1" id="drpicon-2" onchange="drpicon(\'style2\')">' +
                                    '<label for="drpicon-2" class="cr"><i class="feather icon-chevrons-right"></i></label>' +
                                '</div>' +
                            '</div>' +
                            '<div class="form-group d-inline">' +
                                '<div class="radio radio-primary d-inline">' +
                                    '<input type="radio" name="radio-in-1" id="drpicon-3" onchange="drpicon(\'style3\')">' +
                                    '<label for="drpicon-3" class="cr"><i class="feather icon-plus"></i></label>' +
                                '</div>' +
                            '</div>' +
                        '</div>' +
                        '<h6>Menu List Icon</h6>' +
                        '<div class="theme-color">' +
                            '<div class="form-group d-inline">' +
                                '<div class="radio radio-primary d-inline">' +
                                    '<input type="radio" name="radio-in" id="subitem-1" checked onchange="menuitemicon(\'style1\')">' +
                                    '<label for="subitem-1" class="cr"><i class=" "> </i>     </label>' +
                                '</div>' +
                            '</div>' +
                            '<div class="form-group d-inline">' +
                                '<div class="radio radio-primary d-inline">' +
                                    '<input type="radio" name="radio-in" id="subitem-2" onchange="menuitemicon(\'style2\')">' +
                                    '<label for="subitem-2" class="cr"><i class="feather icon-minus"></i></label>' +
                                '</div>' +
                            '</div>' +
                            '<div class="form-group d-inline">' +
                                '<div class="radio radio-primary d-inline">' +
                                    '<input type="radio" name="radio-in" id="subitem-3" onchange="menuitemicon(\'style3\')">' +
                                    '<label for="subitem-3" class="cr"><i class="feather icon-check"></i></label>' +
                                '</div>' +
                            '</div>' +
                            '<div class="form-group d-inline">' +
                                '<div class="radio radio-primary d-inline">' +
                                    '<input type="radio" name="radio-in" id="subitem-4" onchange="menuitemicon(\'style4\')">' +
                                    '<label for="subitem-4" class="cr"><i class="icon feather icon-corner-down-right"></i></label>' +
                                '</div>' +
                            '</div>' +
                            '<div class="form-group d-inline">' +
                                '<div class="radio radio-primary d-inline">' +
                                    '<input type="radio" name="radio-in" id="subitem-5" onchange="menuitemicon(\'style5\')">' +
                                    '<label for="subitem-5" class="cr"><i class="icon feather icon-chevrons-right"></i></label>' +
                                '</div>' +
                            '</div>' +
                            '<div class="form-group d-inline">' +
                                '<div class="radio radio-primary d-inline">' +
                                    '<input type="radio" name="radio-in" id="subitem-6" onchange="menuitemicon(\'style6\')">' +
                                    '<label for="subitem-6" class="cr"><i class="icon feather icon-chevron-right"></i></label>' +
                                '</div>' +
                            '</div>' +
                        '</div>' +
                        '<h6>Active Color</h6>' +
                        '<div class="theme-color active-color small">' +
                            '<a href="#!" class="active" data-value="active-blue"></a>' +
                            '<a href="#!" class="" data-value="active-red"></a>' +
                            '<a href="#!" class="" data-value="active-purple"></a>' +
                            '<a href="#!" class="" data-value="active-info"></a>' +
                            '<a href="#!" class="" data-value="active-dark"></a>' +
                        '</div>' +
                        '<h6>Menu Title Color</h6>' +
                        '<div class="theme-color title-color small">' +
                            '<a href="#!" class="active" data-value="title-default"></a>' +
                            '<a href="#!" class="" data-value="title-blue"></a>' +
                            '<a href="#!" class="" data-value="title-red"></a>' +
                            '<a href="#!" class="" data-value="title-purple"></a>' +
                            '<a href="#!" class="" data-value="title-info"></a>' +
                            '<a href="#!" class="" data-value="title-dark"></a>' +
                        '</div>' +
                        '<div class="form-group mb-0">' +
                            '<div class="switch switch-primary d-inline m-r-10">' +
                                '<input type="checkbox" id="caption-hide">' +
                                '<label for="caption-hide" class="cr"></label>' +
                            '</div>' +
                            '<label>Menu Title Hide</label>' +
                        '</div>' +
                        '<div class="form-group mb-0">' +
                            '<div class="switch switch-primary d-inline m-r-10">' +
                                '<input type="checkbox" id="header-hide">' +
                                '<label for="header-hide" class="cr"></label>' +
                            '</div>' +
                            '<label>Header Breadcrumb Hide</label>' +
                        '</div>' +
                    '</div>' +
                '</div>' +
            '</div>' +
        '</div>');
    setTimeout(function(){
        $('#pills-cust-tabContent').css({'height':'calc(100vh - 340px)','position':'relative'});
        var px = new PerfectScrollbar('#pills-cust-tabContent', {
            wheelSpeed: .5,
            swipeEasing: 0,
            suppressScrollX: !0,
            wheelPropagation: 1,
            minScrollbarLength: 40,
        });
        $('.prelayout-color').css({'height':'calc(100vh - 120px)','position':'relative'});
        var px = new PerfectScrollbar('.prelayout-color', {
            wheelSpeed: .5,
            swipeEasing: 0,
            suppressScrollX: !0,
            wheelPropagation: 1,
            minScrollbarLength: 40,
        });
    },400);
    // =========================================================
    // ==================    Menu Customizer Start   ===========
    // =========================================================
    // open Menu Styler
    $('#styleSelector > .style-toggler').on('click', function() {
        $('#styleSelector').toggleClass('open');
        $('#styleSelector').removeClass('prebuild-open');
    });
    $('.prebuild-link-styler').on('click', function() {
        $('#styleSelector').addClass('open');
        $('#styleSelector').removeClass('prebuild-open');
        $('.prebuild-link-layout').removeClass('active');
        $('.prebuild-link-styler').addClass('active');
    });
    $('#styleSelector > .prebuild-toggler > a, .prebuild-link, .prebuild-link-layout').on('click', function() {
        $('#styleSelector').addClass('open');
        $('#styleSelector').toggleClass('prebuild-open');
        $('.prebuild-link-layout').addClass('active');
        $('.prebuild-link-styler').removeClass('active');

    });
    // layout types
    $('.layout-type > a').on('click', function() {
        var temp = $(this).attr('data-value');
        $('.layout-type > a').removeClass('active');
        $('.pcoded-navbar').removeClassPrefix('navbar-image-');
        $(this).addClass('active');
        $('head').append('<link rel="stylesheet" class="layout-css" href="">');
        if (temp == "menu-dark") {
            $('.pcoded-navbar').removeClassPrefix('menu-');
            $('.pcoded-navbar').removeClass('navbar-dark');
        }
        if (temp == "menu-light") {
            $('.pcoded-navbar').removeClassPrefix('menu-');
            $('.pcoded-navbar').removeClass('navbar-dark');
            $('.pcoded-navbar').addClass(temp);
        }
        if (temp == "reset") {
            location.reload();
        }
        if (temp == "dark") {
            $('.pcoded-navbar').removeClassPrefix('menu-');
            $('.pcoded-navbar').addClass('navbar-dark');
            $('.layout-css').attr("href", "assets/css/layouts/dark.css");
        } else {
            $('.layout-css').attr("href", "");
        }
    });
    // Header Color
    $('.header-color > a').on('click', function() {
        var temp = $(this).attr('data-value');
        $('.header-color > a').removeClass('active');
        $(this).addClass('active');
        if (temp == "header-default") {
            $('.pcoded-header').removeClassPrefix('header-');
        } else {
            $('.pcoded-header').removeClassPrefix('header-');
            $('.pcoded-header').addClass(temp);
        }
    });
    // Menu Color
    $('.navbar-color > a').on('click', function() {
        var temp = $(this).attr('data-value');
        $('.navbar-color > a').removeClass('active');
        $('.pcoded-navbar').removeClassPrefix('menu-');
        $('.pcoded-navbar').addClass('brand-dark');
        $(this).addClass('active');
        if (temp == "navbar-default") {
            $('.pcoded-navbar').removeClassPrefix('navbar-');
            $('.pcoded-navbar').removeClassPrefix('brand-dark');
        } else {
            $('.pcoded-navbar').removeClassPrefix('navbar-');
            $('.pcoded-navbar').addClass(temp);
        }
    });
    // Menu Gradient Color
    $('.navbar-gradient-color > a').on('click', function() {
        var temp = $(this).attr('data-value');
        $('.navbar-gradient-color > a').removeClass('active');
        $('.pcoded-navbar').removeClassPrefix('menu-');
        $('.pcoded-navbar').addClass('brand-dark');
        $(this).addClass('active');
        if (temp == "navbar-default") {
            $('.pcoded-navbar').removeClassPrefix('navbar-');
            $('.pcoded-navbar').removeClassPrefix('brand-dark');
        } else {
            $('.pcoded-navbar').removeClassPrefix('navbar-');
            $('.pcoded-navbar').addClass(temp);
        }
    });
    // Active Color
    $('.active-color > a').on('click', function() {
        var temp = $(this).attr('data-value');
        $('.active-color > a').removeClass('active');
        $(this).addClass('active');
        if (temp == "active-default") {
            $('.pcoded-navbar').removeClassPrefix('active-');
        } else {
            $('.pcoded-navbar').removeClassPrefix('active-');
            $('.pcoded-navbar').addClass(temp);
        }
    });
    // rtl layouts
    $('#theme-rtl').change(function() {
        $('head').append('<link rel="stylesheet" class="rtl-css" href="">');
        if ($(this).is(":checked")) {
            $('.rtl-css').attr("href", "assets/css/layouts/rtl.css");
        } else {
            $('.rtl-css').attr("href", "");
        }
    });
    // Menu Fixed
    $('#menu-fixed').change(function() {
        if ($(this).is(":checked")) {
            $('.pcoded-navbar').addClass('menupos-fixed');
            setTimeout(function() {
                // $(".navbar-content").css({'overflow':'visible','height':'calc(100% - 70px)'});
            }, 400);
        } else {
            $('.pcoded-navbar').removeClass('menupos-fixed');
        }
    });
    // Header Fixed
    $('#header-fixed').change(function() {
        if ($(this).is(":checked")) {
            $('.pcoded-header').addClass('headerpos-fixed');
        } else {
            $('.pcoded-header').removeClass('headerpos-fixed');

        }
    });
    // Menu Icon Color
    $('#icon-colored').change(function() {
        if ($(this).is(":checked")) {
            $('.pcoded-navbar').addClass('icon-colored');
        } else {
            $('.pcoded-navbar').removeClass('icon-colored');
        }
    });
    // Box layouts
    $('#box-layouts').change(function() {
        if ($(this).is(":checked")) {
            $('body').addClass('container');
            $('body').addClass('box-layout');
        } else {
            $('body').removeClass('container');
            $('body').removeClass('box-layout');
        }
    });
    // Caption Hide
    $('#caption-hide').change(function() {
        if ($(this).is(":checked")) {
            $('.pcoded-navbar').addClass('caption-hide');
        } else {
            $('.pcoded-navbar').removeClass('caption-hide');
        }
    });
    // Header Hide
    $('#header-hide').change(function() {
        if ($(this).is(":checked")) {
            $('.pcoded-navbar').addClass('header-hide');
        } else {
            $('.pcoded-navbar').removeClass('header-hide');
        }
    });

    // Menu image background
    $('.navbar-images > a').on('click', function() {
        var temp = $(this).attr('data-value');
        $('.pcoded-navbar').removeClassPrefix('menu-');
        $('.navbar-images > a').removeClass('active');
        $(this).addClass('active');
        $('.pcoded-navbar').removeClassPrefix('navbar-image-');
        $('.pcoded-navbar').addClass(temp);
    });
    // Menu pattern background
    $('.navbar-pattern > a').on('click', function() {
        var temp = $(this).attr('data-value');
        $('.pcoded-navbar').removeClassPrefix('menu-');
        $('.pcoded-navbar').removeClassPrefix('brand-');
        $('.navbar-pattern > a').removeClass('active');
        $(this).addClass('active');
        $('.pcoded-navbar').removeClassPrefix('navbar-pattern-');
        $('.pcoded-navbar').removeClassPrefix('navbar-image-');
        $('.pcoded-navbar').addClass(temp);
    });
    // title Color
    $('.title-color > a').on('click', function() {
        var temp = $(this).attr('data-value');
        $('.title-color > a').removeClass('active');
        $(this).addClass('active');
        if (temp == "title-default") {
            $('.pcoded-navbar').removeClassPrefix('title-');
        } else {
            $('.pcoded-navbar').removeClassPrefix('title-');
            $('.pcoded-navbar').addClass(temp);
        }
    });
    // brand Color
    $('.brand-color > a').on('click', function() {
        var temp = $(this).attr('data-value');
        $('.brand-color > a').removeClass('active');
        $(this).addClass('active');
        if (temp == "brand-default") {
            $('.pcoded-navbar').removeClassPrefix('brand-');
        } else {
            $('.pcoded-navbar').removeClassPrefix('brand-');
            $('.pcoded-navbar').addClass(temp);
        }
    });
    $.fn.removeClassPrefix = function(prefix) {
        this.each(function(i, it) {
            var classes = it.className.split(" ").map(function(item) {
                return item.indexOf(prefix) === 0 ? "" : item;
            });
            it.className = classes.join(" ");
        });
        return this;
    };
    // ==================    Menu Customizer End   =============
    // =========================================================
});
// Menu Dropdown icon
function drpicon(temp) {
    if (temp == "style1") {
        $('.pcoded-navbar').removeClassPrefix('drp-icon-');
    } else {
        $('.pcoded-navbar').removeClassPrefix('drp-icon-');
        $('.pcoded-navbar').addClass('drp-icon-' + temp);
    }
}
// Menu subitem icon
function menuitemicon(temp) {
    if (temp == "style1") {
        $('.pcoded-navbar').removeClassPrefix('menu-item-icon-');
    } else {
        $('.pcoded-navbar').removeClassPrefix('menu-item-icon-');
        $('.pcoded-navbar').addClass('menu-item-icon-' + temp);
    }
}
