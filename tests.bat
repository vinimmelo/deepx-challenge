:: In case anyone wants to run pytest inside Windows... like me, half of the time.
:: To do the same inside Linux do the follow in terminal: while :; pytest; sleep 5; done
@echo off

:begin

pytest --color=auto
sleep 5

goto begin
