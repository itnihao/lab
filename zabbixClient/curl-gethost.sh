curl -i -X POST -H 'Content-Type: application/json' -d '{"jsonrpc":"2.0","method":"host.get","params":{"output":["hostid","name"],"filter":{"host":""}},"auth":"4f173f580be529ed9131dbae1b55f097","id":1}' http://172.16.235.128/zabbix/api_jsonrpc.php