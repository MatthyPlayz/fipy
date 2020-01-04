import os
"""
InitDir("com.matthyfamily")
RefGen("brinify", "Brinify", "1.0", "1.12.2")
InitGen("", "com.matthyfamily", "Brinify.java")
ModItems("brinify", "com.matthyfamily", "Brine.java", "brine")
"""
def ModItems(modid, pkgname, filename, itemname):
    os.chdir("init")
    file = open(filename, "w")
    regs = itemname
    item = regs + " = new ItemBasic(\"" + regs + "\");"
    iteml = regs
    strfile = "package " + pkgname + ";" + """
import """ + pkgname + ".Reference;" + """
import """ + pkgname + ".ItemBasic;" + """
import net.minecraft.client.renderer.block.model.ModelResourceLocation;
import net.minecraft.init.Items;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraftforge.client.event.ModelRegistryEvent;
import net.minecraftforge.client.model.ModelLoader;
import net.minecraftforge.event.RegistryEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.eventhandler.SubscribeEvent;
@Mod.EventBusSubscriber(modid=Reference.MODID)
public class """ + filename.replace(".java", "") + """ {
    static Item """ + regs + """;
    public static void init() {
        """ + item + """
    }
    @SubscribeEvent
    public static void registerItems(RegistryEvent.Register<Item> event) {
        event.getRegistry().registerAll(
            """ + str(iteml) + """
        );
    }
    @SubscribeEvent
    public static void registerRenders(ModelRegistryEvent event) {
        registerRender(""" + str(regs) + """);
    }
    private static void registerRender(Item item) {
        ModelLoader.setCustomModelResourceLocation(item, 0, new ModelResourceLocation( item.getRegistryName(), "inventory"));
    }
}
    """
    file.write(strfile)
    file.close()
    
