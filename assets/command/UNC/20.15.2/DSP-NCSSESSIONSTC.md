---
id: UNC@20.15.2@MMLCommand@DSP NCSSESSIONSTC
type: MMLCommand
name: DSP NCSSESSIONSTC（显示NETCONF会话的统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NCSSESSIONSTC
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 网络配置协议
status: active
---

# DSP NCSSESSIONSTC（显示NETCONF会话的统计信息）

## 功能

该命令用于显示NETCONF会话的统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SESSIONID | NETCONF会话ID | 可选必选说明：可选参数<br>参数含义：NETCONF会话标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NCSSESSIONSTC]] · NETCONF会话的统计信息（NCSSESSIONSTC）

## 使用实例

- 显示NETCONF会话的统计信息：
  ```
  DSP NCSSESSIONSTC:
  SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
  NETCONF会话ID  NETCONF处理总时间（微秒）  CMF处理总时间（微秒）  FTP处理总时间（微秒）  错误信息  统计信息  

  59             6087334                    83351233               0                      NULL      NULL      
  60             2601117                    4347439305             0                      NULL      NULL      
  61             380662                     20256922               0                      NULL      NULL      
  62             369074                     20507319               0                      NULL      NULL      
  64             376323                     20651834               0                      NULL      NULL      
  182            2392924                    133793961              0                      NULL      NULL      
  256            9865974                    148198056              0                      NULL      NULL      
  5140           11848                      4006                   0                      NULL      NULL      
  6282           3346                       6438                   0                      NULL      NULL      
  9423           6586                       2950                   0                      NULL      NULL      
  10463          30291                      155875                 0                      NULL      NULL      
  (结果个数 = 11)

  ---    END
  ```
- 显示指定NETCONF会话的统计信息：
  ```
  DSP NCSSESSIONSTC:SESSIONID=88
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
              NETCONF会话ID  =  59
  NETCONF处理总时间（微秒）  =  6088054
      CMF处理总时间（微秒）  =  83363530
      FTP处理总时间（微秒）  =  0
                   错误信息  =  
      in-use                     : 0              invalid-value           : 0          
      too-big                    : 0              missing-attribute       : 0          
      bad-attribute              : 0              unknown-attribute       : 0          
      missing-element            : 0              bad-element             : 0          
      unknown-element            : 0              unknown-namespace       : 0          
      access-denied              : 0              lock-denied             : 0          
      resource-denied            : 0              rollback-failed         : 0          
      data-exists                : 0              data-missing            : 0          
      operation-not-supported    : 0              operation-failed        : 0          

                   统计信息  =    caml-ctrl-msg: 
       caml-conn-req      : 1            caml-conn-drop-req   : 0            nca-conn-rsp    : 1          
       caml-disconn-req   : 0            nca-disconn-rsp      : 0          
       nca-disconn-req    : 0            caml-disconn-rsp     : 0          
    caml-data-msg: 
       total-recv         : 32971        total-recv_len(Byte) : 10342166     total-send      : 32971      
       recv-seq-drop      : 0            recv-pipe-delay      : 0            recv-close-drop : 0          
    notification: 
       total-recv         : 0            total-send           : 0          
       send-fail-drop     : 0          

  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NCSSESSIONSTC.md`
