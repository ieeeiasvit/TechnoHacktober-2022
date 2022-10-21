    $(document).ready(() => {
        
        document.getElementById("btnSearch").addEventListener("click", e => {
            e.preventDefault();
            $(".grid-item1").remove();
            let index = 0;
            let offsetVal = 0;
            let giphyLimit = 6;
            let string=$("#search").val();
            function getGiphy (i){
                if (i > 0){
                    offsetVal =i*giphyLimit;
                }
                $.ajax({
                    url: 'https://api.giphy.com/v1/gifs/search?',
                    type: 'GET',
                    dataType: 'json',
                    data: {q:string,api_key:'HRRnVVo8ZzM7c98d2N6xjctlIwqyAQTW', limit: giphyLimit, offset: offsetVal},
                    success: (data) => {
                        $.each(data['data'], ( index, value) => {
                            let imageUrl = value['images']['original']['url'];
                            $("#imageWrapper").append("<div data-aos=flip-right class='grid-item1'><img src='"+imageUrl+"' /></div>");
                        })
                        index = index+1;
                    }
                })
            }
            $("#SearchHeading").text(string);
            getGiphy(0);
            $("#search").val("");
            $("#loadMore").css("display","block");

            $("#loadMore").click(() => {
                getGiphy(index);
            });
        });



        let index = 0;
        let offsetVal = 0;
        let giphyLimit = 12;

        function getTrending (i){
            if (i > 0){
                offsetVal = i*giphyLimit;
            }
            $.ajax({
                url: 'https://api.giphy.com/v1/gifs/trending?',
                type: 'GET',
                dataType: 'json',
                data: {api_key:'HRRnVVo8ZzM7c98d2N6xjctlIwqyAQTW', limit: giphyLimit, offset: offsetVal},
                success: (data) => {
                    $.each(data['data'], ( index, value) => {
                        let imageUrl = value['images']['original']['url'];
                        $("#trendingGif").append("<div data-aos=flip-right class='grid-item2'><img src='"+imageUrl+"' /></div>");
                    })
                    index = index+1;
                }
            })
        }
        
        getTrending(0);
        $("#loadMoreTrending").click(() => {
            getTrending(index);
        });
        
    
    })