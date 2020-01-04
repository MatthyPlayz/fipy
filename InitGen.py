import os
def ItemBasicGen(pkgname):
    os.mkdir("items")
    os.chdir("items")
    file = open("ItemBasic.java", "w")
    file.write("""package """ + pkgname + """;

import net.minecraft.item.Item;

public class ItemBasic extends Item {
	
	public ItemBasic(String name) {
		setTranslationKey(name);
		setRegistryName(name);
	}
}""")
    file.close()
    os.chdir("..")
def InitDir(pkgname):
    os.mkdir("src")
    os.chdir("src") #src
    os.mkdir("main")
    os.chdir("main") #srcmain
    os.mkdir("java")
    os.mkdir("resources")
    os.chdir("resources") #src main res
    os.mkdir("textures")
    os.chdir("textures")
    os.mkdir("item") # src main res textures item
    for i in range(3):
        os.chdir("..") # src
    os.chdir("main")
    os.chdir("java") #src main  java
    os.mkdir(pkgname)
    os.chdir(pkgname) # src main java xx.xxxx
    os.mkdir("init")
    os.chdir("init") # src main java xx.xxxx init
    for i in range(4):
        os.chdir("..") # src
    os.chdir("main")
    os.chdir("java")
    os.chdir(pkgname)
def RefGen(pkgname,modid,modname,version,mcversion):
    file = open("Reference.java", "w")
    file.write("""
    package """ + pkgname + """;
    public class Reference {
    public static final String MODID = \"""" + modid + """\";
    public static final String MODNAME = \"""" + modname + """\";
    public static final String VERSION = \"""" + version + """\";
    public static final String ACCEPTED_MINECRAFT_VERSIONS = \"[""" + mcversion + """]\";
}""");
    file.close()

def InitGen(imports,pkgname,filename,initsneeded=["ModItems"]):
    file = open(filename, "w")
    importsa = ""
    inits = ""
    if(imports != []):
        for im in imports:
            importsa += "import " + im + ";\n"
    for ini in initsneeded:
        inits += ini + ".init();\n"
    file.write("package " + pkgname + ";\n" + "import " + pkgname + ".Reference;\n" + importsa + """

import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.Mod.EventHandler;
import net.minecraftforge.fml.common.Mod.Instance;
import net.minecraftforge.fml.common.SidedProxy;
import net.minecraftforge.fml.common.event.FMLInitializationEvent;
import net.minecraftforge.fml.common.event.FMLPostInitializationEvent;
import net.minecraftforge.fml.common.event.FMLPreInitializationEvent;
import net.minecraftforge.fml.common.registry.GameRegistry;

@Mod(modid = Reference.MODID, name=Reference.MODNAME, version=Reference.VERSION, acceptedMinecraftVersions=Reference.ACCEPTED_MINECRAFT_VERSIONS)
public class """ + filename.replace(".java", "") + """ {
    @EventHandler
    public void preInit(FMLPreInitializationEvent event) {
            System.out.println(Reference.MODID + ":preInit");
            """ + inits + """
    }
    
    @EventHandler
    public void init(FMLInitializationEvent event) {
            System.out.println(Reference.MODID + ":init");
    }
    
    @EventHandler
    public void postInit(FMLPostInitializationEvent event) {
            System.out.println(Reference.MODID + ":postInit");
    }
}""")
    file.close()
