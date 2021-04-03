var __spreadArray = (this && this.__spreadArray) || function (to, from) {
    for (var i = 0, il = from.length, j = to.length; i < il; i++, j++)
        to[j] = from[i];
    return to;
};
var inventoryEditor = Vue.extend({
    props: ["item", "category"],
    render: function (createEditor) {
        var editor = null;
        switch (this.item.inventoryType) {
            case "computer":
                editor = inventoryEditor.computer;
                break;
            case "furniture":
                editor = inventoryEditor.furniture;
                break;
        }
        return createEditor(editor, { props: this.$props });
    }
});
inventoryEditor.computer = Vue.extend({
    props: ["item"],
    data: function () { return ({
        minYear: 2010,
        maxYear: new Date().getFullYear()
    }); },
    template: "\n      <div>\n  \n          <div class=\"col-sm-3 form-group\">\n              <label for=\"item-brand\">Brand</label>\n              <input name=\"item-brand\" type=\"text\" class=\"form-control\" v-model=\"item.brand\" />\n          </div>\n  \n          <div class=\"col-sm-3 form-group\">\n              <label for=\"item-model\">Model</label>\n              <input name=\"item-model\" type=\"text\" class=\"form-control\" v-model=\"item.model\" />\n          </div>\n  \n          <div class=\"col-sm-3 form-group\">\n              <label for=\"item-year\">Year</label>\n              <input name=\"item-year\" type=\"number\":min=\"minYear\" :max=\"maxYear\" class=\"form-control\" v-model=\"item.year\" />\n          </div>\n  \n          <div class=\"col-sm-3 form-group\">\n              <label for=\"item-serial-number\">Serial Number</label>\n              <input name=\"item-serial-number\" type=\"text\" class=\"form-control\" v-model=\"item.serialNumber\" />\n          </div>\n  \n      </div>\n      "
});
inventoryEditor.furniture = Vue.extend({
    props: ["item", "category"],
    computed: {
        colors: function () {
            return this.category.colors;
        }
    },
    template: "\n      <div>\n  \n          <div class=\"col-sm-6 form-group\">\n              <label for=\"item.manufacturer\">Manufacturer</label>\n              <input name=\"item.manufacturer\" type=\"text\" class=\"form-control\" v-model=\"item.manufacturer\" />\n          </div>\n  \n          <div class=\"col-sm-6 form-group\">\n              <label for=\"item.model\">Model / Serial Number / Description</label>\n              <input name=\"item.model\" type=\"text\" class=\"form-control\" v-model=\"item.model\" />\n          </div>\n  \n          <div class=\"col-sm-3 form-group\">\n              <label for=\"item.material\">Material</label>\n              <input name=\"item.material\" type=\"text\" class=\"form-control\" v-model=\"item.material\" />\n          </div>\n  \n          <div v-if=\"colors\" class=\"col-sm-3 form-group\">\n            <label for=\"item.color\">Color</label>\n            <select name=\"item.color\"class=\"form-control\" v-model=\"item.color\">\n              <option disabled value=\"\">-- Select --</option>\n              <option v-for=\"color in colors\" :value=\"color\">\n                {{color}}\n              </option>\n            </select>\n        </div>\n\n      </div>\n      "
});
var addItemPage = Vue.extend({
    components: { inventoryEditor: inventoryEditor },
    data: function () { return ({
        categories: inventoryStore.categories,
        errors: [],
        item: {},
        saving: false,
        showSavedMessage: false
    }); },
    computed: {
        canSubmit: function () {
            return this.item && !!this.item.subCategory;
        },
        category: function () {
            var _this = this;
            return this.categories.find(function (x) { return x.name === _this.item.inventoryType; }) || {};
        },
        subCategories: function () {
            return this.category.subCategories;
        }
    },
    methods: {
        onSubmit: function () {
            var _this = this;
            this.saving = true;
            inventoryStore
                .addItem(this.item)
                .then(function () {
                _this.reset();
                _this.showSavedMessage = true;
                _this.saving = false;
                setTimeout(function () { return (_this.showSavedMessage = false); }, 4000);
            })
                .catch(function (errors) {
                var _a;
                (_a = _this.errors).splice.apply(_a, __spreadArray([0, Infinity], errors));
                _this.saving = false;
            });
        },
        reset: function () {
            this.item = {};
            this.errors = [];
            this.showErrors = false;
        },
        hasError: function (field) {
            return !!this.errors.find(function (x) { return x.field === field; });
        }
    },
    template: "\n    <div>\n      <div v-if=\"showSavedMessage\" class=\"alert alert-success alert-dismissible fade\" role=\"alert\">\n        <button @click=\"showSavedMessage = false\" type=\"button\" class=\"close\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>\n        <strong>Inventory item saved!</strong>\n        You have successfully saved your new item!\n        Check it out on the <a href=\"#/inventory\">Inventory page</a>!\n      </div>\n\n      <h2 class=\"text-center\">Add New Inventory Item</h2>\n\n      <div class=\"form-container\">\n        <div class=\"saving\" v-if=\"saving\">\n          Saving...\n        </div>\n\n        <form @submit.prevent=\"onSubmit\">\n\n          <div v-if=\"errors.length\" class=\"panel panel-danger\">\n            <div class=\"panel-heading\">\n              <h3 class=\"panel-title\">Invalid Inventory Item</h3>\n            </div>\n            <div class=\"panel-body\">\n              Please correct the following errors:\n              <ul>\n                <li class=\"error\" v-for=\"error in errors\">\n                  <span>{{ error.message }}</span>\n                </li>\n            </ul>\n            </div>\n          </div>\n\n          <div class=\"row\">\n\n            <div class=\"col-sm-6 form-group\">\n                <label for=\"item-type\">Category</label>\n                <select name=\"item-type\"class=\"form-control\" v-model=\"item.inventoryType\">\n                  <option disabled value=\"\">-- Select --</option>\n                  <option v-for=\"category in categories\" :value=\"category.name\">\n                    {{category.displayName}}\n                  </option>\n                </select>\n            </div>\n\n            <div class=\"col-sm-6 form-group\">\n                <label for=\"item-subCategory\">Sub-Category</label>\n                <select v-if=\"!subCategories\" disabled class=\"form-control\">\n                  <option selected>-- Select a Category --</option>\n                </select>\n                <select name=\"item-subCategory\" class=\"form-control\" \n                    v-if=\"subCategories\" v-model=\"item.subCategory\"\n                  >\n                  <option disabled selected>-- Select --</option>\n                  <option v-for=\"category in subCategories\" :value=\"category.name\">\n                    {{category.displayName}}\n                  </option>\n                </select>\n            </div>\n\n            <div v-if=\"item.subCategory\">\n              <div class=\"col-sm-6 form-group\">\n                  <label for=\"item-name\">Name</label>\n                  <input name=\"item-name\" type=\"text\" class=\"form-control\" v-model=\"item.name\" />\n              </div>\n\n              <div class=\"col-sm-6 form-group\">\n                  <label for=\"item-assigned-to\">Assigned To</label>\n                  <input name=\"item-assigned-to\" type=\"text\" class=\"form-control\" v-model=\"item.assignedTo\"  />\n              </div>\n\n              <inventory-editor :item=\"item\" :category=\"category\"></inventory-editor>\n            </div>\n\n            </div>\n          <div class=\"col-sm-12 clear \">\n            <button :disabled=\"!canSubmit\" type=\"submit\" class=\"btn btn-primary\">Save</button>\n            <a href=\"#/\" class=\"btn btn-default\">Cancel</a>\n          </div>\n\n        </form>\n      </div>\n    </div>\n    "
});
