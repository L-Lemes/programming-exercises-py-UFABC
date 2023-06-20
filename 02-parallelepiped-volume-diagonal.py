def parallelepipedVolumeAndDiagonal(a, b, c):
    volume = int(a * b * c)
    diagonal = float((a**2 + b**2 + c**2)**(1/2))
    
    return (f"volume: {volume} Diagonal: {diagonal:.2f}")

print(parallelepipedVolumeAndDiagonal(1, 2, 3))