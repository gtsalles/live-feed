//<div class="row">
//    <% _.each(noticias, function(noticia) { %>
//        <div class="col-xs-12">
//            <h2><% noticia.get('titulo') %></h2>
//            <div class="texto" style="margin-bottom: 15px">
//                <% noticia.get('texto') %>
//            </div>
//            <p class="lead"><a href="<% noticia.get('url') %>" target="_blank" class="btn btn-default">Ver no site</a></p>
//            <ul class="list-inline">
//                <li><a href="<% noticia.get('site') %>"><% noticia.get('site') %></a></li>
//                <li><% noticia.get('data_publicacao') %></li>
//            </ul>
//        </div>
//    <% }); %>
//</div>