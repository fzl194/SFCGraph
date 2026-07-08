---
id: UNC@20.15.2@MMLCommand@DSP MSSRULE
type: MMLCommand
name: DSP MSSRULE（查询匹配规则）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSRULE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 维测开关统计查询
status: active
---

# DSP MSSRULE（查询匹配规则）

## 功能

该命令用于查询匹配规则。

用户设置规则后通过该命令进行查询当前的规则信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MSSRULE]] · 匹配规则（MSSRULE）

## 使用实例

查询匹配规则：

```
DSP MSSRULE:RUNAME = "VNODE_VNRS_VNFC_IPU_0066";
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
规则ID   偏移类型              引用计数   偏移  规则   掩码
1        UFP包控制块           0          0     ffff   ffff
2        UFP包控制块           0          0     ffff   ffff
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MSSRULE.md`
