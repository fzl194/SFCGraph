---
id: UDG@20.15.2@MMLCommand@DSP IPSOCKET
type: MMLCommand
name: DSP IPSOCKET（查询IP Socket状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IPSOCKET
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- SOCKET
status: active
---

# DSP IPSOCKET（查询IP Socket状态）

## 功能

该命令用于查看已创建的IP Socket信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4协议族。<br>- IPv6：IPv6协议族。<br>默认值：IPv4 |
| SOCKETTYPE | Socket类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Socket类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TCP：TCP报文。<br>- UDP：UDP报文。<br>- RAWIP：RawIP报文。<br>- RAWLINK：Raw-link报文。<br>默认值：无 |
| APPCID | APP组件CID | 可选必选说明：可选参数<br>参数含义：该参数用于指定APP组件CID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| SOCKETFD | Socket实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定Socket实例ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～2147418111。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPSOCKET]] · IP Socket状态（IPSOCKET）

## 使用实例

- 显示当前系统的IPv4 Socket状态：
  ```
  DSP IPSOCKET: APPCID="0x8093042C", SOCKETFD=10;
  ```
  ```

          RETCODE = 0  操作成功

          结果如下
          ----------------------
                      Socket类型  =  TCP协议报文
                      APP组件CID  =  0x8093042C
                    Socket实例ID  =  10
                      协议类型值  =  6
                        本端地址  =  0.0.0.0
                        远端地址  =  0.0.0.0
                      本端端口号  =  22
                      远端端口号  =  0
                    发送窗口大小  =  0
                    接收窗口大小  =  0
          已被占用的发送窗口大小  =  0
          已被占用的接收窗口大小  =  0
          (结果个数 = 1)
          ---    END
  ```
- 显示当前系统的IPv6 Socket状态：
  ```
  DSP IPSOCKET: IPVERSION=IPv6, APPCID="0x80130080", SOCKETFD=1;
  ```
  ```

          RETCODE = 0  操作成功

          结果如下
          ----------------------
                      Socket类型  =  TCP协议报文
                      APP组件CID  =  0x80130080
                    Socket实例ID  =  1
                      协议类型值  =  6
                    IPv6本端地址  =  ::
                    IPv6远端地址  =  2001:db8::11
                      本端端口号  =  179
                      远端端口号  =  0
                    发送窗口大小  =  0
                    接收窗口大小  =  0
          已被占用的发送窗口大小  =  0
          已被占用的接收窗口大小  =  0
          (结果个数 = 1)
          ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-IPSOCKET.md`
