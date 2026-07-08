---
id: UDG@20.15.2@MMLCommand@LST NTPSVR
type: MMLCommand
name: LST NTPSVR（查询NTP服务器）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NTPSVR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- NTP服务器管理
status: active
---

# LST NTPSVR（查询NTP服务器）

## 功能

本命令用于请求系统显示NTP服务器的运行状态。

> **说明**
> 无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| SVRNAME | NTP服务器名 | 可选必选说明：可选参数。<br>参数含义：用于请求系统显示哪个名称的NTP服务器的运行状态；若不输入，则表示所有的NTP服务器。<br>取值范围：长度不超过32个字符。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NTPSVR]] · NTP服务器（NTPSVR）

## 使用实例

1. 显示所有的NTP服务器的运行状态：
  LST NTPSVR:;

  ```
  %%LST NTPSVR:;%% 
  RETCODE = 0  操作成功  

  操作结果如下 
  ------------ 
  NTP服务器名  NTP协议版本  类型        地址族  IP地址                                   身份验证标志  身份验证密钥号  密钥类型   时钟状态  参考时间戳                  
  server1      NTPV4        服务器类型  IPv4    192.168.156.12                           是            1314            SHA256       未同步    03:13:19.019 Aug 14 2020   
  server2      NTPV3        服务器类型  IPv6    2001:0db8:86a3:08d3:1319:8a2e:0370:7344  否            NULL            NULL         未同步    03:13:19.019 Aug 14 2020   
  (结果个数 = 2)
  ---    END
  ```
2. 显示名为“NtpSvrName”的NTP服务器的运行状态：
  LST NTPSVR: SVRNAME="NtpSvrName";

  ```
  %%LST NTPSVR: SVRNAME="NtpSvrName";%%
  RETCODE = 0  操作成功  

  操作结果如下
  ------------    
     NTP服务器名  =  NtpSvrName
     NTP协议版本  =  NTPV4           
            类型  =  服务器类型        
          地址族  =  IPv4         
          IP地址  =  10.10.10.10   
    身份验证标志  =  是 
  身份验证密钥号  =  32323
        密钥类型  =  SHA256       
        时钟状态  =  未同步     
      参考时间戳  =  03:16:28.028 Aug 14 2020 
  (结果个数 = 1)  
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-NTPSVR.md`
