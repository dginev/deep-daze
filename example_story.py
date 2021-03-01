from deep_daze import Imagine

# Sources:
# 1. https://getfreewrite.com/blogs/writing-success/the-power-of-setting-using-vivid-description-to-enthrall-your-readers
# 2. http://read.gov/aesop/012.html
imagine = Imagine(
    text="""
    A path of crushed pine needles wound among the trees and into a shadowy clump of bracken and snow-laden rhododendron bushes. A sharp, icy wind carried the sharp tang of pine and the damp decay of leaves on the forest floor. Sunlight spilled through the canopy of trees and reflected off droplets of water clinging to the sleeve of Alex’s jacket. A twig snapped beneath his boot, and he froze, holding his breath as the deer’s head turned sharply towards him. It sniffed the air, and then, as if it could smell the danger, bolted away through the undergrowth, its hoof-beats seeming to echo the frustrated beating of Alex’s heart.
    """,
    # text="""One bright day in late autumn a family of Ants were bustling about in the warm sunshine, drying out the grain they had stored up during the summer, when a starving Grasshopper, his fiddle under his arm, came up and humbly begged for a bite to eat.
    # "What!" cried the Ants in surprise, "haven't you stored anything away for the winter? What in the world were you doing all last summer?"
    # "I didn't have time to store up any food," whined the Grasshopper
    # "I was so busy making music that before I knew it the summer was gone."
    # The Ants shrugged their shoulders in disgust.
    # "Making music, were you?" they cried. "Very well; now dance!" And they turned their backs on the Grasshopper and went on with their work.""",
    #
    # text="""The Pythagorean Theorem which is also referred to as ‘Pythagoras theorem’ is arguably the most famous formula in mathematics that defines the relationships between the sides of a right triangle.
    #
    # The theorem is attributed to a Greek mathematician and philosopher by the name Pythagoras(569-500 B.C.E.). He has many contributions to the field of mathematics, but the Pythagorean Theorem is the most important of them.
    #
    # Pythagoras is credited with several contributions in the field of mathematics, astronomy, music, religion, philosophy etc. One of his notable contribution to mathematics is the discovery of the Pythagorean Theorem. Pythagoras studied the sides of a right triangle and discovered that, the sum of the square of the two shorter sides of the triangles is equal to the square of the longest side.
    #
    # In this article, we will learn what the Pythagorean Theorem entails, its converse and the Pythagorean Theorem formula. Before getting deeper into the topic, let’s recall about a right triangle. A right triangle is a triangle with one interior angle equals to 90 degrees. In a right triangle, the two short legs meet at an angle of 90 degrees. The hypotenuse of a triangle is side which opposite the 90-degree angle.""",
    story_words_init=10,
    story_words_per_epoch=7,
    num_layers=44,
    save_progress=True,
    create_story=True,
    image_width=512,
    iterations=300,
    batch_size=64,
    save_every=30,
    gradient_accumulate_every=1,
)
imagine()
