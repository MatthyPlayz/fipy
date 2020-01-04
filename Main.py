from InitGen import *
from Item import *
InitDir("com.matthyfamily")
ItemBasicGen("com.matthyfamily")
RefGen("com.matthyfamily", "brinify", "Brinify", "1.0", "1.12.2")
InitGen(["com.matthyfamily.Brine"], "com.matthyfamily", "Brinify.java", ["Brine"])
ModItems("brinify", "com.matthyfamily", "Brine.java", "brine")
os.system("gradlew build")
