<!DOCTYPE html>
<html >
    <head>
        <meta charset="UTF-8">
        <title>Spam Hammer</title>
        <link rel="stylesheet" href="design.css">
    </head>
    <script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.js"></script>

    <body>
        <h1>Project Spam-Hammer</h1>
        <nav class='menu'>
            <input checked='checked' class='menu-toggler' id='menu-toggler' type='checkbox'>
            <label for='menu-toggler'></label>
            <ul>
                <li class='menu-item'>
                    <a href='#' id = "spam" onclick = "getSpam()">Spam</a>
                </li>
                <li class='menu-item'>
                    <a href='#' id = "ham" onclick = "getHam()">Ham</a>
                </li>
            </ul>
        </nav>
         <div style="text-align: center;">
            <textarea id ="text" style="width: 300px;height: 200px;margin-top: 400px;text-align: center;font-family: Neuropol X;">Spam Here</textarea>    
        </div>
    </body>
    <script type="text/javascript">
    menutoggler = document.querySelector(".menu-toggler");
    function getSpam() {
        $.ajax({
            type:'post',
            url:'getResult.php',
            data:{'data':"spam"},
            success: function(data) {
                document.querySelector("#text").innerHTML = data

            }

        })
    }
    function getHam() {
        $.ajax({
            type:'post',
            url:'getResult.php',
            data:{'data':"ham"},
            success: function(data) {
                document.querySelector("#text").innerHTML = data

            }

        })
    }
    </script>
</html>
