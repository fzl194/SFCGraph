---
id: UDG@20.15.2@MMLCommand@DSP SOCKPATH
type: MMLCommand
name: DSP SOCKPATH（查询SOCK路径诊断信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SOCKPATH
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

# DSP SOCKPATH（查询SOCK路径诊断信息）

## 功能

该命令用于查询SOCK路径诊断信息。

可选参数IPVERSION，可以查询指定IP版本的SOCK路径诊断信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPCID | APP组件CID | 可选必选说明：必选参数<br>参数含义：该参数用来指定APP组件CID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| SOCKID | Socket实例ID | 可选必选说明：必选参数<br>参数含义：该参数用来指定Socket实例ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0～4294967295。<br>默认值：无 |
| IPVERSION | IP版本 | 可选必选说明：可选参数<br>参数含义：该参数用于显示IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4协议族。<br>- IPv6：IPv6协议族。<br>默认值：IPv4 |

## 操作的配置对象

- [SOCK路径诊断信息（SOCKPATH）](configobject/UDG/20.15.2/SOCKPATH.md)

## 使用实例

- 查询SOCK IPv4路径诊断信息：
  ```
  DSP SOCKPATH: APPCID="0x8069003C", SOCKID=9;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
                  路径统计  =  1
                    路径ID  =  2
                  路径状态  =  2
              路径中断原因  =  NO ROUTE[7]
     发送至下一个组件的PID  =  0
                下一段的ID  =  4294967295
                  扩展标记  =  0
               VPN实例索引  =  0
                  发送标记  =  0
                源IPv4地址  =  0.0.0.0
              目的IPv4地址  =  10.1.1.2
                出接口索引  =  0
            指定出接口索引  =  0
        指定下一跳IPv4地址  =  0.0.0.0
                  实例标记  =  0
                  隧道类型  =  0
                    隧道ID  =  0
                    XC索引  =  0
                Nickname表  =  0
                   VLAN ID  =  0
                   MAC地址  =  0000-0000-0000
                端口列表ID  =  0
                    VSI ID  =  0
  Socket路径存储的申请状态  =  0
  Socket路径存储的中断原因  =  0
      Socket存储的下一段ID  =  0
  (结果个数 = 1)
  ---    END
  ```
- 查询SOCK IPv6路径诊断信息：
  ```
  DSP SOCKPATH:APPCID="8069003A",SOCKID=13,IPVERSION=IPv6;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
                  路径统计  =  1
                    路径ID  =  2
                  路径状态  =  2
              路径中断原因  =  WAIT ND ENTRY[32829]
     发送至下一个组件的PID  =  0
                下一段的ID  =  4294967295
                  扩展标记  =  0
               VPN实例索引  =  0
                  发送标记  =  0
                源IPv6地址  =  ::
              目的IPv6地址  =  2001:db8::6
                出接口索引  =  0
            指定出接口索引  =  0
        指定下一跳IPv6地址  =  ::
                  实例标记  =  0
                  隧道类型  =  0
                    隧道ID  =  0
                    XC索引  =  0
                Nickname表  =  0
                   VLAN ID  =  0
                   MAC地址  =  0000-0000-0000
                端口列表ID  =  0
                    VSI ID  =  0
  Socket路径存储的申请状态  =  0
  Socket路径存储的中断原因  =  0
      Socket存储的下一段ID  =  0
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SOCK路径诊断信息（DSP-SOCKPATH）_00600737.md`
