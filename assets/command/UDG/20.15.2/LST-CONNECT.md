---
id: UDG@20.15.2@MMLCommand@LST CONNECT
type: MMLCommand
name: LST CONNECT（查询网元长连接信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CONNECT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- Soap维护
status: active
---

# LST CONNECT（查询网元长连接信息）

## 功能

本命令用于查询Soap服务建立的长连接信息，本命令不需要输入任何参数。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CONNECT]] · 网元长连接信息（CONNECT）

## 使用实例

1. 查询网元长连接信息（网管网元建立长连接）。
  ```
  %%LST CONNECT:;%% 
  RETCODE = 0  操作成功  
  操作结果如下 
  ------------ 
  节点IP       链接ID       序号  状态    
  127.0.0.1  *****956*****  1     2      
  127.0.0.1  *****956*****  2     2      
  127.0.0.1  *****956*****  3     2      
  127.0.0.1  *****956*****  4     2      
  127.0.0.1  *****956*****  5     2      
  127.0.0.1  *****956*****  6     2      
  (结果个数 = 6)
  
  ---    END
  ```
2. 查询网元长连接信息（网管网元没有建立长连接）。
  ```
  %%LST CONNECT:;%% 
  RETCODE = 0  操作成功  

  没有查到相应结果 
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-CONNECT.md`
