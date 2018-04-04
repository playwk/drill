/**
 * Created by Tony on 2017/2/23.
 */

window.onload = function () {
    var obj1 = ele("button1");
    bind(obj1, "click", function () {
        upload_ajax();
    });
    var obj2 = ele("button2");
        bind(obj2, "click", function () {
        upload_jquery();
    });
};

function upload_ajax() {
    var form = new FormData();
    form.append("file", ele("file").files[0]);

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            var data = xhr.responseText;
            console.log(data);
        }
    };
    xhr.open("post", "/index/", true);
    xhr.send(form);
}

// dom -> jQuery $("#id")       dom对象转换为jQuery对象
// jQuery -> dom $("#id")[0]    jQuery对象转换为dom对象

function upload_jquery() {
    var form  = new FormData();
    form.append("file", $("#file")[0].files[0]);
    $.ajax({
        type: "POST",
        url: "/index/",
        data: form,
        processData: false, //不做字典到字符串的转换
        contentType: false, //请求头
        success: function (arg) {
            console.log(arg)
        }
    });
}


function bind(obj, type, fun) {
    return obj.addEventListener(type, fun, false);
}

function ele(eleId) {
    return document.getElementById(eleId);
}



