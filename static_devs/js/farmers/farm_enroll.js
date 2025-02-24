// farm_enroll PAGE 2
// 프로필 사진
function readInputFile_1(input) {
    if ($("#id_farmer_profile")) {
        var reader = new FileReader();
        reader.onload = function (e) {
            var path = e.target.result;
            path = "url(" + path + ")";
            $('.default_img_1').css(
                {
                    'background': path,
                    'background-size': 'cover',
                    'background-position': 'center'
                }
            );
        }
        reader.readAsDataURL(input.files[0]);
    }
}
$("#id_farmer_profile").on('change', function () {
    readInputFile_1(this);
});


// 농장 사진
function readInputFile_2(input) {
    if ($("#id_farm_profile")) {
        var reader = new FileReader();
        reader.onload = function (e) {
            var path = e.target.result;
            path = "url(" + path + ")";
            $('.default_img_2').css(
                {
                    'background': path,
                    'background-size': 'cover',
                    'background-position': 'center',
                }
            );
        }
        reader.readAsDataURL(input.files[0]);
    }
}
$("#id_farm_profile").on('change', function () {
    readInputFile_2(this);
});


// 해시 태그

// 선택한 카테고리 해시태그 색상 변경
var checked = document.querySelector('input[name="farm_cat"]:checked')
checked.parentNode.setAttribute('class', 'sel_bk_color')
$("#id_farm_cat label").on("click", function () {
    if ($(this).find('input[type="radio"]').is(':checked')) {
        $(this).addClass('sel_bk_color');
    }
    else {
        $('#id_farm_cat label').removeClass('sel_bk_color');
    }
});


// farmer's page sample
$('#id_farm_name').keyup(function () {
    $('#sample_farm_name').text($(this).val());
});

$('#id_profile_title').keyup(function () {
    $('#sample_profile_title').text($(this).val());
});

$('#id_profile_desc').keyup(function () {
    $('#sample_profile_desc').text("&#34;" + $(this).val() + "&#34;");
});

$('#id_farm_news').keyup(function () {
    $('#sample_farm_news').text($(this).val());
});


// step2 page form valid check
$('#step2_submit').click(function () {
    var categories = document.getElementsByName("farm_cat").length;
    var hashTagList = new Array();
    $("input[name=farm_tag]").each(function(index, item) {
        hashTagList.push($(item).val());
    });
    $("#hashtag_list").val(hashTagList);

    for (var i = 0; i < categories; i++) {
        if (document.getElementsByName("farm_cat")[i].checked == true) {
            let farm_cat = document.getElementsByName("farm_cat")[i].value;
        }
    }

    if ($('#id_farm_name').val() == "") {
        alert("농장 이름을 입력해주세요.");
        return;
    }

    if ($('#id_profile_title').val() == "") {
        alert("농장 한 줄 소개를 입력해주세요.");
        return;
    }

    if ($('#id_farm_cat input').is(":checked") == false) {
        alert("카테고리를 선택해주세요.");
        event.preventDefault();
        return;
    }

})
