---
id: UDG@20.15.2@MMLCommand@DSP MSSACLRULEINFO
type: MMLCommand
name: DSP MSSACLRULEINFO（查询软转发支撑访问控制列表中表项的内容）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSACLRULEINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- QACL统计查询
status: active
---

# DSP MSSACLRULEINFO（查询软转发支撑访问控制列表中表项的内容）

## 功能

该命令用于查询访问控制列表中表项的详细信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| TABLEID | 访问控制列表索引 | 可选必选说明：必选参数<br>参数含义：该参数用于表示访问控制列表索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| RULEPRIORITY | 表项优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于表示表项优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～9223372036854775807。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSSACLRULEINFO]] · 软转发支撑访问控制列表中表项的内容（MSSACLRULEINFO）

## 使用实例

查询软转发支撑访问控制列表中表项的详细信息：

```
DSP MSSACLRULEINFO:TABLEID=0,RULEPRIORITY=0,RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
             优先级 = 1
   表项绑定动作索引 = 101
     表项范围段个数 = 3
         表项关键字 = xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx
                      xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx
     表项关键字掩码 = xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx
                      xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx
表项范围段1起始偏移 = 0
表项范围段1结束偏移 = 15
  表项范围段1起始值 = 0
  表项范围段1结束值 = 99
表项范围段2起始偏移 = 16
表项范围段2结束偏移 = 31
  表项范围段2起始值 = 100
  表项范围段2结束值 = 199
表项范围段3起始偏移 = 32
表项范围段3结束偏移 = 47
  表项范围段3起始值 = 200
  表项范围段3结束值 = 299
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MSSACLRULEINFO.md`
