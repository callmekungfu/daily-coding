const functions = require('../src/experimental');

test('Adding Numbers Test, 100 runs', () => {
    for (let i = 0; i < 100; i++) {
        const a = Math.floor((Math.random() * 100) + 1);
        const b = Math.floor((Math.random() * 100) + 1);
        expect(functions.sum(a, b)).toBe(a + b)
    }
});

test('Object Assignment', () => {
    const original = {
        one: 1
    }
    expect(functions.appendToJSON(original, 'two', 2)).toEqual({
        one: 1,
        two: 2
    })
});

test('Random Integer Generation', () => {
    const result = functions.randInt(0, 100);
    expect(result).toBeLessThanOrEqual(100);
    expect(result).toBeGreaterThanOrEqual(0);
})