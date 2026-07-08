---
id: UNC@20.15.2@MMLCommand@DSP SSHCSTATUSINFO
type: MMLCommand
name: DSP SSHCSTATUSINFO（显示客户端运行状态信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SSHCSTATUSINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- SSH调测
status: active
---

# DSP SSHCSTATUSINFO（显示客户端运行状态信息）

## 功能

该命令用于查询SSH客户端运行状态信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询状态信息的类型 | 可选必选说明：必选参数<br>参数含义：该参数查询状态信息的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GLOBALSTATUS：全局状态信息。<br>- SESSIONSTATUS：会话状态信息。<br>默认值：无 |
| MASTERTYPE | OMU类型 | 可选必选说明：可选参数<br>参数含义：该参数表示网元的主备类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER：主。<br>- SLAVE：备。<br>默认值：MASTER |

## 操作的配置对象

- [客户端运行状态信息（SSHCSTATUSINFO）](configobject/UNC/20.15.2/SSHCSTATUSINFO.md)

## 使用实例

- 显示主SSH客户端运行状态的全局信息：
  ```
  DSP SSHCSTATUSINFO:QUERYTYPE=GLOBALSTATUS,MASTERTYPE=MASTER;
  ```
  ```

  RETCODE = 0  操作成功

  结果如下
  ------------------------
         OMU类型  =  主
  Socket注册状态  =  ACTIVE
        批备状态  =  INIT
    组件倒换状态  =  INIT
  批备消息定时器  =  NOT RUNNING
  倒换结束定时器  =  NOT RUNNING
        总会话数  =  7
  (结果个数 = 1)
  ---    END
  ```
- 显示备SSH客户端运行状态的全局信息：
  ```
  DSP SSHCSTATUSINFO:QUERYTYPE=GLOBALSTATUS,MASTERTYPE=SLAVE;
  ```
  ```

  RETCODE = 0  操作成功

  结果如下
  ------------------------
         OMU类型  =  备
  Socket注册状态  =  ACTIVE
        批备状态  =  INIT
    组件倒换状态  =  INIT
  批备消息定时器  =  NOT RUNNING
  倒换结束定时器  =  NOT RUNNING
        总会话数  =  0
  (结果个数 = 1)
  ---    END
  ```
- 显示主SSH客户端运行状态的会话信息：
  ```
  DSP SSHCSTATUSINFO:QUERYTYPE=SESSIONSTATUS,MASTERTYPE=MASTER;
  ```
  ```

  RETCODE = 0  操作成功

  结果如下
  ------------------------
  OMU类型          会话号           通道ID         会话ID         SSH版本          用户名        服务类型         会话主状态            会话子状态               会话用户状态        Socket拥塞定时器      保持连接定时器      Socket状态                   Socket下一个状态          对端端口        对端地址        本地地址      VPN索引  Socket文件描述符    管道ID              Ctos加密算法                  Stoc加密算法             Ctos HMAC算法         Stoc HMAC算法          Ctos压缩算法                Stoc压缩算法
  主               1                0              6              2.0              VNFP_SYSTEM   SNETCONF         SSH2_MAIN_SESSION     SSH2_SUB1_SERVICE_REQ    SSH_USER_RSP_INIT   NOT RUNNING           RUNNING             SSHC_CTRL_SOCK_STATE_CREATED SSHC_CTRL_SOCK_ACT_NONE   830             192.168.0.2     192.168.0.1   2        22                  524300              AEAD_AES_256_GCM              AEAD_AES_256_GCM         none                  none                   none                        none
  主               2                0              260            2.0              VNFP_SYSTEM   SNETCONF         SSH2_MAIN_SESSION     SSH2_SUB1_SERVICE_REQ    SSH_USER_RSP_INIT   NOT RUNNING           RUNNING             SSHC_CTRL_SOCK_STATE_CREATED SSHC_CTRL_SOCK_ACT_NONE   22              192.168.0.3     192.168.0.1   2        18                  1048585             AEAD_AES_256_GCM              AEAD_AES_256_GCM         none                  none                   none                        none
  (结果个数 = 2)
  ---    END
  ```
- 显示备SSH客户端运行状态的会话信息：
  ```
  DSP SSHCSTATUSINFO:QUERYTYPE=SESSIONSTATUS,MASTERTYPE=SLAVE;
  ```
  ```

  RETCODE = 0  操作成功

  结果如下
  ------------------------
  OMU类型          会话号           通道ID         会话ID         SSH版本          用户名        服务类型         会话主状态            会话子状态               会话用户状态        Socket拥塞定时器      保持连接定时器       Socket状态                   Socket下一个状态          对端端口        对端地址        本地地址      VPN索引  Socket文件描述符    管道ID              Ctos加密算法                  Stoc加密算法             Ctos HMAC算法         Stoc HMAC算法          Ctos压缩算法                Stoc压缩算法

  备               1                0              6              2.0              VNFP_SYSTEM   SNETCONF         SSH2_MAIN_SESSION     SSH2_SUB1_SERVICE_REQ    SSH_USER_RSP_INIT   NOT RUNNING           RUNNING              SSHC_CTRL_SOCK_STATE_CREATED SSHC_CTRL_SOCK_ACT_NONE   830             192.168.0.2     192.168.0.1   2        22                  524300              AEAD_AES_256_GCM              AEAD_AES_256_GCM         none                  none                   none                        none
  备               2                0              260            2.0              VNFP_SYSTEM   SNETCONF         SSH2_MAIN_SESSION     SSH2_SUB1_SERVICE_REQ    SSH_USER_RSP_INIT   NOT RUNNING           RUNNING              SSHC_CTRL_SOCK_STATE_CREATED SSHC_CTRL_SOCK_ACT_NONE   22              192.168.0.3     192.168.0.1   2        18                  1048585             AEAD_AES_256_GCM              AEAD_AES_256_GCM         none                  none                   none                        none
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示客户端运行状态信息（DSP-SSHCSTATUSINFO）_49802106.md`
