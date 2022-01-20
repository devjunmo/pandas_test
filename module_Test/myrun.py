
"""
모듈의 모든것을 불러올때는 파일명을 import 하여 불러온다.
모듈에서 필요한거 하나만 가져올때는 from 파일명 import 클래스or메소드 형태로 가져온다.
"""

import mod2 
from mod2 import Mod2Class

mod2.Mod2Class.mod2_class_mtd()

mod2_tst = Mod2Class(1)
mod2_tst.mtd2()