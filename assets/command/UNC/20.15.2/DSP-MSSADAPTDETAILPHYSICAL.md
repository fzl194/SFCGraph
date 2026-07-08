---
id: UNC@20.15.2@MMLCommand@DSP MSSADAPTDETAILPHYSICAL
type: MMLCommand
name: DSP MSSADAPTDETAILPHYSICAL（查询适配层物理表详细信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSADAPTDETAILPHYSICAL
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 适配层统计查询
status: active
---

# DSP MSSADAPTDETAILPHYSICAL（查询适配层物理表详细信息）

## 功能

该命令用于查询适配层物理表详细信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| TABLEID | 表号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示表号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [适配层物理表详细信息（MSSADAPTDETAILPHYSICAL）](configobject/UNC/20.15.2/MSSADAPTDETAILPHYSICAL.md)

## 使用实例

查询适配层物理表详细信息：

```
DSP MSSADAPTDETAILPHYSICAL:TABLEID = 1,RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
--------
统一转发平台表号  =  54
        业务表名  =  236
      运行实例号  =  2
      物理表属性  =  LINEAR
物理表初始化标识  =  TRUE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询适配层物理表详细信息（DSP-MSSADAPTDETAILPHYSICAL）_00865809.md`
