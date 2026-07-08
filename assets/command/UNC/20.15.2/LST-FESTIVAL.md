---
id: UNC@20.15.2@MMLCommand@LST FESTIVAL
type: MMLCommand
name: LST FESTIVAL（查询计费节假日表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FESTIVAL
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
- 节假日
status: active
---

# LST FESTIVAL（查询计费节假日表）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来查询计费节假日表。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GLOBALFLG | 全局配置 | 可选必选说明：可选参数<br>参数含义：本参数用于指定全局配置属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GLOBAL：指定计费属性为缺省全局计费属性。<br>- CHARGE_CHARACT：指定计费属性为配置的特殊计费属性值。<br>默认值：无<br>配置原则：当没有配置normal、hotbilling或prepaid的节假日相关计费信息时，则对用户采用gloabl所指定的节假日。 |
| CCVALUE | 计费属性值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“GLOBALFLG”配置为“CHARGE_CHARACT”时为必选参数。<br>参数含义：指定Charge Characteristic（计费属性）值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [计费节假日表（FESTIVAL）](configobject/UNC/20.15.2/FESTIVAL.md)

## 使用实例

查询节假日信息，GLOBALFLG为CHARGE_CHARACT，CCVALUE为0x0100 ，命令为：

```
LST FESTIVAL:GLOBALFLG=CHARGE_CHARACT,CCVALUE="0x0100";
```

```

RETCODE = 0  操作成功。

节假日参数配置
--------------
                    全局配置  =  计费属性
     Charge Characteristic值  =  0x0100
   Charge Characteristic掩码  =  0x0100
Charge Characteristic 优先级  =  2
                  节假日年份  =  2015
                  节假日月份  =  10
                  节假日日期  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询计费节假日表（LST-FESTIVAL）_09896829.md`
