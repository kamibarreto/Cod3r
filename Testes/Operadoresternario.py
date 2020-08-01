esta_chovendo = True
print('Estou com as roupas' + (' secas.', ' molhadas.')[esta_chovendo])
#O operador que estiver mais perto do [esta_chovendo] que é o molhado sera o True, e o mais longe "Secas." sera o False

print('Estou com as roupas' + (' molhadas.' if esta_chovendo else ' secas.'))