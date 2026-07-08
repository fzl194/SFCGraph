---
id: UDG@20.15.2@MMLCommand@LST PROTFAGETIME
type: MMLCommand
name: LST PROTFAGETIME（查询协议五元组老化时间）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PROTFAGETIME
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务五元组管理
- 基于协议的五元组节点老化时间
status: active
---

# LST PROTFAGETIME（查询协议五元组老化时间）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示配置的协议组、协议相关的五元组老化时间信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLLEVEL | 协议等级 | 可选必选说明：可选参数<br>参数含义：该参数用于显示配置的协议组、协议级别。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PROTOCOLGROUP：协议组级别。<br>- PROTOCOL：协议级别。<br>默认值：无<br>配置原则：无 |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOLGROUP”时为必选参数。<br>参数含义：该参数用于设置协议组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的默认协议组，可以通过工程命令smctrldsp protocol-list查询。 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOL”时为必选参数。<br>参数含义：该参数用于设置协议名称。数据源为系统支持识别的所有类型的协议、子协议。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的所有类型的协议、子协议，可以通过工程命令smctrldsp protocol-list查询。 |

## 操作的配置对象

- [协议五元组老化时间（PROTFAGETIME）](configobject/UDG/20.15.2/PROTFAGETIME.md)

## 使用实例

- 查询配置的协议组五元组老化时间的一条记录：
  ```
  LST PROTFAGETIME:PROTOCOLLEVEL=PROTOCOLGROUP,PROTGROUPNAME="p2p";
  ```
  ```

  RETCODE = 0  操作成功。

  协议五元组节点老化时间信息
  --------------------------
        协议等级  =  Protocol Group
        协议名称  =  NULL
      协议组名称  =  p2p
  老化时间（秒）  =  60
  (结果个数 = 1)
  ---    END
  ```
- 查询配置的协议组五元组老化时间的所有记录：
  ```
  LST PROTFAGETIME:;
  ```
  ```

  RETCODE = 0  操作成功。

  协议五元组节点老化时间信息
  --------------------------
  协议等级          协议名称    协议组名称    老化时间（秒）

  Protocol          http        NULL          20            
  Protocol Group    NULL        p2p           60            
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询协议五元组老化时间（LST-PROTFAGETIME）_82837298.md`
