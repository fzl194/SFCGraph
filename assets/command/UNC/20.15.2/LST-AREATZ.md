---
id: UNC@20.15.2@MMLCommand@LST AREATZ
type: MMLCommand
name: LST AREATZ（查询区域时区参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AREATZ
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 多时区管理
- 区域时区参数配置
status: active
---

# LST AREATZ（查询区域时区参数）

## 功能

**适用网元：SGSN、MME**

此命令用于查询区域时区记录。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREA | 区域范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该区域的标识类型。<br>取值范围：<br>- “LA(位置区)”：表示该区域标识类型为位置区。<br>- “RA(路由区)”：表示该区域标识类型为路由区。<br>- “TA(跟踪区)”：表示该区域标识类型为跟踪区。<br>默认值：无 |
| MCC | 移动国家代码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动国家代码。<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动网号。<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区域码<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>说明：该参数在<br>“AREA(区域范围)”<br>设置为<br>“LA(位置区)”<br>或<br>“RA(路由区)”<br>时生效。 |
| RAC | 路由区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由区域码<br>取值范围：0x00～0xFF<br>默认值：无<br>说明：该参数在<br>“AREA(区域范围)”<br>设置为<br>“RA(路由区)”<br>时生效。 |
| TAC | 跟踪区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该跟踪区域码。<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>说明：该参数在<br>“AREA(区域范围)”<br>设置为<br>“TA(跟踪区)”<br>时生效。 |

## 操作的配置对象

- [区域时区参数（AREATZ）](configobject/UNC/20.15.2/AREATZ.md)

## 使用实例

查询一条 “区域范围” 为 “LA(位置区)” ， “移动国家代码” 为 “123” ， “移动网号” 为 “03” ， “位置区域码” 为 “200” 的区域时区记录：

LST AREATZ: AREA=LA, MCC="123", MNC="03", LAC="200";

```
%%LST AREATZ: AREA=LA, MCC="123", MNC="03", LAC="200";%%
RETCODE = 0  操作成功。

输出结果如下
--------------
      区域范围  =  位置区
  移动国家代码  =  123
      移动网号  =  03
    位置区域码  =  0x0112
位置区域码范围  =  0x0350
    路由区域码  =  NULL
路由区域码范围  =  NULL
    跟踪区域码  =  NULL
跟踪区域码范围  =  NULL
      时区标识  =  1
(结果个数 = 1)

---    END
```

查询多条区域时区记录

LST AREATZ:;

```
%%LST AREATZ:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
 区域范围  移动国家代码  移动网号  位置区域码  位置区域码范围  路由区域码  路由区域码范围  跟踪区域码  跟踪区域码范围  时区标识

 位置区    123           03        0x5501      0x5501          NULL        NULL            NULL        NULL            1       
 位置区    123           03        0x5502      0x5502          NULL        NULL            NULL        NULL            2       
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询区域时区参数(LST-AREATZ)_26145588.md`
