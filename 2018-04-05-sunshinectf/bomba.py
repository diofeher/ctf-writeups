from enigma.machine import EnigmaMachine

rotors = 'V I IV'
rsets = '18 11 25'
plugboard = 'TS IK AV QP HW FM DX NG CY UE'
machine = EnigmaMachine.from_key_sheet(
       rotors=rotors,
       reflector='B',
       ring_settings=rsets,
       plugboard_settings=plugboard)


machine.set_display('MHW')
msg_key = machine.process_text('FLC')

print(msg_key)

machine.set_display(msg_key)
msg = machine.process_text('VJTLWDQYBJMSAMURBOQXYSBZEYNRLGRNKKVQYJKEKRGMSCYBMH')
print(msg)
