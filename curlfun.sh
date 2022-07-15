curl -X POST 'http://127.0.0.1:8000/api/Vlan_source/' \
      -H 'Content-Type: application/json' \
      -u 'alexissoko:password' \
      -d '{
          "name": "Printing_area",
          "description": "our staples zone"
      }'
      
curl -X GET "http://localhost:8000/api/Vlan_source/"

response=$(curl --write-out 200 --silent --output /dev/null 'http://127.0.0.1:8000/api/Vlan_source/')
echo $response

##################
curl -X PUT 'http://127.0.0.1:8000/api/update_vlan/1' \
      -H 'Content-Type: application/json' \
      -u 'alexissoko:password' \
      -d '{
          "name": "CHANGED Printing_area updated 2nd time",
          "description": "our staples zone updated"
      }'
curl -X GET "http://localhost:8000/api/Vlan_source/"
##############
curl -X DELETE 'http://127.0.0.1:8000/api/vpn_source/1' \                      
      -H 'Content-Type: application/json' \
      -u 'alexissoko:password'

curl -X GET "http://localhost:8000/api/Vlan_source/"