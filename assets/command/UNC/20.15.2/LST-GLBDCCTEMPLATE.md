---
id: UNC@20.15.2@MMLCommand@LST GLBDCCTEMPLATE
type: MMLCommand
name: LST GLBDCCTEMPLATE（查询计费属性与在线计费模板绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBDCCTEMPLATE
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- 信用控制
- 全局信用控制模板
status: active
---

# LST GLBDCCTEMPLATE（查询计费属性与在线计费模板绑定关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询计费属性与在线计费模板的配置绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHARGECHARACT | 计费属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定计费属性类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GLOBAL：指定计费属性为缺省全局计费属性。<br>- CHARGE_CHARACT：指定计费属性为配置的特殊计费属性值。<br>默认值：无<br>配置原则：无 |
| SPECIFICCCVALUE | 计费属性值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CHARGECHARACT”配置为“CHARGE_CHARACT”时为必选参数。<br>参数含义：该参数用于指定特殊计费属性值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GLBDCCTEMPLATE]] · 计费属性与在线计费模板绑定关系（GLBDCCTEMPLATE）

## 使用实例

查询计费属性值为1314的计费属性所绑定的在线计费模板信息：

```
LST GLBDCCTEMPLATE:CHARGECHARACT=CHARGE_CHARACT,SPECIFICCCVALUE="0x1314";
```

```

RETCODE = 0  操作成功。

全局DCC模板
-----------
        计费属性  =  计费属性
      计费属性值  =  0x1314
    计费属性掩码  =  0x1314
          优先级  =  2
在线计费模板名称  =  dcctem3
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GLBDCCTEMPLATE.md`
