---
id: UNC@20.15.2@MMLCommand@LST GLBOFCTEMPLATE
type: MMLCommand
name: LST GLBOFCTEMPLATE（查询全局离线计费模板）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBOFCTEMPLATE
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 离线计费基础参数
- 全局离线计费模板
status: active
---

# LST GLBOFCTEMPLATE（查询全局离线计费模板）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用来查询离线计费模板绑定到全局离线计费配置信息，以及Charge Characteristic绑定离线计费模板中的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GLOBALFLAG | 全局记录 | 可选必选说明：可选参数<br>参数含义：可以为计费属性绑定离线计费模板，也可以为全局绑定离线计费模板。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GLOBAL：指定计费属性为缺省全局计费属性。<br>- CHARGE_CHARACT：指定计费属性为配置的特殊计费属性值。<br>默认值：无<br>配置原则：无 |
| CCVALUE | Charge Characteristic值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GLOBALFLAG”配置为“CHARGE_CHARACT”时为可选参数。<br>参数含义：指定Charge Characteristic值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBOFCTEMPLATE]] · 全局离线计费模板（GLBOFCTEMPLATE）

## 使用实例

查询Charge Characteristic绑定离线计费模板中的配置信息：

```
LST GLBOFCTEMPLATE: GLOBALFLAG=CHARGE_CHARACT,CCVALUE="0x0003";
```

```

RETCODE = 0  操作成功。

全局离线计费模板
----------------
        Charge Characteristic值  =  0x0000
Charge Characteristic特定值掩码  =  0x0003
    Charge Characteristic优先级  =  0x0003
             GGSN离线计费模板名  =  ofc3
              PGW离线计费模板名  =  ofc1
              SGW离线计费模板名  =  ofc2
                       全局记录  =  计费属性
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GLBOFCTEMPLATE.md`
