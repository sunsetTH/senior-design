import FSMHelpers

print "\n\n============    Head Tracking Log   ============"
fsm = FSMHelpers.HeadTrackingFSMClass()

while 1:
#for i in range(1, 100):
  fsm.step()

