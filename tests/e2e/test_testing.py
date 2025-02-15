from subprocess import CalledProcessError

import pytest


@pytest.mark.usefixtures("init")
def test_basic_contract(protostar):
    result = protostar(["test", "tests"])
    assert "1 passed" in result


@pytest.mark.usefixtures("init")
def test_complex(protostar, copy_fixture):
    copy_fixture("basic.cairo", "./src")
    copy_fixture("proxy_contract.cairo", "./src")
    copy_fixture("test_proxy.cairo", "./tests")

    result = protostar(["test", "tests"])

    assert "Collected 2 suits, and 4 test cases" in result
    assert "4 passed" in result


@pytest.mark.usefixtures("init")
def test_expect_revert(protostar, copy_fixture):
    copy_fixture("test_expect_revert.cairo", "./tests")

    result = protostar(["--no-color", "test", "tests/test_expect_revert.cairo"])

    assert "[FAIL] tests/test_expect_revert.cairo test_fail_error_message" in result

    assert (
        "[FAIL] tests/test_expect_revert.cairo test_with_except_revert_fail_expected"
        in result
    )

    assert (
        "[FAIL] tests/test_expect_revert.cairo test_with_except_out_of_scope_revert_fail_expected"
        in result
    )

    assert (
        "[FAIL] tests/test_expect_revert.cairo test_call_not_existing_contract_fail_expected"
        in result
    )
    assert "[error_type] RANDOM_ERROR_NAME" in result

    assert (
        "[FAIL] tests/test_expect_revert.cairo test_error_was_not_raised_before_stopping_expect_revert_fail_expected"
        in result
    )
    assert "5 failed, 5 passed, 10 total" in result
    assert "Unknown location" not in result


def test_loading_cairo_path_from_config_file(protostar, my_private_libs_setup):
    (my_private_libs_dir,) = my_private_libs_setup

    with pytest.raises(CalledProcessError):
        protostar(["test", "tests"])

    with open("./protostar.toml", "a", encoding="utf-8") as protostar_toml:
        protostar_toml.write(
            f"""
["protostar.shared_command_configs"]
cairo_path = ["{str(my_private_libs_dir)}"]
"""
        )

    result = protostar(["test", "tests"])
    assert "/my_lib/utils.cairo" not in result
    assert "1 passed" in result
