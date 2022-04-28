%lang starknet

@contract_interface
namespace AccessControlContract:
    func check_caller():
    end
end

@external
func test_start_prank{syscall_ptr : felt*, range_check_ptr}():
    alloc_locals

    local access_control_address : felt
    %{ 
        ids.access_control_address = deploy_contract("src/access_control.cairo").contract_address 
    %}

    %{ start_prank_for_contract(ids.access_control_address, 42) %}
    AccessControlContract.check_caller(contract_address=access_control_address)
    %{ stop_prank_for_contract(ids.access_control_address) %}

    return ()
end
