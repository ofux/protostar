from os import listdir

import pytest


@pytest.mark.usefixtures("init")
def test_default_build(protostar):
    protostar(["build"])
    dirs = listdir()
    assert "build" in dirs


@pytest.mark.usefixtures("init")
def test_output_dir(protostar):
    protostar(["build", "--output", "out"])
    dirs = listdir()
    assert "build" not in dirs
    assert "out" in dirs


def test_cairo_path_argument(protostar, my_private_libs_setup):
    (my_private_libs_dir,) = my_private_libs_setup

    protostar(["build", "--cairo-path", my_private_libs_dir])

    dirs = listdir()
    assert "build" in dirs


def test_cairo_path_loaded_from_command_config_section_in_config_file(
    protostar, my_private_libs_setup
):
    (my_private_libs_dir,) = my_private_libs_setup

    with open("./protostar.toml", "a", encoding="utf-8") as protostar_toml:
        protostar_toml.write(
            f"""
["protostar.build"]
cairo_path = ["{str(my_private_libs_dir)}"]
"""
        )

    protostar(["build"])

    dirs = listdir()
    assert "build" in dirs


def test_cairo_path_loaded_from_command_shared_section_in_config_file(
    protostar, my_private_libs_setup
):
    (my_private_libs_dir,) = my_private_libs_setup

    with open("./protostar.toml", "a", encoding="utf-8") as protostar_toml:
        protostar_toml.write(
            f"""
["protostar.shared_command_configs"]
cairo_path = ["{str(my_private_libs_dir)}"]
"""
        )

    protostar(["build"])

    dirs = listdir()
    assert "build" in dirs


@pytest.mark.usefixtures("init")
def test_disable_hint_validation(protostar):

    with open("./src/main.cairo", mode="w", encoding="utf-8") as my_contract:
        my_contract.write(
            """%lang starknet

@view
func use_hint():
    tempvar x
    %{
        from foo import bar
        ids.x = 42
    %}
    assert x = 42

    return ()
end
"""
        )

    result = protostar(["build"])
    assert "Hint is not whitelisted." in result

    result = protostar(["build", "--disable-hint-validation"])
    assert result == ""
