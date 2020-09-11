function a() {
    var targetElem = document.getElementById("blockContainer");
    targetElem.style.marginTop = "-5px";
}

function b() {
    var targetElem = document.getElementById("blockContainer");
    targetElem.style.marginTop = "100px";
}

$("button.navbar-toggle.collapsed").click(function () {
    return (this.tog = !this.tog) ? a() : b();
});
