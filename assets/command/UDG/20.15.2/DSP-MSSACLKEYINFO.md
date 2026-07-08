---
id: UDG@20.15.2@MMLCommand@DSP MSSACLKEYINFO
type: MMLCommand
name: DSP MSSACLKEYINFO（通过软转发支撑报文关键字查询访问控制列表的结果）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSACLKEYINFO
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

# DSP MSSACLKEYINFO（通过软转发支撑报文关键字查询访问控制列表的结果）

## 功能

该命令用于使用报文关键字查询访问控制列表中表的结果。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| TABLEID | 访问控制列表索引 | 可选必选说明：必选参数<br>参数含义：该参数用于表示访问控制列表索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| PACKETKEY | 报文关键字 | 可选必选说明：必选参数<br>参数含义：该参数用于表示报文关键字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MSSACLKEYINFO]] · 通过软转发支撑报文关键字查询访问控制列表的结果（MSSACLKEYINFO）

## 使用实例

查询软转发支撑使用报文关键字查询访问控制列表的结果：

```
DSP MSSACLKEYINFO: TABLEID=0,PACKETKEY="01010101",RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
      表项优先级 = 10
表项绑定动作索引 = 100
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MSSACLKEYINFO.md`
