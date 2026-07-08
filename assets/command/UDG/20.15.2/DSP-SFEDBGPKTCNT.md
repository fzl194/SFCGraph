---
id: UDG@20.15.2@MMLCommand@DSP SFEDBGPKTCNT
type: MMLCommand
name: DSP SFEDBGPKTCNT（SFE报文统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFEDBGPKTCNT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- SFE表项统计
status: active
---

# DSP SFEDBGPKTCNT（SFE报文统计）

## 功能

该命令用来查询SFE报文统计信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | 资源单元名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [SFE报文统计（SFEDBGPKTCNT）](configobject/UDG/20.15.2/SFEDBGPKTCNT.md)

## 使用实例

查询指定可用RU的debug的SFE报文统计信息：

```
DSP SFEDBGPKTCNT:RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
匹配计数 = 0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SFE报文统计（DSP-SFEDBGPKTCNT）_00866581.md`
