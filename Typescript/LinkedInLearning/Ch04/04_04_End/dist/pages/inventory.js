var inventoryDetails = Vue.extend({
    props: ["item"],
    render: function (createDetails) {
        var details = null;
        switch (this.item.inventoryType) {
            case "computer":
                details = inventoryDetails.computer;
                break;
            case "furniture":
                details = inventoryDetails.furniture;
                break;
        }
        return createDetails(details, { props: this.$props });
    }
});
inventoryDetails.computer = Vue.extend({
    props: ["item"],
    template: "\n        <div>\n            <div class=\"col-sm-6\">\n                <label>Tracking #</label>\n                <span>{{item.trackingNumber}}</span>\n            </div>\n\n            <div class=\"col-sm-6\">\n                <label>Assigned To:</label>\n                <span>{{item.assignedTo}}</span>\n            </div>\n\n            <div class=\"col-sm-6\">\n                <label>Brand:</label>\n                <span>{{item.brand}}</span>\n            </div>\n\n            <div class=\"col-sm-6\">\n                <label>Serial #:</label>\n                <span>{{item.serialNumber}}</span>\n            </div>\n           \n            <div class=\"col-sm-12\">\n                <label>Model:</label>\n                <span>{{item.year}} {{item.model}}</span>\n            </div>\n\n        </div>\n    "
});
inventoryDetails.furniture = Vue.extend({
    props: ["item"],
    template: "\n        <div>\n        <div class=\"col-sm-6\">\n                <label>Tracking #</label>\n                <span>{{item.trackingNumber}}</span>\n            </div>\n            <div class=\"col-sm-6\">\n                <label>Assigned To:</label>\n                <span>{{item.assignedTo}}</span>\n            </div>\n            <div class=\"col-sm-6\">\n                <label>Manufacturer</label>\n                <span>{{item.manufacturer}}</span>\n            </div>\n            <div class=\"col-sm-12\">\n                <label>Model</label>\n                <span>{{item.model}}</span>\n            </div>\n            <div class=\"col-sm-6\">\n                <label>Material</label>\n                <span>{{item.material}}</span>\n            </div>\n            <div class=\"col-sm-6\">\n                <label>Color</label>\n                <span>{{item.color}}</span>\n            </div>\n        </div>\n    "
});
var InventoryList = Vue.extend({
    props: ["selectedItem", "inventory"],
    methods: {
        getIcon: function (item) {
            switch (item.inventoryType) {
                case "computer":
                    return "fa-desktop";
                case "furniture":
                    return "fa-chair";
                default:
                    return "fa-dolly-flatbed";
            }
        }
    },
    template: "\n    <div class=\"inventory-list list-group\">\n      <a class=\"list-group-item\"\n        v-for=\"item in inventory\"\n        @click=\"$emit('item-selected', item)\"\n        :class=\"{ active: selectedItem && selectedItem.trackingNumber == item.trackingNumber }\"\n      >\n        <i class=\"fas\" :class=\"getIcon(item)\"></i>\n        {{ item.name }}\n      </a>\n    </div>\n  "
});
var inventoryPage = Vue.extend({
    components: { InventoryList: InventoryList, inventoryDetails: inventoryDetails },
    data: function () { return ({
        inventory: null,
        selectedItem: null
    }); },
    methods: {
        deleteItem: function (item) {
            inventoryStore.removeItem(item);
        },
        resetTestData: function () {
            localStorage.clear();
            window.location.reload();
        }
    },
    created: function () {
        this.inventory = inventoryStore.items;
    },
    mounted: function () {
        if (this.inventory.length) {
            this.selectedItem = this.inventory[0];
        }
    },
    template: "\n    <div>\n      <h2 class=\"title\">Current Inventory</h2>\n\n      <div class=\"menu-bar text-right\">\n        <a href=\"#/add-item\" class=\"add-item btn btn-sm btn-primary\">\n          <i class=\"fas fa-plus-circle\"></i>\n          Add New Item\n        </a>\n      </div>\n\n      <div class=\"flex\">\n      \n        <inventory-list \n          :inventory=\"inventory\" \n          :selectedItem=\"selectedItem\" \n          @item-selected=\"selectedItem = $event\"\n        />\n\n        <div v-if=\"selectedItem\" class=\"grow full-height\">\n          <div class=\"inventory-panel panel panel-default\">\n            <div class=\"panel-heading\">\n              <h3 class=\"panel-title col-xs-10\">{{ selectedItem.name }}</h3>\n              <button @click.stop=\"deleteItem(selectedItem)\" class=\"pull-right btn btn-xs btn-danger\">\n                <i class=\"fas fa-times-circle\"></i>\n                Delete\n              </button>\n            </div>\n            <div class=\"panel-body\">\n              <inventory-details :item=\"selectedItem\" />\n            </div>\n          </div>\n        </div>\n      </div>\n\n      <div class=\"text-right\" style=\"margin-top: 10px\">\n        <a @click.stop=\"resetTestData\" class=\"btn btn-xs btn-warning\">\n          <i class=\"fas fa-radiation-alt\"></i>\n          Reset Test Data\n        </a>\n      </div>\n    </div>\n  "
});
