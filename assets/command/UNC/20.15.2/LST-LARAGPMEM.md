---
id: UNC@20.15.2@MMLCommand@LST LARAGPMEM
type: MMLCommand
name: LST LARAGPMEM（查询位置区群组成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LARAGPMEM
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 位置区管理
- 位置区群组成员管理
status: active
---

# LST LARAGPMEM（查询位置区群组成员）

## 功能

**适用网元：SGSN**

此命令用于查询位置区域群成员记录。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LARAGPID | 区域群标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区和路由区的区域群标识。<br>数据来源：整网规划<br>取值范围：1～2048<br>默认值：无 |
| IDTYPE | 标识类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该区域的标识类型。<br>数据来源：整网规划<br>取值范围：<br>- “LA(位置区)”：表示该区域标识类型为位置区。<br>- “RA(路由区)”：表示该区域标识类型为路由区<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定移动国家码。<br>前提条件：该参数在<br>“IDTYPE(标识类型)”<br>设置为<br>“LA(位置区)”<br>或<br>“RA(路由区)”<br>时生效。<br>数据来源：整网规划<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定移动网号。<br>前提条件：该参数在<br>“IDTYPE(标识类型)”<br>设置为<br>“LA(位置区)”<br>或<br>“RA(路由区)”<br>时生效。<br>数据来源：整网规划<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定位置区域码。<br>前提条件：该参数在<br>“IDTYPE(标识类型)”<br>设置为<br>“LA(位置区)”<br>或<br>“RA(路由区)”<br>时生效。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| LACRANGE | 位置区域码范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区域码范围。<br>前提条件：该参数在<br>“IDTYPE(标识类型)”<br>设置为<br>“LA(位置区)”<br>时生效。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| RAC | 路由区域码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定路由区域码。<br>前提条件：该参数在<br>“IDTYPE(标识类型)”<br>设置为<br>“RA(路由区)”<br>时生效。<br>数据来源：整网规划<br>取值范围：0x00～0xFF<br>默认值：无 |
| RACRANGE | 路由区域码范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由区域码范围。<br>前提条件：该参数在<br>“IDTYPE(标识类型)”<br>设置为<br>“RA(路由区)”<br>时生效。<br>数据来源：整网规划<br>取值范围：0x00～0xFF<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LARAGPMEM]] · 位置区群组成员（LARAGPMEM）

## 使用实例

查询所有位置区群组成员：

LST LARAGPMEM:;

```
%%LST LARAGPMEM:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
    区域群标识  =  55
      标识类型  =  位置区
    移动国家码  =  123
      移动网号  =  05
    位置区域码  =  0x20
位置区域码范围  =  0x20
    路由区域码  =  NULL
路由区域码范围  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询位置区群组成员(LST-LARAGPMEM)_72225165.md`
