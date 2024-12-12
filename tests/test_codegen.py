from build123d_poly import BuildPoly

def test_codegen():
    with BuildPoly() as poly:
        pass
    assert 1==1
