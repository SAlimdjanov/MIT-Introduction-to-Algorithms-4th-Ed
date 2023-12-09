/**
 * DirectAddressTable.test.js
 *
 */

const { TableObject, DirectAddressTable } = require("../DirectAddressTable");

const object1 = new TableObject(2, "Hello");
const object2 = new TableObject(15, "World");

const testTable = new DirectAddressTable();

test("An object can be inserted into the table", () => {
    testTable.insert(object1);
    testTable.insert(object2);

    let result = testTable.table;

    expect(result.get(2).key).toStrictEqual(2);
    expect(result.get(2).data).toStrictEqual("Hello");
    expect(result.get(15).key).toStrictEqual(15);
    expect(result.get(15).data).toStrictEqual("World");
});

test("An object can be found", () => {
    let result = testTable.search(2);

    expect(result.key).toStrictEqual(2);
    expect(result.data).toStrictEqual("Hello");
});

test("An object can be deleted", () => {
    testTable.delete(object1);

    expect(testTable.table.get(2)).toStrictEqual(null);
});
