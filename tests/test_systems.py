import ppb
import pytest

from ppb.systems import Renderer


def test_calculate_new_size():
    renderer = Renderer()
    pixel_ratio = 80

    test_width = 240
    test_height = 160

    test_resolution = renderer.target_resolution(test_width, test_height, 1, 1, pixel_ratio)
    assert test_resolution == (120, 80)

    test_width = 80
    test_height = 160

    test_resolution = renderer.target_resolution(test_width, test_height, 2, 2, pixel_ratio)
    assert test_resolution == (160, 320)


@pytest.mark.parametrize("sprite_class", [ppb.Sprite, ppb.RectangleSprite])
def test_skip_sprite_without_image(sprite_class):
    sprite = sprite_class(image=None)

    assert Renderer().prepare_resource(sprite) is None
    assert sprite.__image__() is None


@pytest.mark.parametrize("sprite_class", [ppb.Sprite, ppb.RectangleSprite])
def test_hide_and_restore_sprite_image(sprite_class):
    image = ppb.Image("test-sprite.png")
    sprite = sprite_class(image=image)
    assert sprite.__image__() is image

    sprite.image = None
    assert Renderer().prepare_resource(sprite) is None

    sprite.image = image
    assert sprite.__image__() is image
