var basePath = "src";
var loadDependencies = function () { return Promise.all([
    $.get(basePath + "/testData.js"),
    $.get(basePath + "/storage.js"),
    $.get(basePath + "/inventoryStore.js")
]); };
var loadPages = function () { return Promise.all([
    $.get(basePath + "/pages/addItem.js"),
    $.get(basePath + "/pages/inventory.js")
]); };
Vue.component("loading", {
    template: "\n    <div class=\"loading\">\n      <strong>Loading...</strong>\n      <div class=\"progress\">\n        <div class=\"progress-bar progress-bar-striped active\" role=\"progressbar\" aria-valuenow=\"45\" aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width: 100%\">\n          <span class=\"sr-only\">Loading...</span>\n        </div>\n      </div>\n    </div>\n  "
});
Vue.component("app", function () { return ({
    delay: 200,
    loading: { template: "<loading />" },
    component: loadDependencies()
        .then(function () { return inventoryStore.isInitialized; })
        .then(loadPages)
        .then(function () { return ({
        data: function () { return ({
            inventoryStore: null,
            currentRoute: null,
            CurrentPage: null,
            routes: {
                "add-item": addItemPage,
                "inventory": inventoryPage
            }
        }); },
        methods: {
            syncRoute: function () {
                this.currentRoute = window.location.hash.replace(/^#\//, "");
            }
        },
        watch: {
            currentRoute: function () {
                var page = this.routes[this.currentRoute];
                this.CurrentPage = page || inventoryPage;
            }
        },
        created: function () {
            this.inventoryStore = inventoryStore;
            window.addEventListener("hashchange", this.syncRoute);
            this.syncRoute();
        },
        template: "\n          <div class=\"container-fluid\">\n              <div class=\"header clearfix\">\n                  <h3 class=\"text-muted\">Inventory Management System</h3>\n              </div>\n              <component :is=\"CurrentPage\"></component>\n          </div>"
    }); })
}); });
new Vue({ el: "#app", template: "<app/>" });
