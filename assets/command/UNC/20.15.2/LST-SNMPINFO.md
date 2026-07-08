---
id: UNC@20.15.2@MMLCommand@LST SNMPINFO
type: MMLCommand
name: LST SNMPINFO（查询网元长连接信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SNMPINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- Snmp维护
status: active
---

# LST SNMPINFO（查询网元长连接信息）

## 功能

本命令用于查询SNMP服务建立的长连接信息，本命令不需要输入任何参数。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [网元长连接信息（SNMPINFO）](configobject/UNC/20.15.2/SNMPINFO.md)

## 使用实例

1. 查询网元长连接信息（网管网元建立长连接）。
  ```
  %%LST SNMPINFO:;%%
  RETCODE = 0  操作成功  
  操作结果如下 
  ------------ 
  订阅者IP       订阅ID    订阅时间                  订阅者外出端口    
  10.128.0.8     1         2019-08-15 17:59:50       8001
  10.128.0.9     2         2019-08-15 17:59:55       8002
      
  (结果个数 = 2)  
  ---    END
  ```
2. 查询网元长连接信息（网管网元没有建立长连接）。
  ```
  %%LST SNMPINFO:;%% 
  RETCODE = 0  操作成功
  没有查到相应结果  
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询网元长连接信息（LST-SNMPINFO）_86563519.md`
