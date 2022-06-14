#Cette version remplace les multiples espaces par une chaine de caractrères complexe et retire les espace simples, les espaces multiples sont ensuites restaurés. Le fait que les chaînes soient aussi longue permet de faire en sorte que l'algo marche dans tous les cas (seul cas problématique serait si l'un des mots de passe est entier et non séparé dans le texte).
def byeespace2(texte):
  
  texte = texte.replace("   ", "rSAAhUAWLya?jHtz?eD=6^8NSK^hM$HGCJa!npFB&tfJVuzz3b2!YG8BggVu-GduLPDg_D£$$**µµµ__{{{")
  texte = texte.replace("  ", "rSAAhUAWLya?jHtz?eD=6^8NSK^hM$HGCJa!npFB&tfJVuzz3b2!YG8BggVu-GduLPDg_D£$$**µµµ__{{{")
  texte = texte.replace(" ", "")
  texte = texte.replace("Pds7KPW$-VBeG9Z438sa5+xC&pSGLN=X7Jkf!28NzXW#rk3bptwmpr$6ztr4_h$BD&hhfz%£%£ù£%##~~~µ", "   ")
  texte = texte.replace("Pds7KPW$-VBeG9Z438sa5+xC&pSGLN=X7Jkf!28NzXW#rk3bptwmpr$6ztr4_h$BD&hhfz%£%£ù£%##~~~µ", "  ")
  return texte