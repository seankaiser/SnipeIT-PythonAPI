#!/usr/bin/env python

from snipeit import Locations

server='http://snipeitserver.example.com'
token='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjU5MjFlNDUxZDlkZGJjNjIyOWIyZGQxYzRkNzMyMTE0MzcyZTY2YTZmMmE5NTE2ZTMyNWM2Mzg2ODNjMjdlODMyODE4YmJmM2QxNTg4MjlhIn0.eyJhdWQiOiIxIiwianRpIjoiNTkyMWU0NTFkOWRkYmM2MjI5YjJkZDFjNGQ3MzIxMTQzNzJlNjZhNmYyYTk1MTZlMzI1YzYzODY4M2MyN2U4MzI4MThiYmYzZDE1ODgyOWEiLCJpYXQiOjE1MTUxODI1OTcsIm5iZiI6MTUxNTE4MjU5NywiZXhwIjoxNTQ2NzE4NTk3LCJzdWIiOiIyMzQ2Iiwic2NvcGVzIjpbXX0.E4aHV0NQDlylBXfkfexYl2UBr043wb2suoNrLD2dSwwptIFxNyy8NSWFQxgvYtVeenIbva9dUhI_dYkY7h0W56RZW3DAoqOlzKjFUnhDU3FEqBMsI-CuiGQPwVJ5QQRIzP9VZVpypqokOf-OTZyc-ZyxyGnqz9_dqMFySYZ7EicbtpdYvWVgelK5HF4gxodeBmLm7igVSNkRm_SxHesyjVIvsefnXFF5idUWSwHBn3jXhv-Jm0fhAz8xAw7XjsXMPQXGMAkQHXYpEmobiGSJsvlVPyf4aZjB7FJVzz-1EecFOqBMAS5ZE4YUYi-DOH4YtS6JL_54UOJMeJ3gPh22f4_3yzjNoZ20_ru_O4au2yraG7INCc53XyFj2qgfh9n9eKqRJH2pTB_5jemMCVLjZRDhXA7H0pMxGr_iSlWCXcJGpXjTtW3au53zlqXxgSYtYuti_pU5rahcQWgKEyh7QGdepOa-xaXG_td5pJs2ewmW1Qw3YfFw1ryVZICnloYrGwnoIehXH_7gCBpuUx-NhlKEzhXEQlV0Vcq_btKB5M-AdPD7XSP4Y5SaTmC8B38J6h-uT5cw8XAUv0vR0NMfY9gs-JXZExTqzVcu_GIhy1v_lkeeh7Xud8ZzSlvR6zdDN3LTxh1IReHZBEX8gSh7bFsGe-bGTp40S_RbSilF_pg'


L = Locations()
r = L.get(server, token)
print r
