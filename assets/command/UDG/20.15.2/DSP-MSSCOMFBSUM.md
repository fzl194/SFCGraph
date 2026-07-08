---
id: UDG@20.15.2@MMLCommand@DSP MSSCOMFBSUM
type: MMLCommand
name: DSP MSSCOMFBSUM（查询通信功能块摘要信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSCOMFBSUM
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 通信管理统计查询
status: active
---

# DSP MSSCOMFBSUM（查询通信功能块摘要信息）

## 功能

该命令用于查询通信模块所有FB的摘要信息。

例如，当发现通信丢包时，可执行该命令行查看当前环境的所有FB部署信息，以排查是否是未部署对应的FB或者FB部署失败导致丢包。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称，执行DSP RU查看RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [通信功能块摘要信息（MSSCOMFBSUM）](configobject/UDG/20.15.2/MSSCOMFBSUM.md)

## 使用实例

查询所有FB摘要信息：

```
DSP MSSCOMFBSUM: RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

```

RETCODE = 0  操作成功。

结果如下
--------------------------
功能块ID  功能块属性      实例个数        消息处理函数         报文处理函数

0         Funciton        3               NULL                 pae_FbPktProc
1028      Module          1               sfe_MsgProc          NULL
(结果个数 = 2)
-------  END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询通信功能块摘要信息（DSP-MSSCOMFBSUM）_50121522.md`
