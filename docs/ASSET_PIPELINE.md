# Guide to 3D Asset Creation

This is a step-by-step guid to making 3D assets for this project.
It is a bit of a lengthy process, but it works and means that assets
such as character models are easliy and infinitely customizeable

## Character models

1. Create the character in Vroid Studio, using the 'realistic' base models
2. Exporting the model creates the `.vrm` file
3. Rename this file with the `.glb` extension and import it into Blender
4. Prepare the model by going through every texture and switching 
    the materials to use the PrincipledBSDF shader in Blender's
    Shader Editor
5. Export the model as `.fbx`, and in the export options window enable
    the 'embed textures' option to the right, with 'Path Mode' set to
    `copy`
6. Create a `.zip` archive containing the `fbx` model and a folder
    called 'textures' containing all the texture images the model uses
    (These should be exported automatically by vroid)
7. Upload the model to Mixamo, and go through the process of rigging
8. Choose an animation, and download the skinned model with that animation
    as an `.fbx`
9. Once all animations have been chosen, open one of the animated models
    in a new Blender project, and import all of the others
10. For each model in the scene tree/colection, rename its animation to
    something that can be referenced in the Panda3d code later
11. Delete all of the models except the first one that was imported
    (Their animations are now in the project, so the models themselves
    aren't needed any more)
12. In the animations tab at the bottom of the window, go to the 'multi-
    channel' tab, add a new animation channel for each animation, and
    add the animation as an action strip.
13. Export the animated model as a `.gltf` and add to the project
    (probably a good idea at this point to check that the model actually
    loads and animates properly)
14. convert the model to the `.bam` format that panda3d likes using the 
    `gltf2bam` command-line tool, giving the source file and output
    file paths as arguments. For example:
    ```gltf2bam model.gflt model.bam```

And that's it! The model can now (hopefully) be imported and used with
animations in the P3D game.
