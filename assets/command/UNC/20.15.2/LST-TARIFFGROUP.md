---
id: UNC@20.15.2@MMLCommand@LST TARIFFGROUP
type: MMLCommand
name: LST TARIFFGROUP（查询费率切换组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TARIFFGROUP
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
- 费率切换
- 费率切换组
status: active
---

# LST TARIFFGROUP（查询费率切换组）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询计费属性的已配置的费率切换组信息。如果不指定可选参数，该命令将显示所有配置的费率切换组信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TARIFFGRPNAME | 费率切换组名 | 可选必选说明：可选参数<br>参数含义：指定费率切换组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| GLOBALFLG | 全局配置 | 可选必选说明：可选参数<br>参数含义：指定全局配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GLOBAL：指定计费属性为缺省全局计费属性。<br>- CHARGE_CHARACT：指定计费属性为配置的特殊计费属性值。<br>默认值：无<br>配置原则：<br>- GLOBAL：全局。<br>- CHARGE_CHARACT：计费属性。 |
| CCVALUE | Charge Characteristic值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT”时为必选参数。<br>参数含义：指定Charge Characteristic（计费属性）值。当“GLOBALFLG”设置为“CHARGE_CHARACT”时，该参数必须设置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TARIFFGROUP]] · 费率切换组（TARIFFGROUP）

## 使用实例

查询名为huawei，用户属性为0x0100的费率切换组，命令为：

```
LST TARIFFGROUP:TARIFFGRPNAME="huawei",GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0100";
```

```

RETCODE = 0  操作成功。

费率切换组配置
--------------
                费率切换组名  =  huawei
                    全局配置  =  计费属性
     Charge Characteristic值  =  0x0100
   Charge Characteristic掩码  =  0x0100
Charge Characteristic 优先级  =  2
                    费率类型  =  工作日
            费率切换起始时间  =  09:00
            费率切换终止时间  =  17:00
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询费率切换组（LST-TARIFFGROUP）_09896838.md`
