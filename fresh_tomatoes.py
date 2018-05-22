import webbrowser
import os
import re

main_page_head = '''
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>MOVIE TRAILER</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet"
    href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet"
    href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script
    src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js">
    </script>
    <style type="text/css" media="screen">
        body {
            background-color: whitesmoke;
            padding-top: 80px;
        }

        #trailer .modal2 {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }

        .modal1 {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }

        #trailer-video {
            width: 100%;
            height: 100%;
        }

        .class2 {
            margin-bottom: 10px;
            padding-top: 10px;
            padding: 3%;
        }

        .class2:hover {
            background-color: lightslategray;
            cursor: pointer;
        }

        .sub_class {
            padding-bottom: 56.25%;
            position: relative;
        }

        .sub_class iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        $(document).
        on('click', '.modal1, .modal-backdrop, .modal', function(event)
        {

            $("#trailer-video-container").empty();
        });

        $(document).on('click', '.class2', function(event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl =
            'http://www.youtube.com/embed/'
            + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container")
            .empty().append($("<iframe></iframe>", {
                'id': 'trailer-video',
                'type': 'text-html',
                'src': sourceUrl,
                'frameborder': 10
            }));
        });
        $(document).ready(function() {
            $('.class2').hide().first().show("fast", function showNext() {
                $(this).next("div").show("fast", showNext);
            });
        });
    </script>
</head>
'''
main_page_content = '''
<body>
    <div class="modal" id="trailer">
        <div class="modal2">
            <div class="modal-content">
                <a  class="modal1" data-dismiss="modal" aria-hidden="true">
                    <img src="https://bit.ly/2bxshf7" />
                </a>
                <div class="sub_class" id="trailer-video-container">
                </div>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
            <div class="container">
                <div class="navbar-header">
                    <a class="navbar-brand" href="#"> Movie Trailers</a>
                </div>
            </div>
        </div>
    </div>
    <div class="container">

        <div class="col-sm-6 col-lg-4 class2 text-center"
        data-trailer-youtube-id="NWepvH6LnEw"
        data-toggle="modal" data-target="#trailer">
            <img src="https://bit.ly/2rZ9HDT" width="220" height="342">
            <h2>Avengers Infinity War</h2>
            <p>Stopping Thanos</p>

        </div>

        <div class="col-sm-6 col-lg-4 class2 text-center"
        data-trailer-youtube-id="VSB4wGIdDwo"
        data-toggle="modal" data-target="#trailer">
            <img src="https://bit.ly/2IXVMre" width="220" height="342">
            <h2>Wonder Woman</h2>
            <p>Brave lady</p>
        </div>

        <div class="col-sm-6 col-lg-4 class2 text-center"
        data-trailer-youtube-id="h24gEn3y82Q"
        data-toggle="modal" data-target="#trailer">
            <img src="https://bit.ly/2LjBo20" width="220" height="342">
            <h2>Boss Babby</h2>
            <p>Kid from business school</p>

        </div>

        <div class="col-sm-6 col-lg-4 class2 text-center"
        data-trailer-youtube-id="4fVCKy69zUY"
        data-toggle="modal" data-target="#trailer">
            <img src="https://bit.ly/2IAPJW6" width="220" height="342">
            <h2>THE Croods</h2>
            <p>Cave man Life</p>
        </div>

        <div class="col-sm-6 col-lg-4 class2 text-center"
        data-trailer-youtube-id="R-cdIvgBCWY"
        data-toggle="modal" data-target="#trailer">
            <img src="https://bit.ly/2x3yrQc" width="220" height="342">
            <h2>FROZEN</h2>
            <p>Finding sister</p>
        </div>

        <div class="col-sm-6 col-lg-4 class2 text-center"
        data-trailer-youtube-id="tyE8XnZBJQA"
        data-toggle="modal" data-target="#trailer">
            <img src="https://bit.ly/2ICfucL" width="200" height="342">
            <h2>Tom and Jerry</h2>
            <p>Land of OZ</p>
        </div>
    </div>
</body>

</html>
'''
movie_title = '''
 <div class="col-sm-6 col-lg-4 class2 text-center"
 data-trailer-youtube-id="R-cdIvgBCWY"
 data-toggle="modal" data-target="#trailer">
            <img src="{poster_image_url}" width="220" height="342">
            <h2 style="color:white;">{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    content = ''
    for movie in movies:

        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        content += movie_title.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            storyline=movie.storyline
        )
    return content


def open_movies_page(movies):
    output_file = open('movie2.html', 'w')
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    output_file.write(main_page_head + rendered_content)
    output_file.close()
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
