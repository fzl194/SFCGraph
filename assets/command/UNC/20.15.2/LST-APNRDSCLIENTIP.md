---
id: UNC@20.15.2@MMLCommand@LST APNRDSCLIENTIP
type: MMLCommand
name: LST APNRDSCLIENTIP（查询APN Radius Client IP接口）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNRDSCLIENTIP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- APN的Radius客户端地址属性
status: active
---

# LST APNRDSCLIENTIP（查询APN Radius Client IP接口）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查看APN实例下绑定的radius client ip信息。如果指定可选参数APN，则该命令将显示该APN下配置的radius client ip信息，否则该命令将显示所有配置了radius client ip的APN实例的radius client ip的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定radius client ip需要绑定的APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及部分特殊字符。可以支持的特殊字符有“.”和“-”，“.”不可以是第一个字符且不可以连续出现。<br>默认值：无<br>配置原则：无 |
| AUTHORACCT | 鉴权或计费 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是鉴权时的radius client ip还是计费时的radius client ip。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ACCOUNTING：表示指定的Gi接口的IP地址是计费时的radius client ip。<br>- AUTHENTICATION：表示指定的Gi接口的IP地址是鉴权时的radius client ip。<br>- ACCT_AND_AUTH：表示指定的Gi接口的IP地址既是鉴权时的radius client ip，也是计费时的radius client ip。<br>默认值：无<br>配置原则：无 |
| INTFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该radius client ip配置在哪个接口上。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～13。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNRDSCLIENTIP]] · APN Radius Client IP接口（APNRDSCLIENTIP）

## 使用实例

- 当需要查看APN huawei.com下的计费时的radius client ip的配置信息时，可按如下进行配置：
  ```
  LST APNRDSCLIENTIP:APN="huawei.com",AUTHORACCT=ACCOUNTING,INTFNAME="giif1/0/0";
  ```
  ```

  RETCODE = 0  操作成功。

  APN Radius Client 接口绑定
  --------------------------
     APN名称  =  huawei.com
  鉴权或计费  =  计费
    接口名称  =  giif1/0/0
  (结果个数 = 1)
  ---    END
  ```
- 当需要查看APN huawei.com下的鉴权时的radius client ip的配置信息时，可按如下进行配置：
  ```
  LST APNRDSCLIENTIP:APN="huawei.com",AUTHORACCT=AUTHENTICATION,INTFNAME="giif1/0/0";
  ```
  ```

  RETCODE = 0  操作成功。

  APN Radius Client 接口绑定
  --------------------------
     APN名称  =  huawei.com
  鉴权或计费  =  鉴权
    接口名称  =  giif1/0/0
  (结果个数 = 1)
  ---    END
  ```
- 显示所有配置了radius client ip的APN实例的radius client ip的信息。可按如下进行配置：
  ```
  LST APNRDSCLIENTIP:;
  ```
  ```

  RETCODE = 0  操作成功。

  APN Radius Client 接口绑定
  --------------------------
  APN名称    鉴权或计费    接口名称 

  huawei.com    计费          giif1/0/0
  huawei.com    鉴权          giif1/0/0
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNRDSCLIENTIP.md`
