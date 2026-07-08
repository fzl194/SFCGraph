---
id: UDG@20.15.2@MMLCommand@DSP SSHSSTATUSINFO
type: MMLCommand
name: DSP SSHSSTATUSINFO（显示服务器运行状态信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SSHSSTATUSINFO
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

# DSP SSHSSTATUSINFO（显示服务器运行状态信息）

## 功能

该命令用于查询SSH服务器运行状态信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询状态信息的类型 | 可选必选说明：必选参数<br>参数含义：该参数表示查询状态信息的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GLOBALSTATUS：全局状态信息。<br>- SESSIONSTATUS：会话状态信息。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SSHSSTATUSINFO]] · 服务器运行状态信息（SSHSSTATUSINFO）

## 使用实例

- 显示SSH服务器运行状态的全局信息：
  ```
  DSP SSHSSTATUSINFO:QUERYTYPE=GLOBALSTATUS;
  ```
  ```

  RETCODE = 0  操作成功

  结果如下
  ------------------------
         Socket注册状态  =  ACTIVE
               批备状态  =  INIT
           组件倒换状态  =  SWITCH_INIT
      STelnet最大连接数  =  21
         SFTP最大连接数  =  15
     SNetconf最大连接数  =  20
         批备消息定时器  =  NOT RUNNING
         倒换结束定时器  =  NOT RUNNING
               总会话数  =  1
          STelnet会话数  =  1
             SFTP会话数  =  0
         SNetconf会话数  =  0
  IPv4 Socket文件描述符  =  11
        IPv4 Socket状态  =  SOCK_STATE_LISTEN
  IPv6 Socket文件描述符  =  4294967295
        IPv6 Socket状态  =  SOCK_STATE_DOWN
  (结果个数 = 1)
  ---    END
  ```
- 显示SSH服务器运行状态的会话信息：
  ```
  DSP SSHSSTATUSINFO:QUERYTYPE=SESSIONSTATUS;
  ```
  ```

  RETCODE = 0  操作成功

  结果如下
  ------------------------
                 会话号  =  1
                SSH版本  =  2.0
                VTY索引  =  VTY 0
                 用户名  =  omuser
               服务类型  =  STELNET
               连接状态  =  Connected
             会话主状态  =  SSH_MAIN_SSH_PROCESS
             会话子状态  =  SSH_SUB1_SESSION
           会话用户状态  =  NONE
        会话RSA鉴权状态  =  SSH_SUB3_AUTH_PK
           会话鉴权状态  =  SSH_SUB2_AUTH_ACK
             空闲定时器  =  RUNNING
             认证定时器  =  NOT RUNNING
       Socket拥塞定时器  =  NOT RUNNING
          AAA请求定时器  =  NOT RUNNING
   Socket选项时间定时器  =  NOT RUNNING
        IPv4 Socket状态  =  SOCKCONN_STATE_UP
       Socket下一个状态  =  SSHS_SOCKCONN_ACT_NONE
               对端端口  =  3160
               对端地址  =  192.168.1.11
               本地地址  =  192.168.2.3
                VPN索引  =  1
  IPv4 Socket文件描述符  =  42
                 管道ID  =  3145733
                 通道ID  =  131078
               QX会话数  =  0
               应用类型  =  NULL
                    TEI  =  0
                 交易数  =  0
                EQX动作  =  NULL
               认证状态  =  NULL
              OSP通道ID  =  0
               QX通道ID  =  0
              AAA会话ID  =  0
    QX Socket文件描述符  =  0
             对端网元ID  =  0
             本地网元ID  =  0
             QX会话状态  =  NULL
        QX CAML消息状态  =  NULL
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SSHSSTATUSINFO.md`
