window.app = {};
app.collections = {};
app.models = {};
app.views = {};

app.models.Noticia = Backbone.Model.extend({});

app.collections.PaginatedCollection = Backbone.Paginator.requestPager.extend({
    model: app.models.Noticia,
    paginator_core: {
        dataType: 'json',
        url: '/api/noticias/'
    },

    paginator_ui: {
        firstPage: 1,
        currentPage: 1,
        perPage: 10,
        totalPages: 10
    },

    server_api: {
        'per_page': function() { return this.perPage },
        'page': function() { return this.currentPage }
    },

    parse: function (response) {
        $('#paginated-content').spin(false);
        this.totalRecords = response.count;
        this.totalPages = Math.ceil(response.count / this.perPage);

        return response.results;
    }
});

app.views.NoticiaView = Backbone.View.extend({
    initialize: function() {
        this.template = _.template($('#noticia-template').html());
        this.model.bind('change', this.render, this);
        this.model.bind('remove', this.remove, this);
    },

    render : function () {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }
});

app.views.PaginatedView = Backbone.View.extend({
    events: {
        'click button.prev': 'gotoPrev',
        'click button.next': 'gotoNext',
        'click button.page': 'gotoPage',
        'click button.refresh': 'refresh',
    },

    initialize: function () {
        this.template = _.template($('#noticias-pagination').html());
        this.collection.on('reset', this.render, this);
        this.collection.on('sync', this.render, this);
        this.$el.appendTo('#pagination');
    },

    render: function () {
        var html = this.template(this.collection.info());
        this.$el.html(html);
    },

    gotoPrev: function (e) {
        e.preventDefault();
        $('#paginated-content').spin();
        this.collection.requestPreviousPage();
    },

    gotoNext: function (e) {
        e.preventDefault();
        $('#paginated-content').spin();
        this.collection.requestNextPage();
    },

    refresh: function(e) {
        e.preventDefault();
        this.collection.goTo(1);
    },

    gotoPage: function (e) {
        e.preventDefault();
        $('#paginated-content').spin();
        var page = $(e.target).text();
        this.collection.goTo(page);
    }
});

app.views.AppView = Backbone.View.extend({
    el : '#paginated-content',

    initialize : function () {
        $('#paginated-content').spin();

        var noticias = this.collection;

        noticias.on('add', this.addOne, this);
        noticias.on('all', this.render, this);

        noticias.pager();
    },

    addOne : function (noticia) {
        var view = new app.views.NoticiaView({model:noticia});
        $('#paginated-content').append(view.render().el);
    }
});

$(function(){
    app.collections.paginatedItems = new app.collections.PaginatedCollection();
    app.views.app = new app.views.AppView({collection: app.collections.paginatedItems});
    app.views.pagination = new app.views.PaginatedView({collection:app.collections.paginatedItems});
    $('#refresh').on('click', function() {
        $('#refresh-hide').click();
    });
//    setInterval(function() {
//        $('#refresh-hide').click();
//        console.log('aqui');
//    }, 5000);
});
