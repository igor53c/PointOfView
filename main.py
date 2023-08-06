from Tree import Tree


def tree_tests():
    # Test Scenario 1
    print("Scenario 1 Tests:")
    tree1 = Tree('x', [Tree('a'), Tree('b')])
    result1 = tree1.from_pov('x')
    expected1 = Tree('x', [Tree('a'), Tree('b')])
    assert str(result1) == str(expected1), f"Expected {str(expected1)}, but got {str(result1)}"
    print("Passed Test 1")

    tree2 = Tree('parent', [Tree('target'), Tree('sibling')])
    result2 = tree2.from_pov('target')
    expected2 = Tree('target', [Tree('parent', [Tree('sibling')])])
    assert str(result2) == str(expected2), f"Expected {str(expected2)}, but got {str(result2)}"
    print("Passed Test 2")

    tree3 = Tree('parent', [Tree('a'), Tree('x', [Tree('b'), Tree('c')])])
    result3 = tree3.from_pov('x')
    expected3 = Tree('x', [Tree('b'), Tree('c'), Tree('parent', [Tree('a')])])
    assert str(result3) == str(expected3), f"Expected {str(expected3)}, but got {str(result3)}"
    print("Passed Test 3")

    try:
        result4 = tree3.from_pov('z')
        print("Failed Test 4: Expected ValueError")
    except ValueError as e:
        assert str(e) == "Tree could not be reoriented"
        print("Passed Test 4")

    # Test Scenario 2
    print("\nScenario 2 Tests:")
    tree5 = Tree('parent', [Tree('x'), Tree('sibling')])
    path1 = tree5.path_to('x', 'parent')
    expected_path1 = ['x', 'parent']
    assert path1 == expected_path1, f"Expected path {expected_path1}, but got {path1}"
    print("Passed Test 5")

    tree6 = Tree('parent', [Tree('a'), Tree('x'), Tree('b'), Tree('c')])
    path2 = tree6.path_to('x', 'b')
    expected_path2 = ['x', 'parent', 'b']
    assert path2 == expected_path2, f"Expected path {expected_path2}, but got {path2}"
    print("Passed Test 6")

    path3 = tree6.path_to('a', 'c')
    expected_path3 = ['a', 'parent', 'c']
    assert path3 == expected_path3, f"Expected path {expected_path3}, but got {path3}"
    print("Passed Test 7")

    try:
        path4 = tree6.path_to('x', 'z')
        print("Failed Test 8: Expected ValueError")
    except ValueError as e:
        assert str(e) == "No path found"
        print("Passed Test 8")

    # Additional test from the problematic scenario
    print("\nAdditional Test:")
    test_tree = Tree('x', [
        Tree('level-0', [
            Tree('level-1', [
                Tree('level-2', [
                    Tree('level-3')
                ])
            ])
        ])
    ])

    transformed_tree = test_tree.from_pov('x')
    expected_tree_str = '{"x": [{"level-0": [{"level-1": [{"level-2": [{"level-3": []}]}]}]}]}'
    assert str(transformed_tree) == expected_tree_str, f"Expected {expected_tree_str}, but got {str(transformed_tree)}"
    print("Passed Additional Test")

    print("\nAll tests completed!")


# Run the tests
if __name__ == '__main__':
    tree_tests()
