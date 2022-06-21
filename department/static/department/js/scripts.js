<script src="~/js/scripts.min.js" asp-append-version="true"></script>
<script src="~/lib/bootstrap/dist/js/bootstrap.bundle.min.js"></script>
<script src="~/lib/ckeditor/ckeditor.js"></script>
<script src="~/lib/jquery-validation/dist/jquery.validate.min.js"></script>
<script src="~/lib/jquery-validation-unobtrusive/jquery.validate.unobtrusive.min.js"></script>

<script>
    let menuItems = document.querySelectorAll(".menu-item");
    menuItems.forEach(menuItem => {
        //console.log(menuItem.parentNode.querySelector("ul"))
        let ul = menuItem.parentNode.querySelector("ul");
        ul.classList.add("hide");

        menuItem.onclick = function() {
            if (ul.classList.contains("hide")) {
                ul.classList.remove("hide");
                ul.classList.add("show");
            } else if (ul.classList.contains("show")) {
                ul.classList.remove("show");
                ul.classList.add("hide");
            } else {
                return;
            }
        }
    });
</script>
